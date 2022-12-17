def ():
    '''returns SOAPFaultBuilder\n\n
    (final SOAPFault element, final DeserializationContext context)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def setFaultClass():
    '''returns None\n\n
    setFaultClass(final Class faultClass)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String name, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onEndChild():
    '''returns None\n\n
    onEndChild(final String namespace, final String localName, final DeserializationContext context)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value, final Object hint)\n
    '''
