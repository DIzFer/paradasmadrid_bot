import requests

def obtener_autobuses(parada, claves):
    url = "https://openbus.emtmadrid.es:9443/emt-proxy-server/last/geo/GetArriveStop.php"
    datos = {
        "idClient": claves["id_client"],
        "passKey": claves["key"],
        "idStop": parada,
        "cultureInfo": "ES"
        }
    print(datos)
    return requests.post(url, datos, verify=True).json()

def presentar_autobuses(json): 
    autobuses = ""
    autobus = "{} en {} minutos\n"
    for llegada in json["arrives"]:
        if llegada["busTimeLeft"] == 999999:
            continue
        elif int(round(llegada["busTimeLeft"]/60, 0)) == 0:
            autobuses += "{} ya\n".format(llegada["lineId"])
        else:
            autobuses += autobus.format(llegada["lineId"], int(round(llegada["busTimeLeft"]/60, 0)))
    return autobuses

