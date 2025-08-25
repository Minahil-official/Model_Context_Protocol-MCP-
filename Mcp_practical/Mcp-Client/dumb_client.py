# import requests

# url = "http://localhost:8000/mcp"

# payload = {
#     "jsonrpc":"2.0",
#     "method":"tools/list",
#     "params":{},
#     "id":3  
# }

# headers= {
#     "Content-Type":"application/json",
#     "Accept":"application/json,text/event-stream"
    
# }

# response = requests.post(url,headers=headers,json=payload,stream=True)

# for line in response.iter_lines():
#     if line:
#        print(line.decode("utf-8"))


