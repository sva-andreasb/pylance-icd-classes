TEXT = "String  \"text\""
ITEM = "String  \"item\""
def getStanzaId():
    '''returns String\n\n
    getStanzaId()\n
    '''
def getPacketID():
    '''returns String\n\n
    getPacketID()\n
    '''
def setStanzaId():
    '''returns String\n\n
    setStanzaId(final String id)\n
    setStanzaId()\n
    '''
def setPacketID():
    '''returns None\n\n
    setPacketID(final String packetID)\n
    '''
def hasStanzaIdSet():
    '''returns boolean\n\n
    hasStanzaIdSet()\n
    '''
def getTo():
    '''returns Jid\n\n
    getTo()\n
    '''
def setTo():
    '''returns None\n\n
    setTo(final String to)\n
    setTo(final Jid to)\n
    '''
def getFrom():
    '''returns Jid\n\n
    getFrom()\n
    '''
def setFrom():
    '''returns None\n\n
    setFrom(final String from)\n
    setFrom(final Jid from)\n
    '''
def getError():
    '''returns StanzaError\n\n
    getError()\n
    '''
def setError():
    '''returns None\n\n
    setError(final StanzaError error)\n
    setError(final StanzaError.Builder xmppErrorBuilder)\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def setLanguage():
    '''returns None\n\n
    setLanguage(final String language)\n
    '''
def getExtensions():
    '''returns List<ExtensionElement>\n\n
    getExtensions()\n
    getExtensions(final String elementName, final String namespace)\n
    '''
def getExtension():
    '''returns ExtensionElement\n\n
    getExtension(final String namespace)\n
    '''
def addExtension():
    '''returns None\n\n
    addExtension(final ExtensionElement extension)\n
    '''
def overrideExtension():
    '''returns ExtensionElement\n\n
    overrideExtension(final ExtensionElement extension)\n
    '''
def addExtensions():
    '''returns None\n\n
    addExtensions(final Collection<ExtensionElement> extensions)\n
    '''
def hasExtension():
    '''returns boolean\n\n
    hasExtension(final String elementName, final String namespace)\n
    hasExtension(final String namespace)\n
    '''
def removeExtension():
    '''returns ExtensionElement\n\n
    removeExtension(final String elementName, final String namespace)\n
    removeExtension(final ExtensionElement extension)\n
    '''
