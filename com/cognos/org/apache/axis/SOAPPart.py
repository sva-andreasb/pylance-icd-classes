FORM_STRING = "int  1"
FORM_INPUTSTREAM = "int  2"
FORM_SOAPENVELOPE = "int  3"
FORM_BYTES = "int  4"
FORM_BODYINSTREAM = "int  5"
FORM_FAULT = "int  6"
FORM_OPTIMIZED = "int  7"
ALLOW_FORM_OPTIMIZATION = "String  \"axis.form.optimization\""
def SOAPPart():
    '''public SOAPPart(final Message parent, final Object initialContents, final boolean isBodyStream)
    '''
def getMessage():
    '''public Message getMessage()
    '''
def setMessage():
    '''public void setMessage(final Message msg)
    '''
def getContentType():
    '''public String getContentType()
    '''
def getContentLength():
    '''public long getContentLength()
    '''
def setSOAPEnvelope():
    '''public void setSOAPEnvelope(final SOAPEnvelope env)
    '''
def writeTo():
    '''public void writeTo(final OutputStream os)
    public void writeTo(final Writer writer)
    '''
def getCurrentMessage():
    '''public Object getCurrentMessage()
    '''
def setCurrentMessage():
    '''public void setCurrentMessage(final Object currMsg, final int form)
    '''
def getCurrentForm():
    '''public int getCurrentForm()
    '''
def getAsBytes():
    '''public byte[] getAsBytes()
    '''
def saveChanges():
    '''public void saveChanges()
    '''
def getAsString():
    '''public String getAsString()
    '''
def getAsSOAPEnvelope():
    '''public SOAPEnvelope getAsSOAPEnvelope()
    '''
def addMimeHeader():
    '''public void addMimeHeader(final String header, final String value)
    '''
def getContentLocation():
    '''public String getContentLocation()
    '''
def setContentLocation():
    '''public void setContentLocation(final String loc)
    '''
def setContentId():
    '''public void setContentId(final String newCid)
    '''
def getContentId():
    '''public String getContentId()
    '''
def getContentIdRef():
    '''public String getContentIdRef()
    '''
def getMatchingMimeHeaders():
    '''public Iterator getMatchingMimeHeaders(final String[] match)
    '''
def getNonMatchingMimeHeaders():
    '''public Iterator getNonMatchingMimeHeaders(final String[] match)
    '''
def setContent():
    '''public void setContent(final Source source)
    '''
def getContent():
    '''public Source getContent()
    '''
def getAllMimeHeaders():
    '''public Iterator getAllMimeHeaders()
    '''
def setMimeHeader():
    '''public void setMimeHeader(final String name, final String value)
    '''
def getMimeHeader():
    '''public String[] getMimeHeader(final String name)
    '''
def removeAllMimeHeaders():
    '''public void removeAllMimeHeaders()
    '''
def removeMimeHeader():
    '''public void removeMimeHeader(final String header)
    '''
def getSOAPDocument():
    '''public Document getSOAPDocument()
    '''
def getDoctype():
    '''public DocumentType getDoctype()
    '''
def getImplementation():
    '''public DOMImplementation getImplementation()
    '''
def getDocumentElement():
    '''public Element getDocumentElement()
    '''
def createElement():
    '''public Element createElement(final String tagName)
    '''
def createDocumentFragment():
    '''public DocumentFragment createDocumentFragment()
    '''
def createTextNode():
    '''public Text createTextNode(final String data)
    '''
def createComment():
    '''public Comment createComment(final String data)
    '''
def createCDATASection():
    '''public CDATASection createCDATASection(final String data)
    '''
def createProcessingInstruction():
    '''public ProcessingInstruction createProcessingInstruction(final String target, final String data)
    '''
def createAttribute():
    '''public Attr createAttribute(final String name)
    '''
def createEntityReference():
    '''public EntityReference createEntityReference(final String name)
    '''
def getElementsByTagName():
    '''public NodeList getElementsByTagName(final String tagname)
    '''
def importNode():
    '''public Node importNode(final Node importedNode, final boolean deep)
    '''
def createElementNS():
    '''public Element createElementNS(final String namespaceURI, final String qualifiedName)
    '''
def createAttributeNS():
    '''public Attr createAttributeNS(final String namespaceURI, final String qualifiedName)
    '''
def getElementsByTagNameNS():
    '''public NodeList getElementsByTagNameNS(final String namespaceURI, final String localName)
    '''
def getElementById():
    '''public Element getElementById(final String elementId)
    '''
