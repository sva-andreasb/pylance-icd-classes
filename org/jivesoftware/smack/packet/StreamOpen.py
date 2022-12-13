ELEMENT = "String  \"stream:stream\""
CLIENT_NAMESPACE = "String  \"jabber:client\""
SERVER_NAMESPACE = "String  \"jabber:server\""
VERSION = "String  \"1.0\""
def StreamOpen():
    '''public StreamOpen(final CharSequence to)
    public StreamOpen(final CharSequence to, final CharSequence from, final String id)
    public StreamOpen(final CharSequence to, final CharSequence from, final String id, final String lang, final StreamContentNamespace ns)
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
