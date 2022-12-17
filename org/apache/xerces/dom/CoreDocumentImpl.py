def ():
    '''returns CoreDocumentImpl\n\n
    ()\n
    (final boolean allowGrammarAccess)\n
    (final DocumentType documentType)\n
    (final DocumentType documentType, final boolean b)\n
    '''
def getNodeType():
    '''returns short\n\n
    getNodeType()\n
    '''
def getNodeName():
    '''returns String\n\n
    getNodeName()\n
    '''
def cloneNode():
    '''returns Node\n\n
    cloneNode(final boolean b)\n
    '''
def insertBefore():
    '''returns Node\n\n
    insertBefore(final Node node, final Node node2)\n
    '''
def removeChild():
    '''returns Node\n\n
    removeChild(final Node node)\n
    '''
def replaceChild():
    '''returns Node\n\n
    replaceChild(final Node node, final Node node2)\n
    '''
def getTextContent():
    '''returns String\n\n
    getTextContent()\n
    '''
def setTextContent():
    '''returns None\n\n
    setTextContent(final String s)\n
    '''
def getFeature():
    '''returns Object\n\n
    getFeature(final String s, final String s2)\n
    '''
def createAttribute():
    '''returns Attr\n\n
    createAttribute(final String s)\n
    '''
def createCDATASection():
    '''returns CDATASection\n\n
    createCDATASection(final String s)\n
    '''
def createComment():
    '''returns Comment\n\n
    createComment(final String s)\n
    '''
def createDocumentFragment():
    '''returns DocumentFragment\n\n
    createDocumentFragment()\n
    '''
def createElement():
    '''returns Element\n\n
    createElement(final String s)\n
    '''
def createEntityReference():
    '''returns EntityReference\n\n
    createEntityReference(final String s)\n
    '''
def createProcessingInstruction():
    '''returns ProcessingInstruction\n\n
    createProcessingInstruction(final String s, final String s2)\n
    '''
def createTextNode():
    '''returns Text\n\n
    createTextNode(final String s)\n
    '''
def getDoctype():
    '''returns DocumentType\n\n
    getDoctype()\n
    '''
def getDocumentElement():
    '''returns Element\n\n
    getDocumentElement()\n
    '''
def getElementsByTagName():
    '''returns NodeList\n\n
    getElementsByTagName(final String s)\n
    '''
def getImplementation():
    '''returns DOMImplementation\n\n
    getImplementation()\n
    '''
def setErrorChecking():
    '''returns None\n\n
    setErrorChecking(final boolean errorChecking)\n
    '''
def setStrictErrorChecking():
    '''returns None\n\n
    setStrictErrorChecking(final boolean errorChecking)\n
    '''
def getErrorChecking():
    '''returns boolean\n\n
    getErrorChecking()\n
    '''
def getStrictErrorChecking():
    '''returns boolean\n\n
    getStrictErrorChecking()\n
    '''
def getInputEncoding():
    '''returns String\n\n
    getInputEncoding()\n
    '''
def setInputEncoding():
    '''returns None\n\n
    setInputEncoding(final String actualEncoding)\n
    '''
def setXmlEncoding():
    '''returns None\n\n
    setXmlEncoding(final String encoding)\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String xmlEncoding)\n
    '''
def getXmlEncoding():
    '''returns String\n\n
    getXmlEncoding()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setXmlVersion():
    '''returns None\n\n
    setXmlVersion(final String s)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final String xmlVersion)\n
    '''
def getXmlVersion():
    '''returns String\n\n
    getXmlVersion()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setXmlStandalone():
    '''returns None\n\n
    setXmlStandalone(final boolean standalone)\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone(final boolean xmlStandalone)\n
    '''
def getXmlStandalone():
    '''returns boolean\n\n
    getXmlStandalone()\n
    '''
def getStandalone():
    '''returns boolean\n\n
    getStandalone()\n
    '''
def getDocumentURI():
    '''returns String\n\n
    getDocumentURI()\n
    '''
def renameNode():
    '''returns Node\n\n
    renameNode(final Node node, final String s, final String s2)\n
    '''
def normalizeDocument():
    '''returns None\n\n
    normalizeDocument()\n
    '''
def getDomConfig():
    '''returns DOMConfiguration\n\n
    getDomConfig()\n
    '''
def getBaseURI():
    '''returns String\n\n
    getBaseURI()\n
    '''
def setDocumentURI():
    '''returns None\n\n
    setDocumentURI(final String fDocumentURI)\n
    '''
def getAsync():
    '''returns boolean\n\n
    getAsync()\n
    '''
def setAsync():
    '''returns None\n\n
    setAsync(final boolean b)\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def load():
    '''returns boolean\n\n
    load(final String s)\n
    '''
def loadXML():
    '''returns boolean\n\n
    loadXML(final String s)\n
    '''
def saveXML():
    '''returns String\n\n
    saveXML(Node node)\n
    '''
def createDocumentType():
    '''returns DocumentType\n\n
    createDocumentType(final String s, final String s2, final String s3)\n
    '''
def createEntity():
    '''returns Entity\n\n
    createEntity(final String s)\n
    '''
def createNotation():
    '''returns Notation\n\n
    createNotation(final String s)\n
    '''
def createElementDefinition():
    '''returns ElementDefinitionImpl\n\n
    createElementDefinition(final String s)\n
    '''
def importNode():
    '''returns Node\n\n
    importNode(final Node node, final boolean b)\n
    '''
def adoptNode():
    '''returns Node\n\n
    adoptNode(final Node node)\n
    '''
def getElementById():
    '''returns Element\n\n
    getElementById(final String s)\n
    '''
def putIdentifier():
    '''returns None\n\n
    putIdentifier(final String key, final Element value)\n
    '''
def getIdentifier():
    '''returns Element\n\n
    getIdentifier(final String key)\n
    '''
def removeIdentifier():
    '''returns None\n\n
    removeIdentifier(final String key)\n
    '''
def getIdentifiers():
    '''returns Enumeration\n\n
    getIdentifiers()\n
    '''
def createElementNS():
    '''returns Element\n\n
    createElementNS(final String s, final String s2)\n
    createElementNS(final String s, final String s2, final String s3)\n
    '''
def createAttributeNS():
    '''returns Attr\n\n
    createAttributeNS(final String s, final String s2)\n
    createAttributeNS(final String s, final String s2, final String s3)\n
    '''
def getElementsByTagNameNS():
    '''returns NodeList\n\n
    getElementsByTagNameNS(final String s, final String s2)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def setUserData():
    '''returns Object\n\n
    setUserData(final Node node, final String s, final Object o, final UserDataHandler userDataHandler)\n
    '''
def getUserData():
    '''returns Object\n\n
    getUserData(final Node node, final String key)\n
    '''
