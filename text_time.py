import time
from datetime import datetime
import bs4
from bs4 import BeautifulSoup
import requests
import twilio
from twilio.rest import Client



def text(body):
    account_sid = "ACef4e810916850ca7e12a626e3aa23da8"
    auth_token = "e7f7bb7c77c78a66de0fa9c9a85c2e4a"
    client = Client(account_sid, auth_token)
    client.messages.create(to="9087312915", from_="17609144209", body=body)
    client.messages.create(to="4437725818", from_="17609144209", body=body)

if __name__ == "__main__":
	text("4:20")
