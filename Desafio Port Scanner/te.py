import nmap

# Função para verificar e imprimir as portas abertas
def print_open_ports(result, protocol):
    if protocol in result[ip] and result[ip][protocol]:
        print(f"Portas {protocol.upper()} Abertas:")
        for porta in result[ip][protocol].keys():
            print(f"- {porta}")
    else:
        print(f"Nenhuma porta {protocol.upper()} aberta encontrada.")

# Obtendo o IP a ser varrido
ip = input("Digite o IP a ser varrido: ")

# Criando o objeto do scanner
scanner = nmap.PortScanner()

# Menu de opções
menu = input("""\nTipo de varredura a ser realizada:
        [1] Tipo SYN
        [2] Tipo UDP
        [3] Tipo Intensa0
        Digite a opção escolhida: """)

try:
    if menu == "1":
        print("Versão do Nmap:", scanner.nmap_version())
        resultado = scanner.scan(ip, '1-1024', '-v -sS')
        print("Status IP:", resultado[ip].state())
        print("Informações da varredura:", resultado)
        print_open_ports(resultado, 'tcp')

    elif menu == "2":
        print("Versão do Nmap:", scanner.nmap_version())
        resultado = scanner.scan(ip, '1-1024', '-v -sU')
        print("Status IP:", resultado[ip].state())
        print("Informações da varredura:", resultado)
        print_open_ports(resultado, 'udp')

    elif menu == "3":
        print("Versão do Nmap:", scanner.nmap_version())
        resultado = scanner.scan(ip, '1-1024', '-v -sC')
        print("Status IP:", resultado[ip].state())
        print("Informações da varredura:", resultado)
        print_open_ports(resultado, 'tcp')

    else:
        print("Escolha uma opção correta.")

except Exception as e:
    print(f"Ocorreu um erro durante a varredura: {str(e)}")
