from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from datetime import datetime, timezone
import http.client

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, page:int=1):
   
    conn = http.client.HTTPConnection("ussouthcentral,services,azureml,net")

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"PrescriberID\",\r\n        \"DrugName\",\r\n        \"Qty\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"1003002320\",\r\n          \"METHOTREXATE\",\r\n          \"0\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n}"

    headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer Dar11aHTeOSCBG2Royb/IswYfoT5op9cLerElEoXAl9AvJl2uSqqwvdxWvEk8KnxZL9LEQbDr+gZP1iFue7DUQ==",
    'cache-control': "no-cache",
    'Postman-Token': "cbd578eb-a280-443e-b07e-51301bc85080"
    }

    conn.request("POST", "workspaces,e6b84d59fa974c2ca571e784e250973f,services,aa7ebeeafa9c43c1a300b9fb85aa6e9c,execute", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    context = {
    }

    return request.dmp.render('recommender.html', context)
    