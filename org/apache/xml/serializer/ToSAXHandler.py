def ToSAXHandler():
    '''public ToSAXHandler()
    public ToSAXHandler(final ContentHandler hdlr, final LexicalHandler lex, final String encoding)
    public ToSAXHandler(final ContentHandler handler, final String encoding)
    '''
def startDTD():
    '''public void startDTD(final String arg0, final String arg1, final String arg2)
    '''
def characters():
    '''public void characters(final String characters)
    public void characters(final Node node)
    '''
def comment():
    '''public void comment(final String comment)
    '''
def processingInstruction():
    '''public void processingInstruction(final String target, final String data)
    '''
def startElement():
    '''public void startElement(final String arg0, final String arg1, final String arg2, final Attributes arg3)
    public void startElement(final String uri, final String localName, final String qName)
    public void startElement(final String qName)
    '''
def setLexHandler():
    '''public void setLexHandler(final LexicalHandler _lexHandler)
    '''
def setContentHandler():
    '''public void setContentHandler(final ContentHandler _saxHandler)
    '''
def setCdataSectionElements():
    '''public void setCdataSectionElements(final Vector URI_and_localNames)
    '''
def setShouldOutputNSAttr():
    '''public void setShouldOutputNSAttr(final boolean doOutputNSAttr)
    '''
def flushPending():
    '''public void flushPending()
    '''
def setTransformState():
    '''public void setTransformState(final TransformStateSetter ts)
    '''
def fatalError():
    '''public void fatalError(final SAXParseException exc)
    '''
def error():
    '''public void error(final SAXParseException exc)
    '''
def warning():
    '''public void warning(final SAXParseException exc)
    '''
def reset():
    '''public boolean reset()
    '''
def addUniqueAttribute():
    '''public void addUniqueAttribute(final String qName, final String value, final int flags)
    '''
