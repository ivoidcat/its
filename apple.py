import time, jwt

# 1. Create the JWT header
import requests

header = {
    "alg": "ES256",
    "kid": "S33TFDUPC3",  # your own key ID
    "typ": "JWT"
}
# 2.1 Create the JWT payload
payload = {
    "iss": "abbb439d-91b5-4b05-8198-1d1498838a1e",
    # 在Store Connect上可以点击复制 iss ID
    "exp": int(time.time()) + 60 * 10,
    # token最长有效时间20min，这里设置为10min
    "aud": "appstoreconnect-v1"
}

if __name__ == '__main__':
    # 2.2 privateKey 直接打开导入
    privatekey = open('/Users/dinglihuafushejishi/Desktop/Signature/p8/AuthKey_S33TFDUPC3.p8', 'rb').read()
    # 3. Sign the JWT
    print(privatekey)
    token = str(jwt.encode(payload=payload, key=privatekey, algorithm='ES256', headers=header), 'utf-8')
    print(token)

    # print(itsUtils.registerNewDevice(token, 'd2b3c62995ae4d1e718b013309a9e1a6fea81b94'))
    # print(itsUtils.registerNewBundleID(token, 'com.tes11111tkillld.cn'))
    # csr = open('/Users/dinglihuafushejishi/Desktop/Signature/CertificateSigningRequest.certSigningRequest', 'rb').read()
    # token = 'eyJraWQiOiJTMzNURkRVUEMzIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJhYmJiNDM5ZC05MWI1LTRiMDUtODE5OC0xZDE0OTg4MzhhMWUiLCJhdWQiOiJhcHBzdG9yZWNvbm5lY3QtdjEiLCJleHAiOjE1NjE3NzM4MjF9.xt9ssQ3pqFACkSO-0ERdFg8jhb5rvf1C_SAZG210xRBBCOhJSIdiVpsVuvN9iFoxNNm9-25iCLvKtIIPefd-1A'
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

