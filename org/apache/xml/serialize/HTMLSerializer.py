XHTMLNamespace = "String  \"http://www.w3.org/1999/xhtml\""
def ():
    '''returns HTMLSerializer\n\n
    ()\n
    (final OutputFormat outputFormat)\n
    (final Writer outputCharStream, final OutputFormat outputFormat)\n
    (final OutputStream outputByteStream, final OutputFormat outputFormat)\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final OutputFormat outputFormat)\n
    '''
def setXHTMLNamespace():
    '''returns None\n\n
    setXHTMLNamespace(final String fUserXHTMLNamespace)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String anObject, final String str, String string, final Attributes attributes)\n
    startElement(final String s, final AttributeList list)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String s, final String s2, final String s3)\n
    endElement(final String s)\n
    '''
def endElementIO():
    '''returns None\n\n
    endElementIO(final String s, final String s2, final String s3)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] array, final int n, final int n2)\n
    '''
