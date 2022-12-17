ERROR_CONDITION_AND_TEXT_NAMESPACE = "String  \"urn:ietf:params:xml:ns:xmpp-stanzas\""
NAMESPACE = "String  \"urn:ietf:params:xml:ns:xmpp-stanzas\""
ERROR = "String  \"error\""
def ():
    '''returns StanzaError\n\n
    (final Condition condition, String conditionText, final String errorGenerator, final Type type, final Map<String, String> descriptiveTexts, final List<ExtensionElement> extensions, final Stanza stanza)\n
    '''
def getCondition():
    '''returns Condition\n\n
    getCondition()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getErrorGenerator():
    '''returns String\n\n
    getErrorGenerator()\n
    '''
def getConditionText():
    '''returns String\n\n
    getConditionText()\n
    '''
def getStanza():
    '''returns Stanza\n\n
    getStanza()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
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
    toXML()\n
    toXML(final String enclosingNamespace)\n
    '''
def setCondition():
    '''returns Builder\n\n
    setCondition(final Condition condition)\n
    '''
def setType():
    '''returns Builder\n\n
    setType(final Type type)\n
    '''
def setConditionText():
    '''returns Builder\n\n
    setConditionText(final String conditionText)\n
    '''
def setErrorGenerator():
    '''returns Builder\n\n
    setErrorGenerator(final String errorGenerator)\n
    '''
def setStanza():
    '''returns Builder\n\n
    setStanza(final Stanza stanza)\n
    '''
def copyFrom():
    '''returns Builder\n\n
    copyFrom(final StanzaError xmppError)\n
    '''
def build():
    '''returns StanzaError\n\n
    build()\n
    '''
