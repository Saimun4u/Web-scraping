import webbrowser, sys, pyperclip

# Address to be copied
# https://www.google.ca/maps/place/739+Gerrard+St+E,+Toronto


sys.argv  # ['script.py', '739', 'Gerrard', 'St', 'E', 'Toronto']

# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()
#
# # https://www.google.ca/maps/place/<ADDRESS>
#
# webbrowser.open('https://www.google.ca/maps/place/' + address)



#Downloading from the web with the request module


import requests

res = requests.get('https://www.gutenberg.org/files/2148/2148-0.txt')
# print(res.status_code)

print(len(res.text))

print((res.text[:500]))


