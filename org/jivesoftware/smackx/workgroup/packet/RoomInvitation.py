ELEMENT_NAME = "String  \"invite\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def ():
    '''returns RoomInvitationIQ\n\n
    (final Type type, final Jid invitee, final String sessionID, final String reason)\n
    (final RoomInvitation roomInvitation)\n
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
    '''returns EntityJid\n\n
    getInviter()\n
    '''
def getRoom():
    '''returns EntityBareJid\n\n
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
    '''returns RoomInvitation\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
