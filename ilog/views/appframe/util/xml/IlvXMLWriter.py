DEFAULT_OUTPUT_ENCODING = "String  \"UTF-8\""
def ():
    '''returns IlvXMLWriter\n\n
    ()\n
    (final boolean fCanonical)\n
    '''
def setCanonical():
    '''returns None\n\n
    setCanonical(final boolean fCanonical)\n
    '''
def setOutput():
    '''returns None\n\n
    setOutput(final OutputStream out, final String encoding)\n
    setOutput(final OutputStream outputStream)\n
    setOutput(final Writer out)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettings ilvSettings, final IlvSettingsModel ilvSettingsModel)\n
    '''
def writeDocument():
    '''returns None\n\n
    writeDocument(final Document document)\n
    '''
def setHeaderComment():
    '''returns None\n\n
    setHeaderComment(final String header)\n
    '''
def getHeaderComment():
    '''returns String\n\n
    getHeaderComment()\n
    '''
def writeElement():
    '''returns None\n\n
    writeElement(final Element element, final String s)\n
    writeElement(final Object o, final IlvSettingsModel ilvSettingsModel, final String s)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o, final Object o2)\n
    '''
