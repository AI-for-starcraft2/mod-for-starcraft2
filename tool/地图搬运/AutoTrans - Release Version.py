import sys
import uuid
import requests
import hashlib
import time
from importlib import reload

import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '4a30411b17f8f78e'
APP_SECRET = 'Jf2794FXdngm0fYAOig5CpWF1J44TXq8'
path='D:\Lab\AutoTrans\\'

def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def trans(q):
    global status
    if(q==''):
        return q
    try:
        data = {}
        data['from'] = 'EN'
        data['to'] = 'zh-CHS'
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
        sign = encrypt(signStr)
        data['appKey'] = APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign
        response = do_request(data)
        a=response.content.decode('utf-8')
        false=0
        true=1
        b=eval(a)
        print(b['translation'][0])
    except Exception:
        print('failed to connect to the server.text:',end='')
        print(q)
        status='FAIL'
        return q
    status='SUCCESS'
    return b['translation'][0]

def AutoTrans(text):
    newtext=''
    dptlist=re.findall('<.*?>',text)
    textlist = []
    textlist.append(text)
    for i in range(len(dptlist)):
        templist=textlist[-1].partition(dptlist[i])
        textlist.pop()
        for j in range(len(templist)):
            textlist.append(templist[j])
    for i in range(len(textlist)):
        if not re.match('<.*?>',textlist[i]):
            if textlist[i] != '':
                textlist[i]=connect(textlist[i])
        newtext=newtext+textlist[i]
    return newtext

import re
LR = re.compile('(.+?)=(.+)')
brackets = re.compile("<.+?>")
PREFIX=re.compile('(.+?)/')
status=''
logEnd=False

n=open(path+'GameStringsnew.txt','a+', encoding='utf-8')
f=open(path+'GameStrings.txt', encoding='utf-8')
log=open(path+'TranslationLog.txt','a+', encoding='utf-8')
log.seek(0)
num=0
while True:
    status='SKIP'
    num+=1
    line=f.readline().strip()
    if logEnd==False:
        logline=log.readline().strip()
        if logline=='':
            logEnd=True
        else:
            logline=logline.split('\t')
            if logline[1]=='SUCCESS'or logline[1]=='SKIP':
                continue
    m = (LR.search(line))
    if m:
        head=m.group(1)
        body = m.group(2)
        prefix = PREFIX.search(head)
        if prefix:
            prefix=prefix.group(1)
            if(ord(prefix[0])==65279):
                prefix=prefix[1:]
            if prefix!='Abil' and prefix!='Effect'and prefix!='DocInfo':
                textList = ['']
                bracketsList = []
                m = brackets.search(body)
                while m:
                    textList.append(body[0:m.start()])
                    bracketsList.append(m.group(0))
                    body = body[m.end():len(body)]
                    m = brackets.search(body)
                textList.append(body)
                body=''
                for i in range(len(textList)):
                    textList[i] = trans(textList[i])
                    body = body + textList[i]
                    if i < len(bracketsList):
                        body = body + bracketsList[i]
        n.write(head+'='+body+'\n')
    else:
        n.write(line)
    n.flush()
    print('finish line '+str(num))
    if logEnd==True:
        log.write(str(num)+'\t'+status+'\n')
        log.flush()
    if line=='':
        break
print('finished')
n.close()
f.close()
log.close()