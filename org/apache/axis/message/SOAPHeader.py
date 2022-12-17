def ():
    '''returns SOAPHeader\n\n
    (final String namespace, final String localPart, final String prefix, final Attributes attributes, final DeserializationContext context, final SOAPConstants soapConsts)\n
    '''
def setParentElement():
    '''returns None\n\n
    setParentElement(final SOAPElement parent)\n
    '''
def addHeaderElement():
    '''returns SOAPHeaderElement\n\n
    addHeaderElement(final Name name)\n
    '''
def examineHeaderElements():
    '''returns Iterator\n\n
    examineHeaderElements(final String actor)\n
    '''
def extractHeaderElements():
    '''returns Iterator\n\n
    extractHeaderElements(final String actor)\n
    '''
def examineMustUnderstandHeaderElements():
    '''returns Iterator\n\n
    examineMustUnderstandHeaderElements(final String actor)\n
    '''
def examineAllHeaderElements():
    '''returns Iterator\n\n
    examineAllHeaderElements()\n
    '''
def extractAllHeaderElements():
    '''returns Iterator\n\n
    extractAllHeaderElements()\n
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
def appendChild():
    '''returns Node\n\n
    appendChild(final Node newChild)\n
    '''
