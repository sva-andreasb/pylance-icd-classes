def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
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
    warning(final SAXParseException e)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException e)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException e)\n
    '''
