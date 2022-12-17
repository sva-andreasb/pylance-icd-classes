def ():
    '''returns XMLStreamWriterWrapper\n\n
    (final XMLStreamWriter parent)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def getNamespaceContext():
    '''returns NamespaceContext\n\n
    getNamespaceContext()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String uri)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def setDefaultNamespace():
    '''returns None\n\n
    setDefaultNamespace(final String uri)\n
    '''
def setNamespaceContext():
    '''returns None\n\n
    setNamespaceContext(final NamespaceContext context)\n
    '''
def setPrefix():
    '''returns None\n\n
    setPrefix(final String prefix, final String uri)\n
    '''
def writeAttribute():
    '''returns None\n\n
    writeAttribute(final String prefix, final String namespaceURI, final String localName, final String value)\n
    writeAttribute(final String namespaceURI, final String localName, final String value)\n
    writeAttribute(final String localName, final String value)\n
    '''
def writeCData():
    '''returns None\n\n
    writeCData(final String data)\n
    '''
def writeCharacters():
    '''returns None\n\n
    writeCharacters(final char[] text, final int start, final int len)\n
    writeCharacters(final String text)\n
    '''
def writeComment():
    '''returns None\n\n
    writeComment(final String data)\n
    '''
def writeDefaultNamespace():
    '''returns None\n\n
    writeDefaultNamespace(final String namespaceURI)\n
    '''
def writeDTD():
    '''returns None\n\n
    writeDTD(final String dtd)\n
    '''
def writeEmptyElement():
    '''returns None\n\n
    writeEmptyElement(final String prefix, final String localName, final String namespaceURI)\n
    writeEmptyElement(final String namespaceURI, final String localName)\n
    writeEmptyElement(final String localName)\n
    '''
def writeEndDocument():
    '''returns None\n\n
    writeEndDocument()\n
    '''
def writeEndElement():
    '''returns None\n\n
    writeEndElement()\n
    '''
def writeEntityRef():
    '''returns None\n\n
    writeEntityRef(final String name)\n
    '''
def writeNamespace():
    '''returns None\n\n
    writeNamespace(final String prefix, final String namespaceURI)\n
    '''
def writeProcessingInstruction():
    '''returns None\n\n
    writeProcessingInstruction(final String target, final String data)\n
    writeProcessingInstruction(final String target)\n
    '''
def writeStartDocument():
    '''returns None\n\n
    writeStartDocument()\n
    writeStartDocument(final String encoding, final String version)\n
    writeStartDocument(final String version)\n
    '''
def writeStartElement():
    '''returns None\n\n
    writeStartElement(final String prefix, final String localName, final String namespaceURI)\n
    writeStartElement(final String namespaceURI, final String localName)\n
    writeStartElement(final String localName)\n
    '''
