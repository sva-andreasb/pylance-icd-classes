def with():
'''public final T with(final MapperFeature... features)
public final T with(final MapperFeature feature, final boolean state)
public final T with(final AnnotationIntrospector ai)
public final T with(final ClassIntrospector ci)
public final T with(final TypeFactory tf)
public final T with(final TypeResolverBuilder<?> trb)
public final T with(final PropertyNamingStrategy pns)
public final T with(final HandlerInstantiator hi)
public final T with(final Base64Variant base64)
public T with(final DateFormat df)
public final T with(final Locale l)
public final T with(final TimeZone tz)
'''
pass
def without():
'''public final T without(final MapperFeature... features)
'''
pass
def withAppendedAnnotationIntrospector():
'''public final T withAppendedAnnotationIntrospector(final AnnotationIntrospector ai)
'''
pass
def withInsertedAnnotationIntrospector():
'''public final T withInsertedAnnotationIntrospector(final AnnotationIntrospector ai)
'''
pass
def withAttributes():
'''public T withAttributes(final Map<?, ?> attributes)
'''
pass
def withAttribute():
'''public T withAttribute(final Object key, final Object value)
'''
pass
def withoutAttribute():
'''public T withoutAttribute(final Object key)
'''
pass
def withRootName():
'''public T withRootName(final String rootName)
'''
pass
def getSubtypeResolver():
'''public final SubtypeResolver getSubtypeResolver()
'''
pass
def getRootName():
'''public final String getRootName()
'''
pass
def getFullRootName():
'''public final PropertyName getFullRootName()
'''
pass
def getAttributes():
'''public final ContextAttributes getAttributes()
'''
pass
def getConfigOverride():
'''public final ConfigOverride getConfigOverride(final Class<?> type)
'''
pass
def findConfigOverride():
'''public final ConfigOverride findConfigOverride(final Class<?> type)
'''
pass
def getDefaultMergeable():
'''public Boolean getDefaultMergeable()
public Boolean getDefaultMergeable(final Class<?> baseType)
'''
pass
def findRootName():
'''public PropertyName findRootName(final JavaType rootType)
public PropertyName findRootName(final Class<?> rawRootType)
'''
pass
def mixInCount():
'''public final int mixInCount()
'''
pass
