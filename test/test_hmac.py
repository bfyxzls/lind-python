import base64
import hashlib
import hmac

secret = bytes('123456abcdef', 'utf-8')
message = bytes("""GET
/user-register-backend/backend/platform-account-rel/list
platformId=a50d6cfc-30a1-418a-a038-152d8d52db06
v6
Fri, 28 Mar 2025 06:51:20 GMT
x-demo:123
""", 'utf-8')

hash = hmac.new(secret, message, hashlib.sha256)

# to lowercase base64
print(base64.b64encode(hash.digest()))