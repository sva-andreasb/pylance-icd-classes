def ():
    '''returns XMLStreamWriterTracer\n\n
    ()\n
    (final XMLStreamWriter fStreamWriter, final boolean fRecycleOnEndDocument)\n
    (final XMLStreamWriter xmlStreamWriter, final boolean b)\n
    '''
def createXMLStreamWriter():
    '''returns XMLStreamWriter\n\n
    createXMLStreamWriter(final Writer writer)\n
    createXMLStreamWriter(final OutputStream outputStream)\n
    createXMLStreamWriter(final OutputStream outputStream, final String s)\n
    createXMLStreamWriter(final Result result)\n
    '''
def createXMLEventWriter():
    '''returns XMLEventWriter\n\n
    createXMLEventWriter(final Result result)\n
    createXMLEventWriter(final OutputStream outputStream)\n
    createXMLEventWriter(final OutputStream outputStream, final String s)\n
    createXMLEventWriter(final Writer writer)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    '''
def isPropertySupported():
    '''returns boolean\n\n
    isPropertySupported(final String s)\n
    '''
def writeStartElement():
    '''returns None\n\n
    writeStartElement(final String s)\n
    writeStartElement(final String s, final String s2)\n
    writeStartElement(final String s, final String s2, final String s3)\n
    writeStartElement(final String s)\n
    writeStartElement(final String s, final String s2)\n
    writeStartElement(final String s, final String s2, final String s3)\n
    writeStartElement(final String s)\n
    writeStartElement(final String s, final String s2)\n
    writeStartElement(final String s, final String s2, final String s3)\n
    writeStartElement(final String s)\n
    writeStartElement(final String s, final String s2)\n
    writeStartElement(final String s, final String s2, final String s3)\n
    '''
def writeEmptyElement():
    '''returns None\n\n
    writeEmptyElement(final String s, final String s2)\n
    writeEmptyElement(final String s, final String s2, final String s3)\n
    writeEmptyElement(final String s)\n
    writeEmptyElement(final String s, final String s2)\n
    writeEmptyElement(final String s, final String s2, final String s3)\n
    writeEmptyElement(final String s)\n
    writeEmptyElement(final String s, final String s2)\n
    writeEmptyElement(final String s, final String s2, final String s3)\n
    writeEmptyElement(final String s)\n
    writeEmptyElement(final String s, final String s2)\n
    writeEmptyElement(final String s, final String s2, final String s3)\n
    writeEmptyElement(final String s)\n
    '''
def writeEndElement():
    '''returns None\n\n
    writeEndElement()\n
    writeEndElement()\n
    writeEndElement()\n
    writeEndElement()\n
    '''
def writeEndDocument():
    '''returns None\n\n
    writeEndDocument()\n
    writeEndDocument()\n
    writeEndDocument()\n
    writeEndDocument()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    close()\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    flush()\n
    flush()\n
    flush()\n
    '''
def writeAttribute():
    '''returns None\n\n
    writeAttribute(final String s, final String s2)\n
    writeAttribute(final String s, final String s2, final String s3, final String s4)\n
    writeAttribute(final String s, final String s2, final String s3)\n
    writeAttribute(final String s, final String s2)\n
    writeAttribute(final String s, final String s2, final String s3, final String s4)\n
    writeAttribute(final String s, final String s2, final String s3)\n
    writeAttribute(final String s, final String s2)\n
    writeAttribute(final String s, final String s2, final String s3, final String s4)\n
    writeAttribute(final String s, final String s2, final String s3)\n
    writeAttribute(final String s, final String s2)\n
    writeAttribute(final String s, final String s2, final String s3, final String s4)\n
    writeAttribute(final String s, final String s2, final String s3)\n
    '''
def writeNamespace():
    '''returns None\n\n
    writeNamespace(final String s, final String s2)\n
    writeNamespace(final String s, final String s2)\n
    writeNamespace(final String s, final String s2)\n
    writeNamespace(final String s, final String s2)\n
    '''
