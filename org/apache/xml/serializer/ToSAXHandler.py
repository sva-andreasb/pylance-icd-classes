def ():
    '''returns ToSAXHandler\n\n
    ()\n
    (final ContentHandler hdlr, final LexicalHandler lex, final String encoding)\n
    (final ContentHandler handler, final String encoding)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String arg0, final String arg1, final String arg2)\n
    '''
def characters():
    '''returns None\n\n
    characters(final String characters)\n
    characters(final Node node)\n
    '''
def comment():
    '''returns None\n\n
    comment(final String comment)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String arg0, final String arg1, final String arg2, final Attributes arg3)\n
    startElement(final String uri, final String localName, final String qName)\n
    startElement(final String qName)\n
    '''
def setLexHandler():
    '''returns None\n\n
    setLexHandler(final LexicalHandler _lexHandler)\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler _saxHandler)\n
    '''
def setCdataSectionElements():
    '''returns None\n\n
    setCdataSectionElements(final Vector URI_and_localNames)\n
    '''
def setShouldOutputNSAttr():
    '''returns None\n\n
    setShouldOutputNSAttr(final boolean doOutputNSAttr)\n
    '''
def flushPending():
    '''returns None\n\n
    flushPending()\n
    '''
def setTransformState():
    '''returns None\n\n
    setTransformState(final TransformStateSetter ts)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException exc)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException exc)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException exc)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
def addUniqueAttribute():
    '''returns None\n\n
    addUniqueAttribute(final String qName, final String value, final int flags)\n
    '''
