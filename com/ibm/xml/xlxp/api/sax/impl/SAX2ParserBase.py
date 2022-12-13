def xmlDeclEvent():
'''public void xmlDeclEvent(final XMLString xmlString)
'''
pass
def startElementEvent():
'''public void startElementEvent(final QName qName, final NSDeclList fnsDecls, final AttrList fAttrs, final boolean b)
'''
pass
def endElementEvent():
'''public void endElementEvent(final QName qName, final NSDeclList fnsDecls)
'''
pass
def characters():
'''public void characters(final XMLString xmlString)
'''
pass
def whitespace():
'''public void whitespace(final XMLString xmlString)
'''
pass
def character():
'''public void character(final int n, final boolean b)
'''
pass
def processingInstruction():
'''public void processingInstruction(final XMLString xmlString, final XMLString xmlString2)
'''
pass
def skippedEntity():
'''public boolean skippedEntity(final XMLString xmlString)
'''
pass
def startEntity():
'''public void startEntity(final XMLString xmlString)
'''
pass
def endEntity():
'''public void endEntity(final XMLString xmlString)
'''
pass
def startCDATASection():
'''public void startCDATASection()
'''
pass
def endCDATASection():
'''public void endCDATASection()
'''
pass
def comment():
'''public void comment(final XMLString xmlString)
'''
pass
def reportWarning():
'''public void reportWarning(final String s, final int n, final int n2, final XMLString[] array)
'''
pass
def reportRecoverableError():
'''public void reportRecoverableError(final String s, final int n, final int n2, final XMLString[] array)
'''
pass
def reportFatalError():
'''public void reportFatalError(final String s, final int n, final int n2, final XMLString[] array)
'''
pass
def getLength():
'''public int getLength()
'''
pass
def getURI():
'''public String getURI(final int n)
'''
pass
def getLocalName():
'''public String getLocalName(final int n)
'''
pass
def getQName():
'''public String getQName(final int n)
'''
pass
def getType():
'''public String getType(final int n)
public String getType(final String s, final String s2)
public String getType(final String s)
'''
pass
def getValue():
'''public String getValue(int n)
public String getValue(final String s, final String s2)
public String getValue(final String s)
'''
pass
def getIndex():
'''public int getIndex(final String s, final String s2)
public int getIndex(final String s)
'''
pass
def getPublicId():
'''public String getPublicId()
'''
pass
def getSystemId():
'''public String getSystemId()
'''
pass
def getLineNumber():
'''public int getLineNumber()
'''
pass
def getColumnNumber():
'''public int getColumnNumber()
'''
pass
def getFeature():
'''public boolean getFeature(final String s)
'''
pass
def setFeature():
'''public void setFeature(final String s, final boolean b)
'''
pass
def getProperty():
'''public Object getProperty(final String s)
'''
pass
def setProperty():
'''public void setProperty(final String s, final Object o)
'''
pass
def setContentHandler():
'''public void setContentHandler(final ContentHandler fContentHandler)
'''
pass
def getContentHandler():
'''public ContentHandler getContentHandler()
'''
pass
def setErrorHandler():
'''public void setErrorHandler(final ErrorHandler fErrorHandler)
'''
pass
def getErrorHandler():
'''public ErrorHandler getErrorHandler()
'''
pass
def parse():
'''public void parse(final InputSource inputSource)
public void parse(final String systemId)
'''
pass
