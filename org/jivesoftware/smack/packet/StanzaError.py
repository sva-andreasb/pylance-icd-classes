ERROR_CONDITION_AND_TEXT_NAMESPACE = "String  \"urn:ietf:params:xml:ns:xmpp-stanzas\""
NAMESPACE = "String  \"urn:ietf:params:xml:ns:xmpp-stanzas\""
ERROR = "String  \"error\""
def StanzaError():
    '''public StanzaError(final Condition condition, String conditionText, final String errorGenerator, final Type type, final Map<String, String> descriptiveTexts, final List<ExtensionElement> extensions, final Stanza stanza)
    '''
def getCondition():
    '''public Condition getCondition()
    '''
def getType():
    '''public Type getType()
    '''
def getErrorGenerator():
    '''public String getErrorGenerator()
    '''
def getConditionText():
    '''public String getConditionText()
    '''
def getStanza():
    '''public Stanza getStanza()
    '''
def toString():
    '''public String toString()
    public String toString()
    public String toString()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def toXML():
    '''public XmlStringBuilder toXML()
    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def from():
    '''public static Builder from(final Condition condition, final String descriptiveText)
    '''
def getBuilder():
    '''public static Builder getBuilder()
    public static Builder getBuilder(final Condition condition)
    public static Builder getBuilder(final StanzaError xmppError)
    '''
def setCondition():
    '''public Builder setCondition(final Condition condition)
    '''
def setType():
    '''public Builder setType(final Type type)
    '''
def setConditionText():
    '''public Builder setConditionText(final String conditionText)
    '''
def setErrorGenerator():
    '''public Builder setErrorGenerator(final String errorGenerator)
    '''
def setStanza():
    '''public Builder setStanza(final Stanza stanza)
    '''
def copyFrom():
    '''public Builder copyFrom(final StanzaError xmppError)
    '''
def build():
    '''public StanzaError build()
    '''
def fromString():
    '''public static Type fromString(String string)
    public static Condition fromString(String string)
    '''
