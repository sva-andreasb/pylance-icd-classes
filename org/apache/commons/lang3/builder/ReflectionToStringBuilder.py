def toString():
'''public static String toString(final Object object)
public static String toString(final Object object, final ToStringStyle style)
public static String toString(final Object object, final ToStringStyle style, final boolean outputTransients)
public static String toString(final Object object, final ToStringStyle style, final boolean outputTransients, final boolean outputStatics)
public static <T> String toString(final T object, final ToStringStyle style, final boolean outputTransients, final boolean outputStatics, final Class<? super T> reflectUpToClass)
public String toString()
'''
pass
def toStringExclude():
'''public static String toStringExclude(final Object object, final Collection<String> excludeFieldNames)
public static String toStringExclude(final Object object, final String... excludeFieldNames)
'''
pass
def ReflectionToStringBuilder():
'''public ReflectionToStringBuilder(final Object object)
public ReflectionToStringBuilder(final Object object, final ToStringStyle style)
public ReflectionToStringBuilder(final Object object, final ToStringStyle style, final StringBuffer buffer)
public <T> ReflectionToStringBuilder(final T object, final ToStringStyle style, final StringBuffer buffer, final Class<? super T> reflectUpToClass, final boolean outputTransients, final boolean outputStatics)
'''
pass
def getExcludeFieldNames():
'''public String[] getExcludeFieldNames()
'''
pass
def isAppendStatics():
'''public boolean isAppendStatics()
'''
pass
def isAppendTransients():
'''public boolean isAppendTransients()
'''
pass
def reflectionAppendArray():
'''public ReflectionToStringBuilder reflectionAppendArray(final Object array)
'''
pass
def setAppendStatics():
'''public void setAppendStatics(final boolean appendStatics)
'''
pass
def setAppendTransients():
'''public void setAppendTransients(final boolean appendTransients)
'''
pass
def setExcludeFieldNames():
'''public ReflectionToStringBuilder setExcludeFieldNames(final String... excludeFieldNamesParam)
'''
pass
def setUpToClass():
'''public void setUpToClass(final Class<?> clazz)
'''
pass
