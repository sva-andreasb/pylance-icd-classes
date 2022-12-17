ELEMENT_NAME = "String  \"notify-queue-details\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def ():
    '''returns QueueDetails\n\n
    ()\n
    '''
def getUserCount():
    '''returns int\n\n
    getUserCount()\n
    '''
def getUsers():
    '''returns Set<QueueUser>\n\n
    getUsers()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    '''
def parse():
    '''returns QueueDetails\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
