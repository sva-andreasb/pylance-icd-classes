ELEMENT = "String  \"reference\""
ATTR_BEGIN = "String  \"begin\""
ATTR_END = "String  \"end\""
ATTR_TYPE = "String  \"type\""
ATTR_ANCHOR = "String  \"anchor\""
ATTR_URI = "String  \"uri\""
def ():
    '''returns ReferenceElement\n\n
    (final Integer begin, final Integer end, final Type type, final String anchor, final URI uri, final ExtensionElement child)\n
    (final Integer begin, final Integer end, final Type type, final String anchor, final URI uri)\n
    '''
def getBegin():
    '''returns Integer\n\n
    getBegin()\n
    '''
def getEnd():
    '''returns Integer\n\n
    getEnd()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getAnchor():
    '''returns String\n\n
    getAnchor()\n
    '''
def getUri():
    '''returns URI\n\n
    getUri()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
