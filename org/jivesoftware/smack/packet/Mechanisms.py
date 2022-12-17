ELEMENT = "String  \"mechanisms\""
NAMESPACE = "String  \"urn:ietf:params:xml:ns:xmpp-sasl\""
def ():
    '''returns Mechanisms\n\n
    (final String mechanism)\n
    (final Collection<String> mechanisms)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getMechanisms():
    '''returns List<String>\n\n
    getMechanisms()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
