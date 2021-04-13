# import webbrowser, sys, pyperclip

# Address to be copied
# https://www.google.ca/maps/place/739+Gerrard+St+E,+Toronto


# sys.argv  # ['script.py', '739', 'Gerrard', 'St', 'E', 'Toronto']

# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()
#
# # https://www.google.ca/maps/place/<ADDRESS>
#
# webbrowser.open('https://www.google.ca/maps/place/' + address)



#Downloading from the web with the request module


# import requests

# res = requests.get('https://www.gutenberg.org/files/2148/2148-0.txt')
# print(res.status_code)
#
# print(len(res.text))
#
# print((res.text[:500]))

# import bs4, requests
#
# res = requests.get('https://www.aliexpress.com/item/1005002277130722.html?spm=a2g0o.detail.1000060.3.47096cd4CdTsuc&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.169870.0&scm_id=1007.13339.169870.0&scm-url=1007.13339.169870.0&pvid=25843377-7383-442e-8885-9b0f00f39f01&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.169870.0,pvid:25843377-7383-442e-8885-9b0f00f39f01,tpp_buckets:668%230%23131923%2324_668%230%23131923%2324_668%23888%233325%2320_668%23888%233325%2320_668%232846%238107%231934_668%232717%237565%23769_668%231000022185%231000066058%230_668%233468%2315609%23281_668%232846%238107%231934_668%232717%237565%23769_668%233164%239976%23550_668%233468%2315609%23281')
#
# res.raise_for_status()
#
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
# elems = soup.select('#root > div > div.product-main > div > div.product-info > div.product-price > div.product-price-current > span')
#
# print(elems[0].text)


# import bs4, requests
#
# def getDarazPrice(productUrl):
#     res = requests.get(productUrl)
#     res.raise_for_status()
#
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
#     elems = soup.select('#module_product_price_1 > div > div > span')
#
#     return elems[0].text.strip()
#
# price = getDarazPrice('https://www.daraz.com.bd/products/amazfit-gtr-2-amoled-curved-display-classic-stainless-steel-global-version-silver-i163490760-s1096062719.html?spm=a2a0e.searchlist.list.1.26273b1a3CPUoC&search=1')


from selenium import webdriver

from selenium import webdriver


from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

browser = webdriver.Firefox()

browser.get('https://mail.cse.com.bd/mail/')




