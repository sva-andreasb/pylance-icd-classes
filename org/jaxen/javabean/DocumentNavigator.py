def isElement():
    '''returns boolean\n\n
    isElement(final Object obj)\n
    '''
def isComment():
    '''returns boolean\n\n
    isComment(final Object obj)\n
    '''
def isText():
    '''returns boolean\n\n
    isText(final Object obj)\n
    '''
def isAttribute():
    '''returns boolean\n\n
    isAttribute(final Object obj)\n
    '''
def isProcessingInstruction():
    '''returns boolean\n\n
    isProcessingInstruction(final Object obj)\n
    '''
def isDocument():
    '''returns boolean\n\n
    isDocument(final Object obj)\n
    '''
def isNamespace():
    '''returns boolean\n\n
    isNamespace(final Object obj)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName(final Object obj)\n
    '''
def getElementNamespaceUri():
    '''returns String\n\n
    getElementNamespaceUri(final Object obj)\n
    '''
def getElementQName():
    '''returns String\n\n
    getElementQName(final Object obj)\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName(final Object obj)\n
    '''
def getAttributeNamespaceUri():
    '''returns String\n\n
    getAttributeNamespaceUri(final Object obj)\n
    '''
def getAttributeQName():
    '''returns String\n\n
    getAttributeQName(final Object obj)\n
    '''
def getChildAxisIterator():
    '''returns Iterator\n\n
    getChildAxisIterator(final Object contextNode)\n
    getChildAxisIterator(final Object contextNode, final String localName, final String namespacePrefix, final String namespaceURI)\n
    '''
def getParentAxisIterator():
    '''returns Iterator\n\n
    getParentAxisIterator(final Object contextNode)\n
    '''
def getAttributeAxisIterator():
    '''returns Iterator\n\n
    getAttributeAxisIterator(final Object contextNode)\n
    getAttributeAxisIterator(final Object contextNode, final String localName, final String namespacePrefix, final String namespaceURI)\n
    '''
def getNamespaceAxisIterator():
    '''returns Iterator\n\n
    getNamespaceAxisIterator(final Object contextNode)\n
    '''
def getDocumentNode():
    '''returns Object\n\n
    getDocumentNode(final Object contextNode)\n
    '''
def getParentNode():
    '''returns Object\n\n
    getParentNode(final Object contextNode)\n
    '''
def getTextStringValue():
    '''returns String\n\n
    getTextStringValue(final Object obj)\n
    '''
def getElementStringValue():
    '''returns String\n\n
    getElementStringValue(final Object obj)\n
    '''
def getAttributeStringValue():
    '''returns String\n\n
    getAttributeStringValue(final Object obj)\n
    '''
def getNamespaceStringValue():
    '''returns String\n\n
    getNamespaceStringValue(final Object obj)\n
    '''
def getNamespacePrefix():
    '''returns String\n\n
    getNamespacePrefix(final Object obj)\n
    '''
def getCommentStringValue():
    '''returns String\n\n
    getCommentStringValue(final Object obj)\n
    '''
def translateNamespacePrefixToUri():
    '''returns String\n\n
    translateNamespacePrefixToUri(final String prefix, final Object context)\n
    '''
def getNodeType():
    '''returns short\n\n
    getNodeType(final Object node)\n
    '''
def getDocument():
    '''returns Object\n\n
    getDocument(final String uri)\n
    '''
def getProcessingInstructionTarget():
    '''returns String\n\n
    getProcessingInstructionTarget(final Object obj)\n
    '''
def getProcessingInstructionData():
    '''returns String\n\n
    getProcessingInstructionData(final Object obj)\n
    '''
def parseXPath():
    '''returns XPath\n\n
    parseXPath(final String xpath)\n
    '''
