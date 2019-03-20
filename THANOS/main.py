from slackclient import SlackClient
from slackeventapi import SlackEventAdapter
import schedule
import time
import os

BOT_NAME = "thanos"
slack_token = os.environ["SLACK_SIGNING_SECRET"]  # I'll do it w/ secret signing.
sc = SlackClient(slack_token)

sea = SlackEventAdapter(slack_token, endpoint="/slack/events")
										#  SLACK_SIGNING_SECRET,
										
@sea.on("hear")
def handle_message(event_data):
	hear = event_data["event"]
	return hear
hear = handle_message()

def whispper():
	somebody = hear["user"]
	return somebody

def say(something, towho = False):
	global channel
	channel = hear["channel"]
	tosay = something
	return sc.apicall("chat.postMessage",
						channel = channel,
						text = tosay,
						user = towho)		

if hear.get("subtype") is None and "hi" in hear.get['text']:
	greetings = "Hello <@%s>! :tada:" % hear["user"]
	say(greetings)

count = 0

quantite = 0  # número de necesidades


def need(number):
	needl = "need" + str(number + 1)
	return needl

def end(game):
	return schedule.cancel_job(game)


repetidas = {}
def checking(ou, t):
	# ou = word
	# t  = list
	for n in range(3):
		if ou in t(n + 1): # needs
			if ou not in repetidas:
				repetidas[ou] = 0

			repetidas[ou] = + 1
			'''
			#continuar. Echarle un ojo! Fue lo  ultimo que escribí		
			# ..esta raro esta funcion, tenia sueño ya. LISTO :) '''

'''
seeds = { "need1" : 0,
		  "need2" : 0,
		  "need3" : None}
'''
class Seed:
		
		def __init__(self, seed):
			# its 'name', e. g. need1 = Seeds('')
			'''The name will be 'need'+ str(number) <- it is need(), formely.'''
      # EXAMPLE: 
			# mot = message['text'] <- it's relation w/ hear= handle_message()
      # needl = need()
			# needl.add_mot('mot')
			# then, if we print(need1.mot) -> ['', '', 'etc']
			self.seed = seed
			self.mots = []

		def add_mot(self, mot):
			self.mots.append(mot)
			self.submots = []

		def add_submot(self, submot):
			self.submots.append(mot)


def mot2harvest(nro, dicc,):
	counter = 0
	
	for x in range(nro):
		needl = need(x)

	return None  #building it...


def mot1harvest(nro, cuenta=0):
	cuenta = + 1
	seed = need(cuenta)  # llamo seed a las necesidades primas.
		
	say(seed)  # tell = ..DONE.
	# ^ el say debe ir aquí para que pueda decir la NECESIDAD.
	'''say = None # función que hace decir algo, y la de Needs.
	reemplazado por 'tell'.''' # not after all haha.
	seeds[seed] = convertlist(seeds[seed])
	# aquí se está convirtiendo en lista el 'value' de la necesidad prima.

	if cuenta < nro:
		return cuenta
	else:
		end(mot1harvest)
		time.sleep(60)

		return mot2harvest(nro, seeds) #TODO.


def uP(): # getting ready!
  userPrepare = ["start", "La siembra", "harvest", "la siembra", "sembrar"]
	for i in range(len(userPrepare) + 1):
		up = userPrepare[i]
		return up # user prepare

global principal
if hear.get("subtype") is None and uP() in hear.get['text']:
	principal = whispper
	comeon = "Give me/dame the seeds/las semillas, <@%s>" % hear["user"]
	say(comeon)


users = []
def soul():
	api_call = sc.api_call("users.list")
	if api_call.get('ok'):
		members = api_call.get('members')
		for user in members:
			if 'name' in user and user.get('name') == (BOT_NAME or "Thanos"):
				global BOT_ID
				BOT_ID = '<@{}>'.format(user.get('id'))
    users = api_call
		return users


participants = {principal, } '''  # (sets).
 done_TODO HEAR THE MESSAGE AND SAVE THE SEEDS/NEEDS into the dictionary "seeds".'''
if hear.get("subtype") is None and (whispper == principal) and (len(participants) == 1):
  banned = ['', " ", ",", "y", "and", "et"]
  # ^ later we should create a properly file! (AI alike, huh).

  for y in range(len(banned)):
    aux = hear["text"]
    
    supre = banned[y]
    if supre in aux:
      aux.remove(supre)
  for x in range(len(aux)):
      d = Seed(aux[x])

      seeds[need(x)] = d.seed  # dict[key] = value
  # print(need(x)) -> prints that respective value !
  # need(x).add_mot(WORD) # adds a mot into the [value] Seed class.
  say("Registrado, necesidades: " + print(seeds), whispper)
	
	@soul()
  # now, we start to ask people who wants to join the harvesting!
	while True:

		time.sleep(1)
		if hear.get("subtype", whispper) is None and ("listo" or "ready"):
			break
		if hear.get("subtype") is None and ("yo" or "Yo" or "I" or "i" or ":raising_han:" or "me" or 'moi' or ) in hear.get['text']:
			participants.add(whispper())

say("Ok, let's start!")

schedule.every(60).seconds.do(mot1harvest(quantite=len(aux), count)

