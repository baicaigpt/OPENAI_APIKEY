import http.client
import json

conn = http.client.HTTPSConnection("api.baicaigpt.cn")
payload = json.dumps({
   "model": "gpt-3.5-turbo",
   "messages": [
      {
         "role": "system",
         "content": "You are a helpful assistant."
      },
      {
         "role": "user",
         "content": "Hello!"
      }
   ]
})
headers = {
   'Authorization': 'Bearer sk-eyJhbGciO..........',
   'Content-Type': 'application/json'
}
conn.request("POST", "/v1/chat/completions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
