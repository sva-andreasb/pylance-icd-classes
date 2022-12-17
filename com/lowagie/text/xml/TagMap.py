TAG = "String  \"tag\""
ATTRIBUTE = "String  \"attribute\""
NAME = "String  \"name\""
ALIAS = "String  \"alias\""
VALUE = "String  \"value\""
CONTENT = "String  \"content\""
def ():
    '''returns AttributeHandler\n\n
    (final String tagfile)\n
    (final InputStream in)\n
    (final HashMap tagMap)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String lname, final String tag, final Attributes attrs)\n
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
    endElement(final String uri, final String lname, final String tag)\n
    '''
