def ():
    '''returns SOAPBody\n\n
    (final String namespace, final String localPart, final String prefix, final Attributes attributes, final DeserializationContext context, final SOAPConstants soapConsts)\n
    '''
def setParentElement():
    '''returns None\n\n
    setParentElement(final SOAPElement parent)\n
    '''
def disableFormatting():
    '''returns None\n\n
    disableFormatting()\n
    '''
def setEncodingStyle():
    '''returns None\n\n
    setEncodingStyle(String encodingStyle)\n
    '''
def addFault():
    '''returns SOAPFault\n\n
    addFault(final Name name, final String s, final Locale locale)\n
    addFault(final Name name, final String s)\n
    addFault()\n
    '''
def getFault():
    '''returns SOAPFault\n\n
    getFault()\n
    '''
def hasFault():
    '''returns boolean\n\n
    hasFault()\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final MessageElement element)\n
    '''
def addChildElement():
    '''returns SOAPElement\n\n
    addChildElement(final SOAPElement element)\n
    addChildElement(final Name name)\n
    addChildElement(final String localName)\n
    addChildElement(final String localName, final String prefix)\n
    addChildElement(final String localName, final String prefix, final String uri)\n
    '''
def setSAAJEncodingCompliance():
    '''returns None\n\n
    setSAAJEncodingCompliance(final boolean comply)\n
    '''
