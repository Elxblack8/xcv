import requests
import hashlib
url="https://services.orange.eg/GetToken.svc/GenerateToken"
headers={
"net-msg-id":"234ce4a3021281d16933261842581002","x-microservice-name":"APMS", "Content-Type":"application/json; charset=UTF-8","Content-Length":"78","Host":"services.orange.eg","Connection":"Keep-Alive",
"Accept-Encoding":"gzip",
"User-Agent":"okhttp/3.14.9"
 }
data={
  "channel": {
    "ChannelName": "MobinilAndMe",
    "Password": "ig3yh*mk5l42@oj7QAR8yF"
  }
}
req=requests.post(url, headers=headers,json=data).json()
ext_ctv=req["GenerateTokenResult"]["Token"]
ctv=ext_ctv
def encrypt_string(hash_string):
    htv = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return htv
hash_string = ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
ext_htv= encrypt_string(hash_string)
htv=ext_htv.upper()
print(ctv+"\n"+htv)
#===========≈====================
