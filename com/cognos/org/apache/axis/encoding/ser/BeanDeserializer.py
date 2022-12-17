def ():
    '''returns BeanDeserializer\n\n
    (final Class javaType, final QName xmlType)\n
    (final Class javaType, final QName xmlType, final TypeDesc typeDesc)\n
    (final Class javaType, final QName xmlType, final TypeDesc typeDesc, final Map propertyMap)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def getAnyPropertyDesc():
    '''returns BeanPropertyDescriptor\n\n
    getAnyPropertyDesc()\n
    '''
def onStartElement():
    '''returns None\n\n
    onStartElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] chars, final int start, final int end)\n
    '''
def onEndElement():
    '''returns None\n\n
    onEndElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
