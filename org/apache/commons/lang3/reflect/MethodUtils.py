def invokeMethod():
'''public static Object invokeMethod(final Object object, final String methodName)
public static Object invokeMethod(final Object object, final String methodName, Object... args)
public static Object invokeMethod(final Object object, final String methodName, Object[] args, Class<?>[] parameterTypes)
'''
pass
def invokeExactMethod():
'''public static Object invokeExactMethod(final Object object, final String methodName)
public static Object invokeExactMethod(final Object object, final String methodName, Object... args)
public static Object invokeExactMethod(final Object object, final String methodName, Object[] args, Class<?>[] parameterTypes)
'''
pass
def invokeExactStaticMethod():
'''public static Object invokeExactStaticMethod(final Class<?> cls, final String methodName, Object[] args, Class<?>[] parameterTypes)
public static Object invokeExactStaticMethod(final Class<?> cls, final String methodName, Object... args)
'''
pass
def invokeStaticMethod():
'''public static Object invokeStaticMethod(final Class<?> cls, final String methodName, Object... args)
public static Object invokeStaticMethod(final Class<?> cls, final String methodName, Object[] args, Class<?>[] parameterTypes)
'''
pass
def getAccessibleMethod():
'''public static Method getAccessibleMethod(final Class<?> cls, final String methodName, final Class<?>... parameterTypes)
public static Method getAccessibleMethod(Method method)
'''
pass
def getMatchingAccessibleMethod():
'''public static Method getMatchingAccessibleMethod(final Class<?> cls, final String methodName, final Class<?>... parameterTypes)
'''
pass
def getOverrideHierarchy():
'''public static Set<Method> getOverrideHierarchy(final Method method, final ClassUtils.Interfaces interfacesBehavior)
'''
pass
def getMethodsWithAnnotation():
'''public static Method[] getMethodsWithAnnotation(final Class<?> cls, final Class<? extends Annotation> annotationCls)
'''
pass
def getMethodsListWithAnnotation():
'''public static List<Method> getMethodsListWithAnnotation(final Class<?> cls, final Class<? extends Annotation> annotationCls)
'''
pass
