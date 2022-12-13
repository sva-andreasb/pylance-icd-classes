def ToStream():
'''public ToStream()
'''
pass
def serialize():
'''public void serialize(final Node node)
'''
pass
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def elementDecl():
'''public void elementDecl(final String name, final String model)
'''
pass
def internalEntityDecl():
'''public void internalEntityDecl(final String name, final String value)
'''
pass
def setOutputFormat():
'''public void setOutputFormat(final Properties format)
'''
pass
def getOutputFormat():
'''public Properties getOutputFormat()
'''
pass
def setWriter():
'''public void setWriter(final Writer writer)
'''
pass
def setLineSepUse():
'''public boolean setLineSepUse(final boolean use_sytem_line_break)
'''
pass
def setOutputStream():
'''public void setOutputStream(final OutputStream output)
'''
pass
def setEscaping():
'''public boolean setEscaping(final boolean escape)
'''
pass
def attributeDecl():
'''public void attributeDecl(final String eName, final String aName, final String type, final String valueDefault, final String value)
'''
pass
def getWriter():
'''public Writer getWriter()
'''
pass
def externalEntityDecl():
'''public void externalEntityDecl(final String name, final String publicId, final String systemId)
'''
pass
def endNonEscaping():
'''public void endNonEscaping()
'''
pass
def startNonEscaping():
'''public void startNonEscaping()
'''
pass
def characters():
'''public void characters(final char[] chars, final int start, final int length)
public void characters(final String s)
'''
pass
def startElement():
'''public void startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)
public void startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)
public void startElement(final String elementName)
'''
pass
def processAttributes():
'''public void processAttributes(final Writer writer, final int nAttrs)
'''
pass
def writeAttrString():
'''public void writeAttrString(final Writer writer, final String string, final String encoding)
'''
pass
def endElement():
'''public void endElement(final String namespaceURI, final String localName, final String name)
public void endElement(final String name)
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String prefix, final String uri)
public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
'''
pass
def comment():
'''public void comment(final char[] ch, int start, final int length)
'''
pass
def endCDATA():
'''public void endCDATA()
'''
pass
def endDTD():
'''public void endDTD()
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String prefix)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] ch, final int start, final int length)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String name)
'''
pass
def startCDATA():
'''public void startCDATA()
'''
pass
def startEntity():
'''public void startEntity(final String name)
'''
pass
def startDTD():
'''public void startDTD(final String name, final String publicId, final String systemId)
'''
pass
def getIndentAmount():
'''public int getIndentAmount()
'''
pass
def setIndentAmount():
'''public void setIndentAmount(final int m_indentAmount)
'''
pass
def setCdataSectionElements():
'''public void setCdataSectionElements(final Vector URI_and_localNames)
'''
pass
def flushPending():
'''public void flushPending()
'''
pass
def setContentHandler():
'''public void setContentHandler(final ContentHandler ch)
'''
pass
def addAttributeAlways():
'''public boolean addAttributeAlways(final String uri, final String localName, String rawName, final String type, final String value, final boolean xslAttribute)
'''
pass
def setTransformer():
'''public void setTransformer(final Transformer transformer)
'''
pass
def reset():
'''public boolean reset()
'''
pass
def setEncoding():
'''public void setEncoding(final String encoding)
'''
pass
def notationDecl():
'''public void notationDecl(final String name, final String pubID, final String sysID)
'''
pass
def unparsedEntityDecl():
'''public void unparsedEntityDecl(final String name, final String pubID, final String sysID, final String notationName)
'''
pass
def setDTDEntityExpansion():
'''public void setDTDEntityExpansion(final boolean expand)
'''
pass
def setNewLine():
'''public void setNewLine(final char[] eolChars)
'''
pass
def addCdataSectionElements():
'''public void addCdataSectionElements(final String URI_and_localNames)
'''
pass
def write():
'''public void write(final char[] arg0, final int arg1, final int arg2)
public void write(final int i)
public void write(final String s)
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
def BoolStack():
'''public BoolStack()
public BoolStack(final int size)
'''
pass
def size():
'''public final int size()
'''
pass
def clear():
'''public final void clear()
'''
pass
def push():
'''public final boolean push(final boolean val)
'''
pass
def pop():
'''public final boolean pop()
'''
pass
def popAndTop():
'''public final boolean popAndTop()
'''
pass
def setTop():
'''public final void setTop(final boolean b)
'''
pass
def peek():
'''public final boolean peek()
'''
pass
def peekOrFalse():
'''public final boolean peekOrFalse()
'''
pass
def peekOrTrue():
'''public final boolean peekOrTrue()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
