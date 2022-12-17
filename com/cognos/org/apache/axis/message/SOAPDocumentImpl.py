def ():
    '''returns SOAPDocumentImpl\n\n
    (final SOAPPart sp)\n
    '''
def getDoctype():
    '''returns DocumentType\n\n
    getDoctype()\n
    '''
def getImplementation():
    '''returns DOMImplementation\n\n
    getImplementation()\n
    '''
def getDocumentElement():
    '''returns Element\n\n
    getDocumentElement()\n
    '''
def createElement():
    '''returns Element\n\n
    createElement(final String tagName)\n
    '''
def createDocumentFragment():
    '''returns DocumentFragment\n\n
    createDocumentFragment()\n
    '''
def createTextNode():
    '''returns Text\n\n
    createTextNode(final String data)\n
    '''
def createComment():
    '''returns Comment\n\n
    createComment(final String data)\n
    '''
def createCDATASection():
    '''returns CDATASection\n\n
    createCDATASection(final String data)\n
    '''
def createProcessingInstruction():
    '''returns ProcessingInstruction\n\n
    createProcessingInstruction(final String target, final String data)\n
    '''
def createAttribute():
    '''returns Attr\n\n
    createAttribute(final String name)\n
    '''
def createEntityReference():
    '''returns EntityReference\n\n
    createEntityReference(final String name)\n
    '''
def importNode():
    '''returns Node\n\n
    importNode(final Node importedNode, final boolean deep)\n
    '''
def createElementNS():
    '''returns Element\n\n
    createElementNS(final String namespaceURI, final String qualifiedName)\n
    '''
def createAttributeNS():
    '''returns Attr\n\n
    createAttributeNS(final String namespaceURI, final String qualifiedName)\n
    '''
def getElementsByTagNameNS():
    '''returns NodeList\n\n
    getElementsByTagNameNS(final String namespaceURI, final String localName)\n
    '''
def getElementsByTagName():
    '''returns NodeList\n\n
    getElementsByTagName(final String localName)\n
    '''
def getElementById():
    '''returns Element\n\n
    getElementById(final String elementId)\n
    '''
def adoptNode():
    '''returns Node\n\n
    adoptNode(final Node source)\n
    '''
def getDocumentURI():
    '''returns String\n\n
    getDocumentURI()\n
    '''
def getDomConfig():
    '''returns DOMConfiguration\n\n
    getDomConfig()\n
    '''
def getInputEncoding():
    '''returns String\n\n
    getInputEncoding()\n
    '''
def getStrictErrorChecking():
    '''returns boolean\n\n
    getStrictErrorChecking()\n
    '''
def getXmlEncoding():
    '''returns String\n\n
    getXmlEncoding()\n
    '''
def getXmlStandalone():
    '''returns boolean\n\n
    getXmlStandalone()\n
    '''
def getXmlVersion():
    '''returns String\n\n
    getXmlVersion()\n
    '''
def normalizeDocument():
    '''returns None\n\n
    normalizeDocument()\n
    '''
def renameNode():
    '''returns Node\n\n
    renameNode(final Node n, final String namespaceURI, final String qualifiedName)\n
    '''
def setDocumentURI():
    '''returns None\n\n
    setDocumentURI(final String documentURI)\n
    '''
def setStrictErrorChecking():
    '''returns None\n\n
    setStrictErrorChecking(final boolean strictErrorChecking)\n
    '''
def setXmlStandalone():
    '''returns None\n\n
    setXmlStandalone(final boolean xmlStandalone)\n
    '''
def setXmlVersion():
    '''returns None\n\n
    setXmlVersion(final String xmlVersion)\n
    '''
