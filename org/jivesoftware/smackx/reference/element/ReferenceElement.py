ELEMENT = "String  reference""
ATTR_BEGIN = "String  begin""
ATTR_END = "String  end""
ATTR_TYPE = "String  type""
ATTR_ANCHOR = "String  anchor""
ATTR_URI = "String  uri""
def ReferenceElement():
'''public ReferenceElement(final Integer begin, final Integer end, final Type type, final String anchor, final URI uri, final ExtensionElement child)
public ReferenceElement(final Integer begin, final Integer end, final Type type, final String anchor, final URI uri)
'''
pass
def getBegin():
'''public Integer getBegin()
'''
pass
def getEnd():
'''public Integer getEnd()
'''
pass
def getType():
'''public Type getType()
'''
pass
def getAnchor():
'''public String getAnchor()
'''
pass
def getUri():
'''public URI getUri()
'''
pass
def addMention():
'''public static void addMention(final Stanza stanza, final int begin, final int end, final BareJid jid)
'''
pass
def getReferencesFromStanza():
'''public static List<ReferenceElement> getReferencesFromStanza(final Stanza stanza)
'''
pass
def containsReferences():
'''public static boolean containsReferences(final Stanza stanza)
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
