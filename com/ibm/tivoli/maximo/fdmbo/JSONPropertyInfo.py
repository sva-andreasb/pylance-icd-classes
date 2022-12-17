TYPE_ALN = "int  5"
TYPE_DATETIME = "int  1"
TYPE_DECIMAL = "int  2"
TYPE_INT = "int  3"
TYPE_LONG = "int  4"
TYPE_BOOLEAN = "int  6"
TYPE_FLOAT = "int  7"
TYPE_BIGINT = "int  8"
TYPE_BLOB = "int  9"
MAXTYPE_YORN = "String  \"YORN\""
MAXTYPE_BLOB = "String  \"BLOB\""
MAXTYPE_DATETIME = "String  \"DATETIME\""
MAXTYPE_FLOAT = "String  \"FLOAT\""
MAXTYPE_DATE = "String  \"DATE\""
MAXTYPE_TIME = "String  \"TIME\""
MAXTYPE_ALN = "String  \"ALN\""
MAXTYPE_INTEGER = "String  \"INTEGER\""
MAXTYPE_BIGINT = "String  \"BIGINT\""
MAXTYPE_DECIMAL = "String  \"DECIMAL\""
def ():
    '''returns JSONPropertyInfo\n\n
    (final String name, final int type, final long suggestedLength, final String title)\n
    (final String name, final String attributeName, final int type, final Object defaultValue, final long suggestedLength, final String title, final String dateFormatType, final String dateFormat)\n
    (final String attributeName, final String propName, final String dateFormatType, final String dateFormat)\n
    '''
def setEditable():
    '''returns None\n\n
    setEditable(final boolean editable)\n
    '''
def setDomainName():
    '''returns None\n\n
    setDomainName(final String domainName)\n
    '''
def getDomainName():
    '''returns String\n\n
    getDomainName()\n
    '''
def setRequired():
    '''returns None\n\n
    setRequired(final boolean required)\n
    '''
def isEditable():
    '''returns boolean\n\n
    isEditable()\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired()\n
    '''
def getSuggestedLength():
    '''returns long\n\n
    getSuggestedLength()\n
    '''
def setLength():
    '''returns None\n\n
    setLength(final int l)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName()\n
    '''
def setAttributeName():
    '''returns None\n\n
    setAttributeName(final String attr)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getScale():
    '''returns int\n\n
    getScale()\n
    '''
def setScale():
    '''returns None\n\n
    setScale(final int t)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String t)\n
    '''
def setDefaultValue():
    '''returns None\n\n
    setDefaultValue(final String t)\n
    '''
def getDefaultValue():
    '''returns Object\n\n
    getDefaultValue()\n
    '''
def getMaxType():
    '''returns String\n\n
    getMaxType()\n
    getMaxType(final int type)\n
    '''
def setMaxType():
    '''returns None\n\n
    setMaxType(final String t)\n
    '''
def setDateFormatType():
    '''returns String\n\n
    setDateFormatType(final String dt)\n
    '''
def setDateFormat():
    '''returns String\n\n
    setDateFormat(final String df)\n
    '''
def getDateFormatType():
    '''returns String\n\n
    getDateFormatType()\n
    '''
def getDateFormat():
    '''returns String\n\n
    getDateFormat()\n
    '''
def setDomainMap():
    '''returns None\n\n
    setDomainMap(final Map<Object, String> domainMap)\n
    '''
def setConstraints():
    '''returns None\n\n
    setConstraints(final PropertyConstraints pc)\n
    '''
