from slackclient import SlackClient
from slackeventapi import SlackEventAdapter
import schedule
import os

BOT_NAME = "thanos"
slack_token = os.environ["SLACK_SIGNING_SECRET"] # I'll do it w/ secret signing.
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
hand = True
quantite = 0  # número de necesidades


def need(number):
	needl = "need" + str(number + 1) 
	return needl


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


seeds = { "need1" : 0,
		  "need2" : 0,
		  "need3" : 0}

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


def mot2harvest(nro):
	#nro de 'cuenta'.
  global nro  
  hand = False
  counter = 0
	
  while nro > 0: # it should start with 2 or 3, and decreasing.
	  nro = - 1

    needl = need(counter) # c'est le même qui 
    say()
  

  say()# -->  the words added into the list add_mot() !


  
	return say()  #building it...


def mot1harvest(quantite, cuenta = 0):
  
  planted = need(cuenta)
  cuenta = + 1 

  # planted.add_mot('input') ..it has to be in the listening.
  say(print(seeds[planted])

  if cuenta < quantite: # quantite = len(aux) <- Seeds.
		return cuenta
	else:
		end(mot1harvest)

		#time.sleep(60) # this function can't be.. 'cause we need Thanos keeps listening the words!

    def timeSleep():
      schedule.every().minute.do(schedule.clear('1st')).tag('1st') # making sure it'll do it just once.

      say("2nd -")
      return mot2harvest(cuenta) #nro, seeds) ..nope TODO.
                      # ^ Still blding..

		return schedule.every().minute.do(timeSleep()).tag('1st', 'harvest')


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


def soul():
  global users
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

  ''' I've just realized that this next before decoration could be a
  function, in fact this is "the SEEDING", so it'd be actually -def-
  seeding():                    '''
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
  sayP = "Registrado, necesidades: " + print(seeds)
  say(sayP, whispper)
	
	@soul()
  # now, we start to ask people who wants to join the harvesting!
	while True:

		time.sleep(1)
		if hear.get("subtype", whispper) is None and ("listo" or "ready") in hear.get["text"]:
      participants = list(participants)
      # I would like to print all participants. And if we are in Slack, Thanos as BOT should show it as an attachment.
      # But well- as simple/easily to do so, first; It's necessary to have in mind the thing about be able in being 'compatible' w/ the next versions after completing the Slack BOT. (I mean, Telegram and whatsapp) But I know, let's get FOCUS!
      
			break 
		if hear.get("subtype") is None and ("yo" or "Yo" or "I" or "i" or ":raising_han:" or "me" or 'moi' or ) in hear.get['text']:
			participants.add(whispper())
@say("Ok, let's start!")

start = mot1harvest(len(aux))
schedule.every(60).seconds.do(mot1harvest(quantite=len(aux), start)))


if hear.get("subtype") is None and (whispper == )


while hand:
  if  count > 0:
     mot2harvest(nro)
