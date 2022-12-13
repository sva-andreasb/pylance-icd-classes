def getField():
'''public static Field getField(final Class<?> cls, final String fieldName)
public static Field getField(final Class<?> cls, final String fieldName, final boolean forceAccess)
'''
pass
def getDeclaredField():
'''public static Field getDeclaredField(final Class<?> cls, final String fieldName)
public static Field getDeclaredField(final Class<?> cls, final String fieldName, final boolean forceAccess)
'''
pass
def getAllFields():
'''public static Field[] getAllFields(final Class<?> cls)
'''
pass
def getAllFieldsList():
'''public static List<Field> getAllFieldsList(final Class<?> cls)
'''
pass
def getFieldsWithAnnotation():
'''public static Field[] getFieldsWithAnnotation(final Class<?> cls, final Class<? extends Annotation> annotationCls)
'''
pass
def getFieldsListWithAnnotation():
'''public static List<Field> getFieldsListWithAnnotation(final Class<?> cls, final Class<? extends Annotation> annotationCls)
'''
pass
def readStaticField():
'''public static Object readStaticField(final Field field)
public static Object readStaticField(final Field field, final boolean forceAccess)
public static Object readStaticField(final Class<?> cls, final String fieldName)
public static Object readStaticField(final Class<?> cls, final String fieldName, final boolean forceAccess)
'''
pass
def readDeclaredStaticField():
'''public static Object readDeclaredStaticField(final Class<?> cls, final String fieldName)
public static Object readDeclaredStaticField(final Class<?> cls, final String fieldName, final boolean forceAccess)
'''
pass
def readField():
'''public static Object readField(final Field field, final Object target)
public static Object readField(final Field field, final Object target, final boolean forceAccess)
public static Object readField(final Object target, final String fieldName)
public static Object readField(final Object target, final String fieldName, final boolean forceAccess)
'''
pass
def readDeclaredField():
'''public static Object readDeclaredField(final Object target, final String fieldName)
public static Object readDeclaredField(final Object target, final String fieldName, final boolean forceAccess)
'''
pass
def writeStaticField():
'''public static void writeStaticField(final Field field, final Object value)
public static void writeStaticField(final Field field, final Object value, final boolean forceAccess)
public static void writeStaticField(final Class<?> cls, final String fieldName, final Object value)
public static void writeStaticField(final Class<?> cls, final String fieldName, final Object value, final boolean forceAccess)
'''
pass
def writeDeclaredStaticField():
'''public static void writeDeclaredStaticField(final Class<?> cls, final String fieldName, final Object value)
public static void writeDeclaredStaticField(final Class<?> cls, final String fieldName, final Object value, final boolean forceAccess)
'''
pass
def writeField():
'''public static void writeField(final Field field, final Object target, final Object value)
public static void writeField(final Field field, final Object target, final Object value, final boolean forceAccess)
public static void writeField(final Object target, final String fieldName, final Object value)
public static void writeField(final Object target, final String fieldName, final Object value, final boolean forceAccess)
'''
pass
def removeFinalModifier():
'''public static void removeFinalModifier(final Field field)
public static void removeFinalModifier(final Field field, final boolean forceAccess)
'''
pass
def writeDeclaredField():
'''public static void writeDeclaredField(final Object target, final String fieldName, final Object value)
public static void writeDeclaredField(final Object target, final String fieldName, final Object value, final boolean forceAccess)
'''
pass
