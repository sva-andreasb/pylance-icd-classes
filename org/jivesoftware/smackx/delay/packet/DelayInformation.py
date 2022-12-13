ELEMENT = "String  \"delay\""
NAMESPACE = "String  \"urn:xmpp:delay\""
def DelayInformation():
    '''public DelayInformation(final Date stamp, final String from, final String reason)
    public DelayInformation(final Date stamp)
    '''
def getFrom():
    '''public String getFrom()
    public static DelayInformation getFrom(final Stanza packet)
    '''
def getStamp():
    '''public Date getStamp()
    '''
def getReason():
    '''public String getReason()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def from():
    '''public static DelayInformation from(final Stanza packet)
    '''
