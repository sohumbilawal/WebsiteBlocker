import time
from datetime import datetime as dt

hosts = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
web_list = ["www.facebook.com", "facebook.com", "mail.google.com", "www.mail.google.com", "mail.google.com/mail/?authuser=0"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            hosts_content = file.read()
            for website in web_list:
                if website in hosts_content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            hosts_content=file.readlines()
            file.seek(0)
            for line in hosts_content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
