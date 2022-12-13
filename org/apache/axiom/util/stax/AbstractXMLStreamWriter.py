def AbstractXMLStreamWriter():
'''public AbstractXMLStreamWriter()
'''
pass
def getNamespaceContext():
'''public final NamespaceContext getNamespaceContext()
'''
pass
def setNamespaceContext():
'''public final void setNamespaceContext(final NamespaceContext context)
'''
pass
def getPrefix():
'''public final String getPrefix(final String uri)
'''
pass
def setDefaultNamespace():
'''public final void setDefaultNamespace(final String uri)
'''
pass
def setPrefix():
'''public final void setPrefix(final String prefix, final String uri)
'''
pass
def writeStartDocument():
'''public final void writeStartDocument()
public final void writeStartDocument(final String encoding, final String version)
public final void writeStartDocument(final String version)
'''
pass
def writeDTD():
'''public final void writeDTD(final String dtd)
'''
pass
def writeEndDocument():
'''public final void writeEndDocument()
'''
pass
def writeStartElement():
'''public final void writeStartElement(final String prefix, final String localName, final String namespaceURI)
public final void writeStartElement(final String namespaceURI, final String localName)
public final void writeStartElement(final String localName)
'''
pass
def writeEndElement():
'''public final void writeEndElement()
'''
pass
def writeEmptyElement():
'''public final void writeEmptyElement(final String prefix, final String localName, final String namespaceURI)
public final void writeEmptyElement(final String namespaceURI, final String localName)
public final void writeEmptyElement(final String localName)
'''
pass
def writeAttribute():
'''public final void writeAttribute(final String prefix, final String namespaceURI, final String localName, final String value)
public final void writeAttribute(final String namespaceURI, final String localName, final String value)
public final void writeAttribute(final String localName, final String value)
'''
pass
def writeNamespace():
'''public final void writeNamespace(final String prefix, final String namespaceURI)
'''
pass
def writeDefaultNamespace():
'''public final void writeDefaultNamespace(final String namespaceURI)
'''
pass
def writeCharacters():
'''public final void writeCharacters(final char[] text, final int start, final int len)
public final void writeCharacters(final String text)
'''
pass
def writeCData():
'''public final void writeCData(final String data)
'''
pass
def writeComment():
'''public final void writeComment(final String data)
'''
pass
def writeEntityRef():
'''public final void writeEntityRef(final String name)
'''
pass
def writeProcessingInstruction():
'''public final void writeProcessingInstruction(final String target, final String data)
public final void writeProcessingInstruction(final String target)
'''
pass
