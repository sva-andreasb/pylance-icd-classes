def ():
    '''returns EnvelopeBuilder\n\n
    (final String messageType, final SOAPConstants soapConstants)\n
    (final SOAPEnvelope env, final String messageType)\n
    '''
def getEnvelope():
    '''returns SOAPEnvelope\n\n
    getEnvelope()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onEndChild():
    '''returns None\n\n
    onEndChild(final String namespace, final String localName, final DeserializationContext context)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
