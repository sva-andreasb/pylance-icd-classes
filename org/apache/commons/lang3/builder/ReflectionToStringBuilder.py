def ():
    '''returns ReflectionToStringBuilder\n\n
    (final Object object)\n
    (final Object object, final ToStringStyle style)\n
    (final Object object, final ToStringStyle style, final StringBuffer buffer)\n
    '''
def ReflectionToStringBuilder():
    '''returns <T>\n\n
    ReflectionToStringBuilder(final T object, final ToStringStyle style, final StringBuffer buffer, final Class<? super T> reflectUpToClass, final boolean outputTransients, final boolean outputStatics)\n
    '''
def getExcludeFieldNames():
    '''returns String[]\n\n
    getExcludeFieldNames()\n
    '''
def isAppendStatics():
    '''returns boolean\n\n
    isAppendStatics()\n
    '''
def isAppendTransients():
    '''returns boolean\n\n
    isAppendTransients()\n
    '''
def reflectionAppendArray():
    '''returns ReflectionToStringBuilder\n\n
    reflectionAppendArray(final Object array)\n
    '''
def setAppendStatics():
    '''returns None\n\n
    setAppendStatics(final boolean appendStatics)\n
    '''
def setAppendTransients():
    '''returns None\n\n
    setAppendTransients(final boolean appendTransients)\n
    '''
def setExcludeFieldNames():
    '''returns ReflectionToStringBuilder\n\n
    setExcludeFieldNames(final String... excludeFieldNamesParam)\n
    '''
def setUpToClass():
    '''returns None\n\n
    setUpToClass(final Class<?> clazz)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
