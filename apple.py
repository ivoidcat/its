import time, jwt

# 1. Create the JWT header
import requests

header = {
    "alg": "ES256",
    "kid": "文档中提到的kid",
    "typ": "JWT"
}
# 2.1 Create the JWT payload
payload = {
    "iss": "文档提到的iss",
    # 在Store Connect上可以点击复制 iss ID
    "exp": int(time.time()) + 60 * 10,
    # token最长有效时间20min，这里设置为10min
    "aud": "appstoreconnect-v1"
}

if __name__ == '__main__':
    # 2.2 privateKey 直接打开导入
    privatekey = open('读取p8文件', 'rb').read()
    # 3. Sign the JWT
    print(privatekey)
    token = str(jwt.encode(payload=payload, key=privatekey, algorithm='ES256', headers=header), 'utf-8')
    print(token)
    url = 'https://api.appstoreconnect.apple.com/v1/apps'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token,
    }
    print(token)
    print(requests.get(url, headers=headers).text)
    # requests.post(url, headers=headers, data=json.dumps(data))

    # print(csr.decode())
    # itsUtils.createCertificate('', csr.decode('utf-8'))

