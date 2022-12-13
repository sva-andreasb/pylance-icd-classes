def RESTParamInfo():
    '''public RESTParamInfo(final String paramName, final Object paramDefaultValue)
    public RESTParamInfo(final String paramName, final String paramDataType, final Object paramDefaultValue)
    public RESTParamInfo(final String paramName, final String paramDataType, final Object paramDefaultValue, final boolean isRequired)
    public RESTParamInfo(final String paramName, final String paramDataType, final Object paramDefaultValue, final boolean isRequired, final List<Object> enumValues)
    '''
def getParamName():
    '''public String getParamName()
    '''
def getParamDataType():
    '''public Object getParamDataType()
    '''
def getParamDefaultValue():
    '''public Object getParamDefaultValue()
    '''
def isRequired():
    '''public boolean isRequired()
    '''
def toJSON():
    '''public JSONObject toJSON()
    '''
def toOASParam():
    '''public JSONObject toOASParam(final String in)
    '''
