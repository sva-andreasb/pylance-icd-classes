def ():
    '''returns RESTParamInfo\n\n
    (final String paramName, final Object paramDefaultValue)\n
    (final String paramName, final String paramDataType, final Object paramDefaultValue)\n
    (final String paramName, final String paramDataType, final Object paramDefaultValue, final boolean isRequired)\n
    (final String paramName, final String paramDataType, final Object paramDefaultValue, final boolean isRequired, final List<Object> enumValues)\n
    '''
def getParamName():
    '''returns String\n\n
    getParamName()\n
    '''
def getParamDataType():
    '''returns Object\n\n
    getParamDataType()\n
    '''
def getParamDefaultValue():
    '''returns Object\n\n
    getParamDefaultValue()\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired()\n
    '''
def toJSON():
    '''returns JSONObject\n\n
    toJSON()\n
    '''
def toOASParam():
    '''returns JSONObject\n\n
    toOASParam(final String in)\n
    '''
