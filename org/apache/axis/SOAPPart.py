FORM_STRING = "int  1"
FORM_INPUTSTREAM = "int  2"
FORM_SOAPENVELOPE = "int  3"
FORM_BYTES = "int  4"
FORM_BODYINSTREAM = "int  5"
FORM_FAULT = "int  6"
FORM_OPTIMIZED = "int  7"
ALLOW_FORM_OPTIMIZATION = "String  \"axis.form.optimization\""
def ():
    '''returns SOAPPart\n\n
    (final Message parent, final Object initialContents, final boolean isBodyStream)\n
    '''
def getMessage():
    '''returns Message\n\n
    getMessage()\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final Message msg)\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def setSOAPEnvelope():
    '''returns None\n\n
    setSOAPEnvelope(final SOAPEnvelope env)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream os)\n
    writeTo(final Writer writer)\n
    '''
def getCurrentMessage():
    '''returns Object\n\n
    getCurrentMessage()\n
    '''
def setCurrentMessage():
    '''returns None\n\n
    setCurrentMessage(final Object currMsg, final int form)\n
    '''
def getCurrentForm():
    '''returns int\n\n
    getCurrentForm()\n
    '''
def getAsBytes():
    '''returns byte[]\n\n
    getAsBytes()\n
    '''
def saveChanges():
    '''returns None\n\n
    saveChanges()\n
    '''
def getAsString():
    '''returns String\n\n
    getAsString()\n
    '''
def getAsSOAPEnvelope():
    '''returns SOAPEnvelope\n\n
    getAsSOAPEnvelope()\n
    '''
def addMimeHeader():
    '''returns None\n\n
    addMimeHeader(final String header, final String value)\n
    '''
def getContentLocation():
    '''returns String\n\n
    getContentLocation()\n
    '''
def setContentLocation():
    '''returns None\n\n
    setContentLocation(final String loc)\n
    '''
def setContentId():
    '''returns None\n\n
    setContentId(final String newCid)\n
    '''
def getContentId():
    '''returns String\n\n
    getContentId()\n
    '''
def getContentIdRef():
    '''returns String\n\n
    getContentIdRef()\n
    '''
def getMatchingMimeHeaders():
    '''returns Iterator\n\n
    getMatchingMimeHeaders(final String[] match)\n
    '''
def getNonMatchingMimeHeaders():
    '''returns Iterator\n\n
    getNonMatchingMimeHeaders(final String[] match)\n
    '''
def setContent():
    '''returns None\n\n
    setContent(final Source source)\n
    '''
def getContent():
    '''returns Source\n\n
    getContent()\n
    '''
def getAllMimeHeaders():
    '''returns Iterator\n\n
    getAllMimeHeaders()\n
    '''
def setMimeHeader():
    '''returns None\n\n
    setMimeHeader(final String name, final String value)\n
    '''
def getMimeHeader():
    '''returns String[]\n\n
    getMimeHeader(final String name)\n
    '''
def removeAllMimeHeaders():
    '''returns None\n\n
    removeAllMimeHeaders()\n
    '''
def removeMimeHeader():
    '''returns None\n\n
    removeMimeHeader(final String header)\n
    '''
def getSOAPDocument():
    '''returns Document\n\n
    getSOAPDocument()\n
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
def getElementsByTagName():
    '''returns NodeList\n\n
    getElementsByTagName(final String tagname)\n
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
def getElementById():
    '''returns Element\n\n
    getElementById(final String elementId)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String s)\n
    '''
def getStandalone():
    '''returns boolean\n\n
    getStandalone()\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone(final boolean flag)\n
    '''
def getStrictErrorChecking():
    '''returns boolean\n\n
    getStrictErrorChecking()\n
    '''
def setStrictErrorChecking():
    '''returns None\n\n
    setStrictErrorChecking(final boolean flag)\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final String s)\n
    '''
def adoptNode():
    '''returns Node\n\n
    adoptNode(final Node node)\n
    '''
def getNodeName():
    '''returns String\n\n
    getNodeName()\n
    '''
def getNodeValue():
    '''returns String\n\n
    getNodeValue()\n
    '''
def setNodeValue():
    '''returns None\n\n
    setNodeValue(final String nodeValue)\n
    '''
def getNodeType():
    '''returns short\n\n
    getNodeType()\n
    '''
def getParentNode():
    '''returns Node\n\n
    getParentNode()\n
    '''
def getChildNodes():
    '''returns NodeList\n\n
    getChildNodes()\n
    '''
def getFirstChild():
    '''returns Node\n\n
    getFirstChild()\n
    '''
def getLastChild():
    '''returns Node\n\n
    getLastChild()\n
    '''
def getPreviousSibling():
    '''returns Node\n\n
    getPreviousSibling()\n
    '''
def getNextSibling():
    '''returns Node\n\n
    getNextSibling()\n
    '''
def getAttributes():
    '''returns NamedNodeMap\n\n
    getAttributes()\n
    '''
def getOwnerDocument():
    '''returns Document\n\n
    getOwnerDocument()\n
    '''
def insertBefore():
    '''returns Node\n\n
    insertBefore(final Node newChild, final Node refChild)\n
    '''
def replaceChild():
    '''returns Node\n\n
    replaceChild(final Node newChild, final Node oldChild)\n
    '''
def removeChild():
    '''returns Node\n\n
    removeChild(final Node oldChild)\n
    '''
def appendChild():
    '''returns Node\n\n
    appendChild(final Node newChild)\n
    '''
def hasChildNodes():
    '''returns boolean\n\n
    hasChildNodes()\n
    '''
def cloneNode():
    '''returns Node\n\n
    cloneNode(final boolean deep)\n
    '''
def normalize():
    '''returns None\n\n
    normalize()\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported(final String feature, final String version)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    '''
def setPrefix():
    '''returns None\n\n
    setPrefix(final String prefix)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName()\n
    '''
def hasAttributes():
    '''returns boolean\n\n
    hasAttributes()\n
    '''
def isBodyStream():
    '''returns boolean\n\n
    isBodyStream()\n
    '''
