# Solutions/Syntax/logger.py
#

import datetime
def logit( s):
    timestamp = datetime.datetime.now()
    print(timestamp)
    print( "{0}:{1}".format( timestamp, s.upper()))