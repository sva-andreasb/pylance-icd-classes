def ():
    '''returns AttributesMap\n\n
    (final IlvSettings ilvSettings)\n
    ()\n
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
def getSchemaTypeInfo():
    '''returns TypeInfo\n\n
    getSchemaTypeInfo()\n
    '''
def setIdAttribute():
    '''returns None\n\n
    setIdAttribute(final String s, final boolean b)\n
    '''
def setIdAttributeNS():
    '''returns None\n\n
    setIdAttributeNS(final String s, final String s2, final boolean b)\n
    '''
def setIdAttributeNode():
    '''returns None\n\n
    setIdAttributeNode(final Attr attr, final boolean b)\n
    '''
def getNodeType():
    '''returns short\n\n
    getNodeType()\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String s)\n
    getInt(final String s, final int n)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final String s, final int value)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String s)\n
    getString(final String s, final String s2)\n
    '''
def setString():
    '''returns None\n\n
    setString(final String s, final String s2)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String s)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String s)\n
    getBoolean(final String s, final boolean b)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final String s, final boolean value)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final String s)\n
    getFloat(final String s, final float n)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final String s, final float f)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final String s)\n
    getDouble(final String s, final double n)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final String s, final double d)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final String s)\n
    getDate(final String s, final Date date)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final String s, final Date date)\n
    '''
def getColor():
    '''returns Color\n\n
    getColor(final String s)\n
    getColor(final String s, final Color color)\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final String s, final Color color)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont(final String s)\n
    getFont(final String s, final Font font)\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final String s, final Font font)\n
    '''
def getRectangle():
    '''returns Rectangle\n\n
    getRectangle()\n
    getRectangle(final Rectangle rectangle)\n
    '''
def setRectangle():
    '''returns None\n\n
    setRectangle(final Rectangle rectangle)\n
    '''
def getAttributeValue():
    '''returns Object\n\n
    getAttributeValue(final String key)\n
    getAttributeValue(final Object o, final String s)\n
    '''
def setAttributeValue():
    '''returns None\n\n
    setAttributeValue(final String key, Object value)\n
    setAttributeValue(final Object o, final String s, final Object o2)\n
    '''
def getStringArray():
    '''returns String[]\n\n
    getStringArray(final String s, final String s2)\n
    '''
def setStringArray():
    '''returns None\n\n
    setStringArray(final String s, final String s2, String[] array)\n
    '''
def getColorArray():
    '''returns Color[]\n\n
    getColorArray(final String s, final String s2)\n
    '''
def setColorArray():
    '''returns None\n\n
    setColorArray(final String s, final String s2, Color[] array)\n
    '''
def getAttributeNodes():
    '''returns IlvSettingsAttribute[]\n\n
    getAttributeNodes()\n
    '''
def getAttributeNames():
    '''returns String[]\n\n
    getAttributeNames()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    getType(final Object o)\n
    '''
def getFirstChild():
    '''returns Node\n\n
    getFirstChild(final String s)\n
    getFirstChild()\n
    '''
def getChildren():
    '''returns Object[]\n\n
    getChildren(final IlvSettingsQuery ilvSettingsQuery)\n
    getChildren(final String s)\n
    getChildren()\n
    getChildren(final Object o)\n
    '''
def getChild():
    '''returns IlvSettingsElement\n\n
    getChild(final String s, final String s2, final Object o)\n
    '''
def ensureChildElement():
    '''returns IlvSettingsElement\n\n
    ensureChildElement(final IlvSettingsQuery ilvSettingsQuery)\n
    ensureChildElement(final String s)\n
    ensureChildElement(final String s, final String s2, final Object o)\n
    '''
def getElement():
    '''returns IlvSettingsElement\n\n
    getElement(final String s, final String s2, final Object o)\n
    '''
def getDefaultAttributeValue():
    '''returns Object\n\n
    getDefaultAttributeValue(final String key)\n
    '''
def getID():
    '''returns Object\n\n
    getID()\n
    '''
def setID():
    '''returns boolean\n\n
    setID(final Object o)\n
    '''
def addSettingsElement():
    '''returns None\n\n
    addSettingsElement(final Object o, final Object o2, final int n)\n
    '''
def removeSettingsElement():
    '''returns boolean\n\n
    removeSettingsElement(final Object o, final Object o2)\n
    '''
def createSettingsElement():
    '''returns Object\n\n
    createSettingsElement(final String s)\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object o)\n
    '''
def getAttributes():
    '''returns NamedNodeMap\n\n
    getAttributes(final Object o)\n
    getAttributes()\n
    '''
def add():
    '''returns None\n\n
    add(final IlvSettingsElement ilvSettingsElement)\n
    '''
def insert():
    '''returns None\n\n
    insert(final IlvSettingsElement ilvSettingsElement, final int n)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final IlvSettingsElement ilvSettingsElement)\n
    '''
def removeFromParent():
    '''returns None\n\n
    removeFromParent()\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll(final String s)\n
    '''
def getCascadedElementCount():
    '''returns int\n\n
    getCascadedElementCount()\n
    '''
def getCascadedElement():
    '''returns Object\n\n
    getCascadedElement(final int index)\n
    getCascadedElement(final IlvSettings ilvSettings)\n
    '''
def getCascadedSettings():
    '''returns IlvSettings\n\n
    getCascadedSettings(final int index)\n
    '''
def removeCascadedElement():
    '''returns boolean\n\n
    removeCascadedElement(final Object o)\n
    '''
def isDOMElement():
    '''returns boolean\n\n
    isDOMElement()\n
    '''
def getDOMElement():
    '''returns Element\n\n
    getDOMElement()\n
    '''
def matchType():
    '''returns boolean\n\n
    matchType(final String s)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def resetModifications():
    '''returns None\n\n
    resetModifications()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
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
    setNodeValue(final String text)\n
    '''
