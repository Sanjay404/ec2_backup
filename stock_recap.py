import time
from datetime import datetime
import bs4
from bs4 import BeautifulSoup
import requests
import twilio
from twilio.rest import Client

def get_stocks(url):
    r = requests.get(url).text
    soup = bs4.BeautifulSoup(r, 'html.parser')
    alldata = soup.find_all("tbody")
    try:
        table1 = alldata[0].find_all("tr")
    except:
        table1 = None
    try:
        table2 = alldata[1].find_all("tr")
    except:
        table2 = None
    l={}

    for i in range(0,len(table1)):
        try:
            table1_td = table1[i].find_all('td')
        except:
            table1_td = None
        l[table1_td[0].text] = table1_td[1].text
    return l

def text(name , dic, mess_type):
    date_time = time.strftime("%b %d %Y %-I:%M %p")
    body = (f"{name} as of {date_time} \n")

    if mess_type == 'morning':
            body+= f"{'Previous Close'}: {dic['Previous Close']} \n"
            body+= f"{'Open'}: {dic['Open']} \n"
    elif mess_type == 'evening':
        for key in dic:
            body+= f"{key}: {dic[key]} \n"

    # put your own credentials here
    account_sid = "#"
    auth_token = "#"
    client = Client(account_sid, auth_token)
    client.messages.create(
    to="#",
    from_="#",
    body=body)


if __name__ == '__main__':
    stocks = {"TESLA":'https://finance.yahoo.com/quote/TSLA?p=TSLA', 
    "UBER": 'https://finance.yahoo.com/quote/UBER?p=UBER&.tsrc=fin-srch', 
    "LYFT": 'https://finance.yahoo.com/quote/LYFT?p=LYFT&.tsrc=fin-srch',
    "DISNEY": 'https://finance.yahoo.com/quote/DIS?p=DIS&.tsrc=fin-srch',
    "APPLE" : 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch', 
    "GOOGLE" : 'https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch'
    }
     
    current_time = datetime.utcnow() #checks UTC time
    if(current_time.hour == 13):
        for key in stocks.keys():
            text(key, get_stocks(stocks[key]), 'morning')
    elif(current_time.hour == 20):
        for key in stocks.keys():
            text(key, get_stocks(stocks[key]), 'evening')
    
