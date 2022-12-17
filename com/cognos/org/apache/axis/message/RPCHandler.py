def ():
    '''returns RPCHandler\n\n
    (final RPCElement rpcElem, final boolean isResponse)\n
    '''
def setOperation():
    '''returns None\n\n
    setOperation(final OperationDesc myOperation)\n
    '''
def setHeaderElement():
    '''returns None\n\n
    setHeaderElement(final boolean value)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
