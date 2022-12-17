def ():
    '''returns CdmAttribute\n\n
    (final InputStream stream1, final InputStream stream2, final InputStream xsd, final Connection con)\n
    (final String tableName, final String attributeName, final String assetattrid)\n
    (final String className, final String attributeName)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def getCDMClass():
    '''returns String\n\n
    getCDMClass(final String objectName, final String classstructureid)\n
    '''
def getAllClassesForMBO():
    '''returns List<String>\n\n
    getAllClassesForMBO(final String mboObjectName)\n
    '''
def getAllMBONamingAttributes():
    '''returns List<MboAttribute>\n\n
    getAllMBONamingAttributes(final String objectName, final String classstructureid)\n
    '''
def getCDMNamingAttribute():
    '''returns CdmAttribute\n\n
    getCDMNamingAttribute(final MboAttribute mboAttribute)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String qName, final Attributes attrs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespaceURI, final String localName, final String qName)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException e)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException e)\n
    '''
def getVersionStr():
    '''returns String\n\n
    getVersionStr()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName()\n
    getAttributeName()\n
    '''
def getAssetattrid():
    '''returns String\n\n
    getAssetattrid()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
