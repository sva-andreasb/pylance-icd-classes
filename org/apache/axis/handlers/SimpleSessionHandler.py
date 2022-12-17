SESSION_ID = "String  \"SimpleSession.id\""
SESSION_NS = "String  \"http://xml.apache.org/axis/session\""
SESSION_LOCALPART = "String  \"sessionID\""
def ():
    '''returns SimpleSessionHandler\n\n
    ()\n
    '''
def invoke():
    '''returns None\n\n
    invoke(final MessageContext context)\n
    '''
def doClient():
    '''returns None\n\n
    doClient(final MessageContext context)\n
    '''
def doServer():
    '''returns None\n\n
    doServer(final MessageContext context)\n
    '''
def setReapPeriodicity():
    '''returns None\n\n
    setReapPeriodicity(final long reapTime)\n
    '''
def setDefaultSessionTimeout():
    '''returns None\n\n
    setDefaultSessionTimeout(final int defaultSessionTimeout)\n
    '''
