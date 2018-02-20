from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
import json, datetime, time, pytz, re, sys, traceback, unicodedata, pymongo
from pymongo import MongoClient
import numpy as np
from collections import defaultdict
from bson.objectid import ObjectId
import MeCab as mc

KEYS = {
        'consumer_key':'************',
        'consumer_secret':'**************',
        'access_token':'***************',
        'access_secret':'******************'
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
