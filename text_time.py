import time
from datetime import datetime
import bs4
from bs4 import BeautifulSoup
import requests
import twilio
from twilio.rest import Client



def text(body):
    account_sid = "#"
    auth_token = "#"
    client = Client(account_sid, auth_token)
    client.messages.create(to="#", from_="#", body=body)
    client.messages.create(to="#", from_="#", body=body)

if __name__ == "__main__":
	text("3:51")
