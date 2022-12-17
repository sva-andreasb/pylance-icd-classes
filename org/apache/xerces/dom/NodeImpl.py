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
def ():
    '''returns NodeImpl\n\n
    ()\n
    '''
def getNodeValue():
    '''returns String\n\n
    getNodeValue()\n
    '''
def setNodeValue():
    '''returns None\n\n
    setNodeValue(final String s)\n
    '''
def appendChild():
    '''returns Node\n\n
    appendChild(final Node node)\n
    '''
def cloneNode():
    '''returns Node\n\n
    cloneNode(final boolean b)\n
    '''
def getOwnerDocument():
    '''returns Document\n\n
    getOwnerDocument()\n
    '''
def getParentNode():
    '''returns Node\n\n
    getParentNode()\n
    '''
def getNextSibling():
    '''returns Node\n\n
    getNextSibling()\n
    '''
def getPreviousSibling():
    '''returns Node\n\n
    getPreviousSibling()\n
    '''
def getAttributes():
    '''returns NamedNodeMap\n\n
    getAttributes()\n
    '''
def hasAttributes():
    '''returns boolean\n\n
    hasAttributes()\n
    '''
def hasChildNodes():
    '''returns boolean\n\n
    hasChildNodes()\n
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
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def item():
    '''returns Node\n\n
    item(final int n)\n
    '''
def normalize():
    '''returns None\n\n
    normalize()\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported(final String s, final String s2)\n
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
    setPrefix(final String s)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName()\n
    '''
def addEventListener():
    '''returns None\n\n
    addEventListener(final String s, final EventListener eventListener, final boolean b)\n
    '''
def removeEventListener():
    '''returns None\n\n
    removeEventListener(final String s, final EventListener eventListener, final boolean b)\n
    '''
def dispatchEvent():
    '''returns boolean\n\n
    dispatchEvent(final Event event)\n
    '''
def getBaseURI():
    '''returns String\n\n
    getBaseURI()\n
    '''
def compareTreePosition():
    '''returns short\n\n
    compareTreePosition(final Node node)\n
    '''
def compareDocumentPosition():
    '''returns short\n\n
    compareDocumentPosition(final Node node)\n
    '''
def getTextContent():
    '''returns String\n\n
    getTextContent()\n
    '''
def setTextContent():
    '''returns None\n\n
    setTextContent(final String nodeValue)\n
    '''
def isSameNode():
    '''returns boolean\n\n
    isSameNode(final Node node)\n
    '''
def isDefaultNamespace():
    '''returns boolean\n\n
    isDefaultNamespace(final String s)\n
    '''
def lookupPrefix():
    '''returns String\n\n
    lookupPrefix(final String s)\n
    '''
def lookupNamespaceURI():
    '''returns String\n\n
    lookupNamespaceURI(final String s)\n
    '''
def isEqualNode():
    '''returns boolean\n\n
    isEqualNode(final Node node)\n
    '''
def getFeature():
    '''returns Object\n\n
    getFeature(final String s, final String s2)\n
    '''
def setUserData():
    '''returns None\n\n
    setUserData(final String s, final Object o, final UserDataHandler userDataHandler)\n
    setUserData(final Object o)\n
    '''
def getUserData():
    '''returns Object\n\n
    getUserData(final String s)\n
    getUserData()\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly(final boolean b, final boolean b2)\n
    '''
def getReadOnly():
    '''returns boolean\n\n
    getReadOnly()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
