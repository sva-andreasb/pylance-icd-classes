def ():
    '''returns MTOMXMLStreamWriter\n\n
    (final XMLStreamWriter xmlWriter)\n
    (final OutputStream outStream, final OMOutputFormat format)\n
    '''
def generateContentID():
    '''returns String\n\n
    generateContentID(final String existingContentID)\n
    '''
def writeStartElement():
    '''returns None\n\n
    writeStartElement(final String string)\n
    writeStartElement(final String string, final String string1)\n
    writeStartElement(final String string, final String string1, final String string2)\n
    '''
def writeEmptyElement():
    '''returns None\n\n
    writeEmptyElement(final String string, final String string1)\n
    writeEmptyElement(final String string, final String string1, final String string2)\n
    writeEmptyElement(final String string)\n
    '''
def writeEndElement():
    '''returns None\n\n
    writeEndElement()\n
    '''
def writeEndDocument():
    '''returns None\n\n
    writeEndDocument()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def writeAttribute():
    '''returns None\n\n
    writeAttribute(final String string, final String string1)\n
    writeAttribute(final String string, final String string1, final String string2, final String string3)\n
    writeAttribute(final String string, final String string1, final String string2)\n
    '''
def writeNamespace():
    '''returns None\n\n
    writeNamespace(final String string, final String string1)\n
    '''
def writeDefaultNamespace():
    '''returns None\n\n
    writeDefaultNamespace(final String string)\n
    '''
def writeComment():
    '''returns None\n\n
    writeComment(final String string)\n
    '''
def writeProcessingInstruction():
    '''returns None\n\n
    writeProcessingInstruction(final String string)\n
    writeProcessingInstruction(final String string, final String string1)\n
    '''
def writeCData():
    '''returns None\n\n
    writeCData(final String string)\n
    '''
def writeDTD():
    '''returns None\n\n
    writeDTD(final String string)\n
    '''
def writeEntityRef():
    '''returns None\n\n
    writeEntityRef(final String string)\n
    '''
def writeStartDocument():
    '''returns None\n\n
    writeStartDocument()\n
    writeStartDocument(final String string)\n
    writeStartDocument(final String string, final String string1)\n
    '''
def writeCharacters():
    '''returns None\n\n
    writeCharacters(final String string)\n
    writeCharacters(final char[] chars, final int i, final int i1)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String string)\n
    '''
def setPrefix():
    '''returns None\n\n
    setPrefix(final String string, final String string1)\n
    '''
def setDefaultNamespace():
    '''returns None\n\n
    setDefaultNamespace(final String string)\n
    '''
def setNamespaceContext():
    '''returns None\n\n
    setNamespaceContext(final NamespaceContext namespaceContext)\n
    '''
def getNamespaceContext():
    '''returns NamespaceContext\n\n
    getNamespaceContext()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String string)\n
    '''
def isOptimized():
    '''returns boolean\n\n
    isOptimized()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def writeOptimized():
    '''returns None\n\n
    writeOptimized(final OMText node)\n
    '''
def isOptimizedThreshold():
    '''returns boolean\n\n
    isOptimizedThreshold(final OMText node)\n
    '''
def setXmlStreamWriter():
    '''returns None\n\n
    setXmlStreamWriter(final XMLStreamWriter xmlWriter)\n
    '''
def getXmlStreamWriter():
    '''returns XMLStreamWriter\n\n
    getXmlStreamWriter()\n
    '''
def getMimeBoundary():
    '''returns String\n\n
    getMimeBoundary()\n
    '''
def getRootContentId():
    '''returns String\n\n
    getRootContentId()\n
    '''
def getNextContentId():
    '''returns String\n\n
    getNextContentId()\n
    '''
def getCharSetEncoding():
    '''returns String\n\n
    getCharSetEncoding()\n
    '''
def setCharSetEncoding():
    '''returns None\n\n
    setCharSetEncoding(final String charSetEncoding)\n
    '''
def getXmlVersion():
    '''returns String\n\n
    getXmlVersion()\n
    '''
def setXmlVersion():
    '''returns None\n\n
    setXmlVersion(final String xmlVersion)\n
    '''
def setSoap11():
    '''returns None\n\n
    setSoap11(final boolean b)\n
    '''
def isIgnoreXMLDeclaration():
    '''returns boolean\n\n
    isIgnoreXMLDeclaration()\n
    '''
def setIgnoreXMLDeclaration():
    '''returns None\n\n
    setIgnoreXMLDeclaration(final boolean ignoreXMLDeclaration)\n
    '''
def setDoOptimize():
    '''returns None\n\n
    setDoOptimize(final boolean b)\n
    '''
def getOutputFormat():
    '''returns OMOutputFormat\n\n
    getOutputFormat()\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final OMOutputFormat format)\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
