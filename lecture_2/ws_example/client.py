from websocket import create_connection

# Запросить у пользователя название чата
chat_name = input("Введите название чата: ")
ws = create_connection(f"ws://localhost:8000/chat/{chat_name}")
print(f"Подключено к чату {chat_name}. Теперь можно отправлять сообщения.\n")

# Цикл для отправки и получения сообщений
while True:
    # Ввод сообщения от пользователя
    message = input("Введите сообщение: ")
    ws.send(message)
    
    # Получение ответа от сервера (сообщения из чата)
    response = ws.recv()
    print(response)
