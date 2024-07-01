import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

ip = input("Digite o host ou ip a ser verificar: ")
port = int(input("Digite a porta a ser verificada: "))


code = client.connect_ex((ip, port))

if code == 0:
    print("Porta Aberta")
else:
    print("Porta Fechada")  