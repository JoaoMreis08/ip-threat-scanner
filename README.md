# IP Threat Intelligence Scanner

Um script em Python desenvolvido para automatizar a verificação de reputação de endereços IP, utilizando a API do **AbuseIPDB**. Ideal para analistas de SOC e pesquisadores de segurança que precisam validar ameaças rapidamente.

## Funcionalidades
- **Verificação em Tempo Real:** Consulta a base de dados do AbuseIPDB para identificar IPs maliciosos.
- **Score de Confiança:** Retorna a probabilidade de abuso em escala percentual (0-100%).
- **Geolocalização Básica:** Identifica o país de origem do tráfego.
- **Segurança de Credenciais:** Implementação de variáveis de ambiente (`.env`) para proteção de chaves de API.

## Tecnologias
- [Python 3.x](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/)
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)
- [AbuseIPDB API](https://www.abuseipdb.com/)

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone (https://github.com/JoaoMreis08/ip-threat-scanner.git)


2. Instale as dependências:

    pip install -r requirements.txt


3. Configure sua API Key:

    Crie um arquivo .env na raiz do projeto.
    Adicione sua chave: ABUSE_API_KEY=sua_chave_aqui

4. Execute o programa:

    python main.py
