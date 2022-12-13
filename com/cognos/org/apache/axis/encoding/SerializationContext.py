def SerializationContext():
'''public SerializationContext(final Writer writer)
public SerializationContext(final Writer writer, final MessageContext msgContext)
'''
pass
def getPretty():
'''public boolean getPretty()
'''
pass
def setPretty():
'''public void setPretty(final boolean pretty)
'''
pass
def getDoMultiRefs():
'''public boolean getDoMultiRefs()
'''
pass
def setDoMultiRefs():
'''public void setDoMultiRefs(final boolean shouldDo)
'''
pass
def setSendDecl():
'''public void setSendDecl(final boolean sendDecl)
'''
pass
def shouldSendXSIType():
'''public boolean shouldSendXSIType()
'''
pass
def getTypeMapping():
'''public TypeMapping getTypeMapping()
'''
pass
def getTypeMappingRegistry():
'''public TypeMappingRegistry getTypeMappingRegistry()
'''
pass
def getPrefixForURI():
'''public String getPrefixForURI(final String uri)
public String getPrefixForURI(final String uri, final String defaultPrefix)
public String getPrefixForURI(final String uri, final String defaultPrefix, final boolean attribute)
'''
pass
def registerPrefixForURI():
'''public void registerPrefixForURI(final String prefix, final String uri)
'''
pass
def getCurrentMessage():
'''public Message getCurrentMessage()
'''
pass
def getMessageContext():
'''public MessageContext getMessageContext()
'''
pass
def getEncodingStyle():
'''public String getEncodingStyle()
'''
pass
def isEncoded():
'''public boolean isEncoded()
'''
pass
def qName2String():
'''public String qName2String(final QName qName, final boolean writeNS)
public String qName2String(final QName qName)
'''
pass
def attributeQName2String():
'''public String attributeQName2String(final QName qName)
'''
pass
def getQNameForClass():
'''public QName getQNameForClass(final Class cls)
'''
pass
def isPrimitive():
'''public boolean isPrimitive(final Object value)
'''
pass
def serialize():
'''public void serialize(final QName elemQName, final Attributes attributes, final Object value)
public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType)
public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Class javaType)
public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final boolean sendNull, final Boolean sendType)
public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Boolean sendNull, final Boolean sendType)
public void serialize(final QName elemQName, final Attributes attributes, final Object value, final QName xmlType, final Class javaClass, Boolean sendNull, final Boolean sendType)
'''
pass
def outputMultiRefs():
'''public void outputMultiRefs()
'''
pass
def writeXMLDeclaration():
'''public void writeXMLDeclaration()
'''
pass
def startElement():
'''public void startElement(final QName qName, Attributes attributes)
'''
pass
def endElement():
'''public void endElement()
'''
pass
def writeChars():
'''public void writeChars(final char[] p1, final int p2, final int p3)
'''
pass
def writeString():
'''public void writeString(final String string)
'''
pass
def writeSafeString():
'''public void writeSafeString(final String string)
'''
pass
def writeDOMElement():
'''public void writeDOMElement(final Element el)
'''
pass
def getSerializerForJavaType():
'''public final Serializer getSerializerForJavaType(final Class javaType)
'''
pass
def setTypeAttribute():
'''public Attributes setTypeAttribute(final Attributes attributes, final QName type)
'''
pass
def getCurrentXMLType():
'''public QName getCurrentXMLType()
'''
pass
def getValueAsString():
'''public String getValueAsString(final Object value, final QName xmlType, final Class javaClass)
'''
pass
def setWriteXMLType():
'''public void setWriteXMLType(final QName type)
'''
pass
def getEncoder():
'''public XMLEncoder getEncoder()
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def setEncoding():
'''public void setEncoding(final String encoding)
'''
pass
def getItemQName():
'''public QName getItemQName()
'''
pass
def setItemQName():
'''public void setItemQName(final QName itemQName)
'''
pass
def getItemType():
'''public QName getItemType()
'''
pass
def setItemType():
'''public void setItemType(final QName itemType)
'''
pass
