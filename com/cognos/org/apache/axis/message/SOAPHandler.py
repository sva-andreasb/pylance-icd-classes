def ():
    '''returns SOAPHandler\n\n
    ()\n
    (final MessageElement[] elements, final int index)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def makeNewElement():
    '''returns MessageElement\n\n
    makeNewElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onEndChild():
    '''returns None\n\n
    onEndChild(final String namespace, final String localName, final DeserializationContext context)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] chars, final int start, final int end)\n
    '''
