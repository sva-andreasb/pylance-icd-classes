TRANSLATE_FLAG = "int  1"
GLOBAL_FLAG = "int  2"
FORMAT_FLAG = "int  16"
FINAL = "int  32"
SYSTEM = "int  64"
NONCONDITIONAL = "int  128"
RENDERID = "int  256"
LABEL_SOURCE_ID = "String  \"id\""
def Property():
    '''    public Property(final String name)
    public Property(final String name, final String value)
    public Property(final Property prop)
    '''
def setFlag():
    '''    public void setFlag(final long index)
    '''
def setFlags():
    '''    public void setFlags(final long flags)
    '''
def setValue():
    '''    public void setValue(final String value)
    '''
def getValue():
    '''    public String getValue()
    public String getValue(final List<String> paramValues)
    '''
def setDetaultValue():
    '''    public void setDetaultValue(final String val)
    '''
def getDefaultValue():
    '''    public String getDefaultValue()
    '''
def setName():
    '''    public void setName(final String name)
    '''
def getName():
    '''    public String getName()
    '''
def clearFlags():
    '''    public void clearFlags()
    '''
def clearFlag():
    '''    public void clearFlag(final long index)
    '''
def getFlag():
    '''    public boolean getFlag(final long index)
    '''
def getFlags():
    '''    public long getFlags()
    '''
def clone():
    '''    public Object clone()
    '''
def setFlagsFromString():
    '''    public void setFlagsFromString(final String flags)
    '''
def setFlagFromString():
    '''    public void setFlagFromString(final String flag)
    '''
def isParameterized():
    '''    public boolean isParameterized()
    '''
def getParameterList():
    '''    public List<String> getParameterList()
    '''
def setRegexPattern():
    '''    public void setRegexPattern(final String regex)
    '''
def getTranslatable():
    '''    public String getTranslatable(final WebClientSession sc, final String controlId, final String property)
    public String getTranslatable(final WebClientSession sc, final String controlId, final String property, final String defaultValue)
    '''
def getString():
    '''    public String getString(final String property)
    '''
def toString():
    '''    public String toString()
    '''
