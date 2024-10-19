from dataclasses import dataclass, field
from uuid import uuid4
import random
import string

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect

app = FastAPI()

@dataclass(slots=True)
class Broadcaster:
    # Теперь у нас есть разные чаты
    chats: dict[str, list[WebSocket]] = field(init=False, default_factory=dict)

    async def subscribe(self, chat_name: str, ws: WebSocket) -> None:
        await ws.accept()
        if chat_name not in self.chats:
            self.chats[chat_name] = []
        self.chats[chat_name].append(ws)

    async def unsubscribe(self, chat_name: str, ws: WebSocket) -> None:
        self.chats[chat_name].remove(ws)
        if not self.chats[chat_name]:
            del self.chats[chat_name]

    async def publish(self, chat_name: str, message: str) -> None:
        for ws in self.chats.get(chat_name, []):
            await ws.send_text(message)


broadcaster = Broadcaster()

# Функция для генерации случайного имени пользователя
def generate_username() -> str:
    return ''.join(random.choices(string.ascii_letters, k=8))

@app.websocket("/chat/{chat_name}")
async def ws_chat(ws: WebSocket, chat_name: str):
    username = generate_username()  # Генерация случайного имени пользователя
    await broadcaster.subscribe(chat_name, ws)
    await broadcaster.publish(chat_name, f"{username} присоединился к чату")

    try:
        while True:
            # Получение текста от клиента
            text = await ws.receive_text()
            # Отправка сообщения всем пользователям в чате
            await broadcaster.publish(chat_name, f"{username} :: {text}")
    except WebSocketDisconnect:
        await broadcaster.unsubscribe(chat_name, ws)
        await broadcaster.publish(chat_name, f"{username} покинул чат")
