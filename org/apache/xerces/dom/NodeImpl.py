TREE_POSITION_PRECEDING = "short  1"
TREE_POSITION_FOLLOWING = "short  2"
TREE_POSITION_ANCESTOR = "short  4"
TREE_POSITION_DESCENDANT = "short  8"
TREE_POSITION_EQUIVALENT = "short  16"
TREE_POSITION_SAME_NODE = "short  32"
TREE_POSITION_DISCONNECTED = "short  0"
DOCUMENT_POSITION_DISCONNECTED = "short  1"
DOCUMENT_POSITION_PRECEDING = "short  2"
DOCUMENT_POSITION_FOLLOWING = "short  4"
DOCUMENT_POSITION_CONTAINS = "short  8"
DOCUMENT_POSITION_IS_CONTAINED = "short  16"
DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = "short  32"
ELEMENT_DEFINITION_NODE = "short  21"
def NodeImpl():
    '''    public NodeImpl()
    '''
def getNodeValue():
    '''    public String getNodeValue()
    '''
def setNodeValue():
    '''    public void setNodeValue(final String s)
    '''
def appendChild():
    '''    public Node appendChild(final Node node)
    '''
def cloneNode():
    '''    public Node cloneNode(final boolean b)
    '''
def getOwnerDocument():
    '''    public Document getOwnerDocument()
    '''
def getParentNode():
    '''    public Node getParentNode()
    '''
def getNextSibling():
    '''    public Node getNextSibling()
    '''
def getPreviousSibling():
    '''    public Node getPreviousSibling()
    '''
def getAttributes():
    '''    public NamedNodeMap getAttributes()
    '''
def hasAttributes():
    '''    public boolean hasAttributes()
    '''
def hasChildNodes():
    '''    public boolean hasChildNodes()
    '''
def getChildNodes():
    '''    public NodeList getChildNodes()
    '''
def getFirstChild():
    '''    public Node getFirstChild()
    '''
def getLastChild():
    '''    public Node getLastChild()
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
def getLength():
    '''    public int getLength()
    '''
def item():
    '''    public Node item(final int n)
    '''
def normalize():
    '''    public void normalize()
    '''
def isSupported():
    '''    public boolean isSupported(final String s, final String s2)
    '''
def getNamespaceURI():
    '''    public String getNamespaceURI()
    '''
def getPrefix():
    '''    public String getPrefix()
    '''
def setPrefix():
    '''    public void setPrefix(final String s)
    '''
def getLocalName():
    '''    public String getLocalName()
    '''
def addEventListener():
    '''    public void addEventListener(final String s, final EventListener eventListener, final boolean b)
    '''
def removeEventListener():
    '''    public void removeEventListener(final String s, final EventListener eventListener, final boolean b)
    '''
def dispatchEvent():
    '''    public boolean dispatchEvent(final Event event)
    '''
def getBaseURI():
    '''    public String getBaseURI()
    '''
def compareTreePosition():
    '''    public short compareTreePosition(final Node node)
    '''
def compareDocumentPosition():
    '''    public short compareDocumentPosition(final Node node)
    '''
def getTextContent():
    '''    public String getTextContent()
    '''
def setTextContent():
    '''    public void setTextContent(final String nodeValue)
    '''
def isSameNode():
    '''    public boolean isSameNode(final Node node)
    '''
def isDefaultNamespace():
    '''    public boolean isDefaultNamespace(final String s)
    '''
def lookupPrefix():
    '''    public String lookupPrefix(final String s)
    '''
def lookupNamespaceURI():
    '''    public String lookupNamespaceURI(final String s)
    '''
def isEqualNode():
    '''    public boolean isEqualNode(final Node node)
    '''
def getFeature():
    '''    public Object getFeature(final String s, final String s2)
    '''
def setUserData():
    '''    public Object setUserData(final String s, final Object o, final UserDataHandler userDataHandler)
    public void setUserData(final Object o)
    '''
def getUserData():
    '''    public Object getUserData(final String s)
    public Object getUserData()
    '''
def setReadOnly():
    '''    public void setReadOnly(final boolean b, final boolean b2)
    '''
def getReadOnly():
    '''    public boolean getReadOnly()
    '''
def needsSyncChildren():
    '''    public final void needsSyncChildren(final boolean b)
    '''
def toString():
    '''    public String toString()
    '''
