SYSTEM_PROPERTY_REMOVE_PROVIDERS = "String  \"com.ibm.ws.management.application.removeProviders\""
EXTENSION_POINT_ID = "String  \"app-depl-providers\""
RESOURCE_NAME = "String  \"META-INF/ibm-app-depl-providers.xml\""
def toString():
    '''returns String\n\n
    toString()\n
    '''
def ():
    '''returns ProviderHandler\n\n
    ()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final URL url)\n
    '''
def getProviders():
    '''returns Map\n\n
    getProviders()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String qName)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException arg0)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException arg0)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException arg0)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator arg0)\n
    '''
