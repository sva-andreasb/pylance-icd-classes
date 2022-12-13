def schemaType():
    '''    public SchemaType schemaType()
    '''
def validate():
    '''    public boolean validate()
    public boolean validate(final XmlOptions options)
    '''
def selectPath():
    '''    public XmlObject[] selectPath(final String path)
    public XmlObject[] selectPath(final String path, final XmlOptions options)
    '''
def execQuery():
    '''    public XmlObject[] execQuery(final String query)
    public XmlObject[] execQuery(final String query, final XmlOptions options)
    '''
def changeType():
    '''    public XmlObject changeType(final SchemaType newType)
    '''
def isNil():
    '''    public boolean isNil()
    '''
def setNil():
    '''    public void setNil()
    '''
def isImmutable():
    '''    public boolean isImmutable()
    '''
def set():
    '''    public XmlObject set(final XmlObject srcObj)
    public void set(final String obj)
    public void set(final boolean v)
    public void set(final byte v)
    public void set(final short v)
    public void set(final int v)
    public void set(final long v)
    public void set(final BigInteger obj)
    public void set(final BigDecimal obj)
    public void set(final float v)
    public void set(final double v)
    public void set(final byte[] obj)
    public void set(final StringEnumAbstractBase obj)
    public void set(final Calendar obj)
    public void set(final Date obj)
    public void set(final GDateSpecification obj)
    public void set(final GDurationSpecification obj)
    public void set(final QName obj)
    public void set(final List obj)
    '''
def copy():
    '''    public XmlObject copy()
    public XmlObject copy(final XmlOptions options)
    '''
def valueEquals():
    '''    public boolean valueEquals(final XmlObject obj)
    '''
def valueHashCode():
    '''    public int valueHashCode()
    '''
def compareTo():
    '''    public int compareTo(final Object obj)
    '''
def compareValue():
    '''    public int compareValue(final XmlObject obj)
    '''
def monitor():
    '''    public Object monitor()
    '''
def documentProperties():
    '''    public XmlDocumentProperties documentProperties()
    '''
def newCursor():
    '''    public XmlCursor newCursor()
    '''
def newXMLInputStream():
    '''    public XMLInputStream newXMLInputStream()
    public XMLInputStream newXMLInputStream(final XmlOptions options)
    '''
def newXMLStreamReader():
    '''    public XMLStreamReader newXMLStreamReader()
    public XMLStreamReader newXMLStreamReader(final XmlOptions options)
    '''
def xmlText():
    '''    public String xmlText()
    public String xmlText(final XmlOptions options)
    '''
def newInputStream():
    '''    public InputStream newInputStream()
    public InputStream newInputStream(final XmlOptions options)
    '''
def newReader():
    '''    public Reader newReader()
    public Reader newReader(final XmlOptions options)
    '''
def newDomNode():
    '''    public Node newDomNode()
    public Node newDomNode(final XmlOptions options)
    '''
def getDomNode():
    '''    public Node getDomNode()
    '''
def save():
    '''    public void save(final ContentHandler ch, final LexicalHandler lh)
    public void save(final File file)
    public void save(final OutputStream os)
    public void save(final Writer w)
    public void save(final ContentHandler ch, final LexicalHandler lh, final XmlOptions options)
    public void save(final File file, final XmlOptions options)
    public void save(final OutputStream os, final XmlOptions options)
    public void save(final Writer w, final XmlOptions options)
    '''
def instanceType():
    '''    public SchemaType instanceType()
    '''
def stringValue():
    '''    public String stringValue()
    '''
def booleanValue():
    '''    public boolean booleanValue()
    '''
def byteValue():
    '''    public byte byteValue()
    '''
def shortValue():
    '''    public short shortValue()
    '''
def intValue():
    '''    public int intValue()
    '''
def longValue():
    '''    public long longValue()
    '''
def bigIntegerValue():
    '''    public BigInteger bigIntegerValue()
    '''
def bigDecimalValue():
    '''    public BigDecimal bigDecimalValue()
    '''
def floatValue():
    '''    public float floatValue()
    '''
def doubleValue():
    '''    public double doubleValue()
    '''
def byteArrayValue():
    '''    public byte[] byteArrayValue()
    '''
def enumValue():
    '''    public StringEnumAbstractBase enumValue()
    '''
