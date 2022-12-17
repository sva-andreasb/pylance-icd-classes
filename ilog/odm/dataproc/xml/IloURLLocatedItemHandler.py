COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
URL_TAG = "String  \"url\""
JAVA_LOCATION_TAG = "String  \"javaLocation\""
CLASS_ATTR = "String  \"class\""
RESOURCE_NAME_ATTR = "String  \"resourceName\""
LINK_TAG = "String  \"link\""
HREF_ATTR = "String  \"href\""
def ():
    '''returns IloURLLocatedItemHandler\n\n
    (final IloDefaultRecursiveHandler previous, final String startTag)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String qName, final Attributes attrs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespaceURI, final String localName, final String qName)\n
    '''
def urlLocations():
    '''returns Iterator\n\n
    urlLocations()\n
    '''
def urlLocationCount():
    '''returns int\n\n
    urlLocationCount()\n
    '''
def getFirstURLLocation():
    '''returns IloURLLocation\n\n
    getFirstURLLocation()\n
    '''
