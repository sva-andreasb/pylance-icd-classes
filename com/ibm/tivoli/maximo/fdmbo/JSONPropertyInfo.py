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
def JSONPropertyInfo():
    '''public JSONPropertyInfo(final String name, final int type, final long suggestedLength, final String title)
    public JSONPropertyInfo(final String name, final String attributeName, final int type, final Object defaultValue, final long suggestedLength, final String title, final String dateFormatType, final String dateFormat)
    public JSONPropertyInfo(final String attributeName, final String propName, final String dateFormatType, final String dateFormat)
    '''
def setEditable():
    '''public void setEditable(final boolean editable)
    '''
def setDomainName():
    '''public void setDomainName(final String domainName)
    '''
def getDomainName():
    '''public String getDomainName()
    '''
def setRequired():
    '''public void setRequired(final boolean required)
    '''
def isEditable():
    '''public boolean isEditable()
    '''
def isRequired():
    '''public boolean isRequired()
    '''
def getSuggestedLength():
    '''public long getSuggestedLength()
    '''
def setLength():
    '''public void setLength(final int l)
    '''
def getName():
    '''public String getName()
    '''
def getAttributeName():
    '''public String getAttributeName()
    '''
def setAttributeName():
    '''public void setAttributeName(final String attr)
    '''
def getType():
    '''public int getType()
    '''
def getScale():
    '''public int getScale()
    '''
def setScale():
    '''public void setScale(final int t)
    '''
def getTitle():
    '''public String getTitle()
    '''
def setTitle():
    '''public void setTitle(final String t)
    '''
def setDefaultValue():
    '''public void setDefaultValue(final String t)
    '''
def getDefaultValue():
    '''public Object getDefaultValue()
    '''
def getMaxType():
    '''public String getMaxType()
    public String getMaxType(final int type)
    '''
def setMaxType():
    '''public void setMaxType(final String t)
    '''
def setDateFormatType():
    '''public String setDateFormatType(final String dt)
    '''
def setDateFormat():
    '''public String setDateFormat(final String df)
    '''
def getDomainMap():
    '''public Map<Object, String> getDomainMap()
    '''
def getDateFormatType():
    '''public String getDateFormatType()
    '''
def getDateFormat():
    '''public String getDateFormat()
    '''
def setDomainMap():
    '''public void setDomainMap(final Map<Object, String> domainMap)
    '''
def setConstraints():
    '''public void setConstraints(final PropertyConstraints pc)
    '''
