from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
import json, datetime, time, pytz, re, sys, traceback, unicodedata, pymongo
from pymongo import MongoClient
import numpy as np
from collections import defaultdict
from bson.objectid import ObjectId
import MeCab as mc

KEYS = {
        'consumer_key':'GoRovpWFtE7gDnDSSNKipImWt',
        'consumer_secret':'fxApsiXXQu1taSqFZdKpzIWujn1cFeY8xGmeoDlY1X5QSECZSl',
        'access_token':'124660542-Vz0nuB6APuqmm8varDByMNOzq0Kx2z17S1pjJfox',
        'access_secret':'4RvhRM4befO6IrNkE9FKSxiYutxVnnJlKDAwhQwptqGf4'
        }

twitter = None
connect = None
db      = None
tweetdata = None
meta      = None
posi_nega_dict = None

def initialize():
    global twitter, twitter, connect, db, tweetdata, meta
    twitter = OAuth1Session(KEYS['consumer_key'],KEYS['consumer_secret'], KEYS['access_token'],KEYS['access_secret'])
    connect = MongoClient('localhost', 27017)
    db = connect.osakacity
    meta = db.metadata
    posi_nega_dict = db.posi_nega_dict

initialize()
