import json, requests, os

from requests.models import Response

BASE_URL = ' http://127.0.0.1:5000/'
dir_path = os.path.dirname(os.path.realpath(__file__))

#---------------------------------------Buscar Post----------------------------------------#
def searchPost(id):
    response = requests.get(f'{BASE_URL}posts/{id}') 
    print(response.status_code) 
    print(response.text)

#---------------------------------------Modificar Post----------------------------------------#
def changePost(id, data):
    response = requests.put(f'{BASE_URL}posts/{id}', json = data) 
    print(response.status_code) 
    print(response.text)

#---------------------------------------Edit Post----------------------------------------#
def editPost(post_id, title=None, body=None, userId = None):
    data = {
        "userId": userId,
        "title": title,
        "body": body
    }
    changePost(post_id, data)

#---------------------------------------Eliminar Post----------------------------------------#
def removePost(id):
    response = requests.delete(f'{BASE_URL}posts/{id}')
    print(response.status_code) 
    print(response.text) 

#---------------------------------------Subir Post----------------------------------------#
def loadPosts(data):
    response = requests.post(f'{BASE_URL}posts', json = data) 
    print(response.status_code) 
    print(response.text)

#---------------------------------------Guardar Posts----------------------------------------#
def savePosts():
    result = requests.get(f'{BASE_URL}posts')
    if result.status_code != 200:
        print('ERROR')
        exit(-1)

    # data = result.json()
    # user_id = data[0]['userId']

    with open(f'{dir_path}/posts.json', 'w') as f:
        # f.write(json.dumps(result.json(), indent=4))
        f.write(result.text)

#---------------------------------------Get Posts----------------------------------------#
def getPosts():
    result = requests.get(f'{BASE_URL}posts')
    if result.status_code == 200:
        return result.json()
    return []

#---------------------------------------Delete all Posts----------------------------------------#
def fullPostDelete():
    id=0
    while True:
        id+=1
        response = requests.delete(f'{BASE_URL}posts/{id}')
        if(response.status_code >= 400):
            break





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

#---------------------------------------Get Posts By User----------------------------------------#
def getPostByUserId(user_id, posts):
    pst = []
    for p in posts:
        if p["userId"] == user_id:
            pst.append(p)
    return pst







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

#--------------------------------------- Save users with info ----------------------------------------#
def saveFullUser(user_id):
    user = {}
    user["id"] = user_id
    user["posts"] = getPostByUserId(user_id, getPosts())
    for post in user["posts"]:
        post["coments"] = getCommentByPostId(post["id"])
        post.pop("userId")
        for coment in post["coments"]:
            coment.pop("postId")
    with open(f'{dir_path}/fullUsuario{user_id}.json', 'w') as f:
        json.dump(user, f, indent = 4)







#---------------------------------------Delete Comment----------------------------------------#
def removeComment(comment_id):
    response = requests.delete(f'{BASE_URL}comments/{comment_id}')
    print(response.status_code)

#---------------------------------------Get Comments----------------------------------------#
def getComments():
    result = requests.get(f'{BASE_URL}comments')
    if result.status_code == 200:
        return result.json()
    return []

#---------------------------------------Get Comment by ID----------------------------------------#
def getCommentById(id):
    result = requests.get(f'{BASE_URL}comments/{id}')
    return result.json()

#---------------------------------------Get Comment by Post Id----------------------------------------#
def getCommentByPostId(post_id):
    coms = []
    for coment in getComments():
        if coment["postId"]==post_id:
            coms.append(coment)
    return coms

#--------------------------------------Subir Comentarios----------------------------------------#
def loadComment(data):
    response = requests.post(f'{BASE_URL}comments', json = data) 
    print(response.status_code) 
    print(response.text)

#---------------------------------------Guardar Comentarios----------------------------------------#
def saveComments():
    with open(f'{dir_path}/comentarios.json', 'w') as f:
        f.write(json.dumps(getComments(), indent=4))

#--------------------------------------- Remove comments without posts ----------------------------------------#
def removeCommentsWithoutPost():
    post_id_list = [post["id"] for post in getPosts()]
    coms_list = getComments()
    for c in coms_list:
        if c["postId"] not in post_id_list:
            removeComment(c["id"])

def removeCommentsWithoutPostAndBackup():
    post_id_list = [post["id"] for post in getPosts()]
    deletedComents = []
    coms_list = getComments()
    for c in coms_list:
        if c["postId"] not in post_id_list:
            deletedComents.append(getCommentById(c["id"]))
            removeComment(c["id"])
    with open(f'{dir_path}/comentarioSinPostBackup.json', 'w') as f:
        f.write(json.dumps(deletedComents, indent=4))








#--------------------------------------- Main ----------------------------------------#

# data = {
#     "userId": 0,
#     "title": "Titulo",
#     "body": "Contenido del post"
# }



# changePost(1, data)
# fullDelete()
# savePosts()
# removePost(4)
# searchPost(4)
# print(json.dumps(getPostByUserId(2, getPosts()), indent=4))
# editPost(3, title="Titulo aaaaaaa", body="Body bbbbbbb", userId = "id qweqweqweqwe")
# savePosts()
# print(json.dumps(getComments(), indent=4))


# removePost(1)
# removeCommentsWithoutPost()
# savePosts()

# data = {
#         "body": "99999999999999999999999999999999maiores sed dolores similique labore et inventore et\nquasi temporibus esse sunt id et\neos voluptatem aliquam\naliquid ratione corporis molestiae mollitia quia et magnam dolor",
#         "email": "D99999999999999999999999999allas@ole.me",
#         "id": 123123,
#         "name": "9999999999999999999999repellat consequatur praesentium vel minus molestias voluptatum",
#         "postId": 21231
#     }
# loadComment(data)
# saveComments()


# removeCommentsWithoutPostAndBackup()
saveFullUser(6)

exit(0)