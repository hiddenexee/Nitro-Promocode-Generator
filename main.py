from os import system
from random import randint
from uuid import uuid4
from json import dumps
from requests import post
from threading import Thread, Lock

lock = Lock()

headers = {
  'authority': 'api.discord.gx.games',
  'accept': '*/*',
  'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/json',
  'origin': 'https://www.opera.com',
  'referer': 'https://www.opera.com/',
  'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}

def gen_user_id() -> str:
    return str(uuid.uuid4())

def gen() -> None:
    while True:
        try:
            res = post("https://api.discord.gx.games/v1/direct-fulfillment", headers=headers, data=dumps({
                "partnerUserId": gen_user_id()
            })).json()["token"]

            with lock:
                open("codes.txt", "a+").write(f"{code_url}{res}" + "\n")
                print(f"[+] Nitro code generated => {res}")
        except Exception as e:
          print(f"[-] Nitro code not generated => {e}")

if __name__ == '__main__':
    system("title Nitro Generator ^| @hiddenexe")
    code_url = "https://discord.com/billing/partner-promotions/1180231712274387115/"

    for _ in range(10):
        Thread(target=gen).start()



