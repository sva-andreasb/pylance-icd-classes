def getInstance():
    '''public static Navigator getInstance()
    '''
def isElement():
    '''public boolean isElement(final Object obj)
    '''
def isComment():
    '''public boolean isComment(final Object obj)
    '''
def isText():
    '''public boolean isText(final Object obj)
    '''
def isAttribute():
    '''public boolean isAttribute(final Object obj)
    '''
def isProcessingInstruction():
    '''public boolean isProcessingInstruction(final Object obj)
    '''
def isDocument():
    '''public boolean isDocument(final Object obj)
    '''
def isNamespace():
    '''public boolean isNamespace(final Object obj)
    '''
def getElementName():
    '''public String getElementName(final Object obj)
    '''
def getElementNamespaceUri():
    '''public String getElementNamespaceUri(final Object obj)
    '''
def getAttributeName():
    '''public String getAttributeName(final Object obj)
    '''
def getAttributeNamespaceUri():
    '''public String getAttributeNamespaceUri(final Object obj)
    '''
def getChildAxisIterator():
    '''public Iterator getChildAxisIterator(final Object contextNode)
    public Iterator getChildAxisIterator(final Object contextNode, final String localName, final String namespacePrefix, final String namespaceURI)
    '''
def getNamespaceAxisIterator():
    '''public Iterator getNamespaceAxisIterator(final Object contextNode)
    '''
def getParentAxisIterator():
    '''public Iterator getParentAxisIterator(final Object contextNode)
    '''
def getAttributeAxisIterator():
    '''public Iterator getAttributeAxisIterator(final Object contextNode)
    public Iterator getAttributeAxisIterator(final Object contextNode, final String localName, final String namespacePrefix, final String namespaceURI)
    '''
def parseXPath():
    '''public XPath parseXPath(final String xpath)
    '''
def getDocumentNode():
    '''public Object getDocumentNode(final Object contextNode)
    '''
def getElementQName():
    '''public String getElementQName(final Object obj)
    '''
def getAttributeQName():
    '''public String getAttributeQName(final Object obj)
    '''
def getNamespaceStringValue():
    '''public String getNamespaceStringValue(final Object obj)
    '''
def getNamespacePrefix():
    '''public String getNamespacePrefix(final Object obj)
    '''
def getTextStringValue():
    '''public String getTextStringValue(final Object obj)
    '''
def getAttributeStringValue():
    '''public String getAttributeStringValue(final Object obj)
    '''
def getElementStringValue():
    '''public String getElementStringValue(final Object obj)
    '''
def getProcessingInstructionTarget():
    '''public String getProcessingInstructionTarget(final Object obj)
    '''
def getProcessingInstructionData():
    '''public String getProcessingInstructionData(final Object obj)
    '''
def getCommentStringValue():
    '''public String getCommentStringValue(final Object obj)
    '''
def translateNamespacePrefixToUri():
    '''public String translateNamespacePrefixToUri(final String prefix, final Object context)
    '''
def getDocument():
    '''public Object getDocument(final String url)
    '''
