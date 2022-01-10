import json, requests, os

BASE_URL = 'https://jsonplaceholder.typicode.com/'
dir_path = os.path.dirname(os.path.realpath(__file__))

#---------------------------------------Modificar Comentario----------------------------------------#
def changePost(id, data):
    response = requests.put(f'{BASE_URL}posts/{id}', data) 
    print(response.status_code) 
    print(response.text)



# dataaa = {
#     'userId':1,
#     "title": "Test de Python",
#     "body": "doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores"
#     }

# changePost(20, dataaa)

# exit(0)
#---------------------------------------Eliminar Comentario----------------------------------------#
def deletePost(id):
    response = requests.delete(f'{BASE_URL}posts/{id}') 
    print(response.status_code) 
    print(response.text) 

#---------------------------------------Subir Comentario----------------------------------------#
def loadPosts(data):
    #data = {
    #   'userId':1,
    #   "title": "Test de Python",
    #   "body": "doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores"
    # } 
    response = requests.post(f'{BASE_URL}posts', data) 
    print(response.status_code) 
    print(response.text) 

#---------------------------------------Users con Comentarios----------------------------------------#
def loadUsersAndPosts():
    users = requests.get(f'{BASE_URL}users')
    if users.status_code != 200:
        print('ERROR')
        exit(-2)
    users = users.json()

    for u in users:
        coments = requests.get(f'{BASE_URL}posts/?userId={u["id"]}')
        if coments.status_code != 200:
            print(f'ERROR in {u}')
            exit(-1)
        u['posts'] = coments.json()
        for k in u['posts']:
            k.pop('userId', None)

    with open(f'{dir_path}/usuarios.json', 'w') as f:
        f.write(json.dumps(users, indent=4))

#---------------------------------------Guardar Comentarios----------------------------------------#
def savePosts():
    result = requests.get(f'{BASE_URL}posts')
    if result.status_code != 200:
        print('ERROR')
        exit(-1)

    # data = result.json()
    # user_id = data[0]['userId']

    with open(f'{dir_path}/comentarios.json', 'w') as f:
        # f.write(json.dumps(result.json(), indent=4))
        f.write(result.text)


#---------------------------------------Guardar Usuarios-------------------------------------------#


def saveUsers():
    result = requests.get(f'{BASE_URL}users')
    if result.status_code != 200:
        print('ERROR')
        exit(-2)
    with open(f'{dir_path}/usuarios.json', 'w') as f:
        f.write(result.text)

    user = result.json()
    print(user)

#-------------------------------------------------------------------------------------------------------------------------------#

# result = requests.get(f'{BASE_URL}users')

# if result.status_code != 200:
#     print('ERROR')
#     exit(-2)

# def getUserById (userDict, userId):
#     for user in userDict:
#         if user['id'] == userId:
#             return user
#     return None

# users = result.json()
# user = getUserById(users, 1)
# print(user)

#-------------------------------------------------------------------------------------------------------------------------------#

#print(f"{data[0]['body']}")

# print(result.status_code)

