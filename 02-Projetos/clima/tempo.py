import requests
import json

def obter_dados_tempo(cidade, api_key):
    """
    Obtém dados meteorológicos de uma cidade usando a API da OpenWeatherMap.
    """
    url_base = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",  # Para obter a temperatura em Celsius
        "lang": "pt"       # Para a descrição em português
    }
    
    try:
        resposta = requests.get(url_base, params=parametros)
        resposta.raise_for_status()  # Lança um erro se a resposta não for 200 (OK)
        dados = resposta.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao ligar à API: {e}")
        return None

# --- Início do Programa ---
# Substitui 'TUA_CHAVE_AQUI' pela tua chave da API da OpenWeatherMap
# Substitui 'Sua Cidade' pelo nome da cidade que queres
api_key_openweathermap = "1b6855b2aa4552e6cf951999ff14c7cc"
cidade_desejada = "São Paulo" 

dados_tempo = obter_dados_tempo(cidade_desejada, api_key_openweathermap)

if dados_tempo:
    # Extrair os dados relevantes
    nome_cidade = dados_tempo['name']
    temperatura = dados_tempo['main']['temp']
    descricao = dados_tempo['weather'][0]['description']
    humidade = dados_tempo['main']['humidity']
    
    # Criar a mensagem formatada
    mensagem = (
        f"Previsão do tempo para {nome_cidade}:\n"
        f"-------------------------------\n"
        f"Temperatura: {temperatura}°C\n"
        f"Condição: {descricao.capitalize()}\n"
        f"Humidade: {humidade}%\n"
        f"-------------------------------\n"
        f"Informação obtida do OpenWeatherMap."
    )
    
    # Mostrar a mensagem formatada
    print(mensagem)

else:
    print("Não foi possível obter os dados do tempo.")