ELEMENT_NAME = "String  \"chat-metadata\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ():
    '''returns ChatMetadata\n\n
    ()\n
    '''
def getSessionID():
    '''returns String\n\n
    getSessionID()\n
    '''
def setSessionID():
    '''returns None\n\n
    setSessionID(final String sessionID)\n
    '''
def setMetadata():
    '''returns None\n\n
    setMetadata(final Map<String, List<String>> metadata)\n
    '''
def parse():
    '''returns ChatMetadata\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
