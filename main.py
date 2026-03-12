import requests
import os
import sys
from dotenv import load_dotenv

# Carrega a chave da API do arquivo .env
load_dotenv()
API_KEY = os.getenv("ABUSE_API_KEY")

def check_ip(ip_address):
    """Verifica a reputação de um IP na API AbuseIPDB."""
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90',
        'verbose': True
    }

    try:
        print(f"[*] Analisando IP: {ip_address}...")
        response = requests.get(url, headers=headers, params=params)
        
        # Verifica se a requisição foi bem sucedida
        response.raise_for_status()
        
        data = response.json()['data']
        
        # Resultados
        score = data['abuseConfidenceScore']
        country = data['countryCode']
        usage = data.get('usageType', 'Desconhecido')
        
        print("-" * 30)
        print(f"RESULTADO PARA: {ip_address}")
        print(f"País: {country}")
        print(f"Tipo de Uso: {usage}")
        print(f"Score de Abuso: {score}%")
        
        if score > 50:
            print("[ALERTA] Este IP tem alta probabilidade de ser malicioso!")
        else:
            print("[INFO] Este IP parece ser seguro.")
        print("-" * 30)

    except requests.exceptions.HTTPError:
        print("[ERRO] Chave de API inválida ou limite de buscas atingido.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("[!] Erro: Chave API_KEY não encontrada no arquivo .env")
        sys.exit(1)
        
    target = input("Digite o IP para verificar (ex: 8.8.8.8): ")
    check_ip(target)