import requests
from sklearn import svm
import json


symbols = ["NBEV", "NEM", "AMD", "MKTX", "NVDA", "REGN",
           'NLOK', 'HUM', 'VRTX', 'RMD', 'APPL', 'ODFL', 'MSCI', 'CTXS', 'DVA', 'SBAC', 'TGT', 'DG', 'MSFT', 'LDOS', 'ANSS']

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-news"
for symbol in symbols:
    querystring = {"region": "US", "category": symbol}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "905e430bd0mshd43484628817f0ap1f4dcfjsn2ce124f44cdb"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    # print(response.text)

    '''with open(('./data.json'), 'w') as f:
      json.dump(response.text, f)'''
    with open(('./data'+symbol+'.json'), 'w') as f:
        json.dump(response.json(), f)
    print(response.json())
