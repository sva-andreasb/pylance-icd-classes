def ():
    '''returns DeserializerImpl\n\n
    ()\n
    '''
def getMechanismType():
    '''returns String\n\n
    getMechanismType()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    getValue(final Object hint)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value)\n
    setValue(final Object value, final Object hint)\n
    '''
def setChildValue():
    '''returns None\n\n
    setChildValue(final Object value, final Object hint)\n
    '''
def setDefaultType():
    '''returns None\n\n
    setDefaultType(final QName qName)\n
    '''
def getDefaultType():
    '''returns QName\n\n
    getDefaultType()\n
    '''
def registerValueTarget():
    '''returns None\n\n
    registerValueTarget(final Target target)\n
    '''
def getValueTargets():
    '''returns Vector\n\n
    getValueTargets()\n
    '''
def removeValueTargets():
    '''returns None\n\n
    removeValueTargets()\n
    '''
def moveValueTargets():
    '''returns None\n\n
    moveValueTargets(final Deserializer other)\n
    '''
def componentsReady():
    '''returns boolean\n\n
    componentsReady()\n
    '''
def valueComplete():
    '''returns None\n\n
    valueComplete()\n
    '''
def addChildDeserializer():
    '''returns None\n\n
    addChildDeserializer(final Deserializer dSer)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onStartElement():
    '''returns None\n\n
    onStartElement(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onStartChild():
    '''returns SOAPHandler\n\n
    onStartChild(final String namespace, final String localName, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def onEndElement():
    '''returns None\n\n
    onEndElement(final String namespace, final String localName, final DeserializationContext context)\n
    '''
