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
def without():
    '''public final T without(final MapperFeature... features)
    '''
def withAppendedAnnotationIntrospector():
    '''public final T withAppendedAnnotationIntrospector(final AnnotationIntrospector ai)
    '''
def withInsertedAnnotationIntrospector():
    '''public final T withInsertedAnnotationIntrospector(final AnnotationIntrospector ai)
    '''
def withAttributes():
    '''public T withAttributes(final Map<?, ?> attributes)
    '''
def withAttribute():
    '''public T withAttribute(final Object key, final Object value)
    '''
def withoutAttribute():
    '''public T withoutAttribute(final Object key)
    '''
def withRootName():
    '''public T withRootName(final String rootName)
    '''
def getSubtypeResolver():
    '''public final SubtypeResolver getSubtypeResolver()
    '''
def getRootName():
    '''public final String getRootName()
    '''
def getFullRootName():
    '''public final PropertyName getFullRootName()
    '''
def getAttributes():
    '''public final ContextAttributes getAttributes()
    '''
def getConfigOverride():
    '''public final ConfigOverride getConfigOverride(final Class<?> type)
    '''
def findConfigOverride():
    '''public final ConfigOverride findConfigOverride(final Class<?> type)
    '''
def getDefaultMergeable():
    '''public Boolean getDefaultMergeable()
    public Boolean getDefaultMergeable(final Class<?> baseType)
    '''
def findRootName():
    '''public PropertyName findRootName(final JavaType rootType)
    public PropertyName findRootName(final Class<?> rawRootType)
    '''
def mixInCount():
    '''public final int mixInCount()
    '''
