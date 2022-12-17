def ():
    '''returns SerializationContext\n\n
    (final Writer writer)\n
    (final Writer writer, final MessageContext msgContext)\n
    '''
def getPretty():
    '''returns boolean\n\n
    getPretty()\n
    '''
def setPretty():
    '''returns None\n\n
    setPretty(final boolean pretty)\n
    '''
def getDoMultiRefs():
    '''returns boolean\n\n
    getDoMultiRefs()\n
    '''
def setDoMultiRefs():
    '''returns None\n\n
    setDoMultiRefs(final boolean shouldDo)\n
    '''
def setSendDecl():
    '''returns None\n\n
    setSendDecl(final boolean sendDecl)\n
    '''
def shouldSendXSIType():
    '''returns boolean\n\n
    shouldSendXSIType()\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping()\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getPrefixForURI():
    '''returns String\n\n
    getPrefixForURI(final String uri)\n
    getPrefixForURI(final String uri, final String defaultPrefix)\n
    getPrefixForURI(final String uri, final String defaultPrefix, final boolean attribute)\n
    '''
def registerPrefixForURI():
    '''returns None\n\n
    registerPrefixForURI(final String prefix, final String uri)\n
    '''
def getCurrentMessage():
    '''returns Message\n\n
    getCurrentMessage()\n
    '''
def getMessageContext():
    '''returns MessageContext\n\n
    getMessageContext()\n
    '''
def getEncodingStyle():
    '''returns String\n\n
    getEncodingStyle()\n
    '''
def isEncoded():
    '''returns boolean\n\n
    isEncoded()\n
    '''
def qName2String():
    '''returns String\n\n
    qName2String(final QName qName, final boolean writeNS)\n
    qName2String(final QName qName)\n
    '''
def attributeQName2String():
    '''returns String\n\n
    attributeQName2String(final QName qName)\n
    '''
def getQNameForClass():
    '''returns QName\n\n
    getQNameForClass(final Class cls)\n
    '''
def isPrimitive():
    '''returns boolean\n\n
    isPrimitive(final Object value)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final QName elemQName, final Attributes attributes, final Object value)\n
    serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType)\n
    serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Class javaType)\n
    serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final boolean sendNull, final Boolean sendType)\n
    serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Boolean sendNull, final Boolean sendType)\n
    serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Class javaClass, Boolean sendNull, final Boolean sendType)\n
    '''
def outputMultiRefs():
    '''returns None\n\n
    outputMultiRefs()\n
    '''
def writeXMLDeclaration():
    '''returns None\n\n
    writeXMLDeclaration()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement()\n
    '''
def writeChars():
    '''returns None\n\n
    writeChars(final char[] p1, final int p2, final int p3)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final String string)\n
    '''
def writeSafeString():
    '''returns None\n\n
    writeSafeString(final String string)\n
    '''
def writeDOMElement():
    '''returns None\n\n
    writeDOMElement(final Element el)\n
    '''
def setTypeAttribute():
    '''returns Attributes\n\n
    setTypeAttribute(final Attributes attributes, final QName type)\n
    '''
def getCurrentXMLType():
    '''returns QName\n\n
    getCurrentXMLType()\n
    '''
def getValueAsString():
    '''returns String\n\n
    getValueAsString(final Object value, final QName xmlType, final Class javaClass)\n
    '''
def setWriteXMLType():
    '''returns None\n\n
    setWriteXMLType(final QName type)\n
    '''
def getEncoder():
    '''returns XMLEncoder\n\n
    getEncoder()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    '''
def getItemQName():
    '''returns QName\n\n
    getItemQName()\n
    '''
def setItemQName():
    '''returns None\n\n
    setItemQName(final QName itemQName)\n
    '''
def getItemType():
    '''returns QName\n\n
    getItemType()\n
    '''
def setItemType():
    '''returns None\n\n
    setItemType(final QName itemType)\n
    '''
