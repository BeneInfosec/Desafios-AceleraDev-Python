from datetime import datetime
from operator import itemgetter


ENCARGO_FIXO = 0.36
TAXA_LIGACAO_MINUTO_DIURNO = 0.09
MANHA = '21:59:59'
NOITE = '06:00:00'

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]





def classify_by_phone_number(records):
	lista = [] # cria lista
	for item in records: #Para todo item na lista records
		comeco = str(datetime.fromtimestamp(item['start']))

		hora_comeco = int(datetime.strptime(comeco, '%Y-%m-%d %H:%M:%S').strftime("%H"))
		segundo_comeco = int(datetime.strptime(comeco, '%Y-%m-%d %H:%M:%S').strftime("%s"))
		
		final = str(datetime.fromtimestamp(item['end']))
		hora_final = int(datetime.strptime(final, '%Y-%m-%d %H:%M:%S').strftime("%H"))
		segundo_final = int(datetime.strptime(final, '%Y-%m-%d %H:%M:%S').strftime("%s"))
		source = item['source']
		#Comeca e termina de manha
		if hora_comeco >= 6 and hora_final < 22:
			minutos_totais = abs((segundo_final - segundo_comeco)//60)
			total = ENCARGO_FIXO + (TAXA_LIGACAO_MINUTO_DIURNO * minutos_totais)
		#Comeca de manha e termina a noite
		elif (hora_comeco >= 6 and hora_comeco < 22 ) and (hora_final >= 22 or hora_final < 6):
			data,tempo = final.split()
			novo_final = data + ' ' +  MANHA
			segundo_final = datetime.strptime(novo_final, '%Y-%m-%d %H:%M:%S')
			segundo_final = int(segundo_final.strftime("%s"))
			minutos_totais = abs((segundo_final - segundo_comeco)//60)
			total = ENCARGO_FIXO + (TAXA_LIGACAO_MINUTO_DIURNO * minutos_totais)
		#Comeca a noite e termina de manha
		elif (hora_comeco >= 22 or hora_comeco > 6) and (hora_final >= 6 and hora_final < 22) :
			data,tempo = final.split()
			novo_final = data + ' ' +  NOITE
			segundo_comeco = datetime.strptime(novo_final, '%Y-%m-%d %H:%M:%S')
			segundo_comeco = int(segundo_comeco.strftime("%s"))
			minutos_totais = abs((segundo_final - segundo_comeco)//60)
			total = ENCARGO_FIXO + (TAXA_LIGACAO_MINUTO_DIURNO * minutos_totais)
		#Comeca e termina a noite
		else:
			total = ENCARGO_FIXO

		adicionar_na_lista(source, total, lista)
	return(remover_duplicada(lista_de_strings(lista), lista))



def adicionar_na_lista(source, total, lista):
		dic = {}
		dic['source'] = source
		dic['total'] = round(total,2)
		lista.append(dic)

def lista_de_strings(lista):
	lista_contato_string = [] #Lista de strings
	for item in lista:
		if item['source'] not in lista_contato_string:
			lista_contato_string.append(item['source'])
	return lista_contato_string

def remover_duplicada(lista_contato_string, lista):
	lista_contato = []
	for i in lista_contato_string: #Cada elemento da lista de strings
		total_completo = 0
		for item in lista: # #Percorre a lista toda
		    if item["source"] == i:
		        total = item['total']
		        total_completo = total_completo + total
		        total_completo = round(total_completo, 2)

		lista_contato.append({"source": i, "total": total_completo})#
	return sorted(lista_contato, key=itemgetter('total'), reverse=True) #Ordenar pelo maior valor

print(classify_by_phone_number(records))