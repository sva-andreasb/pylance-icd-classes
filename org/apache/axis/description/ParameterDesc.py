IN = "byte  1"
OUT = "byte  2"
INOUT = "byte  3"
def ParameterDesc():
    '''public ParameterDesc()
    public ParameterDesc(final ParameterDesc copy)
    public ParameterDesc(final QName name, final byte mode, final QName typeQName)
    public ParameterDesc(final QName name, final byte mode, final QName typeQName, final Class javaType, final boolean inHeader, final boolean outHeader)
    public ParameterDesc(final QName name, final byte mode, final QName typeQName, final Class javaType)
    '''
def toString():
    '''public String toString()
    public String toString(final String indent)
    '''
def modeFromString():
    '''public static byte modeFromString(final String modeStr)
    '''
def getModeAsString():
    '''public static String getModeAsString(final byte mode)
    '''
def getQName():
    '''public QName getQName()
    '''
def getName():
    '''public String getName()
    '''
def setName():
    '''public void setName(final String name)
    '''
def setQName():
    '''public void setQName(final QName name)
    '''
def getTypeQName():
    '''public QName getTypeQName()
    '''
def setTypeQName():
    '''public void setTypeQName(final QName typeQName)
    '''
def getJavaType():
    '''public Class getJavaType()
    '''
def setJavaType():
    '''public void setJavaType(final Class javaType)
    '''
def getMode():
    '''public byte getMode()
    '''
def setMode():
    '''public void setMode(final byte mode)
    '''
def getOrder():
    '''public int getOrder()
    '''
def setOrder():
    '''public void setOrder(final int order)
    '''
def setInHeader():
    '''public void setInHeader(final boolean value)
    '''
def isInHeader():
    '''public boolean isInHeader()
    '''
def setOutHeader():
    '''public void setOutHeader(final boolean value)
    '''
def isOutHeader():
    '''public boolean isOutHeader()
    '''
def getIsReturn():
    '''public boolean getIsReturn()
    '''
def setIsReturn():
    '''public void setIsReturn(final boolean value)
    '''
def getDocumentation():
    '''public String getDocumentation()
    '''
def setDocumentation():
    '''public void setDocumentation(final String documentation)
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
def isOmittable():
    '''public boolean isOmittable()
    '''
def setOmittable():
    '''public void setOmittable(final boolean omittable)
    '''
def isNillable():
    '''public boolean isNillable()
    '''
def setNillable():
    '''public void setNillable(final boolean nillable)
    '''
