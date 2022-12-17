ELEMENT = "String  \"file-too-large\""
NAMESPACE = "String  \"urn:xmpp:http:upload:0\""
def ():
    '''returns FileTooLargeError\n\n
    (final long maxFileSize)\n
    '''
def getMaxFileSize():
    '''returns long\n\n
    getMaxFileSize()\n
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
