def ():
    '''returns SAXOutputter\n\n
    (final SerializationContext context)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String p1, final String p2)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String p1)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] p1, final int p2, final int p3)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] p1, final int p2, final int p3)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String p1)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String qName, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final String qName)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
