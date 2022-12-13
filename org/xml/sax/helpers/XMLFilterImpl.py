def XMLFilterImpl():
'''public XMLFilterImpl()
public XMLFilterImpl(final XMLReader parent)
'''
pass
def setParent():
'''public void setParent(final XMLReader parent)
'''
pass
def getParent():
'''public XMLReader getParent()
'''
pass
def setFeature():
'''public void setFeature(final String str, final boolean b)
'''
pass
def getFeature():
'''public boolean getFeature(final String str)
'''
pass
def setProperty():
'''public void setProperty(final String str, final Object o)
'''
pass
def getProperty():
'''public Object getProperty(final String str)
'''
pass
def setEntityResolver():
'''public void setEntityResolver(final EntityResolver entityResolver)
'''
pass
def getEntityResolver():
'''public EntityResolver getEntityResolver()
'''
pass
def setDTDHandler():
'''public void setDTDHandler(final DTDHandler dtdHandler)
'''
pass
def getDTDHandler():
'''public DTDHandler getDTDHandler()
'''
pass
def setContentHandler():
'''public void setContentHandler(final ContentHandler contentHandler)
'''
pass
def getContentHandler():
'''public ContentHandler getContentHandler()
'''
pass
def setErrorHandler():
'''public void setErrorHandler(final ErrorHandler errorHandler)
'''
pass
def getErrorHandler():
'''public ErrorHandler getErrorHandler()
'''
pass
def parse():
'''public void parse(final InputSource inputSource)
public void parse(final String s)
'''
pass
def resolveEntity():
'''public InputSource resolveEntity(final String s, final String s2)
'''
pass
def notationDecl():
'''public void notationDecl(final String s, final String s2, final String s3)
'''
pass
def unparsedEntityDecl():
'''public void unparsedEntityDecl(final String s, final String s2, final String s3, final String s4)
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final Locator locator)
'''
pass
def startDocument():
'''public void startDocument()
'''
pass
def endDocument():
'''public void endDocument()
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String s, final String s2)
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String s)
'''
pass
def startElement():
'''public void startElement(final String s, final String s2, final String s3, final Attributes attributes)
'''
pass
def endElement():
'''public void endElement(final String s, final String s2, final String s3)
'''
pass
def characters():
'''public void characters(final char[] array, final int n, final int n2)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] array, final int n, final int n2)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String s, final String s2)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String s)
'''
pass
def warning():
'''public void warning(final SAXParseException ex)
'''
pass
def error():
'''public void error(final SAXParseException ex)
'''
pass
def fatalError():
'''public void fatalError(final SAXParseException ex)
'''
pass
