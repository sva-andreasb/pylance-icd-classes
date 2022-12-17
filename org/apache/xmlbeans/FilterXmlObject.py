def schemaType():
    '''returns SchemaType\n\n
    schemaType()\n
    '''
def validate():
    '''returns boolean\n\n
    validate()\n
    validate(final XmlOptions options)\n
    '''
def selectPath():
    '''returns XmlObject[]\n\n
    selectPath(final String path)\n
    selectPath(final String path, final XmlOptions options)\n
    '''
def execQuery():
    '''returns XmlObject[]\n\n
    execQuery(final String query)\n
    execQuery(final String query, final XmlOptions options)\n
    '''
def changeType():
    '''returns XmlObject\n\n
    changeType(final SchemaType newType)\n
    '''
def isNil():
    '''returns boolean\n\n
    isNil()\n
    '''
def setNil():
    '''returns None\n\n
    setNil()\n
    '''
def isImmutable():
    '''returns boolean\n\n
    isImmutable()\n
    '''
def set():
    '''returns None\n\n
    set(final XmlObject srcObj)\n
    set(final String obj)\n
    set(final boolean v)\n
    set(final byte v)\n
    set(final short v)\n
    set(final int v)\n
    set(final long v)\n
    set(final BigInteger obj)\n
    set(final BigDecimal obj)\n
    set(final float v)\n
    set(final double v)\n
    set(final byte[] obj)\n
    set(final StringEnumAbstractBase obj)\n
    set(final Calendar obj)\n
    set(final Date obj)\n
    set(final GDateSpecification obj)\n
    set(final GDurationSpecification obj)\n
    set(final QName obj)\n
    set(final List obj)\n
    '''
def copy():
    '''returns XmlObject\n\n
    copy()\n
    copy(final XmlOptions options)\n
    '''
def valueEquals():
    '''returns boolean\n\n
    valueEquals(final XmlObject obj)\n
    '''
def valueHashCode():
    '''returns int\n\n
    valueHashCode()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object obj)\n
    '''
def compareValue():
    '''returns int\n\n
    compareValue(final XmlObject obj)\n
    '''
def monitor():
    '''returns Object\n\n
    monitor()\n
    '''
def documentProperties():
    '''returns XmlDocumentProperties\n\n
    documentProperties()\n
    '''
def newCursor():
    '''returns XmlCursor\n\n
    newCursor()\n
    '''
def newXMLInputStream():
    '''returns XMLInputStream\n\n
    newXMLInputStream()\n
    newXMLInputStream(final XmlOptions options)\n
    '''
def newXMLStreamReader():
    '''returns XMLStreamReader\n\n
    newXMLStreamReader()\n
    newXMLStreamReader(final XmlOptions options)\n
    '''
def xmlText():
    '''returns String\n\n
    xmlText()\n
    xmlText(final XmlOptions options)\n
    '''
def newInputStream():
    '''returns InputStream\n\n
    newInputStream()\n
    newInputStream(final XmlOptions options)\n
    '''
def newReader():
    '''returns Reader\n\n
    newReader()\n
    newReader(final XmlOptions options)\n
    '''
def newDomNode():
    '''returns Node\n\n
    newDomNode()\n
    newDomNode(final XmlOptions options)\n
    '''
def getDomNode():
    '''returns Node\n\n
    getDomNode()\n
    '''
def save():
    '''returns None\n\n
    save(final ContentHandler ch, final LexicalHandler lh)\n
    save(final File file)\n
    save(final OutputStream os)\n
    save(final Writer w)\n
    save(final ContentHandler ch, final LexicalHandler lh, final XmlOptions options)\n
    save(final File file, final XmlOptions options)\n
    save(final OutputStream os, final XmlOptions options)\n
    save(final Writer w, final XmlOptions options)\n
    '''
def instanceType():
    '''returns SchemaType\n\n
    instanceType()\n
    '''
def stringValue():
    '''returns String\n\n
    stringValue()\n
    '''
def booleanValue():
    '''returns boolean\n\n
    booleanValue()\n
    '''
def byteValue():
    '''returns byte\n\n
    byteValue()\n
    '''
def shortValue():
    '''returns short\n\n
    shortValue()\n
    '''
def intValue():
    '''returns int\n\n
    intValue()\n
    '''
def longValue():
    '''returns long\n\n
    longValue()\n
    '''
def bigIntegerValue():
    '''returns BigInteger\n\n
    bigIntegerValue()\n
    '''
def bigDecimalValue():
    '''returns BigDecimal\n\n
    bigDecimalValue()\n
    '''
def floatValue():
    '''returns float\n\n
    floatValue()\n
    '''
def doubleValue():
    '''returns double\n\n
    doubleValue()\n
    '''
def byteArrayValue():
    '''returns byte[]\n\n
    byteArrayValue()\n
    '''
def enumValue():
    '''returns StringEnumAbstractBase\n\n
    enumValue()\n
    '''
def calendarValue():
    '''returns Calendar\n\n
    calendarValue()\n
    '''
