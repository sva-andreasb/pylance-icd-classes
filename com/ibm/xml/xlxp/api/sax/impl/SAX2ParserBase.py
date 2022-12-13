def xmlDeclEvent():
    '''    public void xmlDeclEvent(final XMLString xmlString)
    '''
def startElementEvent():
    '''    public void startElementEvent(final QName qName, final NSDeclList fnsDecls, final AttrList fAttrs, final boolean b)
    '''
def endElementEvent():
    '''    public void endElementEvent(final QName qName, final NSDeclList fnsDecls)
    '''
def characters():
    '''    public void characters(final XMLString xmlString)
    '''
def whitespace():
    '''    public void whitespace(final XMLString xmlString)
    '''
def character():
    '''    public void character(final int n, final boolean b)
    '''
def processingInstruction():
    '''    public void processingInstruction(final XMLString xmlString, final XMLString xmlString2)
    '''
def skippedEntity():
    '''    public boolean skippedEntity(final XMLString xmlString)
    '''
def startEntity():
    '''    public void startEntity(final XMLString xmlString)
    '''
def endEntity():
    '''    public void endEntity(final XMLString xmlString)
    '''
def startCDATASection():
    '''    public void startCDATASection()
    '''
def endCDATASection():
    '''    public void endCDATASection()
    '''
def comment():
    '''    public void comment(final XMLString xmlString)
    '''
def reportWarning():
    '''    public void reportWarning(final String s, final int n, final int n2, final XMLString[] array)
    '''
def reportRecoverableError():
    '''    public void reportRecoverableError(final String s, final int n, final int n2, final XMLString[] array)
    '''
def reportFatalError():
    '''    public void reportFatalError(final String s, final int n, final int n2, final XMLString[] array)
    '''
def getLength():
    '''    public int getLength()
    '''
def getURI():
    '''    public String getURI(final int n)
    '''
def getLocalName():
    '''    public String getLocalName(final int n)
    '''
def getQName():
    '''    public String getQName(final int n)
    '''
def getType():
    '''    public String getType(final int n)
    public String getType(final String s, final String s2)
    public String getType(final String s)
    '''
def getValue():
    '''    public String getValue(int n)
    public String getValue(final String s, final String s2)
    public String getValue(final String s)
    '''
def getIndex():
    '''    public int getIndex(final String s, final String s2)
    public int getIndex(final String s)
    '''
def getPublicId():
    '''    public String getPublicId()
    '''
def getSystemId():
    '''    public String getSystemId()
    '''
def getLineNumber():
    '''    public int getLineNumber()
    '''
def getColumnNumber():
    '''    public int getColumnNumber()
    '''
def getFeature():
    '''    public boolean getFeature(final String s)
    '''
def setFeature():
    '''    public void setFeature(final String s, final boolean b)
    '''
def getProperty():
    '''    public Object getProperty(final String s)
    '''
def setProperty():
    '''    public void setProperty(final String s, final Object o)
    '''
def setContentHandler():
    '''    public void setContentHandler(final ContentHandler fContentHandler)
    '''
def getContentHandler():
    '''    public ContentHandler getContentHandler()
    '''
def setErrorHandler():
    '''    public void setErrorHandler(final ErrorHandler fErrorHandler)
    '''
def getErrorHandler():
    '''    public ErrorHandler getErrorHandler()
    '''
def parse():
    '''    public void parse(final InputSource inputSource)
    public void parse(final String systemId)
    '''
