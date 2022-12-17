WRITABLE = "short  2"
READABLE = "short  1"
UNREADABLE = "short  0"
SET_MODE = "short  0"
APPLY_DIFF_MODE = "short  1"
def ():
    '''returns IDAttributeMapper\n\n
    ()\n
    (final String a)\n
    (final String a, final IlvSettingsModel d)\n
    (final IlvSettingsElement[] a)\n
    ()\n
    (final int n)\n
    (final IlvSettingsNode e)\n
    (final NodeList list)\n
    (final IlvSettingsElement[] array)\n
    (final IlvSettingsAttribute[] array)\n
    (final String a, final String b, final Object c)\n
    (final String a, final String b)\n
    '''
def getBaseURI():
    '''returns String\n\n
    getBaseURI()\n
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
    setTextContent(final String s)\n
    '''
def isSameNode():
    '''returns boolean\n\n
    isSameNode(final Node node)\n
    '''
def lookupPrefix():
    '''returns String\n\n
    lookupPrefix(final String s)\n
    '''
def isDefaultNamespace():
    '''returns boolean\n\n
    isDefaultNamespace(final String s)\n
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
    '''returns Object\n\n
    setUserData(final String s, final Object o, final UserDataHandler userDataHandler)\n
    '''
def getUserData():
    '''returns Object\n\n
    getUserData(final String s)\n
    '''
def getInputEncoding():
    '''returns String\n\n
    getInputEncoding()\n
    '''
def getXmlEncoding():
    '''returns String\n\n
    getXmlEncoding()\n
    '''
def getXmlStandalone():
    '''returns boolean\n\n
    getXmlStandalone()\n
    '''
def setXmlStandalone():
    '''returns None\n\n
    setXmlStandalone(final boolean b)\n
    '''
def getXmlVersion():
    '''returns String\n\n
    getXmlVersion()\n
    '''
def setXmlVersion():
    '''returns None\n\n
    setXmlVersion(final String s)\n
    '''
def getStrictErrorChecking():
    '''returns boolean\n\n
    getStrictErrorChecking()\n
    '''
def setStrictErrorChecking():
    '''returns None\n\n
    setStrictErrorChecking(final boolean b)\n
    '''
def getDocumentURI():
    '''returns String\n\n
    getDocumentURI()\n
    '''
def setDocumentURI():
    '''returns None\n\n
    setDocumentURI(final String s)\n
    '''
def adoptNode():
    '''returns Node\n\n
    adoptNode(final Node node)\n
    '''
def getDomConfig():
    '''returns DOMConfiguration\n\n
    getDomConfig()\n
    '''
def normalizeDocument():
    '''returns None\n\n
    normalizeDocument()\n
    '''
def renameNode():
    '''returns Node\n\n
    renameNode(final Node node, final String s, final String s2)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String a)\n
    '''
def initializeSettings():
    '''returns boolean\n\n
    initializeSettings()\n
    '''
def areSettingsInitialized():
    '''returns boolean\n\n
    areSettingsInitialized()\n
    '''
def setModel():
    '''returns None\n\n
    setModel(final IlvSettingsModel d)\n
    '''
def getModel():
    '''returns IlvSettingsModel\n\n
    getModel()\n
    '''
def getMutableModel():
    '''returns IlvMutableSettingsModel\n\n
    getMutableModel()\n
    '''
def getSettingsManager():
    '''returns IlvSettingsManager\n\n
    getSettingsManager()\n
    '''
def setSettingsManager():
    '''returns None\n\n
    setSettingsManager(final IlvSettingsManager c)\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication h)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def getAccessRights():
    '''returns short\n\n
    getAccessRights()\n
    '''
def setAccessRights():
    '''returns None\n\n
    setAccessRights(final short f)\n
    '''
def canWrite():
    '''returns boolean\n\n
    canWrite()\n
    '''
def getID():
    '''returns Object\n\n
    getID(final Object o)\n
    getID(final Object o, final String anObject, final IlvSettingsModel ilvSettingsModel)\n
    '''
def addIDResolver():
    '''returns None\n\n
    addIDResolver(final IDResolver idResolver)\n
    '''
def removeIDResolver():
    '''returns boolean\n\n
    removeIDResolver(final IDResolver o)\n
    '''
def selectElement():
    '''returns IlvSettingsElement\n\n
    selectElement(final IlvSettingsQuery ilvSettingsQuery)\n
    selectElement(final String s, final String s2, final Object o)\n
    selectElement(final String s)\n
    '''
def select():
    '''returns IlvSettingsElement[]\n\n
    select(final IlvSettingsQuery ilvSettingsQuery)\n
    select(final String s, final IlvSettingsElement[] relativeElementList)\n
    select(final IlvSettingsQuery ilvSettingsQuery, final IlvSettingsElement[] relativeElementList)\n
    '''
