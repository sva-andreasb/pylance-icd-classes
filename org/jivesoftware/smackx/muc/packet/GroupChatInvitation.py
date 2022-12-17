ELEMENT = "String  \"x\""
NAMESPACE = "String  \"jabber:x:conference\""
def ():
    '''returns GroupChatInvitation\n\n
    (final String roomAddress)\n
    '''
def getRoomAddress():
    '''returns String\n\n
    getRoomAddress()\n
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
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
def parse():
    '''returns GroupChatInvitation\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
