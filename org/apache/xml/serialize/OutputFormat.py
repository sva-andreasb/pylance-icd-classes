Indent = "int  4"
Encoding = "String  \"UTF-8\""
LineWidth = "int  72"
HTMLPublicId = "String  \"-//W3C//DTD HTML 4.01//EN\""
HTMLSystemId = "String  \"http://www.w3.org/TR/html4/strict.dtd\""
XHTMLPublicId = "String  \"-//W3C//DTD XHTML 1.0 Strict//EN\""
XHTMLSystemId = "String  \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\""
def ():
    '''returns OutputFormat\n\n
    ()\n
    (final String method, final String encoding, final boolean indenting)\n
    (final Document document)\n
    (final Document document, final String encoding, final boolean indenting)\n
    '''
def getMethod():
    '''returns String\n\n
    getMethod()\n
    '''
def setMethod():
    '''returns None\n\n
    setMethod(final String method)\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final String version)\n
    '''
def getIndent():
    '''returns int\n\n
    getIndent()\n
    '''
def getIndenting():
    '''returns boolean\n\n
    getIndenting()\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final int indent)\n
    '''
def setIndenting():
    '''returns None\n\n
    setIndenting(final boolean b)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    setEncoding(final EncodingInfo encodingInfo)\n
    '''
def getEncodingInfo():
    '''returns EncodingInfo\n\n
    getEncodingInfo()\n
    '''
def setAllowJavaNames():
    '''returns boolean\n\n
    setAllowJavaNames(final boolean allowJavaNames)\n
    setAllowJavaNames()\n
    '''
def getMediaType():
    '''returns String\n\n
    getMediaType()\n
    '''
def setMediaType():
    '''returns None\n\n
    setMediaType(final String mediaType)\n
    '''
def setDoctype():
    '''returns None\n\n
    setDoctype(final String doctypePublic, final String doctypeSystem)\n
    '''
def getDoctypePublic():
    '''returns String\n\n
    getDoctypePublic()\n
    '''
def getDoctypeSystem():
    '''returns String\n\n
    getDoctypeSystem()\n
    '''
def getOmitComments():
    '''returns boolean\n\n
    getOmitComments()\n
    '''
def setOmitComments():
    '''returns None\n\n
    setOmitComments(final boolean omitComments)\n
    '''
def getOmitDocumentType():
    '''returns boolean\n\n
    getOmitDocumentType()\n
    '''
def setOmitDocumentType():
    '''returns None\n\n
    setOmitDocumentType(final boolean omitDoctype)\n
    '''
def getOmitXMLDeclaration():
    '''returns boolean\n\n
    getOmitXMLDeclaration()\n
    '''
def setOmitXMLDeclaration():
    '''returns None\n\n
    setOmitXMLDeclaration(final boolean omitXmlDeclaration)\n
    '''
def getStandalone():
    '''returns boolean\n\n
    getStandalone()\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone(final boolean standalone)\n
    '''
def getCDataElements():
    '''returns String[]\n\n
    getCDataElements()\n
    '''
def isCDataElement():
    '''returns boolean\n\n
    isCDataElement(final String anObject)\n
    '''
def setCDataElements():
    '''returns None\n\n
    setCDataElements(final String[] cdataElements)\n
    '''
def getNonEscapingElements():
    '''returns String[]\n\n
    getNonEscapingElements()\n
    '''
def isNonEscapingElement():
    '''returns boolean\n\n
    isNonEscapingElement(final String anObject)\n
    '''
def setNonEscapingElements():
    '''returns None\n\n
    setNonEscapingElements(final String[] nonEscapingElements)\n
    '''
def getLineSeparator():
    '''returns String\n\n
    getLineSeparator()\n
    '''
def setLineSeparator():
    '''returns None\n\n
    setLineSeparator(final String lineSeparator)\n
    '''
def getPreserveSpace():
    '''returns boolean\n\n
    getPreserveSpace()\n
    '''
def setPreserveSpace():
    '''returns None\n\n
    setPreserveSpace(final boolean preserve)\n
    '''
def getLineWidth():
    '''returns int\n\n
    getLineWidth()\n
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final int lineWidth)\n
    '''
def getPreserveEmptyAttributes():
    '''returns boolean\n\n
    getPreserveEmptyAttributes()\n
    '''
def setPreserveEmptyAttributes():
    '''returns None\n\n
    setPreserveEmptyAttributes(final boolean preserveEmptyAttributes)\n
    '''
def getLastPrintable():
    '''returns char\n\n
    getLastPrintable()\n
    '''
