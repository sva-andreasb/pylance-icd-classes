ELEMENT_NAME = "String  \"session\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ():
    '''returns SessionID\n\n
    (final String sessionID)\n
    '''
def getSessionID():
    '''returns String\n\n
    getSessionID()\n
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
    '''returns SessionID\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
