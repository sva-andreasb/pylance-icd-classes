ELEMENT_NAME = "String  \"queue-status\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def ():
    '''returns QueueUpdate\n\n
    (final int position, final int remainingTime)\n
    '''
def getPosition():
    '''returns int\n\n
    getPosition()\n
    '''
def getRemaingTime():
    '''returns int\n\n
    getRemaingTime()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def parse():
    '''returns QueueUpdate\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
