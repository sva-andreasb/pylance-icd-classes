def ():
    '''returns XMLSerializer\n\n
    ()\n
    (final OutputFormat outputFormat)\n
    (final Writer outputCharStream, final OutputFormat outputFormat)\n
    (final OutputStream outputByteStream, final OutputFormat outputFormat)\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final OutputFormat outputFormat)\n
    '''
def setNamespaces():
    '''returns None\n\n
    setNamespaces(final boolean fNamespaces)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String s, final String s2, String string, Attributes namespaces)\n
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
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
