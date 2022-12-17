ELEMENT = "String  \"offline\""
NAMESPACE = "String  \"http://jabber.org/protocol/offline\""
def ():
    '''returns Item\n\n
    ()\n
    (final String node)\n
    '''
def getItems():
    '''returns List<Item>\n\n
    getItems()\n
    '''
def addItem():
    '''returns None\n\n
    addItem(final Item item)\n
    '''
def isPurge():
    '''returns boolean\n\n
    isPurge()\n
    '''
def setPurge():
    '''returns None\n\n
    setPurge(final boolean purge)\n
    '''
def isFetch():
    '''returns boolean\n\n
    isFetch()\n
    '''
def setFetch():
    '''returns None\n\n
    setFetch(final boolean fetch)\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def getAction():
    '''returns String\n\n
    getAction()\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final String action)\n
    '''
def getJid():
    '''returns String\n\n
    getJid()\n
    '''
def setJid():
    '''returns None\n\n
    setJid(final String jid)\n
    '''
def toXML():
    '''returns String\n\n
    toXML()\n
    '''
def parse():
    '''returns OfflineMessageRequest\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
