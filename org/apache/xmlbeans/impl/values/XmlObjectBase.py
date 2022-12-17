MAJOR_VERSION_NUMBER = "short  1"
MINOR_VERSION_NUMBER = "short  1"
KIND_SETTERHELPER_SINGLETON = "short  1"
KIND_SETTERHELPER_ARRAYITEM = "short  2"
def documentProperties():
    '''returns XmlDocumentProperties\n\n
    documentProperties()\n
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
def getDomNode():
    '''returns Node\n\n
    getDomNode()\n
    '''
def newDomNode():
    '''returns Node\n\n
    newDomNode()\n
    newDomNode(final XmlOptions options)\n
    '''
def save():
    '''returns None\n\n
    save(final ContentHandler ch, final LexicalHandler lh, final XmlOptions options)\n
    save(final File file, final XmlOptions options)\n
    save(final OutputStream os, final XmlOptions options)\n
    save(final Writer w, final XmlOptions options)\n
    save(final ContentHandler ch, final LexicalHandler lh)\n
    save(final File file)\n
    save(final OutputStream os)\n
    save(final Writer w)\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    '''
def newCursorForce():
    '''returns XmlCursor\n\n
    newCursorForce()\n
    '''
def newCursor():
    '''returns XmlCursor\n\n
    newCursor()\n
    '''
def instanceType():
    '''returns SchemaType\n\n
    instanceType()\n
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
    execQuery(final String path)\n
    execQuery(final String queryExpr, final XmlOptions options)\n
    '''
def changeType():
    '''returns XmlObject\n\n
    changeType(final SchemaType type)\n
    '''
def substitute():
    '''returns XmlObject\n\n
    substitute(final QName name, final SchemaType type)\n
    '''
def init_flags():
    '''returns None\n\n
    init_flags(final SchemaProperty prop)\n
    '''
def setValidateOnSet():
    '''returns None\n\n
    setValidateOnSet()\n
    '''
def setImmutable():
    '''returns None\n\n
    setImmutable()\n
    '''
def isImmutable():
    '''returns boolean\n\n
    isImmutable()\n
    '''
def build_nil():
    '''returns boolean\n\n
    build_nil()\n
    '''
def validate_now():
    '''returns None\n\n
    validate_now()\n
    '''
def disconnect_store():
    '''returns None\n\n
    disconnect_store()\n
    '''
def create_element_user():
    '''returns TypeStoreUser\n\n
    create_element_user(final QName eltName, final QName xsiType)\n
    '''
def create_attribute_user():
    '''returns TypeStoreUser\n\n
    create_attribute_user(final QName attrName)\n
    '''
def get_schema_type():
    '''returns SchemaType\n\n
    get_schema_type()\n
    '''
def get_element_type():
    '''returns SchemaType\n\n
    get_element_type(final QName eltName, final QName xsiType)\n
    '''
def get_attribute_type():
    '''returns SchemaType\n\n
    get_attribute_type(final QName attrName)\n
    '''
def get_default_element_text():
    '''returns String\n\n
    get_default_element_text(final QName eltName)\n
    '''
def get_default_attribute_text():
    '''returns String\n\n
    get_default_attribute_text(final QName attrName)\n
    '''
def get_elementflags():
    '''returns int\n\n
    get_elementflags(final QName eltName)\n
    '''
def get_attributeflags():
    '''returns int\n\n
    get_attributeflags(final QName attrName)\n
    '''
def is_child_element_order_sensitive():
    '''returns boolean\n\n
    is_child_element_order_sensitive()\n
    '''
def new_visitor():
    '''returns TypeStoreVisitor\n\n
    new_visitor()\n
    '''
def get_attribute_field():
    '''returns SchemaField\n\n
    get_attribute_field(final QName attrName)\n
    '''
def getFloatValue():
    '''returns float\n\n
    getFloatValue()\n
    '''
def getDoubleValue():
    '''returns double\n\n
    getDoubleValue()\n
    '''
def getBigDecimalValue():
    '''returns BigDecimal\n\n
    getBigDecimalValue()\n
    '''
def getBigIntegerValue():
    '''returns BigInteger\n\n
    getBigIntegerValue()\n
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
def xmlText():
    '''returns String\n\n
    xmlText()\n
    xmlText(final XmlOptions options)\n
    '''
def getEnumValue():
    '''returns StringEnumAbstractBase\n\n
    getEnumValue()\n
    '''
def getStringValue():
    '''returns String\n\n
    getStringValue()\n
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
def xlistValue():
    '''returns List\n\n
    xlistValue()\n
    '''
def listValue():
    '''returns List\n\n
    listValue()\n
    '''
def objectValue():
    '''returns Object\n\n
    objectValue()\n
    '''
def set():
    '''returns None\n\n
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
def objectSet():
    '''returns None\n\n
    objectSet(final Object obj)\n
    '''
def getByteArrayValue():
    '''returns byte[]\n\n
    getByteArrayValue()\n
    '''
def getBooleanValue():
    '''returns boolean\n\n
    getBooleanValue()\n
    '''
def getGDateValue():
    '''returns GDate\n\n
    getGDateValue()\n
    '''
def getDateValue():
    '''returns Date\n\n
    getDateValue()\n
    '''
def getCalendarValue():
    '''returns Calendar\n\n
    getCalendarValue()\n
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
def setObjectValue():
    '''returns None\n\n
    setObjectValue(final Object o)\n
    '''
def valueHashCode():
    '''returns int\n\n
    valueHashCode()\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final SchemaType type)\n
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
def writeReplace():
    '''returns Object\n\n
    writeReplace()\n
    '''
def invalid():
    '''returns None\n\n
    invalid(final String message)\n
    invalid(final String code, final Object[] args)\n
    invalid(final String message)\n
    invalid(final String code, final Object[] args)\n
    '''
