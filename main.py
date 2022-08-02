import PyPDF2
from store import *
from utils import *
import sys
# import webbrowser
# import requests
# from bs4 import BeautifulSoup

pdf_file = open(sys.argv[1],'rb')

store_param = "urbanbarn"
if len(sys.argv) > 2:
    store_param = sys.argv[2]

pdf = PyPDF2.PdfFileReader(pdf_file)
pages = pdf.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

links = []
products_by_store = {}
for page in range(pages):
    page_sliced = pdf.getPage(page)
    page_object = page_sliced.getObject()
    if key in page_object.keys():
        ann = page_object[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                hyperlink = u[ank][uri]
                links.append(hyperlink)
                store = get_store(hyperlink)
                if store not in products_by_store:
                    products_by_store[store] = []

                products_by_store[store].append(hyperlink)

sorted = sort_by_amount_of_values(products_by_store)

for prod_url in products_by_store[store_param]:
    # webbrowser.open(prod_url, new=0, autoraise=True)
    print(prod_url)

# URL=products_by_store['homedepot'][0]
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
# }
# page = requests.get(url = URL, headers = HEADERS)
# soup = BeautifulSoup(page.text, 'html.parser')

# # for div in divs.find(_class="hdca-product__description-pricing-price-value"):
# for div in soup.find_all('span'):
#     if hasattr(div, 'class'):
#         try:
#             print(div['class'])
#             print()
#         except:
#             print(div)
#             print()