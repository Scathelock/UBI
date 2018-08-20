from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.automap import automap_base

import requests
from bs4 import BeautifulSoup
import sys, io

import datetime
import time
import random

from connect_PF import *
from grab_page import *

def add_link_to_PFdb(artist, album, reviewer, review_date, link,
                     page_from, url_from, grab_date, grab_time, table):
    i = table.insert()

    i.execute(
        {'artist_name': artist, 'album_name':album, 'reviewer_name':reviewer, 
         'date_published':review_date, 'review_url':link, 'page_grabbed_from':page_from, 
         'url_grabbed_from':url_from, 'date_grabbed':grab_date, 'datetime_grabbed':grab_time, 
         'album_name':album, 'album_name':album, 'album_name':album
        }
    )
    #print "I did get called"


def check_link_in_PFdb(artist, album, table, verbose):
    s = table.select(and_(table.c.artist_name == artist, 
                          table.c.album_name == album))
    rs = s.execute()

    if rs.fetchone() == None:
        return False
    elif verbose == True:
        for row in rs:
            print row
        return True
    else:
        return True


def add_page_to_PFdb(base_url, page, table, Verbose):
    artist_soup, album_soup,reviewer_soup,review_date_soup,link_soup, page_grabbed, url_grabbed, grab_date, grab_time = GrabPage(base_url, page, Verbose)

    exist_count = 0
    add_count = 0
    for item in range(0, len(artist_soup)):
        exists = check_link_in_PFdb(artist_soup[item].string,
                                    album_soup[item].string,
                                    table, Verbose)
        if exists:
            exist_count += 1
        else:
            add_link_to_PFdb(artist_soup[item].string, album_soup[item].string,
                             reviewer_soup[item].string, 
                             datetime.datetime.strptime(review_date_soup[item].string, "%b %d, %Y").date(),
                             str(base_url+link_soup[item].get('href')), page_grabbed, url_grabbed,
                             grab_date, grab_time, table)

            add_count += 1

    if Verbose:
        print 'exist count is %n and add count is %n' % (exist_count, add_count)
    else:
        pass
        
    if exist_count + add_count == 20:
        return True
    else:
        return False
        


#START MAIN

Verbose = False


db_name = 'sqlite:///PF1.db'


db, metadata, links, Session, session, Base, Links = connect_PF_db(db_name)

total_time = 3000
base_delay = 9
time_count = 0

base_url = 'http://pitchfork.com'

start_page = 503
page = start_page

while time_count < total_time:
    wait_time = base_delay + random.randint(1, 6)
    was_page_added = add_page_to_PFdb(base_url, page, links, Verbose)
    if Verbose:
        print was_page_added
    else:
        pass
    time.sleep(wait_time)
    page += 1
    time_count += wait_time
            
print page-1





### tests

if Verbose:
    s =select([func.count(links.c.link_id)])
    rs = s.execute()
    for row in rs:
        print row




