def calendarValue():
    '''    public Calendar calendarValue()
    '''
def dateValue():
    '''    public Date dateValue()
    '''
def gDateValue():
    '''    public GDate gDateValue()
    '''
def gDurationValue():
    '''    public GDuration gDurationValue()
    '''
def qNameValue():
    '''    public QName qNameValue()
    '''
def listValue():
    '''    public List listValue()
    '''
def xlistValue():
    '''    public List xlistValue()
    '''
def objectValue():
    '''    public Object objectValue()
    '''
def getStringValue():
    '''    public String getStringValue()
    '''
def getBooleanValue():
    '''    public boolean getBooleanValue()
    '''
def getByteValue():
    '''    public byte getByteValue()
    '''
def getShortValue():
    '''    public short getShortValue()
    '''
def getIntValue():
    '''    public int getIntValue()
    '''
def getLongValue():
    '''    public long getLongValue()
    '''
def getBigIntegerValue():
    '''    public BigInteger getBigIntegerValue()
    '''
def getBigDecimalValue():
    '''    public BigDecimal getBigDecimalValue()
    '''
def getFloatValue():
    '''    public float getFloatValue()
    '''
def getDoubleValue():
    '''    public double getDoubleValue()
    '''
def getByteArrayValue():
    '''    public byte[] getByteArrayValue()
    '''
def getEnumValue():
    '''    public StringEnumAbstractBase getEnumValue()
    '''
def getCalendarValue():
    '''    public Calendar getCalendarValue()
    '''
def getDateValue():
    '''    public Date getDateValue()
    '''
def getGDateValue():
    '''    public GDate getGDateValue()
    '''
def getGDurationValue():
    '''    public GDuration getGDurationValue()
    '''
def getQNameValue():
    '''    public QName getQNameValue()
    '''
def getListValue():
    '''    public List getListValue()
    '''
def xgetListValue():
    '''    public List xgetListValue()
    '''
def getObjectValue():
    '''    public Object getObjectValue()
    '''
def setStringValue():
    '''    public void setStringValue(final String obj)
    '''
def setBooleanValue():
    '''    public void setBooleanValue(final boolean v)
    '''
def setByteValue():
    '''    public void setByteValue(final byte v)
    '''
def setShortValue():
    '''    public void setShortValue(final short v)
    '''
def setIntValue():
    '''    public void setIntValue(final int v)
    '''
def setLongValue():
    '''    public void setLongValue(final long v)
    '''
def setBigIntegerValue():
    '''    public void setBigIntegerValue(final BigInteger obj)
    '''
def setBigDecimalValue():
    '''    public void setBigDecimalValue(final BigDecimal obj)
    '''
def setFloatValue():
    '''    public void setFloatValue(final float v)
    '''
def setDoubleValue():
    '''    public void setDoubleValue(final double v)
    '''
def setByteArrayValue():
    '''    public void setByteArrayValue(final byte[] obj)
    '''
def setEnumValue():
    '''    public void setEnumValue(final StringEnumAbstractBase obj)
    '''
def setCalendarValue():
    '''    public void setCalendarValue(final Calendar obj)
    '''
def setDateValue():
    '''    public void setDateValue(final Date obj)
    '''
def setGDateValue():
    '''    public void setGDateValue(final GDate obj)
    '''
def setGDurationValue():
    '''    public void setGDurationValue(final GDuration obj)
    '''
def setQNameValue():
    '''    public void setQNameValue(final QName obj)
    '''
def setListValue():
    '''    public void setListValue(final List obj)
    '''
def setObjectValue():
    '''    public void setObjectValue(final Object obj)
    '''
def objectSet():
    '''    public void objectSet(final Object obj)
    '''
def selectChildren():
    '''    public XmlObject[] selectChildren(final QName elementName)
    public XmlObject[] selectChildren(final String elementUri, final String elementLocalName)
    public XmlObject[] selectChildren(final QNameSet elementNameSet)
    '''
def selectAttribute():
    '''    public XmlObject selectAttribute(final QName attributeName)
    public XmlObject selectAttribute(final String attributeUri, final String attributeLocalName)
    '''
def selectAttributes():
    '''    public XmlObject[] selectAttributes(final QNameSet attributeNameSet)
    '''
