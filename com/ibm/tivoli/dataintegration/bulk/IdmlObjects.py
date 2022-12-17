FULL_XML_STRING = "int  0"
MSS_XML_STRING = "int  1"
ME_XML_STRING = "int  2"
REL_XML_STRING = "int  3"
def ():
    '''returns IdmlNamespaceContext\n\n
    ()\n
    ()\n
    '''
def parse():
    '''returns None\n\n
    parse(final InputSource is)\n
    parse(final String xml, final int xmltype)\n
    '''
def getMssElements():
    '''returns List\n\n
    getMssElements()\n
    '''
def getManagedElements():
    '''returns List\n\n
    getManagedElements()\n
    '''
def getExtendedAttributes():
    '''returns List\n\n
    getExtendedAttributes()\n
    '''
def getRelationships():
    '''returns List\n\n
    getRelationships()\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String prefix)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String namespaceURI)\n
    '''
def getPrefixes():
    '''returns Iterator\n\n
    getPrefixes(final String namespaceURI)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException spe)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException spe)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException spe)\n
    '''
