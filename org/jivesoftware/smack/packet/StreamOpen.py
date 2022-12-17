ELEMENT = "String  \"stream:stream\""
CLIENT_NAMESPACE = "String  \"jabber:client\""
SERVER_NAMESPACE = "String  \"jabber:server\""
VERSION = "String  \"1.0\""
def ():
    '''returns StreamOpen\n\n
    (final CharSequence to)\n
    (final CharSequence to, final CharSequence from, final String id)\n
    (final CharSequence to, final CharSequence from, final String id, final String lang, final StreamContentNamespace ns)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
