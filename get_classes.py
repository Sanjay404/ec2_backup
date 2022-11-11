import time
from datetime import datetime
import bs4
from bs4 import BeautifulSoup
import requests
import twilio
from twilio.rest import Client
import pickle

def get_open_sections(url):
    r = requests.get(url).text
    soup = bs4.BeautifulSoup(r, "html.parser")
    instructor_name = soup.findAll("span", {"class": "section-instructor"})
    section_id = soup.findAll("span", {"class": "section-id"})
    open_seats = soup.findAll("span", {"class": "open-seats-count"})
    return zip(instructor_name, section_id, open_seats)


def text(body):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    client.messages.create(to="#", from_="#", body=body)


if __name__ == "__main__":
    classes = {
        "Stat401":
       "https://app.testudo.umd.edu/soc/search?courseId=stat401&sectionId=&termId=202108&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on",
       "JOUR282":
       "https://app.testudo.umd.edu/soc/search?courseId=JOUR282&sectionId=&termId=202108&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
       ,
       "ENGL394":
       "https://app.testudo.umd.edu/soc/search?courseId=ENGL394&sectionId=&termId=202108&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
    }
    message = ""
    professors = ["Archana Khurana", "Sarah Oates"]
    for course in classes:
        check = get_open_sections(classes[course])
        for name, c_id, seats in check:
            name = name.text.strip()
            c_id = c_id.text.strip()
            seats = seats.text.strip()
            #print(f"{course}; section {c_id} with {name}: {seats} seat\n")
            if course == "Stat401" and int(seats) > 0 and c_id == "0401":
                message += f"{course}; section {c_id} with {name}: {seats} seat\n"
            if course == "ENGL394" and int(seats) <= 6 and c_id == "9016":
                message += f"{course}; section {c_id} with {name}: {seats} seat\n"
            if course!= "Stat401" and course!="ENGL394" and int(seats) > 0:
                message += f"{course}; section {c_id} with {name}: {seats} seat\n"
    try:
        log = pickle.load(open("log.p", "rb"))
    except:
        log = None
    if message and log != message:
        text(message)
    pickle.dump(message, open("log.p", "wb"))

  