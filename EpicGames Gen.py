import requests
import time

# ---
# Coded by RedDev,LogicLord,NegerSours!
# BombaClat
# Github: https://github.com/LeonWare
# this shi is open source
# ---

print("fast remake of my old operaGX gen just fixxed.\n\n discord.gg/dio\n\n\n")

def get_token():
  url = "https://api.gx.me/profile/token"
  headers = {
      'accept':
      'application/json',
      'accept-language':
      'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
      'authority':
      'api.gx.me',
      'cookie':
      'SESSION_TYPE=user; SESSION=NzFjMjg3NDAtMDhkOC00ODkwLWJhNzEtODA0YTcwMjNiM2U0',
      'origin':
      'https://www.opera.com',
      'referer':
      'https://www.opera.com/',
      'sec-ch-ua':
      '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
      'sec-ch-ua-mobile':
      '?0',
      'sec-ch-ua-platform':
      '"Windows"',
      'sec-fetch-dest':
      'empty',
      'sec-fetch-mode':
      'cors',
      'sec-fetch-site':
      'cross-site',
      'user-agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
  }

  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    data = response.json()
    return data['data']
  else:
    print("Failed to retrieve token")
    return None


def main():
  while True:
    token = get_token()
    if token:
      new_url = f"https://discord.com/billing/promotions/ebzkEMVWtKN29ZEru5UVeMxC/{token}"
      print(f"{new_url}\n\n")
      with open("token_url.txt", "a") as file:
        file.write(new_url + "\n")
    time.sleep(0.5)


if __name__ == "__main__":
  main()
