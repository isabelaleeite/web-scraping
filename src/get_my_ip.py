import requests


url = "http://lumtest.com/myip.json"
url2 = "https://globo.com" 


response = requests.get(url2)

if response.status_code == 200:
    print(response.json())
    
else:
    print("Erro")
