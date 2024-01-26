
from O365 import Account, MSGraphProtocol  # same as from O365.connection import MSGraphProtocol
import configparser
from utils import * 

config = configparser.ConfigParser()
config.read('config.ini')

username_nu = config.get('credentials', 'username_nu')
username_uwo = config.get('credentials', 'username_uwo')
password_nu = config.get('credentials', 'password_nu')

credentials = (username_nu, password_nu)
protocol = MSGraphProtocol(api_version='beta')  # MSGraphProtocol defaults to v1.0 api version
account = Account(credentials, protocol=protocol)

mailbox = account.mailbox()

inbox = mailbox.inbox_folder()

messages = inbox.get_messages()
print("You have {} messages in your inbox".format(len(messages)))
print(messages[0].subject)

# o365_auth = (username_nu, password_nu) 
# m = Message(auth=o365_auth)
# m.setRecipients(username_uwo)
# m.setSubject('I made an email script.')
# m.setBody('Talk to the computer, cause the human does not want to hear it any more.')
# m.sendMessage()