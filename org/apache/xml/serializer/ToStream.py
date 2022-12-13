def ToStream():
    '''public ToStream()
    '''
def serialize():
    '''public void serialize(final Node node)
    '''
def getOutputStream():
    '''public OutputStream getOutputStream()
    '''
def elementDecl():
    '''public void elementDecl(final String name, final String model)
    '''
def internalEntityDecl():
    '''public void internalEntityDecl(final String name, final String value)
    '''
def setOutputFormat():
    '''public void setOutputFormat(final Properties format)
    '''
def getOutputFormat():
    '''public Properties getOutputFormat()
    '''
def setWriter():
    '''public void setWriter(final Writer writer)
    '''
def setLineSepUse():
    '''public boolean setLineSepUse(final boolean use_sytem_line_break)
    '''
def setOutputStream():
    '''public void setOutputStream(final OutputStream output)
    '''
def setEscaping():
    '''public boolean setEscaping(final boolean escape)
    '''
def attributeDecl():
    '''public void attributeDecl(final String eName, final String aName, final String type, final String valueDefault, final String value)
    '''
def getWriter():
    '''public Writer getWriter()
    '''
def externalEntityDecl():
    '''public void externalEntityDecl(final String name, final String publicId, final String systemId)
    '''
def endNonEscaping():
    '''public void endNonEscaping()
    '''
def startNonEscaping():
    '''public void startNonEscaping()
    '''
def characters():
    '''public void characters(final char[] chars, final int start, final int length)
    public void characters(final String s)
    '''
def startElement():
    '''public void startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)
    public void startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)
    public void startElement(final String elementName)
    '''
def processAttributes():
    '''public void processAttributes(final Writer writer, final int nAttrs)
    '''
def writeAttrString():
    '''public void writeAttrString(final Writer writer, final String string, final String encoding)
    '''
def endElement():
    '''public void endElement(final String namespaceURI, final String localName, final String name)
    public void endElement(final String name)
    '''
def startPrefixMapping():
    '''public void startPrefixMapping(final String prefix, final String uri)
    public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
    '''
def comment():
    '''public void comment(final char[] ch, int start, final int length)
    '''
def endCDATA():
    '''public void endCDATA()
    '''
def endDTD():
    '''public void endDTD()
    '''
def endPrefixMapping():
    '''public void endPrefixMapping(final String prefix)
    '''
def ignorableWhitespace():
    '''public void ignorableWhitespace(final char[] ch, final int start, final int length)
    '''
def skippedEntity():
    '''public void skippedEntity(final String name)
    '''
def startCDATA():
    '''public void startCDATA()
    '''
def startEntity():
    '''public void startEntity(final String name)
    '''
def startDTD():
    '''public void startDTD(final String name, final String publicId, final String systemId)
    '''
def getIndentAmount():
    '''public int getIndentAmount()
    '''
def setIndentAmount():
    '''public void setIndentAmount(final int m_indentAmount)
    '''
def setCdataSectionElements():
    '''public void setCdataSectionElements(final Vector URI_and_localNames)
    '''
def flushPending():
    '''public void flushPending()
    '''
def setContentHandler():
    '''public void setContentHandler(final ContentHandler ch)
    '''
def addAttributeAlways():
    '''public boolean addAttributeAlways(final String uri, final String localName, String rawName, final String type, final String value, final boolean xslAttribute)
    '''
def setTransformer():
    '''public void setTransformer(final Transformer transformer)
    '''
def reset():
    '''public boolean reset()
    '''
def setEncoding():
    '''public void setEncoding(final String encoding)
    '''
def notationDecl():
    '''public void notationDecl(final String name, final String pubID, final String sysID)
    '''
def unparsedEntityDecl():
    '''public void unparsedEntityDecl(final String name, final String pubID, final String sysID, final String notationName)
    '''
def setDTDEntityExpansion():
    '''public void setDTDEntityExpansion(final boolean expand)
    '''
def setNewLine():
    '''public void setNewLine(final char[] eolChars)
    '''
def addCdataSectionElements():
    '''public void addCdataSectionElements(final String URI_and_localNames)
    '''
def write():
    '''public void write(final char[] arg0, final int arg1, final int arg2)
    public void write(final int i)
    public void write(final String s)
    '''
def flush():
    '''public void flush()
    '''
def close():
    '''public void close()
    '''
def BoolStack():
    '''public BoolStack()
    public BoolStack(final int size)
    '''
def size():
    '''public final int size()
    '''
def clear():
    '''public final void clear()
    '''
def push():
    '''public final boolean push(final boolean val)
    '''
def pop():
    '''public final boolean pop()
    '''
def popAndTop():
    '''public final boolean popAndTop()
    '''
def setTop():
    '''public final void setTop(final boolean b)
    '''
def peek():
    '''public final boolean peek()
    '''
def peekOrFalse():
    '''public final boolean peekOrFalse()
    '''
def peekOrTrue():
    '''public final boolean peekOrTrue()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
