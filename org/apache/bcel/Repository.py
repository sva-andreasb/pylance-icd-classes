def setRepository():
    '''public static void setRepository(final org.apache.bcel.util.Repository rep)
    '''
def lookupClass():
    '''public static JavaClass lookupClass(final String class_name)
    public static JavaClass lookupClass(final Class clazz)
    '''
def clearCache():
    '''public static void clearCache()
    '''
def addClass():
    '''public static JavaClass addClass(final JavaClass clazz)
    '''
def removeClass():
    '''public static void removeClass(final String clazz)
    public static void removeClass(final JavaClass clazz)
    '''
def getSuperClasses():
    '''public static JavaClass[] getSuperClasses(final JavaClass clazz)
    public static JavaClass[] getSuperClasses(final String class_name)
    '''
def getInterfaces():
    '''public static JavaClass[] getInterfaces(final JavaClass clazz)
    public static JavaClass[] getInterfaces(final String class_name)
    '''
def instanceOf():
    '''public static boolean instanceOf(final JavaClass clazz, final JavaClass super_class)
    public static boolean instanceOf(final String clazz, final String super_class)
    public static boolean instanceOf(final JavaClass clazz, final String super_class)
    public static boolean instanceOf(final String clazz, final JavaClass super_class)
    '''
def implementationOf():
    '''public static boolean implementationOf(final JavaClass clazz, final JavaClass inter)
    public static boolean implementationOf(final String clazz, final String inter)
    public static boolean implementationOf(final JavaClass clazz, final String inter)
    public static boolean implementationOf(final String clazz, final JavaClass inter)
    '''
