FORM_STRING = "int  1"
FORM_INPUTSTREAM = "int  2"
FORM_SOAPENVELOPE = "int  3"
FORM_BYTES = "int  4"
FORM_BODYINSTREAM = "int  5"
FORM_FAULT = "int  6"
FORM_OPTIMIZED = "int  7"
ALLOW_FORM_OPTIMIZATION = "String  axis.form.optimization""
def SOAPPart():
'''public SOAPPart(final Message parent, final Object initialContents, final boolean isBodyStream)
'''
pass
def getMessage():
'''public Message getMessage()
'''
pass
def setMessage():
'''public void setMessage(final Message msg)
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getContentLength():
'''public long getContentLength()
'''
pass
def setSOAPEnvelope():
'''public void setSOAPEnvelope(final SOAPEnvelope env)
'''
pass
def writeTo():
'''public void writeTo(final OutputStream os)
public void writeTo(final Writer writer)
'''
pass
def getCurrentMessage():
'''public Object getCurrentMessage()
'''
pass
def setCurrentMessage():
'''public void setCurrentMessage(final Object currMsg, final int form)
'''
pass
def getCurrentForm():
'''public int getCurrentForm()
'''
pass
def getAsBytes():
'''public byte[] getAsBytes()
'''
pass
def saveChanges():
'''public void saveChanges()
'''
pass
def getAsString():
'''public String getAsString()
'''
pass
def getAsSOAPEnvelope():
'''public SOAPEnvelope getAsSOAPEnvelope()
'''
pass
def addMimeHeader():
'''public void addMimeHeader(final String header, final String value)
'''
pass
def getContentLocation():
'''public String getContentLocation()
'''
pass
def setContentLocation():
'''public void setContentLocation(final String loc)
'''
pass
def setContentId():
'''public void setContentId(final String newCid)
'''
pass
def getContentId():
'''public String getContentId()
'''
pass
def getContentIdRef():
'''public String getContentIdRef()
'''
pass
def getMatchingMimeHeaders():
'''public Iterator getMatchingMimeHeaders(final String[] match)
'''
pass
def getNonMatchingMimeHeaders():
'''public Iterator getNonMatchingMimeHeaders(final String[] match)
'''
pass
def setContent():
'''public void setContent(final Source source)
'''
pass
def getContent():
'''public Source getContent()
'''
pass
def getAllMimeHeaders():
'''public Iterator getAllMimeHeaders()
'''
pass
def setMimeHeader():
'''public void setMimeHeader(final String name, final String value)
'''
pass
def getMimeHeader():
'''public String[] getMimeHeader(final String name)
'''
pass
def removeAllMimeHeaders():
'''public void removeAllMimeHeaders()
'''
pass
def removeMimeHeader():
'''public void removeMimeHeader(final String header)
'''
pass
def getSOAPDocument():
'''public Document getSOAPDocument()
'''
pass
def getDoctype():
'''public DocumentType getDoctype()
'''
pass
def getImplementation():
'''public DOMImplementation getImplementation()
'''
pass
def getDocumentElement():
'''public Element getDocumentElement()
'''
pass
def createElement():
'''public Element createElement(final String tagName)
'''
pass
def createDocumentFragment():
'''public DocumentFragment createDocumentFragment()
'''
pass
def createTextNode():
'''public Text createTextNode(final String data)
'''
pass
def createComment():
'''public Comment createComment(final String data)
'''
pass
def createCDATASection():
'''public CDATASection createCDATASection(final String data)
'''
pass
def createProcessingInstruction():
'''public ProcessingInstruction createProcessingInstruction(final String target, final String data)
'''
pass
def createAttribute():
'''public Attr createAttribute(final String name)
'''
pass
def createEntityReference():
'''public EntityReference createEntityReference(final String name)
'''
pass
def getElementsByTagName():
'''public NodeList getElementsByTagName(final String tagname)
'''
pass
def importNode():
'''public Node importNode(final Node importedNode, final boolean deep)
'''
pass
def createElementNS():
'''public Element createElementNS(final String namespaceURI, final String qualifiedName)
'''
pass
def createAttributeNS():
'''public Attr createAttributeNS(final String namespaceURI, final String qualifiedName)
'''
pass
def getElementsByTagNameNS():
'''public NodeList getElementsByTagNameNS(final String namespaceURI, final String localName)
'''
pass
def getElementById():
'''public Element getElementById(final String elementId)
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def setEncoding():
'''public void setEncoding(final String s)
'''
pass
def getStandalone():
'''public boolean getStandalone()
'''
pass
def setStandalone():
'''public void setStandalone(final boolean flag)
'''
pass
def getStrictErrorChecking():
'''public boolean getStrictErrorChecking()
'''
pass
def setStrictErrorChecking():
'''public void setStrictErrorChecking(final boolean flag)
'''
pass
def getVersion():
'''public String getVersion()
'''
pass
def setVersion():
'''public void setVersion(final String s)
'''
pass
def adoptNode():
'''public Node adoptNode(final Node node)
'''
pass
def getNodeName():
'''public String getNodeName()
'''
pass
def getNodeValue():
'''public String getNodeValue()
'''
pass
def setNodeValue():
'''public void setNodeValue(final String nodeValue)
'''
pass
def getNodeType():
'''public short getNodeType()
'''
pass
def getParentNode():
'''public Node getParentNode()
'''
pass
def getChildNodes():
'''public NodeList getChildNodes()
'''
pass
def getFirstChild():
'''public Node getFirstChild()
'''
pass
def getLastChild():
'''public Node getLastChild()
'''
pass
def getPreviousSibling():
'''public Node getPreviousSibling()
'''
pass
def getNextSibling():
'''public Node getNextSibling()
'''
pass
def getAttributes():
'''public NamedNodeMap getAttributes()
'''
pass
def getOwnerDocument():
'''public Document getOwnerDocument()
'''
pass
def insertBefore():
'''public Node insertBefore(final Node newChild, final Node refChild)
'''
pass
def replaceChild():
'''public Node replaceChild(final Node newChild, final Node oldChild)
'''
pass
def removeChild():
'''public Node removeChild(final Node oldChild)
'''
pass
def appendChild():
'''public Node appendChild(final Node newChild)
'''
pass
def hasChildNodes():
'''public boolean hasChildNodes()
'''
pass
def cloneNode():
'''public Node cloneNode(final boolean deep)
'''
pass
def normalize():
'''public void normalize()
'''
pass
def isSupported():
'''public boolean isSupported(final String feature, final String version)
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI()
'''
pass
def getPrefix():
'''public String getPrefix()
'''
pass
def setPrefix():
'''public void setPrefix(final String prefix)
'''
pass
def getLocalName():
'''public String getLocalName()
'''
pass
def hasAttributes():
'''public boolean hasAttributes()
'''
pass
def isBodyStream():
'''public boolean isBodyStream()
'''
pass
def getDocumentURI():
'''public String getDocumentURI()
'''
pass
def getDomConfig():
'''public DOMConfiguration getDomConfig()
'''
pass
def getInputEncoding():
'''public String getInputEncoding()
'''
pass
def getXmlEncoding():
'''public String getXmlEncoding()
'''
pass
def getXmlStandalone():
'''public boolean getXmlStandalone()
'''
pass
def getXmlVersion():
'''public String getXmlVersion()
'''
pass
def normalizeDocument():
'''public void normalizeDocument()
'''
pass
def renameNode():
'''public Node renameNode(final Node n, final String namespaceURI, final String qualifiedName)
'''
pass
def setDocumentURI():
'''public void setDocumentURI(final String documentURI)
'''
pass
def setXmlStandalone():
'''public void setXmlStandalone(final boolean xmlStandalone)
'''
pass
def setXmlVersion():
'''public void setXmlVersion(final String xmlVersion)
'''
pass
def compareDocumentPosition():
'''public short compareDocumentPosition(final Node other)
'''
pass
def getBaseURI():
'''public String getBaseURI()
'''
pass
def getFeature():
'''public Object getFeature(final String feature, final String version)
'''
pass
def getTextContent():
'''public String getTextContent()
'''
pass
def getUserData():
'''public Object getUserData(final String key)
'''
pass
def isDefaultNamespace():
'''public boolean isDefaultNamespace(final String namespaceURI)
'''
pass
def isEqualNode():
'''public boolean isEqualNode(final Node arg)
'''
pass
def isSameNode():
'''public boolean isSameNode(final Node other)
'''
pass
def lookupNamespaceURI():
'''public String lookupNamespaceURI(final String prefix)
'''
pass
def lookupPrefix():
'''public String lookupPrefix(final String namespaceURI)
'''
pass
def setTextContent():
'''public void setTextContent(final String textContent)
'''
pass
def setUserData():
'''public Object setUserData(final String key, final Object data, final UserDataHandler handler)
'''
pass