def writeDefaultNamespace():
    '''returns None\n\n
    writeDefaultNamespace(final String s)\n
    writeDefaultNamespace(final String s)\n
    writeDefaultNamespace(final String s)\n
    writeDefaultNamespace(final String s)\n
    '''
def writeComment():
    '''returns None\n\n
    writeComment(final String s)\n
    writeComment(final String s)\n
    writeComment(final String s)\n
    writeComment(final String s)\n
    '''
def writeProcessingInstruction():
    '''returns None\n\n
    writeProcessingInstruction(final String s)\n
    writeProcessingInstruction(final String s, final String s2)\n
    writeProcessingInstruction(final String s)\n
    writeProcessingInstruction(final String s, final String s2)\n
    writeProcessingInstruction(final String s)\n
    writeProcessingInstruction(final String s, final String s2)\n
    writeProcessingInstruction(final String s)\n
    writeProcessingInstruction(final String s, final String s2)\n
    '''
def writeCData():
    '''returns None\n\n
    writeCData(final String s)\n
    writeCData(final String s)\n
    writeCData(final String s)\n
    writeCData(final String s)\n
    '''
def writeDTD():
    '''returns None\n\n
    writeDTD(final String s)\n
    writeDTD(final String s)\n
    writeDTD(final String s)\n
    writeDTD(final String s)\n
    '''
def writeEntityRef():
    '''returns None\n\n
    writeEntityRef(final String s)\n
    writeEntityRef(final String s)\n
    writeEntityRef(final String s)\n
    writeEntityRef(final String s)\n
    '''
def writeStartDocument():
    '''returns None\n\n
    writeStartDocument()\n
    writeStartDocument(final String s)\n
    writeStartDocument(final String s, final String s2)\n
    writeStartDocument()\n
    writeStartDocument(final String s)\n
    writeStartDocument(final String s, final String s2)\n
    writeStartDocument()\n
    writeStartDocument(final String s)\n
    writeStartDocument(final String s, final String s2)\n
    writeStartDocument()\n
    writeStartDocument(final String s)\n
    writeStartDocument(final String s, final String s2)\n
    '''
def writeCharacters():
    '''returns None\n\n
    writeCharacters(final String s)\n
    writeCharacters(final char[] array, final int n, final int n2)\n
    writeCharacters(final String s)\n
    writeCharacters(final char[] array, final int n, final int n2)\n
    writeCharacters(final String s)\n
    writeCharacters(final char[] array, final int n, final int n2)\n
    writeCharacters(final String s)\n
    writeCharacters(final char[] array, final int value, final int value2)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String s)\n
    getPrefix(final String s)\n
    getPrefix(final String s)\n
    getPrefix(final String s)\n
    '''
def setPrefix():
    '''returns None\n\n
    setPrefix(final String s, final String s2)\n
    setPrefix(final String s, final String s2)\n
    setPrefix(final String s, final String s2)\n
    setPrefix(final String s, final String s2)\n
    '''
def setDefaultNamespace():
    '''returns None\n\n
    setDefaultNamespace(final String defaultNamespace)\n
    setDefaultNamespace(final String s)\n
    setDefaultNamespace(final String s)\n
    setDefaultNamespace(final String defaultNamespace)\n
    '''
def setNamespaceContext():
    '''returns None\n\n
    setNamespaceContext(final NamespaceContext namespaceContext)\n
    setNamespaceContext(final NamespaceContext namespaceContext)\n
    setNamespaceContext(final NamespaceContext namespaceContext)\n
    setNamespaceContext(final NamespaceContext namespaceContext)\n
    '''
def getNamespaceContext():
    '''returns NamespaceContext\n\n
    getNamespaceContext()\n
    getNamespaceContext()\n
    getNamespaceContext()\n
    getNamespaceContext()\n
    '''
def writeStAXProfile():
    '''returns None\n\n
    writeStAXProfile(final String s)\n
    '''
def writeReadableProfile():
    '''returns None\n\n
    writeReadableProfile(final String s)\n
    '''