def selectNodes():
    '''returns IlvSettingsNode[]\n\n
    selectNodes(final IlvSettingsQuery ilvSettingsQuery)\n
    '''
def ensureSettingsElement():
    '''returns IlvSettingsElement\n\n
    ensureSettingsElement(final IlvSettingsQuery ilvSettingsQuery)\n
    ensureSettingsElement(final String s)\n
    '''
def getCascadingMode():
    '''returns short\n\n
    getCascadingMode()\n
    '''
def setCascadingMode():
    '''returns None\n\n
    setCascadingMode(final short g)\n
    '''
def createSettingsElement():
    '''returns IlvSettingsElement\n\n
    createSettingsElement(final String s)\n
    '''
def removeSettingsElement():
    '''returns boolean\n\n
    removeSettingsElement(final IlvSettingsElement ilvSettingsElement)\n
    '''
def addSettingsElement():
    '''returns None\n\n
    addSettingsElement(final IlvSettingsElement ilvSettingsElement, final IlvSettingsElement ilvSettingsElement2, final int n)\n
    '''
def removeAllSettingsElements():
    '''returns boolean\n\n
    removeAllSettingsElements(final IlvSettingsElement ilvSettingsElement, final String s)\n
    '''
def ensureCorrespondingElement():
    '''returns Object\n\n
    ensureCorrespondingElement(final IlvSettingsElement ilvSettingsElement)\n
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
    createElement(final String s)\n
    '''
def createDocumentFragment():
    '''returns DocumentFragment\n\n
    createDocumentFragment()\n
    '''
def createTextNode():
    '''returns Text\n\n
    createTextNode(final String s)\n
    '''
def createComment():
    '''returns Comment\n\n
    createComment(final String s)\n
    '''
def createCDATASection():
    '''returns CDATASection\n\n
    createCDATASection(final String s)\n
    '''
def createProcessingInstruction():
    '''returns ProcessingInstruction\n\n
    createProcessingInstruction(final String s, final String s2)\n
    '''
def createAttribute():
    '''returns Attr\n\n
    createAttribute(final String s)\n
    '''
def createEntityReference():
    '''returns EntityReference\n\n
    createEntityReference(final String s)\n
    '''
def importNode():
    '''returns Node\n\n
    importNode(final Node node, final boolean b)\n
    '''
def createElementNS():
    '''returns Element\n\n
    createElementNS(final String s, final String s2)\n
    '''
def createAttributeNS():
    '''returns Attr\n\n
    createAttributeNS(final String s, final String s2)\n
    '''
def getElementById():
    '''returns Element\n\n
    getElementById(final String s)\n
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
    setNodeValue(final String s)\n
    '''
def getNodeType():
    '''returns short\n\n
    getNodeType()\n
    '''
def getParentNode():
    '''returns Node\n\n
    getParentNode()\n
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
    insertBefore(final Node node, final Node node2)\n
    '''
def replaceChild():
    '''returns Node\n\n
    replaceChild(final Node node, final Node node2)\n
    '''
def removeChild():
    '''returns Node\n\n
    removeChild(final Node node)\n
    '''
def appendChild():
    '''returns Node\n\n
    appendChild(final Node node)\n
    '''
def hasChildNodes():
    '''returns boolean\n\n
    hasChildNodes()\n
    '''
def cloneNode():
    '''returns Node\n\n
    cloneNode(final boolean b)\n
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
def hasAttributes():
    '''returns boolean\n\n
    hasAttributes()\n
    '''
def item():
    '''returns Node\n\n
    item(final int n)\n
    item(final int n)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    getLength()\n
    '''
def newNodeList():
    '''returns AbstractNodeList\n\n
    newNodeList()\n
    newNodeList(final AbstractNodeList list)\n
    newNodeList(final int n)\n
    newNodeList(final IlvSettingsAttribute[] array)\n
    newNodeList(final IlvSettingsNode ilvSettingsNode)\n
    '''
def getChildren():
    '''returns None\n\n
    getChildren(final IlvSettings ilvSettings, final IlvSettingsElement ilvSettingsElement, final String s, final AbstractNodeList list)\n
    '''
def copy():
    '''returns None\n\n
    copy(final AbstractNodeList list)\n
    '''
def insertNode():
    '''returns None\n\n
    insertNode(final int n, final IlvSettingsNode element)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def setID():
    '''returns boolean\n\n
    setID(final Object o, final Object o2, final String anObject, final IlvMutableSettingsModel ilvMutableSettingsModel)\n
    '''
