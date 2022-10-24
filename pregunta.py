"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    #
    # Inserte su código aquí
    #
    # archivo = open("C:/Users/jlopezl/OneDrive - Renting Colombia S.A/Archivos/Personal/Especializaci�n/Ciencia de los datos/data-ingestion---clusters-report-JuanesLopez/clusters_report.txt", mode="r")
    archivo = open("clusters_report.txt", mode="r")
    
    crudo = [re.sub('^\s+$', '\n', line) for line in archivo.readlines()]
    crudo = crudo[4:]
    
    limpio1=[]
    aux = ""
    
    for i in crudo:
        if i != "\n":
            aux += " " + i.replace("\n", "").strip()
        else:
            aux.strip()
            limpio1.append(aux)
            aux = ''
           
    limpio1 = [i.strip() for i in limpio1]
    
    limpio2 = []
    
    for i in limpio1:
        aux = re.search('(^[0-9]+)\s+([0-9]+)\s+([0-9]+),([0-9]) %\s+(.+)$', i)
        aux2 = aux.group(1)+"*"+aux.group(2)+"*"+aux.group(3)+"."+aux.group(4)+"*"+re.sub('\s{2,}','',aux.group(5))
        limpio2.append(aux2)
    
    limpio2 = [i.split("*") for i in limpio2]
    datos = pd.DataFrame(data=limpio2, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    
    palabras = [i.split(",") for i in datos['principales_palabras_clave']]
    for i in range(len(palabras)):
        palabras[i] = [palabra.strip() for palabra in palabras[i]]
    
    datos['principales_palabras_clave'] = [", ".join(i).replace(".","") for i in palabras]
    
    datos['cluster'] = datos['cluster'].astype('int')
    datos['cantidad_de_palabras_clave'] = datos['cantidad_de_palabras_clave'].astype('int')
    datos['porcentaje_de_palabras_clave'] = datos['porcentaje_de_palabras_clave'].astype('float')
    return datos
