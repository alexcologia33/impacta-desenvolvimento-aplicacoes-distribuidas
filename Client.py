import requests as req

url = "http://localhost:5000/alunos"

print("Cadastrando alunos")

aluno = {"ra":"1700072", "nome":"Alex Augusto"}
print(req.api.post(url, json=aluno).json())

aluno = {"ra":"1700693", "nome":"Cinthia Queiroz"}
print(req.api.post(url, json=aluno).json())

aluno = {"ra":"1700381", "nome":"Michael da Silva de Souza"}
print(req.api.post(url, json=aluno).json())

aluno = {"ra":"1700603", "nome":"Fabio Aurelio Abe Nogueira"}
print(req.api.post(url, json=aluno).json())

aluno = {"ra":"1601606", "nome":"Gabriel Bueno"}
print(req.api.post(url, json=aluno).json())

aluno = {"ra":"1700054", "nome":"Henrique Borges da Silva"}
print(req.api.post(url, json=aluno).json())

aluno = {"ra":"1700677", "nome":"Diego santos"}
print(req.api.post(url, json=aluno).json())

print("Lista alunos")
print(req.api.get(url).json())

print("Cria forum")
Forum = {"ForumId":"1", "OwnerId":"1700072", "Title": "Title", "Description":"Description", "CreateDate":"10/10/2017", "LastPostDate":"10/10/2017", "Active":True}

url = "http://localhost:5000/forum"
print(req.api.post(url, json=Forum).json())

print("Lista forum")
print(req.api.get(url).json())

print("Registrar aluno no forum")

url = "http://localhost:5000/forum/register"
print(req.api.post(url, json={"ForumId":"1", "ra":"1700693"}).json())
print(req.api.post(url, json={"ForumId":"1", "ra":"1700603"}).json())

print("Tirar registro do aluno no forum")
url = "http://localhost:5000/forum/unregister"
print(req.api.post(url, json={"ForumId":"1", "ra":"1700603"}).json())

print("Criar post no forum")
Postagem = {"PostId":"1", "ForumId": "1", "OwnerId":"1700693", "CreateDate":"10/10/2017", "Message": "Teste", "Visible":True}
url = "http://localhost:5000/forum/post"
print(req.api.post(url, json=Postagem).json())

print("Posts do forum")
url = "http://localhost:5000/forum/1/post?ra=1700693"
print(req.api.get(url).json())


print("Ler post")
url = "http://localhost:5000/forum/post/1?ra=1700693"
print(req.api.get(url).json())

