ELEMENT = "String  \"delay\""
NAMESPACE = "String  \"urn:xmpp:delay\""
def ():
    '''returns DelayInformation\n\n
    (final Date stamp, final String from, final String reason)\n
    (final Date stamp)\n
    '''
def getFrom():
    '''returns String\n\n
    getFrom()\n
    '''
def getStamp():
    '''returns Date\n\n
    getStamp()\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
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
