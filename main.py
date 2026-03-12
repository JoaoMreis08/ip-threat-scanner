import requests
import os
import sys
import ipaddress
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Inicializa as cores no terminal
init(autoreset=True)

load_dotenv()
API_KEY = os.getenv("ABUSE_API_KEY")

def validate_ip(ip):
    """Verifica se a string é um IP válido antes de gastar a API."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def check_ip(ip_address):
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {'Accept': 'application/json', 'Key': API_KEY}
    params = {'ipAddress': ip_address, 'maxAgeInDays': '90'}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        
        score = data['abuseConfidenceScore']
        country = data['countryCode']
        
        # Lógica de Cores (Ideia 3)
        if score == 0:
            color = Fore.GREEN
            status = "[SEGURO]"
        elif score < 50:
            color = Fore.YELLOW
            status = "[SUSPEITO]"
        else:
            color = Fore.RED + Style.BRIGHT
            status = "[PERIGO - MALICIOSO]"

        print(f"{color}{status} IP: {ip_address} | Score: {score}% | País: {country}")

    except Exception as e:
        print(f"{Fore.RED}[ERRO] Não foi possível verificar o IP {ip_address}: {e}")

def main():
    if not API_KEY:
        print(f"{Fore.RED}[!] Erro: ABUSE_API_KEY não encontrada no .env")
        return

    print(f"{Fore.CYAN}--- IP Threat Scanner Pro ---")
    print("1. Verificar um único IP")
    print("2. Verificar lista de IPs (ips.txt)")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        target = input("Digite o IP: ")
        if validate_ip(target):
            check_ip(target)
        else:
            print(f"{Fore.RED}IP Inválido!")

    elif opcao == "2":
        if not os.path.exists("ips.txt"):
            print(f"{Fore.YELLOW}[!] Crie um arquivo chamado 'ips.txt' com um IP por linha.")
            return
        
        with open("ips.txt", "r") as f:
            lista_ips = [line.strip() for line in f if line.strip()]
        
        # Limite de segurança para não gastar a API toda (Ideia 1)
        LIMITE = 50 
        if len(lista_ips) > LIMITE:
            print(f"{Fore.YELLOW}[!] Lista muito grande ({len(lista_ips)}). Limitando aos primeiros {LIMITE} IPs.")
            lista_ips = lista_ips[:LIMITE]

        print(f"[*] Verificando {len(lista_ips)} IPs...\n")
        for ip in lista_ips:
            if validate_ip(ip):
                check_ip(ip)
            else:
                print(f"{Fore.RED}[IGNORADO] {ip} não é um formato de IP válido.")

if __name__ == "__main__":
    main()