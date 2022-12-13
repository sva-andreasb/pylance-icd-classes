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
'''public NodeImpl()
'''
pass
def getNodeValue():
'''public String getNodeValue()
'''
pass
def setNodeValue():
'''public void setNodeValue(final String s)
'''
pass
def appendChild():
'''public Node appendChild(final Node node)
'''
pass
def cloneNode():
'''public Node cloneNode(final boolean b)
'''
pass
def getOwnerDocument():
'''public Document getOwnerDocument()
'''
pass
def getParentNode():
'''public Node getParentNode()
'''
pass
def getNextSibling():
'''public Node getNextSibling()
'''
pass
def getPreviousSibling():
'''public Node getPreviousSibling()
'''
pass
def getAttributes():
'''public NamedNodeMap getAttributes()
'''
pass
def hasAttributes():
'''public boolean hasAttributes()
'''
pass
def hasChildNodes():
'''public boolean hasChildNodes()
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
def insertBefore():
'''public Node insertBefore(final Node node, final Node node2)
'''
pass
def removeChild():
'''public Node removeChild(final Node node)
'''
pass
def replaceChild():
'''public Node replaceChild(final Node node, final Node node2)
'''
pass
def getLength():
'''public int getLength()
'''
pass
def item():
'''public Node item(final int n)
'''
pass
def normalize():
'''public void normalize()
'''
pass
def isSupported():
'''public boolean isSupported(final String s, final String s2)
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
'''public void setPrefix(final String s)
'''
pass
def getLocalName():
'''public String getLocalName()
'''
pass
def addEventListener():
'''public void addEventListener(final String s, final EventListener eventListener, final boolean b)
'''
pass
def removeEventListener():
'''public void removeEventListener(final String s, final EventListener eventListener, final boolean b)
'''
pass
def dispatchEvent():
'''public boolean dispatchEvent(final Event event)
'''
pass
def getBaseURI():
'''public String getBaseURI()
'''
pass
def compareTreePosition():
'''public short compareTreePosition(final Node node)
'''
pass
def compareDocumentPosition():
'''public short compareDocumentPosition(final Node node)
'''
pass
def getTextContent():
'''public String getTextContent()
'''
pass
def setTextContent():
'''public void setTextContent(final String nodeValue)
'''
pass
def isSameNode():
'''public boolean isSameNode(final Node node)
'''
pass
def isDefaultNamespace():
'''public boolean isDefaultNamespace(final String s)
'''
pass
def lookupPrefix():
'''public String lookupPrefix(final String s)
'''
pass
def lookupNamespaceURI():
'''public String lookupNamespaceURI(final String s)
'''
pass
def isEqualNode():
'''public boolean isEqualNode(final Node node)
'''
pass
def getFeature():
'''public Object getFeature(final String s, final String s2)
'''
pass
def setUserData():
'''public Object setUserData(final String s, final Object o, final UserDataHandler userDataHandler)
public void setUserData(final Object o)
'''
pass
def getUserData():
'''public Object getUserData(final String s)
public Object getUserData()
'''
pass
def setReadOnly():
'''public void setReadOnly(final boolean b, final boolean b2)
'''
pass
def getReadOnly():
'''public boolean getReadOnly()
'''
pass
def needsSyncChildren():
'''public final void needsSyncChildren(final boolean b)
'''
pass
def toString():
'''public String toString()
'''
pass
