# myLogger.py
from datetime import datetime
def logger(msg, fname="log.txt"):
    with open(fname, "a+") as f:
        f.write(str(datetime.now()) + ":" + msg + "\n");
def myLogger( func ):
    def onCall( *args, **kwargs):
        logger("{} called".format(func.__name__));
        rc = func( *args, **kwargs);
        return rc;
    return onCall;
