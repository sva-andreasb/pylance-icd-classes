def toString():
    '''public static String toString(final Object object)
    public static String toString(final Object object, final ToStringStyle style)
    public static String toString(final Object object, final ToStringStyle style, final boolean outputTransients)
    public static String toString(final Object object, final ToStringStyle style, final boolean outputTransients, final boolean outputStatics)
    public static <T> String toString(final T object, final ToStringStyle style, final boolean outputTransients, final boolean outputStatics, final Class<? super T> reflectUpToClass)
    public String toString()
    '''
def toStringExclude():
    '''public static String toStringExclude(final Object object, final Collection<String> excludeFieldNames)
    public static String toStringExclude(final Object object, final String... excludeFieldNames)
    '''
def ReflectionToStringBuilder():
    '''public ReflectionToStringBuilder(final Object object)
    public ReflectionToStringBuilder(final Object object, final ToStringStyle style)
    public ReflectionToStringBuilder(final Object object, final ToStringStyle style, final StringBuffer buffer)
    public <T> ReflectionToStringBuilder(final T object, final ToStringStyle style, final StringBuffer buffer, final Class<? super T> reflectUpToClass, final boolean outputTransients, final boolean outputStatics)
    '''
def getExcludeFieldNames():
    '''public String[] getExcludeFieldNames()
    '''
def isAppendStatics():
    '''public boolean isAppendStatics()
    '''
def isAppendTransients():
    '''public boolean isAppendTransients()
    '''
def reflectionAppendArray():
    '''public ReflectionToStringBuilder reflectionAppendArray(final Object array)
    '''
def setAppendStatics():
    '''public void setAppendStatics(final boolean appendStatics)
    '''
def setAppendTransients():
    '''public void setAppendTransients(final boolean appendTransients)
    '''
def setExcludeFieldNames():
    '''public ReflectionToStringBuilder setExcludeFieldNames(final String... excludeFieldNamesParam)
    '''
def setUpToClass():
    '''public void setUpToClass(final Class<?> clazz)
    '''
