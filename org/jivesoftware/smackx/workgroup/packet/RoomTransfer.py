ELEMENT_NAME = "String  \"transfer\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def ():
    '''returns RoomTransferIQ\n\n
    (final Type type, final String invitee, final String sessionID, final String reason)\n
    (final RoomTransfer roomTransfer)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getInviter():
    '''returns String\n\n
    getInviter()\n
    '''
def getRoom():
    '''returns String\n\n
    getRoom()\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    '''
def getSessionID():
    '''returns String\n\n
    getSessionID()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
def parse():
    '''returns RoomTransfer\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
