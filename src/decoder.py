import re
import sqlite3
import string
from logger import scraper_log


#Decode and remove extraneous hex data, leaving only ascii characters

def decode(cur):
    for row in cur.execute("SELECT data FROM object_data"):
     row_str = str(row)
     row_str_decoded = bytes(row_str, "utf-8").decode("unicode_escape")
     row_decoded = re.sub('r\\\\x[0-9a-fA-F]{2}', "", row_str_decoded)
     print_me = row_decoded.encode('ascii', 'ignore').decode('ascii')
     print(print_me)
     scraper_log(print_me)

