NAMESPACE = "String  urn:xmpp:markup:0""
ELEMENT = "String  markup""
ATTR_START = "String  start""
ATTR_END = "String  end""
def MarkupElement():
'''public MarkupElement(final List<MarkupChildElement> childElements)
'''
pass
def getBuilder():
'''public static Builder getBuilder()
'''
pass
def getChildElements():
'''public List<MarkupChildElement> getChildElements()
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
def setDeleted():
'''public Builder setDeleted(final int start, final int end)
'''
pass
def setEmphasis():
'''public Builder setEmphasis(final int start, final int end)
'''
pass
def setCode():
'''public Builder setCode(final int start, final int end)
'''
pass
def addSpan():
'''public Builder addSpan(final int start, final int end, final Set<SpanElement.SpanStyle> styles)
'''
pass
def setBlockQuote():
'''public Builder setBlockQuote(final int start, final int end)
'''
pass
def setCodeBlock():
'''public Builder setCodeBlock(final int start, final int end)
'''
pass
def beginList():
'''public ListBuilder beginList()
'''
pass
def build():
'''public MarkupElement build()
'''
pass
def addEntry():
'''public ListBuilder addEntry(final int start, final int end)
'''
pass
def endList():
'''public Builder endList()
'''
pass
