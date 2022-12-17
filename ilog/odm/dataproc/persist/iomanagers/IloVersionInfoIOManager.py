COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
VERSION_TAG = "String  \"version\""
PROPERTY_TAG = "String  \"property\""
NAME_TAG = "String  \"name\""
VALUE_TAG = "String  \"value\""
def ():
    '''returns Writer\n\n
    ()\n
    (final IloVersionInfo versionInfo, final OutputStream ostream)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String qName, final Attributes attrs)\n
    '''
def getVersionInfo():
    '''returns IloVersionInfo\n\n
    getVersionInfo()\n
    '''
def writeDocument():
    '''returns None\n\n
    writeDocument()\n
    '''
