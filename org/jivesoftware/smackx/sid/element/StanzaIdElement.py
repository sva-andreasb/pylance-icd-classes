ELEMENT = "String  \"stanza-id\""
ATTR_BY = "String  \"by\""
def StanzaIdElement():
    '''public StanzaIdElement(final String by)
    public StanzaIdElement(final String id, final String by)
    '''
def hasStanzaId():
    '''public static boolean hasStanzaId(final Message message)
    '''
def getStanzaId():
    '''public static StanzaIdElement getStanzaId(final Message message)
    '''
def getBy():
    '''public String getBy()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def getElementName():
    '''public String getElementName()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
