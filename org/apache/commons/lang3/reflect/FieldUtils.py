def getField():
    '''public static Field getField(final Class<?> cls, final String fieldName)
    public static Field getField(final Class<?> cls, final String fieldName, final boolean forceAccess)
    '''
def getDeclaredField():
    '''public static Field getDeclaredField(final Class<?> cls, final String fieldName)
    public static Field getDeclaredField(final Class<?> cls, final String fieldName, final boolean forceAccess)
    '''
def getAllFields():
    '''public static Field[] getAllFields(final Class<?> cls)
    '''
def getAllFieldsList():
    '''public static List<Field> getAllFieldsList(final Class<?> cls)
    '''
def getFieldsWithAnnotation():
    '''public static Field[] getFieldsWithAnnotation(final Class<?> cls, final Class<? extends Annotation> annotationCls)
    '''
def getFieldsListWithAnnotation():
    '''public static List<Field> getFieldsListWithAnnotation(final Class<?> cls, final Class<? extends Annotation> annotationCls)
    '''
def readStaticField():
    '''public static Object readStaticField(final Field field)
    public static Object readStaticField(final Field field, final boolean forceAccess)
    public static Object readStaticField(final Class<?> cls, final String fieldName)
    public static Object readStaticField(final Class<?> cls, final String fieldName, final boolean forceAccess)
    '''
def readDeclaredStaticField():
    '''public static Object readDeclaredStaticField(final Class<?> cls, final String fieldName)
    public static Object readDeclaredStaticField(final Class<?> cls, final String fieldName, final boolean forceAccess)
    '''
def readField():
    '''public static Object readField(final Field field, final Object target)
    public static Object readField(final Field field, final Object target, final boolean forceAccess)
    public static Object readField(final Object target, final String fieldName)
    public static Object readField(final Object target, final String fieldName, final boolean forceAccess)
    '''
def readDeclaredField():
    '''public static Object readDeclaredField(final Object target, final String fieldName)
    public static Object readDeclaredField(final Object target, final String fieldName, final boolean forceAccess)
    '''
def writeStaticField():
    '''public static void writeStaticField(final Field field, final Object value)
    public static void writeStaticField(final Field field, final Object value, final boolean forceAccess)
    public static void writeStaticField(final Class<?> cls, final String fieldName, final Object value)
    public static void writeStaticField(final Class<?> cls, final String fieldName, final Object value, final boolean forceAccess)
    '''
def writeDeclaredStaticField():
    '''public static void writeDeclaredStaticField(final Class<?> cls, final String fieldName, final Object value)
    public static void writeDeclaredStaticField(final Class<?> cls, final String fieldName, final Object value, final boolean forceAccess)
    '''
def writeField():
    '''public static void writeField(final Field field, final Object target, final Object value)
    public static void writeField(final Field field, final Object target, final Object value, final boolean forceAccess)
    public static void writeField(final Object target, final String fieldName, final Object value)
    public static void writeField(final Object target, final String fieldName, final Object value, final boolean forceAccess)
    '''
def removeFinalModifier():
    '''public static void removeFinalModifier(final Field field)
    public static void removeFinalModifier(final Field field, final boolean forceAccess)
    '''
def writeDeclaredField():
    '''public static void writeDeclaredField(final Object target, final String fieldName, final Object value)
    public static void writeDeclaredField(final Object target, final String fieldName, final Object value, final boolean forceAccess)
    '''
