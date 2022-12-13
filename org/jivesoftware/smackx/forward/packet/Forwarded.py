NAMESPACE = "String  \"urn:xmpp:forward:0\""
ELEMENT = "String  \"forwarded\""
def Forwarded():
    '''    public Forwarded(final DelayInformation delay, final Stanza fwdPacket)
    public Forwarded(final Stanza fwdPacket)
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def getForwardedPacket():
    '''    public Stanza getForwardedPacket()
    '''
def getForwardedStanza():
    '''    public Stanza getForwardedStanza()
    '''
def getDelayInformation():
    '''    public DelayInformation getDelayInformation()
    '''
def from():
    '''    public static Forwarded from(final Stanza packet)
    '''
def extractMessagesFrom():
    '''    public static List<Message> extractMessagesFrom(final Collection<Forwarded> forwardedCollection)
    '''
