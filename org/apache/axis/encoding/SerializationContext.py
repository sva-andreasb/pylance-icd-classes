def SerializationContext():
    '''public SerializationContext(final Writer writer)
    public SerializationContext(final Writer writer, final MessageContext msgContext)
    '''
def getPretty():
    '''public boolean getPretty()
    '''
def setPretty():
    '''public void setPretty(final boolean pretty)
    '''
def getDoMultiRefs():
    '''public boolean getDoMultiRefs()
    '''
def setDoMultiRefs():
    '''public void setDoMultiRefs(final boolean shouldDo)
    '''
def setSendDecl():
    '''public void setSendDecl(final boolean sendDecl)
    '''
def shouldSendXSIType():
    '''public boolean shouldSendXSIType()
    '''
def getTypeMapping():
    '''public TypeMapping getTypeMapping()
    '''
def getTypeMappingRegistry():
    '''public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getPrefixForURI():
    '''public String getPrefixForURI(final String uri)
    public String getPrefixForURI(final String uri, final String defaultPrefix)
    public String getPrefixForURI(final String uri, final String defaultPrefix, final boolean attribute)
    '''
def registerPrefixForURI():
    '''public void registerPrefixForURI(final String prefix, final String uri)
    '''
def getCurrentMessage():
    '''public Message getCurrentMessage()
    '''
def getMessageContext():
    '''public MessageContext getMessageContext()
    '''
def getEncodingStyle():
    '''public String getEncodingStyle()
    '''
def isEncoded():
    '''public boolean isEncoded()
    '''
def qName2String():
    '''public String qName2String(final QName qName, final boolean writeNS)
    public String qName2String(final QName qName)
    '''
def attributeQName2String():
    '''public String attributeQName2String(final QName qName)
    '''
def getQNameForClass():
    '''public QName getQNameForClass(final Class cls)
    '''
def isPrimitive():
    '''public boolean isPrimitive(final Object value)
    '''
def serialize():
    '''public void serialize(final QName elemQName, final Attributes attributes, final Object value)
    public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType)
    public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Class javaType)
    public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final boolean sendNull, final Boolean sendType)
    public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Boolean sendNull, final Boolean sendType)
    public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Class javaClass, Boolean sendNull, final Boolean sendType)
    '''
def outputMultiRefs():
    '''public void outputMultiRefs()
    '''
def writeXMLDeclaration():
    '''public void writeXMLDeclaration()
    '''
def startElement():
    '''public void startElement(final QName qName, Attributes attributes)
    '''
def endElement():
    '''public void endElement()
    '''
def writeChars():
    '''public void writeChars(final char[] p1, final int p2, final int p3)
    '''
def writeString():
    '''public void writeString(final String string)
    '''
def writeSafeString():
    '''public void writeSafeString(final String string)
    '''
def writeDOMElement():
    '''public void writeDOMElement(final Element el)
    '''
def getSerializerForJavaType():
    '''public final Serializer getSerializerForJavaType(final Class javaType)
    '''
def setTypeAttribute():
    '''public Attributes setTypeAttribute(final Attributes attributes, final QName type)
    '''
def getCurrentXMLType():
    '''public QName getCurrentXMLType()
    '''
def getValueAsString():
    '''public String getValueAsString(final Object value, final QName xmlType, final Class javaClass)
    '''
def setWriteXMLType():
    '''public void setWriteXMLType(final QName type)
    '''
def getEncoder():
    '''public XMLEncoder getEncoder()
    '''
def getEncoding():
    '''public String getEncoding()
    '''
def setEncoding():
    '''public void setEncoding(final String encoding)
    '''
def getItemQName():
    '''public QName getItemQName()
    '''
def setItemQName():
    '''public void setItemQName(final QName itemQName)
    '''
def getItemType():
    '''public QName getItemType()
    '''
def setItemType():
    '''public void setItemType(final QName itemType)
    '''
