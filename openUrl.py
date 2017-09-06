import requests

r = requests.get("http://www.google.com", 
                 proxies={"http": "http://ngproxy.persistent.co.in:8080"})
print(r.text)
