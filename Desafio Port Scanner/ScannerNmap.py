import nmap

scanner = nmap.PortScanner()

ip = input("Digite o ip a ser varrido: ")

menu = input("""\n Tipo de varredura a ser realizado
        [1] Tipo SYN
        [2] Tipo UDP
        [3] Tipo Intensa
        Digite a opção escolhida: """)
try:
    if menu == "1":
        print("Versão do Nmap ", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("Status IP: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print()
        print("Portas Abertas: ", scanner[ip]['tcp'].keys())

    elif  menu == "2":
        print("Versão do Nmap ", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("Status IP: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print()
        if 'udp' in scanner[ip]:
            print("Portas Abertas:", scanner[ip]['udp'].keys())
        else:
            print("Nenhuma porta UDP aberta encontrada.")

    elif menu =="3":
        print("Versão do Nmap ", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sC')
        print(scanner.scaninfo())
        print("Status IP: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print()
        if 'udp' in scanner[ip]:
            print("Portas Abertas: ", scanner[ip]['tcp'].keys())
        else:
            print("Nenhuma porta TCP aberta encontrada.")

    else:
        print("Escolha uma opção correta")
except:
    print(f"Ocorreu um erro durante a varredura.")