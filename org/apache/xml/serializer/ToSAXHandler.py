def ToSAXHandler():
'''public ToSAXHandler()
public ToSAXHandler(final ContentHandler hdlr, final LexicalHandler lex, final String encoding)
public ToSAXHandler(final ContentHandler handler, final String encoding)
'''
pass
def startDTD():
'''public void startDTD(final String arg0, final String arg1, final String arg2)
'''
pass
def characters():
'''public void characters(final String characters)
public void characters(final Node node)
'''
pass
def comment():
'''public void comment(final String comment)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String target, final String data)
'''
pass
def startElement():
'''public void startElement(final String arg0, final String arg1, final String arg2, final Attributes arg3)
public void startElement(final String uri, final String localName, final String qName)
public void startElement(final String qName)
'''
pass
def setLexHandler():
'''public void setLexHandler(final LexicalHandler _lexHandler)
'''
pass
def setContentHandler():
'''public void setContentHandler(final ContentHandler _saxHandler)
'''
pass
def setCdataSectionElements():
'''public void setCdataSectionElements(final Vector URI_and_localNames)
'''
pass
def setShouldOutputNSAttr():
'''public void setShouldOutputNSAttr(final boolean doOutputNSAttr)
'''
pass
def flushPending():
'''public void flushPending()
'''
pass
def setTransformState():
'''public void setTransformState(final TransformStateSetter ts)
'''
pass
def fatalError():
'''public void fatalError(final SAXParseException exc)
'''
pass
def error():
'''public void error(final SAXParseException exc)
'''
pass
def warning():
'''public void warning(final SAXParseException exc)
'''
pass
def reset():
'''public boolean reset()
'''
pass
def addUniqueAttribute():
'''public void addUniqueAttribute(final String qName, final String value, final int flags)
'''
pass
