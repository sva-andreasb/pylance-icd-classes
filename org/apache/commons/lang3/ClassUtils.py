PACKAGE_SEPARATOR_CHAR = "char  '.'"
INNER_CLASS_SEPARATOR_CHAR = "char  '$'"
def getShortClassName():
    '''    public static String getShortClassName(final Object object, final String valueIfNull)
    public static String getShortClassName(final Class<?> cls)
    public static String getShortClassName(String className)
    '''
def getSimpleName():
    '''    public static String getSimpleName(final Class<?> cls)
    public static String getSimpleName(final Object object, final String valueIfNull)
    '''
def getPackageName():
    '''    public static String getPackageName(final Object object, final String valueIfNull)
    public static String getPackageName(final Class<?> cls)
    public static String getPackageName(String className)
    '''
def getAbbreviatedName():
    '''    public static String getAbbreviatedName(final Class<?> cls, final int len)
    public static String getAbbreviatedName(final String className, final int len)
    '''
def convertClassesToClassNames():
    '''    public static List<String> convertClassesToClassNames(final List<Class<?>> classes)
    '''
def isAssignable():
    '''    public static boolean isAssignable(final Class<?>[] classArray, final Class<?>... toClassArray)
    public static boolean isAssignable(Class<?>[] classArray, Class<?>[] toClassArray, final boolean autoboxing)
    public static boolean isAssignable(final Class<?> cls, final Class<?> toClass)
    public static boolean isAssignable(Class<?> cls, final Class<?> toClass, final boolean autoboxing)
    '''
def isPrimitiveOrWrapper():
    '''    public static boolean isPrimitiveOrWrapper(final Class<?> type)
    '''
def isPrimitiveWrapper():
    '''    public static boolean isPrimitiveWrapper(final Class<?> type)
    '''
def isInnerClass():
    '''    public static boolean isInnerClass(final Class<?> cls)
    '''
def getPublicMethod():
    '''    public static Method getPublicMethod(final Class<?> cls, final String methodName, final Class<?>... parameterTypes)
    '''
def getShortCanonicalName():
    '''    public static String getShortCanonicalName(final Object object, final String valueIfNull)
    public static String getShortCanonicalName(final Class<?> cls)
    public static String getShortCanonicalName(final String canonicalName)
    '''
def getPackageCanonicalName():
    '''    public static String getPackageCanonicalName(final Object object, final String valueIfNull)
    public static String getPackageCanonicalName(final Class<?> cls)
    public static String getPackageCanonicalName(final String canonicalName)
    '''
def hasNext():
    '''    public boolean hasNext()
    public boolean hasNext()
    '''
def remove():
    '''    public void remove()
    public void remove()
    '''
