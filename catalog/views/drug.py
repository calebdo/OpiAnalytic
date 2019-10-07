from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from account import models as amod 
import http.client
import requests
import json


def calcQuant(drugID):
    y= []
    num = 0
    x = cmod.DrugPrescriber.objects.all()
    for item in x:
        if item.drug.id == drugID:
            y.append(item)
    for item in y:
        num += item.quantity_prescribed

    y.sort(key=lambda z: z.quantity_prescribed, reverse=True)
    return y

@view_function
def process_request(request, drug:cmod.Drug):
    details = drug

    

    url = "https://ussouthcentral.services.azureml.net/workspaces/e6b84d59fa974c2ca571e784e250973f/services/1886a08aa03149f1b4c4eaf182679f94/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DrugName\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + drug.name + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n}"
    headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer U6Sb5gd3t6bGFX+s5fh1RyM7PQISpy3YA56enxsKXWjjPicFJW205b92FxyLG5EbwWoWp1t/YJCN65c+ctfA/A==",
    'cache-control': "no-cache",
    'Postman-Token': "d531fa67-3b5b-41af-a9c4-0363b52c089b"
    }

    related = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    results = json.loads(related.text)
    rel1 = str(results["Results"]["output1"]["value"]["Values"][0][1])
    rel2 = str(results["Results"]["output1"]["value"]["Values"][0][2])
    rel3 = str(results["Results"]["output1"]["value"]["Values"][0][3])
    rel4 = str(results["Results"]["output1"]["value"]["Values"][0][4])
    rel5 = str(results["Results"]["output1"]["value"]["Values"][0][5])

    relOutput = [rel1,rel2,rel3,rel4,rel5]
    relatedDrugs = []
    for ro in relOutput:
        relatedDrugs.append(cmod.Drug.objects.get(name=ro))

    pres = calcQuant(drug.id)

    return request.dmp.render('drug.html', {
        'details': details,
        'relatedDrugs': relatedDrugs,
        'pres': pres,
    })