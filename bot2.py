import time
import requests
print ("conectando ao server...")
print ("bot em funcionamento, analizando e monitorando em tempo real...")
while True:
	try:
		url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
		resposta = requests.get(url)
		moedas_virtuais = resposta.json()
		moedas_vips = moedas_virtuais [:20]
		print (f"⏰ [Análise de Mercado realizada em: {time.strftime('%H:%M:%S')}]")
		for coin in moedas_vips:
			nome = coin["name"]
			preco_atual = coin["current_price"]
			rank = coin["market_cap_rank"]
			variacao = coin["price_change_percentage_24h"]
			print (f"Rank {rank} | {nome}: U$ {preco_atual} ({variacao:+.2f}%)")
			if variacao <= -5.0:
				print (f"🚨 [ALERTA OPÇÃO DE COMPRA] {nome} (Rank {rank}) está derretendo! Queda de {variacao:.2f}% nas últimas 24h. Preço atual: U$ {preco_atual}")
		with open ("criptos_promissoras.txt", "w") as arquivo:
			arquivo.write("---RELATORIO COMERCIAL TOP 15 CRIPTOS---\n\n")
			arquivo.write(f"Última varredura: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
			for coin in moedas_vips:
				arquivo.write(f"Rank: {coin['market_cap_rank']} | {coin['name']} | Preço: U$ {coin['current_price']} | 24h: {coin['price_change_percentage_24h']:.2f}%\n")
		print ("aguardando 1h até a proxima verificação💤")
		time.sleep(3600)
	except Exception as e:
		print ("⚠️erro de conexão, tentando novamemte em 1 minuto")
		time.sleep(60)
