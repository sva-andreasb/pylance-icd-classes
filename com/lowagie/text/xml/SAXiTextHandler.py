def ():
    '''returns SAXiTextHandler\n\n
    (final DocListener document)\n
    '''
def setControlOpenClose():
    '''returns None\n\n
    setControlOpenClose(final boolean controlOpenClose)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String lname, final String name, final Attributes attrs)\n
    '''
def handleStartingTags():
    '''returns None\n\n
    handleStartingTags(final String name, final Properties attributes)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String lname, final String name)\n
    '''
def handleEndingTags():
    '''returns None\n\n
    handleEndingTags(final String name)\n
    '''
