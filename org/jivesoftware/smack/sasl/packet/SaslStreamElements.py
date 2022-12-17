NAMESPACE = "String  \"urn:ietf:params:xml:ns:xmpp-sasl\""
ELEMENT = "String  \"failure\""
def ():
    '''returns SASLFailure\n\n
    (final String mechanism, final String authenticationText)\n
    (final String data)\n
    ()\n
    (final String authenticationText)\n
    (final String data)\n
    (final String saslError)\n
    (final String saslError, final Map<String, String> descriptiveTexts)\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    '''
def getMechanism():
    '''returns String\n\n
    getMechanism()\n
    '''
def getAuthenticationText():
    '''returns String\n\n
    getAuthenticationText()\n
    getAuthenticationText()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    getNamespace()\n
    getNamespace()\n
    getNamespace()\n
    getNamespace()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    getElementName()\n
    getElementName()\n
    getElementName()\n
    getElementName()\n
    '''
def getData():
    '''returns String\n\n
    getData()\n
    '''
def getSASLError():
    '''returns SASLError\n\n
    getSASLError()\n
    '''
def getSASLErrorString():
    '''returns String\n\n
    getSASLErrorString()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
