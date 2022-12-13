ELEMENT = "String  \"data\""
NAMESPACE = "String  \"http://jabber.org/protocol/ibb\""
def DataPacketExtension():
    '''public DataPacketExtension(final String sessionID, final long seq, final String data)
    '''
def getSessionID():
    '''public String getSessionID()
    '''
def getSeq():
    '''public long getSeq()
    '''
def getData():
    '''public String getData()
    '''
def getDecodedData():
    '''public byte[] getDecodedData()
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
