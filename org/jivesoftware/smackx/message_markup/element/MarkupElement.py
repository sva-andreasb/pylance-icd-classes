NAMESPACE = "String  \"urn:xmpp:markup:0\""
ELEMENT = "String  \"markup\""
ATTR_START = "String  \"start\""
ATTR_END = "String  \"end\""
def MarkupElement():
    '''    public MarkupElement(final List<MarkupChildElement> childElements)
    '''
def getBuilder():
    '''    public static Builder getBuilder()
    '''
def getChildElements():
    '''    public List<MarkupChildElement> getChildElements()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def setDeleted():
    '''    public Builder setDeleted(final int start, final int end)
    '''
def setEmphasis():
    '''    public Builder setEmphasis(final int start, final int end)
    '''
def setCode():
    '''    public Builder setCode(final int start, final int end)
    '''
def addSpan():
    '''    public Builder addSpan(final int start, final int end, final Set<SpanElement.SpanStyle> styles)
    '''
def setBlockQuote():
    '''    public Builder setBlockQuote(final int start, final int end)
    '''
def setCodeBlock():
    '''    public Builder setCodeBlock(final int start, final int end)
    '''
def beginList():
    '''    public ListBuilder beginList()
    '''
def build():
    '''    public MarkupElement build()
    '''
def addEntry():
    '''    public ListBuilder addEntry(final int start, final int end)
    '''
def endList():
    '''    public Builder endList()
    '''
