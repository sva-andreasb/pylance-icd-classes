def ():
    '''returns NGCCRuntime\n\n
    ()\n
    '''
def setRootHandler():
    '''returns None\n\n
    setRootHandler(final NGCCHandler rootHandler)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator _loc)\n
    '''
def getLocator():
    '''returns Locator\n\n
    getLocator()\n
    '''
def getCurrentAttributes():
    '''returns Attributes\n\n
    getCurrentAttributes()\n
    '''
def replace():
    '''returns int\n\n
    replace(final NGCCEventReceiver o, final NGCCEventReceiver n)\n
    '''
def processList():
    '''returns None\n\n
    processList(final String str)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localname, final String qname, final Attributes atts)\n
    '''
def onEnterElementConsumed():
    '''returns None\n\n
    onEnterElementConsumed(final String uri, final String localName, final String qname, final Attributes atts)\n
    '''
def onLeaveElementConsumed():
    '''returns None\n\n
    onLeaveElementConsumed(final String uri, final String localName, final String qname)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localname, final String qname)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def getAttributeIndex():
    '''returns int\n\n
    getAttributeIndex(final String uri, final String localname)\n
    '''
def consumeAttribute():
    '''returns None\n\n
    consumeAttribute(final int index)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def sendEnterAttribute():
    '''returns None\n\n
    sendEnterAttribute(final int threadId, final String uri, final String local, final String qname)\n
    '''
def sendEnterElement():
    '''returns None\n\n
    sendEnterElement(final int threadId, final String uri, final String local, final String qname, final Attributes atts)\n
    '''
def sendLeaveAttribute():
    '''returns None\n\n
    sendLeaveAttribute(final int threadId, final String uri, final String local, final String qname)\n
    '''
def sendLeaveElement():
    '''returns None\n\n
    sendLeaveElement(final int threadId, final String uri, final String local, final String qname)\n
    '''
def sendText():
    '''returns None\n\n
    sendText(final int threadId, final String value)\n
    '''
def redirectSubtree():
    '''returns None\n\n
    redirectSubtree(final ContentHandler child, final String uri, final String local, final String qname)\n
    '''
def resolveNamespacePrefix():
    '''returns String\n\n
    resolveNamespacePrefix(final String prefix)\n
    '''
def trace():
    '''returns None\n\n
    trace(final String s)\n
    '''
def traceln():
    '''returns None\n\n
    traceln(final String s)\n
    '''
