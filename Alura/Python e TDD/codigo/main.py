import requests

# Substitua 'SEU_TOKEN_AQUI' pelo token real do seu bot
token = '6530505719:AAEiA_W7zir3838cgW8aGjy47USiVLlSR60'

# Substitua 'ID_DO_CHAT' pelo ID do chat para o qual você deseja obter as mensagens
chat_id = '-4033044915'

# URL da API para obter atualizações
api_url = f'https://api.telegram.org/bot{token}/getUpdates'

# Parâmetros da solicitação
params = {
    'offset': 1000,
    'limit': 1,
    'timeout': 30
}

# Envie a solicitação
response = requests.get(api_url, params=params)

# Obtenha e processe as mensagens
updates = response.json().get('result', [])
for update in updates:
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    
    # Faça algo com o chat_id e o texto da mensagem, por exemplo, imprimir no console
    print(f"Chat ID: {chat_id}, Mensagem: {text}")
