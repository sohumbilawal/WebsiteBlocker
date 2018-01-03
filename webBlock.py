import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
web_list = ["www.facebook.com", "facebook.com", "https://mail.google.com/mail/u/0/#inbox"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16, 55):
        print("Working hours...")
        #print(1)
    else:
        print("Fun hours...")
    time.sleep(5)
