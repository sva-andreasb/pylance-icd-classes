ELEMENT = "String  \"data\""
NAMESPACE = "String  \"http://jabber.org/protocol/ibb\""
def ():
    '''returns DataPacketExtension\n\n
    (final String sessionID, final long seq, final String data)\n
    '''
def getSessionID():
    '''returns String\n\n
    getSessionID()\n
    '''
def getSeq():
    '''returns long\n\n
    getSeq()\n
    '''
def getData():
    '''returns String\n\n
    getData()\n
    '''
def getDecodedData():
    '''returns byte[]\n\n
    getDecodedData()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
