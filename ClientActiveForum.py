import requests as Req

Url = "http://localhost/forums/forum/activate"

Forum = {"ForumId":"1", "OwnerId":"Alan"}
Retorno = Req.api.post(Url, json = forum).json()

print (Retorno)