def getChildNodes():
    '''returns NodeList\n\n
    getChildNodes()\n
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
def getTagName():
    '''returns String\n\n
    getTagName()\n
    '''
def getAttribute():
    '''returns String\n\n
    getAttribute(final String s)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String s, final String s2)\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final String s)\n
    '''
def getAttributeNode():
    '''returns Attr\n\n
    getAttributeNode(final String s)\n
    '''
def setAttributeNode():
    '''returns Attr\n\n
    setAttributeNode(final Attr attr)\n
    '''
def removeAttributeNode():
    '''returns Attr\n\n
    removeAttributeNode(final Attr attr)\n
    '''
def getElementsByTagName():
    '''returns NodeList\n\n
    getElementsByTagName(final String s)\n
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
def getAttributeNS():
    '''returns String\n\n
    getAttributeNS(final String s, final String s2)\n
    '''
def setAttributeNS():
    '''returns None\n\n
    setAttributeNS(final String s, final String s2, final String s3)\n
    '''
def removeAttributeNS():
    '''returns None\n\n
    removeAttributeNS(final String s, final String s2)\n
    '''
def getAttributeNodeNS():
    '''returns Attr\n\n
    getAttributeNodeNS(final String s, final String s2)\n
    '''
def setAttributeNodeNS():
    '''returns Attr\n\n
    setAttributeNodeNS(final Attr attributeNodeNS)\n
    '''
def getElementsByTagNameNS():
    '''returns NodeList\n\n
    getElementsByTagNameNS(final String s, final String s2)\n
    '''
def hasAttribute():
    '''returns boolean\n\n
    hasAttribute(final String s)\n
    '''
def hasAttributeNS():
    '''returns boolean\n\n
    hasAttributeNS(final String s, final String s2)\n
    '''
def getNamedItem():
    '''returns Node\n\n
    getNamedItem(final String s)\n
    '''
def setNamedItem():
    '''returns Node\n\n
    setNamedItem(final Node node)\n
    '''
def removeNamedItem():
    '''returns Node\n\n
    removeNamedItem(final String s)\n
    '''
def item():
    '''returns Node\n\n
    item(final int n)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getNamedItemNS():
    '''returns Node\n\n
    getNamedItemNS(final String s, final String s2)\n
    '''
def setNamedItemNS():
    '''returns Node\n\n
    setNamedItemNS(final Node node)\n
    '''
def removeNamedItemNS():
    '''returns Node\n\n
    removeNamedItemNS(final String s, final String s2)\n
    '''
