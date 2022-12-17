IN = "byte  1"
OUT = "byte  2"
INOUT = "byte  3"
def ():
    '''returns ParameterDesc\n\n
    ()\n
    (final ParameterDesc copy)\n
    (final QName name, final byte mode, final QName typeQName)\n
    (final QName name, final byte mode, final QName typeQName, final Class javaType, final boolean inHeader, final boolean outHeader)\n
    (final QName name, final byte mode, final QName typeQName, final Class javaType)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String indent)\n
    '''
def getQName():
    '''returns QName\n\n
    getQName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setQName():
    '''returns None\n\n
    setQName(final QName name)\n
    '''
def getTypeQName():
    '''returns QName\n\n
    getTypeQName()\n
    '''
def setTypeQName():
    '''returns None\n\n
    setTypeQName(final QName typeQName)\n
    '''
def getJavaType():
    '''returns Class\n\n
    getJavaType()\n
    '''
def setJavaType():
    '''returns None\n\n
    setJavaType(final Class javaType)\n
    '''
def getMode():
    '''returns byte\n\n
    getMode()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final byte mode)\n
    '''
def getOrder():
    '''returns int\n\n
    getOrder()\n
    '''
def setOrder():
    '''returns None\n\n
    setOrder(final int order)\n
    '''
def setInHeader():
    '''returns None\n\n
    setInHeader(final boolean value)\n
    '''
def isInHeader():
    '''returns boolean\n\n
    isInHeader()\n
    '''
def setOutHeader():
    '''returns None\n\n
    setOutHeader(final boolean value)\n
    '''
def isOutHeader():
    '''returns boolean\n\n
    isOutHeader()\n
    '''
def getIsReturn():
    '''returns boolean\n\n
    getIsReturn()\n
    '''
def setIsReturn():
    '''returns None\n\n
    setIsReturn(final boolean value)\n
    '''
def getDocumentation():
    '''returns String\n\n
    getDocumentation()\n
    '''
def setDocumentation():
    '''returns None\n\n
    setDocumentation(final String documentation)\n
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
def isOmittable():
    '''returns boolean\n\n
    isOmittable()\n
    '''
def setOmittable():
    '''returns None\n\n
    setOmittable(final boolean omittable)\n
    '''
def isNillable():
    '''returns boolean\n\n
    isNillable()\n
    '''
def setNillable():
    '''returns None\n\n
    setNillable(final boolean nillable)\n
    '''
