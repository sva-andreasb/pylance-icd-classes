ELEMENT_NAME = "String  \"transfer\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def RoomTransfer():
    '''    public RoomTransfer(final Type type, final String invitee, final String sessionID, final String reason)
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def getInviter():
    '''    public String getInviter()
    '''
def getRoom():
    '''    public String getRoom()
    '''
def getReason():
    '''    public String getReason()
    '''
def getSessionID():
    '''    public String getSessionID()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def RoomTransferIQ():
    '''    public RoomTransferIQ(final RoomTransfer roomTransfer)
    '''
def parse():
    '''    public RoomTransfer parse(final XmlPullParser parser, final int initialDepth)
    '''
