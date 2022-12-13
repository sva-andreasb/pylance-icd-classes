ELEMENT = "String  \"reference\""
ATTR_BEGIN = "String  \"begin\""
ATTR_END = "String  \"end\""
ATTR_TYPE = "String  \"type\""
ATTR_ANCHOR = "String  \"anchor\""
ATTR_URI = "String  \"uri\""
def ReferenceElement():
    '''public ReferenceElement(final Integer begin, final Integer end, final Type type, final String anchor, final URI uri, final ExtensionElement child)
    public ReferenceElement(final Integer begin, final Integer end, final Type type, final String anchor, final URI uri)
    '''
def getBegin():
    '''public Integer getBegin()
    '''
def getEnd():
    '''public Integer getEnd()
    '''
def getType():
    '''public Type getType()
    '''
def getAnchor():
    '''public String getAnchor()
    '''
def getUri():
    '''public URI getUri()
    '''
def addMention():
    '''public static void addMention(final Stanza stanza, final int begin, final int end, final BareJid jid)
    '''
def getReferencesFromStanza():
    '''public static List<ReferenceElement> getReferencesFromStanza(final Stanza stanza)
    '''
def containsReferences():
    '''public static boolean containsReferences(final Stanza stanza)
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def getElementName():
    '''public String getElementName()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
