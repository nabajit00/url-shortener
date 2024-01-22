import hashlib
import validators
from flask import current_app
from os import getenv
from random import randrange

__urls = {} #URL, 


def get_url(key):
    #Get redirect url using main url 
    print(__urls)   
    return __urls.get(key,None)


def get_short_url(key):
    return getenv('host')+get_url(key)

def url_exists(url):
    return not (__urls.get(url,None) is None)

__URL_HASH_SIZE = 6
def __format_url_hash(url:str):
    digest = hashlib.sha1(url.encode()).hexdigest()
    start_pos = randrange(0,len(digest)-__URL_HASH_SIZE)

    return digest[start_pos:start_pos+__URL_HASH_SIZE]


def add_url(url):
    #Add a new url
    url_hash = __format_url_hash(url)

    __urls[url] = url_hash
    __urls[url_hash] = url
    return get_short_url(url)