def dateValue():
    '''returns Date\n\n
    dateValue()\n
    '''
def gDateValue():
    '''returns GDate\n\n
    gDateValue()\n
    '''
def gDurationValue():
    '''returns GDuration\n\n
    gDurationValue()\n
    '''
def qNameValue():
    '''returns QName\n\n
    qNameValue()\n
    '''
def listValue():
    '''returns List\n\n
    listValue()\n
    '''
def xlistValue():
    '''returns List\n\n
    xlistValue()\n
    '''
def objectValue():
    '''returns Object\n\n
    objectValue()\n
    '''
def getStringValue():
    '''returns String\n\n
    getStringValue()\n
    '''
def getBooleanValue():
    '''returns boolean\n\n
    getBooleanValue()\n
    '''
def getByteValue():
    '''returns byte\n\n
    getByteValue()\n
    '''
def getShortValue():
    '''returns short\n\n
    getShortValue()\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue()\n
    '''
def getLongValue():
    '''returns long\n\n
    getLongValue()\n
    '''
def getBigIntegerValue():
    '''returns BigInteger\n\n
    getBigIntegerValue()\n
    '''
def getBigDecimalValue():
    '''returns BigDecimal\n\n
    getBigDecimalValue()\n
    '''
def getFloatValue():
    '''returns float\n\n
    getFloatValue()\n
    '''
def getDoubleValue():
    '''returns double\n\n
    getDoubleValue()\n
    '''
def getByteArrayValue():
    '''returns byte[]\n\n
    getByteArrayValue()\n
    '''
def getEnumValue():
    '''returns StringEnumAbstractBase\n\n
    getEnumValue()\n
    '''
def getCalendarValue():
    '''returns Calendar\n\n
    getCalendarValue()\n
    '''
def getDateValue():
    '''returns Date\n\n
    getDateValue()\n
    '''
def getGDateValue():
    '''returns GDate\n\n
    getGDateValue()\n
    '''
def getGDurationValue():
    '''returns GDuration\n\n
    getGDurationValue()\n
    '''
def getQNameValue():
    '''returns QName\n\n
    getQNameValue()\n
    '''
def getListValue():
    '''returns List\n\n
    getListValue()\n
    '''
def xgetListValue():
    '''returns List\n\n
    xgetListValue()\n
    '''
def getObjectValue():
    '''returns Object\n\n
    getObjectValue()\n
    '''
def setStringValue():
    '''returns None\n\n
    setStringValue(final String obj)\n
    '''
def setBooleanValue():
    '''returns None\n\n
    setBooleanValue(final boolean v)\n
    '''
def setByteValue():
    '''returns None\n\n
    setByteValue(final byte v)\n
    '''
def setShortValue():
    '''returns None\n\n
    setShortValue(final short v)\n
    '''
def setIntValue():
    '''returns None\n\n
    setIntValue(final int v)\n
    '''
def setLongValue():
    '''returns None\n\n
    setLongValue(final long v)\n
    '''
def setBigIntegerValue():
    '''returns None\n\n
    setBigIntegerValue(final BigInteger obj)\n
    '''
def setBigDecimalValue():
    '''returns None\n\n
    setBigDecimalValue(final BigDecimal obj)\n
    '''
def setFloatValue():
    '''returns None\n\n
    setFloatValue(final float v)\n
    '''
def setDoubleValue():
    '''returns None\n\n
    setDoubleValue(final double v)\n
    '''
def setByteArrayValue():
    '''returns None\n\n
    setByteArrayValue(final byte[] obj)\n
    '''
def setEnumValue():
    '''returns None\n\n
    setEnumValue(final StringEnumAbstractBase obj)\n
    '''
def setCalendarValue():
    '''returns None\n\n
    setCalendarValue(final Calendar obj)\n
    '''
def setDateValue():
    '''returns None\n\n
    setDateValue(final Date obj)\n
    '''
def setGDateValue():
    '''returns None\n\n
    setGDateValue(final GDate obj)\n
    '''
def setGDurationValue():
    '''returns None\n\n
    setGDurationValue(final GDuration obj)\n
    '''
def setQNameValue():
    '''returns None\n\n
    setQNameValue(final QName obj)\n
    '''
def setListValue():
    '''returns None\n\n
    setListValue(final List obj)\n
    '''
def setObjectValue():
    '''returns None\n\n
    setObjectValue(final Object obj)\n
    '''
def objectSet():
    '''returns None\n\n
    objectSet(final Object obj)\n
    '''
def selectChildren():
    '''returns XmlObject[]\n\n
    selectChildren(final QName elementName)\n
    selectChildren(final String elementUri, final String elementLocalName)\n
    selectChildren(final QNameSet elementNameSet)\n
    '''
def selectAttribute():
    '''returns XmlObject\n\n
    selectAttribute(final QName attributeName)\n
    selectAttribute(final String attributeUri, final String attributeLocalName)\n
    '''
def selectAttributes():
    '''returns XmlObject[]\n\n
    selectAttributes(final QNameSet attributeNameSet)\n
    '''
