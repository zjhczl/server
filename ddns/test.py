import requests
import requests   #导包
import time


def getIp():
    r = requests.get('http://myip.ipip.net', timeout=6).text
    ip = r.split(" ")[1].split("：")[1]
    return ip

def setDomainIp(ip):
        url="https://dnsapi.cn/Record.Create" #拼接地址
        #参数
        body={"login_token":"412861,8eb56c565e88de8ff1bf75fa85501797",
              "format":"json",
              "domain":"zjhczl.xyz",
              "record_type":"A",
              "value":ip,
              "record_line":"默认",
              "sub_domain":"ssr"
              }
        #发送请求
        r=requests.post(url=url,data=body)
        #输出返回
        print(r.text)
print(getIp())
setDomainIp("119.8.116.203")
