ELEMENT_NAME = "String  \"invite\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def RoomInvitation():
    '''public RoomInvitation(final Type type, final Jid invitee, final String sessionID, final String reason)
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def getInviter():
    '''public EntityJid getInviter()
    '''
def getRoom():
    '''public EntityBareJid getRoom()
    '''
def getReason():
    '''public String getReason()
    '''
def getSessionID():
    '''public String getSessionID()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def RoomInvitationIQ():
    '''public RoomInvitationIQ(final RoomInvitation roomInvitation)
    '''
def parse():
    '''public RoomInvitation parse(final XmlPullParser parser, final int initialDepth)
    '''
