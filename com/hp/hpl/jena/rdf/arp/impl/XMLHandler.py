def ():
    '''returns XMLHandler\n\n
    ()\n
    '''
def triple():
    '''returns None\n\n
    triple(final ANode s, final ANode p, final ANode o)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def getLocator():
    '''returns Locator\n\n
    getLocator()\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String rawName, final Attributes atts)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String rawName)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def warning():
    '''returns None\n\n
    warning(final Taint taintMe, final int id, final String msg)\n
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
def endLocalScope():
    '''returns None\n\n
    endLocalScope(final ANode v)\n
    '''
def endRDF():
    '''returns None\n\n
    endRDF()\n
    endRDF()\n
    '''
def startRDF():
    '''returns None\n\n
    startRDF()\n
    startRDF()\n
    '''
def isError():
    '''returns boolean\n\n
    isError(final int eCode)\n
    '''
def getHandlers():
    '''returns ARPHandlers\n\n
    getHandlers()\n
    '''
def getOptions():
    '''returns ARPOptions\n\n
    getOptions()\n
    '''
def setOptionsWith():
    '''returns None\n\n
    setOptionsWith(final ARPOptions newOpts)\n
    '''
def setHandlersWith():
    '''returns None\n\n
    setHandlersWith(final ARPHandlers newHh)\n
    '''
def initParse():
    '''returns None\n\n
    initParse(final String base, final String lang)\n
    '''
def location():
    '''returns Location\n\n
    location()\n
    '''
def allowRelativeURIs():
    '''returns boolean\n\n
    allowRelativeURIs()\n
    '''
def sameDocRef():
    '''returns IRI\n\n
    sameDocRef()\n
    '''
def setBadStatementHandler():
    '''returns None\n\n
    setBadStatementHandler(final StatementHandler sh)\n
    '''
def statement():
    '''returns None\n\n
    statement(final AResource s, final AResource p, final AResource o)\n
    statement(final AResource s, final AResource p, final ALiteral o)\n
    '''
def endBNodeScope():
    '''returns None\n\n
    endBNodeScope(final AResource bnode)\n
    '''
def discardNodesWithNodeID():
    '''returns boolean\n\n
    discardNodesWithNodeID()\n
    '''
