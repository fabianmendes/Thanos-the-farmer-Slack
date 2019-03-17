from slackclient import SlackClient
import schedule
import time
import os

slack_token = os.environ["SLACK_SIGNING_SECRET"]  # lo haré con el secret signing.
sc = SlackClient(slack_token)

sea = SlackEventAdapter(SLACK_SIGNING_SECRET, endpoint="/slack/events")

@sea.on("hear")
def handle_message(event_data):
	hear = event_data["event"]

if hear.get("subtype") is None and "hi" in hear.get['text']:
	greetings = "Hello <@%s>! :tada:" % hear["user"]
	say(greetings)

def whispper():
	somebody = hear["user"]
	return somebody

def say(something, towho = False):
	channel = hear["channel"]
	tosay = something
	sc.apicall("chat.postMessage",
						channel = channel,
						text = tosay
						user = towho)		


count = 0

quantite = 0 #número de necesidades


def need(number):
	needl = "need" + str(number + 1)
	return needl

def end(game):
	return schedule.cancel_job(game)

def convertlist(mot):
	mot = []
	'''TODO. Done: pasar la palabra en sí a una lista!
	Y si dicha palabra se encuentra ya en una lista, 
	'''
	return mot # lista

def addtolist(self, what):
	self.append = what
	# devuelve la lista 'actualizada'

def nextword(string, position):
	#from list! Para la 2da siembra y las votaciones.
	word = string[position]
	return word # TODO 


repetidas = {}
def checking(ou, t):
	# ou = word
	# t  = list
	
	for n in range(3):
		if ou in t(n + 1): # needs
			if ou not in repetidas:
				repetidas[ou] = 0

			repetidas[ou] = + 1
						#continuar. Echarle un ojo! Fue lo  ultimo que escribí
						# ..esta raro esta funcion, tenia sueño ya. LISTO

# TODO add the slack_client.apicall SEND (say) message.
def say():
	sc.api_call(
		""
	)
	return


seeds = { "need1" : 0,
					"need2" : 0,
					"need3" : None}

def mot1harvest(cuenta, nro):

	if cuenta < nro:
		seed= need(cuenta)  # llamo seed a las necesidades primas.
		
		tell = 
		# ^ el say debe ir aquí para que pueda decir la NECESIDAD.
		seeds[seed] = convertlist(seeds[seed])

		"""say = None # función que hace decir algo, y la de Needs.
		reemplazado por 'tell'."""

		cuenta =+ 1
		return cuenta #say
	else:
		seed= need(cuenta)  # llamo seed a las necesidades primas
		convertlist(seed)

		blah = None
			#say
				
		return end(mot1harvest)

schedule.every(60).seconds(mot1harvest(count, quantite,))
