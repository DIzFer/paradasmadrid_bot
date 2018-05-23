import requests

def obtener_autobuses(parada, claves):
    url = "https://openbus.emtmadrid.es:9443/emt-proxy-server/last/geo/GetArriveStop.php"
    datos = {
            "idClient": claves["id_client"],
            "passKey": claves["key"],
            "idStop": parada,
            "cultureInfo": "ES"
            }
    return requests.post(url, datos, verify=True).json()
