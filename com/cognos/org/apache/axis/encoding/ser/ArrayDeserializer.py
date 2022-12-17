def ():
    '''returns ArrayDeserializer\n\n
    ()\n
    '''
def onStartElement():
    '''returns None\n\n
    onStartElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
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
    characters(final char[] chars, int i, final int i1)\n
    '''
def setChildValue():
    '''returns None\n\n
    setChildValue(final Object value, final Object hint)\n
    '''
def valueComplete():
    '''returns None\n\n
    valueComplete()\n
    '''
def setConvertedValue():
    '''returns None\n\n
    setConvertedValue(final Class cls, final Object value)\n
    '''
def getConvertedValue():
    '''returns Object\n\n
    getConvertedValue(final Class cls)\n
    '''
def getDestClass():
    '''returns Class\n\n
    getDestClass()\n
    '''
