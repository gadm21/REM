
from O365 import Message
import configparser
from utils import * 

config = configparser.ConfigParser()
config.read('config.ini')

username_nu = config.get('credentials', 'username_nu')
username_uwo = config.get('credentials', 'username_uwo')
password_nu = config.get('credentials', 'password_nu')

o365_auth = (username_nu, password_nu) 
m = Message(auth=o365_auth)
m.setRecipients(username_uwo)
m.setSubject('I made an email script.')
m.setBody('Talk to the computer, cause the human does not want to hear it any more.')
m.sendMessage()