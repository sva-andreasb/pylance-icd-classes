TAG = "String  \"tag\""
ATTRIBUTE = "String  \"attribute\""
NAME = "String  \"name\""
ALIAS = "String  \"alias\""
VALUE = "String  \"value\""
CONTENT = "String  \"content\""
def TagMap():
    '''    public TagMap(final String tagfile)
    public TagMap(final InputStream in)
    '''
def AttributeHandler():
    '''    public AttributeHandler(final HashMap tagMap)
    '''
def startElement():
    '''    public void startElement(final String uri, final String lname, final String tag, final Attributes attrs)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final char[] ch, final int start, final int length)
    '''
def characters():
    '''    public void characters(final char[] ch, final int start, final int length)
    '''
def endElement():
    '''    public void endElement(final String uri, final String lname, final String tag)
    '''
