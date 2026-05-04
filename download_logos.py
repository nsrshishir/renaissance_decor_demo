import os
import urllib.request

logos = {
    "BASB": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Bangladesh_Armed_Forces_emblem.svg",
    "Shanta": "https://shantalifestyle.com/wp-content/uploads/2023/11/shanta-lifestyle-logo.png",
    "Premier": "https://premier1888.com/wp-content/uploads/2020/07/logo.png",
    "Agileminds": "https://agileminds.com/wp-content/uploads/2021/04/AgileMinds_logo_web.png",
    "MU": "https://mucycles.com/wp-content/uploads/2022/01/logo.png",
    "IDIYA": "https://idiya.co.nz/cdn/shop/files/Idiya_Logo_2021.png"
}

os.makedirs("Client_logo", exist_ok=True)
for name, url in logos.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(f"Client_logo/{name}.png", 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
