NAMESPACE = "String  \"urn:xmpp:idle:1\""
ELEMENT = "String  \"idle\""
ATTR_SINCE = "String  \"since\""
def ():
    '''returns IdleElement\n\n
    ()\n
    (final Date since)\n
    '''
def getSince():
    '''returns Date\n\n
    getSince()\n
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
