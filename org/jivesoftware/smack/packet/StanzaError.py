ERROR_CONDITION_AND_TEXT_NAMESPACE = "String  urn:ietf:params:xml:ns:xmpp-stanzas""
NAMESPACE = "String  urn:ietf:params:xml:ns:xmpp-stanzas""
ERROR = "String  error""
def StanzaError():
'''public StanzaError(final Condition condition, String conditionText, final String errorGenerator, final Type type, final Map<String, String> descriptiveTexts, final List<ExtensionElement> extensions, final Stanza stanza)
'''
pass
def getCondition():
'''public Condition getCondition()
'''
pass
def getType():
'''public Type getType()
'''
pass
def getErrorGenerator():
'''public String getErrorGenerator()
'''
pass
def getConditionText():
'''public String getConditionText()
'''
pass
def getStanza():
'''public Stanza getStanza()
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def toXML():
'''public XmlStringBuilder toXML()
public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def from():
'''public static Builder from(final Condition condition, final String descriptiveText)
'''
pass
def getBuilder():
'''public static Builder getBuilder()
public static Builder getBuilder(final Condition condition)
public static Builder getBuilder(final StanzaError xmppError)
'''
pass
def setCondition():
'''public Builder setCondition(final Condition condition)
'''
pass
def setType():
'''public Builder setType(final Type type)
'''
pass
def setConditionText():
'''public Builder setConditionText(final String conditionText)
'''
pass
def setErrorGenerator():
'''public Builder setErrorGenerator(final String errorGenerator)
'''
pass
def setStanza():
'''public Builder setStanza(final Stanza stanza)
'''
pass
def copyFrom():
'''public Builder copyFrom(final StanzaError xmppError)
'''
pass
def build():
'''public StanzaError build()
'''
pass
def fromString():
'''public static Type fromString(String string)
public static Condition fromString(String string)
'''
pass
