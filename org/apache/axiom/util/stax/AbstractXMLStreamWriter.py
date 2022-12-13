def AbstractXMLStreamWriter():
    '''public AbstractXMLStreamWriter()
    '''
def getNamespaceContext():
    '''public final NamespaceContext getNamespaceContext()
    '''
def setNamespaceContext():
    '''public final void setNamespaceContext(final NamespaceContext context)
    '''
def getPrefix():
    '''public final String getPrefix(final String uri)
    '''
def setDefaultNamespace():
    '''public final void setDefaultNamespace(final String uri)
    '''
def setPrefix():
    '''public final void setPrefix(final String prefix, final String uri)
    '''
def writeStartDocument():
    '''public final void writeStartDocument()
    public final void writeStartDocument(final String encoding, final String version)
    public final void writeStartDocument(final String version)
    '''
def writeDTD():
    '''public final void writeDTD(final String dtd)
    '''
def writeEndDocument():
    '''public final void writeEndDocument()
    '''
def writeStartElement():
    '''public final void writeStartElement(final String prefix, final String localName, final String namespaceURI)
    public final void writeStartElement(final String namespaceURI, final String localName)
    public final void writeStartElement(final String localName)
    '''
def writeEndElement():
    '''public final void writeEndElement()
    '''
def writeEmptyElement():
    '''public final void writeEmptyElement(final String prefix, final String localName, final String namespaceURI)
    public final void writeEmptyElement(final String namespaceURI, final String localName)
    public final void writeEmptyElement(final String localName)
    '''
def writeAttribute():
    '''public final void writeAttribute(final String prefix, final String namespaceURI, final String localName, final String value)
    public final void writeAttribute(final String namespaceURI, final String localName, final String value)
    public final void writeAttribute(final String localName, final String value)
    '''
def writeNamespace():
    '''public final void writeNamespace(final String prefix, final String namespaceURI)
    '''
def writeDefaultNamespace():
    '''public final void writeDefaultNamespace(final String namespaceURI)
    '''
def writeCharacters():
    '''public final void writeCharacters(final char[] text, final int start, final int len)
    public final void writeCharacters(final String text)
    '''
def writeCData():
    '''public final void writeCData(final String data)
    '''
def writeComment():
    '''public final void writeComment(final String data)
    '''
def writeEntityRef():
    '''public final void writeEntityRef(final String name)
    '''
def writeProcessingInstruction():
    '''public final void writeProcessingInstruction(final String target, final String data)
    public final void writeProcessingInstruction(final String target)
    '''
