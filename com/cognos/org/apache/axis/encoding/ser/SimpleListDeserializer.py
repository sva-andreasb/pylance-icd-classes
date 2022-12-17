def ():
    '''returns SimpleListDeserializer\n\n
    (final Class javaType, final QName xmlType)\n
    (final Class javaType, final QName xmlType, final TypeDesc typeDesc)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def setConstructor():
    '''returns None\n\n
    setConstructor(final Constructor c)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] chars, final int start, final int end)\n
    '''
def onEndElement():
    '''returns None\n\n
    onEndElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
def makeValue():
    '''returns Object\n\n
    makeValue(final String source)\n
    '''
def onStartElement():
    '''returns None\n\n
    onStartElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
