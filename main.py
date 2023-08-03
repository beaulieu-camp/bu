from bs4 import BeautifulSoup
import json
import requests


urls = ["https://univ-rennes.libcal.com/widget/hours/today?iid=4074&systemTime=1&date=now","https://univ-rennes.libcal.com/widget/hours/today?iid=4074&systemTime=1&date=tomorrow"]

ret_liste = []

for url in urls :
    req = requests.get(url)
    
    if req.status_code != 200 : raise Exception("Api Univ Pété") 

    data=req.text
    state = BeautifulSoup(data,features="html.parser")

    liste = []

    trs = state.find_all("tr")

    for tr in trs :
        tds = tr.findAll("td")
        if tds == [] : continue

        nom = tds[0].text.replace("\n","")
        ouverture = tds[1].text.replace("\n","")

        liste.append({
            "nom":nom,
            "ouverture":ouverture
        })

    ret_liste.append(liste)


with open("./out/index.json","w+") as file:
    file.write(json.dumps(ret_liste))