def getEncoding():
    '''public String getEncoding()
    '''
def setEncoding():
    '''public void setEncoding(final String s)
    '''
def getStandalone():
    '''public boolean getStandalone()
    '''
def setStandalone():
    '''public void setStandalone(final boolean flag)
    '''
def getStrictErrorChecking():
    '''public boolean getStrictErrorChecking()
    '''
def setStrictErrorChecking():
    '''public void setStrictErrorChecking(final boolean flag)
    '''
def getVersion():
    '''public String getVersion()
    '''
def setVersion():
    '''public void setVersion(final String s)
    '''
def adoptNode():
    '''public Node adoptNode(final Node node)
    '''
def getNodeName():
    '''public String getNodeName()
    '''
def getNodeValue():
    '''public String getNodeValue()
    '''
def setNodeValue():
    '''public void setNodeValue(final String nodeValue)
    '''
def getNodeType():
    '''public short getNodeType()
    '''
def getParentNode():
    '''public Node getParentNode()
    '''
def getChildNodes():
    '''public NodeList getChildNodes()
    '''
def getFirstChild():
    '''public Node getFirstChild()
    '''
def getLastChild():
    '''public Node getLastChild()
    '''
def getPreviousSibling():
    '''public Node getPreviousSibling()
    '''
def getNextSibling():
    '''public Node getNextSibling()
    '''
def getAttributes():
    '''public NamedNodeMap getAttributes()
    '''
def getOwnerDocument():
    '''public Document getOwnerDocument()
    '''
def insertBefore():
    '''public Node insertBefore(final Node newChild, final Node refChild)
    '''
def replaceChild():
    '''public Node replaceChild(final Node newChild, final Node oldChild)
    '''
def removeChild():
    '''public Node removeChild(final Node oldChild)
    '''
def appendChild():
    '''public Node appendChild(final Node newChild)
    '''
def hasChildNodes():
    '''public boolean hasChildNodes()
    '''
def cloneNode():
    '''public Node cloneNode(final boolean deep)
    '''
def normalize():
    '''public void normalize()
    '''
def isSupported():
    '''public boolean isSupported(final String feature, final String version)
    '''
def getNamespaceURI():
    '''public String getNamespaceURI()
    '''
def getPrefix():
    '''public String getPrefix()
    '''
def setPrefix():
    '''public void setPrefix(final String prefix)
    '''
def getLocalName():
    '''public String getLocalName()
    '''
def hasAttributes():
    '''public boolean hasAttributes()
    '''
def isBodyStream():
    '''public boolean isBodyStream()
    '''
def getDocumentURI():
    '''public String getDocumentURI()
    '''
def getDomConfig():
    '''public DOMConfiguration getDomConfig()
    '''
def getInputEncoding():
    '''public String getInputEncoding()
    '''
def getXmlEncoding():
    '''public String getXmlEncoding()
    '''
def getXmlStandalone():
    '''public boolean getXmlStandalone()
    '''
def getXmlVersion():
    '''public String getXmlVersion()
    '''
def normalizeDocument():
    '''public void normalizeDocument()
    '''
def renameNode():
    '''public Node renameNode(final Node n, final String namespaceURI, final String qualifiedName)
    '''
def setDocumentURI():
    '''public void setDocumentURI(final String documentURI)
    '''
def setXmlStandalone():
    '''public void setXmlStandalone(final boolean xmlStandalone)
    '''
def setXmlVersion():
    '''public void setXmlVersion(final String xmlVersion)
    '''
def compareDocumentPosition():
    '''public short compareDocumentPosition(final Node other)
    '''
def getBaseURI():
    '''public String getBaseURI()
    '''
def getFeature():
    '''public Object getFeature(final String feature, final String version)
    '''
def getTextContent():
    '''public String getTextContent()
    '''
def getUserData():
    '''public Object getUserData(final String key)
    '''
def isDefaultNamespace():
    '''public boolean isDefaultNamespace(final String namespaceURI)
    '''
def isEqualNode():
    '''public boolean isEqualNode(final Node arg)
    '''
def isSameNode():
    '''public boolean isSameNode(final Node other)
    '''
def lookupNamespaceURI():
    '''public String lookupNamespaceURI(final String prefix)
    '''
def lookupPrefix():
    '''public String lookupPrefix(final String namespaceURI)
    '''
def setTextContent():
    '''public void setTextContent(final String textContent)
    '''
def setUserData():
    '''public Object setUserData(final String key, final Object data, final UserDataHandler handler)
    '''
