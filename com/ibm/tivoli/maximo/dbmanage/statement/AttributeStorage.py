def ():
    '''returns AttributeStorage\n\n
    (final String[] names, final AttributeClass[] storage)\n
    (final AttributeStorageDefinition definition)\n
    (final AttributeStorageDefinition asd, final Element element)\n
    '''
def set():
    '''returns None\n\n
    set(final String attrName, final Object value)\n
    '''
def get():
    '''returns Object\n\n
    get(final String attrName)\n
    get(final int n)\n
    '''
def isSet():
    '''returns boolean\n\n
    isSet(final String attrName)\n
    '''
def clear():
    '''returns None\n\n
    clear(final String attrName)\n
    '''
def loadFromElement():
    '''returns None\n\n
    loadFromElement(final Element fromElement)\n
    '''
def saveToElement():
    '''returns None\n\n
    saveToElement(final Element toElement)\n
    saveToElement(final String[] columnDefAttributes, final Element toElement)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getSetAttr():
    '''returns Set<String>\n\n
    getSetAttr()\n
    '''
def setWithIgnore():
    '''returns None\n\n
    setWithIgnore(final String string, final Object object)\n
    '''
def copyFromStorage():
    '''returns None\n\n
    copyFromStorage(final AttributeStorage attr)\n
    '''
def loadFromResultSet():
    '''returns None\n\n
    loadFromResultSet(final ResultSet rs)\n
    '''
def hasAttribute():
    '''returns boolean\n\n
    hasAttribute(final String attrName)\n
    '''
def getAttrClass():
    '''returns AttributeClass\n\n
    getAttrClass(final String attr)\n
    '''
def getNameIterator():
    '''returns Iterator<String>\n\n
    getNameIterator()\n
    '''
def getValues():
    '''returns Object[]\n\n
    getValues()\n
    '''
def getDefinition():
    '''returns AttributeStorageDefinition\n\n
    getDefinition()\n
    '''
def getCommaLine():
    '''returns String\n\n
    getCommaLine()\n
    '''
def getTimestamp():
    '''returns Timestamp\n\n
    getTimestamp(final String attrName)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hasNoValues():
    '''returns boolean\n\n
    hasNoValues()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
