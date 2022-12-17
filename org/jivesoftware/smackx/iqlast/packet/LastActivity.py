ELEMENT = "String  \"query\""
NAMESPACE = "String  \"jabber:iq:last\""
def ():
    '''returns LastActivity\n\n
    ()\n
    (final Jid to)\n
    '''
def setLastActivity():
    '''returns None\n\n
    setLastActivity(final long lastActivity)\n
    '''
def getIdleTime():
    '''returns long\n\n
    getIdleTime()\n
    '''
def getStatusMessage():
    '''returns String\n\n
    getStatusMessage()\n
    '''
def parse():
    '''returns LastActivity\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
