# Programa de calculo de tasa de cambio VEF/CLP

import urllib.request
import urllib.error
import json
import datetime

vefCLP = 0

url = "https://s3.amazonaws.com/dolartoday/data.json";
url2 = "http://mindicador.cl/api";

mensaje = """
#################################
#### Convertidor CLP a VEF ####
#################################
"""
print(mensaje)

try:
  print("Consultando USD/CLP...")
  respuesta2 = urllib.request.urlopen(url2)
  datapeso = respuesta2.read()
  datapeso = datapeso.decode(encoding='UTF-8', errors='replace')
  data2 = json.loads(datapeso)
  peso = ((data2['dolar']['valor']))
  print("USD/CLP: " + str(peso))
except urllib.error.URLError:
  print("**** Pagina de mindicador.cl no encontrada ****")

try:
  print("Consultando a Dolartoday...")
  respuesta1 = urllib.request.urlopen(url)
  datadolar = respuesta1.read()
  datadolar = datadolar.decode(encoding='UTF-8', errors='replace')
  data = json.loads(datadolar)
  dolar = ((data['USD']['promedio']))
  print("USD/VEF: " + str(dolar))
except urllib.error.URLError:
  print("**** Pagina de DolarToday no encontrada ****")

vefCLP = round(dolar / peso, 2)
print("#### TASA CLP/VEF ####")
print(vefCLP)
