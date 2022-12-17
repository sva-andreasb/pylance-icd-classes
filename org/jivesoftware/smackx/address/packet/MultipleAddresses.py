NAMESPACE = "String  \"http://jabber.org/protocol/address\""
ELEMENT = "String  \"address\""
def ():
    '''returns MultipleAddresses\n\n
    ()\n
    '''
def addAddress():
    '''returns None\n\n
    addAddress(final Type type, final Jid jid, final String node, final String desc, final boolean delivered, final String uri)\n
    '''
def setNoReply():
    '''returns None\n\n
    setNoReply()\n
    '''
def getAddressesOfType():
    '''returns List<Address>\n\n
    getAddressesOfType(final Type type)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getJid():
    '''returns Jid\n\n
    getJid()\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def isDelivered():
    '''returns boolean\n\n
    isDelivered()\n
    '''
def getUri():
    '''returns String\n\n
    getUri()\n
    '''
