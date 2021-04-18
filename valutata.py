'''
We make a request to Google, get the result from the element code
'''
print('''
	
╔═══╗───────╔╗─────╔╗╔╗──────╔╗╔═╗
║╔═╗║──────╔╝╚╗────║║║║──────║║║╔╝
║║─╚╬═╦══╦═╩╗╔╬══╦═╝║║╚═╦╗─╔╗║╚╝╝╔══╦═╗╔══╦══╦═╗
║║─╔╣╔╣║═╣╔╗║║║║═╣╔╗║║╔╗║║─║║║╔╗║║╔╗║╔╗╣╔╗║║═╣╔╗╗
║╚═╝║║║║═╣╔╗║╚╣║═╣╚╝║║╚╝║╚═╝║║║║╚╣╚╝║║║║╚╝║║═╣║║║
╚═══╩╝╚══╩╝╚╩═╩══╩══╝╚══╩═╗╔╝╚╝╚═╩══╩╝╚╩═╗╠══╩╝╚╝
────────────────────────╔═╝║───────────╔═╝║
────────────────────────╚══╝───────────╚══╝
	''')


#import
import requests
from bs4 import BeautifulSoup

#start message
print('''
First enter the first currency (for example dollar)

Then enter the second currency (for example ruble)
	''')

#print
print('------------------------------------------------')
print('')
first = str(input('First currency: '))
print('')
second = str(input('Second currency: '))

#assign the url with currencies to the variable
VALUTA = 'https://www.google.com/search?q=' + first + '%20to%20' + second + '%20rate'

#so that we are not considered a robot
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def check():

	full_page = requests.get(VALUTA, headers=headers)

	soup = BeautifulSoup(full_page.content, 'html.parser')

	#filter
	convert = soup.findAll('span', {'class': 'DFlfde SwHCTb' })

	return(convert[0].text)
try:
	print('Course ' + first + ' to ' + second + ' = ' + check()) #result
except:
	print('Введена неверная валюта') #If there is an error

#a very stupid program created by a schoolchild who dreams of becoming an IT specialist