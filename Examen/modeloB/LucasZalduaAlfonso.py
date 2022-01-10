import requests, json, os

from requests.models import Response

BASE_URL = 'http://127.0.0.1:5000/'
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_exam_version():
	# return 'a'
	return 'b'
	# return 'c'

def ejercicio1():
	posts = requests.get(f'{BASE_URL}posts')
	if posts.status_code != 200:
		return "Falla el GET"
	posts = posts.json()
	userList = []
	for p in posts:
		if p["userId"] not in userList:
			userList.append(p["userId"])
	return len(userList)

def ejercicio2():
	posts = requests.get(f'{BASE_URL}posts')
	if posts.status_code != 200:
		return "Falla el GET"
	posts = posts.json()
	try:
		for p in posts:
			if  "Nice job, Jennifer" in p["body"]:
				return p["id"]
		return "No se ha encontrado"
	except:
		return "Los Posts no tiene Body"

def ejercicio3():
	comms = requests.get(f'{BASE_URL}comments')
	if comms.status_code != 200:
		return "Falla el GET"
	comms = comms.json()
	for c in comms:
		c['name'] += ' (Examen)'
		c["body"] = ''
		a = requests.delete(f'{BASE_URL}comments/{c["id"]}')
		b = requests.post(f'{BASE_URL}comments', json = c)
	return

def ejercicio4():
	comms = requests.get(f'{BASE_URL}comments')
	if comms.status_code != 200:
		return "Falla el GET"
	comms = comms.json()
	try:
		for c in comms:
			if c['body'] == '':
				requests.delete(f'{BASE_URL}comments/{c["id"]}')
	except:
		return 'Los comentarios no tienen Body'
	return

def ejercicio5():

	def getMaxPostId():
		posts = requests.get(f'{BASE_URL}posts')
		if posts.status_code != 200:
			return "Falla el GET"
		posts = posts.json()
		if len(posts) > 0:
			maxId = posts[0]['id']
			for p in posts:
				if p['id'] > maxId:
					maxId = p['id']
			return maxId
		return 0

	with open(f'{dir_path}/new_comment.json', 'r') as f:
		comm = json.loads(f.read())
	comm['postId'] = getMaxPostId()
	result = requests.post(f'{BASE_URL}comments', json = comm)
	return result.json()["id"]

# No tocar
def reset_data(data = 'a'):
	requests.post(f'{BASE_URL}data/{data}')

def main():
	reset_data()
	print(ejercicio1())
	print(ejercicio2())
	print(ejercicio3())
	print(ejercicio4())
	print(ejercicio5())

# No tocar
if __name__ == "__main__":
	main()