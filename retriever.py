import requests
import json
import schedule
import datetime

day = int(datetime.datetime.now().strftime ("%d"))-1


r = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=GBP&apikey=CI01JL2ZAULIBQZ8')
python_obj = json.loads(r.text)
print (python_obj["Time Series (Digital Currency Monthly)"]["2017-11-%s"%(day)]["1a. open (GBP)"])

