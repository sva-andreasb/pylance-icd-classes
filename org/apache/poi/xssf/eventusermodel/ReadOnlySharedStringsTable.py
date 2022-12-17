def ():
    '''returns ReadOnlySharedStringsTable\n\n
    (final OPCPackage pkg)\n
    (final OPCPackage pkg, final boolean includePhoneticRuns)\n
    (final PackagePart part)\n
    (final PackagePart part, final boolean includePhoneticRuns)\n
    '''
def readFrom():
    '''returns None\n\n
    readFrom(final InputStream is)\n
    '''
def getCount():
    '''returns int\n\n
    getCount()\n
    '''
def getUniqueCount():
    '''returns int\n\n
    getUniqueCount()\n
    '''
def getEntryAt():
    '''returns String\n\n
    getEntryAt(final int idx)\n
    '''
def getItems():
    '''returns List<String>\n\n
    getItems()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String name, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String name)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
