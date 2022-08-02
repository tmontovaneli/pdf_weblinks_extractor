from handler import *
from urllib.parse import urlparse

stores = {
    'homedepot': HomedepotHandler() , 
    'etsy': DefaultHandler(), 
    'structube': DefaultHandler(), 
    'thebrick': DefaultHandler(), 
    'ikea': Ikea(), 
    'urbanbarn': DefaultHandler(), 
    'amazon': DefaultHandler(), 
    'signaturelighting': DefaultHandler(), 
    'bouclair': DefaultHandler(), 
    'wayfair': DefaultHandler(), 
    'cartwrightlighting': DefaultHandler(), 
    'bedbathandbeyond': DefaultHandler(), 
    'lowes': DefaultHandler()}

def get_store_strategy(store):
    result = DefaultHandler()
    if store in stores:
        result = stores[store]
    return result

def get_store(hyperlink):
    parsed_uri = urlparse(hyperlink)
    netloc = '{uri.netloc}'.format(uri=parsed_uri)
    store = netloc.split(".")[1]
    if store not in stores:
        stores[store] = DefaultHandler()
    return store
