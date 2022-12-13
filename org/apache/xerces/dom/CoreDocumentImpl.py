def CoreDocumentImpl():
    '''    public CoreDocumentImpl()
    public CoreDocumentImpl(final boolean allowGrammarAccess)
    public CoreDocumentImpl(final DocumentType documentType)
    public CoreDocumentImpl(final DocumentType documentType, final boolean b)
    '''
def getOwnerDocument():
    '''    public final Document getOwnerDocument()
    '''
def getNodeType():
    '''    public short getNodeType()
    '''
def getNodeName():
    '''    public String getNodeName()
    '''
def cloneNode():
    '''    public Node cloneNode(final boolean b)
    '''
def insertBefore():
    '''    public Node insertBefore(final Node node, final Node node2)
    '''
def removeChild():
    '''    public Node removeChild(final Node node)
    '''
def replaceChild():
    '''    public Node replaceChild(final Node node, final Node node2)
    '''
def getTextContent():
    '''    public String getTextContent()
    '''
def setTextContent():
    '''    public void setTextContent(final String s)
    '''
def getFeature():
    '''    public Object getFeature(final String s, final String s2)
    '''
def createAttribute():
    '''    public Attr createAttribute(final String s)
    '''
def createCDATASection():
    '''    public CDATASection createCDATASection(final String s)
    '''
def createComment():
    '''    public Comment createComment(final String s)
    '''
def createDocumentFragment():
    '''    public DocumentFragment createDocumentFragment()
    '''
def createElement():
    '''    public Element createElement(final String s)
    '''
def createEntityReference():
    '''    public EntityReference createEntityReference(final String s)
    '''
def createProcessingInstruction():
    '''    public ProcessingInstruction createProcessingInstruction(final String s, final String s2)
    '''
def createTextNode():
    '''    public Text createTextNode(final String s)
    '''
def getDoctype():
    '''    public DocumentType getDoctype()
    '''
def getDocumentElement():
    '''    public Element getDocumentElement()
    '''
def getElementsByTagName():
    '''    public NodeList getElementsByTagName(final String s)
    '''
def getImplementation():
    '''    public DOMImplementation getImplementation()
    '''
def setErrorChecking():
    '''    public void setErrorChecking(final boolean errorChecking)
    '''
def setStrictErrorChecking():
    '''    public void setStrictErrorChecking(final boolean errorChecking)
    '''
def getErrorChecking():
    '''    public boolean getErrorChecking()
    '''
def getStrictErrorChecking():
    '''    public boolean getStrictErrorChecking()
    '''
def getInputEncoding():
    '''    public String getInputEncoding()
    '''
def setInputEncoding():
    '''    public void setInputEncoding(final String actualEncoding)
    '''
def setXmlEncoding():
    '''    public void setXmlEncoding(final String encoding)
    '''
def setEncoding():
    '''    public void setEncoding(final String xmlEncoding)
    '''
def getXmlEncoding():
    '''    public String getXmlEncoding()
    '''
def getEncoding():
    '''    public String getEncoding()
    '''
def setXmlVersion():
    '''    public void setXmlVersion(final String s)
    '''
def setVersion():
    '''    public void setVersion(final String xmlVersion)
    '''
def getXmlVersion():
    '''    public String getXmlVersion()
    '''
def getVersion():
    '''    public String getVersion()
    '''
def setXmlStandalone():
    '''    public void setXmlStandalone(final boolean standalone)
    '''
def setStandalone():
    '''    public void setStandalone(final boolean xmlStandalone)
    '''
def getXmlStandalone():
    '''    public boolean getXmlStandalone()
    '''
def getStandalone():
    '''    public boolean getStandalone()
    '''
def getDocumentURI():
    '''    public String getDocumentURI()
    '''
def renameNode():
    '''    public Node renameNode(final Node node, final String s, final String s2)
    '''
def normalizeDocument():
    '''    public void normalizeDocument()
    '''
def getDomConfig():
    '''    public DOMConfiguration getDomConfig()
    '''
def getBaseURI():
    '''    public String getBaseURI()
    '''
def setDocumentURI():
    '''    public void setDocumentURI(final String fDocumentURI)
    '''
def getAsync():
    '''    public boolean getAsync()
    '''
def setAsync():
    '''    public void setAsync(final boolean b)
    '''
def abort():
    '''    public void abort()
    '''
def load():
    '''    public boolean load(final String s)
    '''
def loadXML():
    '''    public boolean loadXML(final String s)
    '''
def saveXML():
    '''    public String saveXML(Node node)
    '''
def createDocumentType():
    '''    public DocumentType createDocumentType(final String s, final String s2, final String s3)
    '''
def createEntity():
    '''    public Entity createEntity(final String s)
    '''
def createNotation():
    '''    public Notation createNotation(final String s)
    '''
def createElementDefinition():
    '''    public ElementDefinitionImpl createElementDefinition(final String s)
    '''
def importNode():
    '''    public Node importNode(final Node node, final boolean b)
    '''
def adoptNode():
    '''    public Node adoptNode(final Node node)
    '''
def getElementById():
    '''    public Element getElementById(final String s)
    '''
def putIdentifier():
    '''    public void putIdentifier(final String key, final Element value)
    '''
def getIdentifier():
    '''    public Element getIdentifier(final String key)
    '''
def removeIdentifier():
    '''    public void removeIdentifier(final String key)
    '''
def getIdentifiers():
    '''    public Enumeration getIdentifiers()
    '''
def createElementNS():
    '''    public Element createElementNS(final String s, final String s2)
    public Element createElementNS(final String s, final String s2, final String s3)
    '''
def createAttributeNS():
    '''    public Attr createAttributeNS(final String s, final String s2)
    public Attr createAttributeNS(final String s, final String s2, final String s3)
    '''
def getElementsByTagNameNS():
    '''    public NodeList getElementsByTagNameNS(final String s, final String s2)
    '''
def clone():
    '''    public Object clone()
    '''
def isXMLName():
    '''    public static final boolean isXMLName(final String s, final boolean b)
    '''
def isValidQName():
    '''    public static final boolean isValidQName(final String s, final String s2, final boolean b)
    '''
def setUserData():
    '''    public Object setUserData(final Node node, final String s, final Object o, final UserDataHandler userDataHandler)
    '''
def getUserData():
    '''    public Object getUserData(final Node node, final String key)
    '''
