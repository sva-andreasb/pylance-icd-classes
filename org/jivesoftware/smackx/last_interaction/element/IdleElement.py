NAMESPACE = "String  \"urn:xmpp:idle:1\""
ELEMENT = "String  \"idle\""
ATTR_SINCE = "String  \"since\""
def IdleElement():
    '''    public IdleElement()
    public IdleElement(final Date since)
    '''
def getSince():
    '''    public Date getSince()
    '''
def addToPresence():
    '''    public static void addToPresence(final Presence presence)
    '''
def fromPresence():
    '''    public static IdleElement fromPresence(final Presence presence)
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
