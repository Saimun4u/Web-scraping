import webbrowser, sys, pyperclip

# Address to be copied
# https://www.google.ca/maps/place/739+Gerrard+St+E,+Toronto


sys.argv  # ['script.py', '739', 'Gerrard', 'St', 'E', 'Toronto']

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.ca/maps/place/<ADDRESS>

webbrowser.open('https://www.google.ca/maps/place/' + address)

