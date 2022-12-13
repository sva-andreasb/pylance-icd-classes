def GsonBuilder():
    '''    public GsonBuilder()
    '''
def setVersion():
    '''    public GsonBuilder setVersion(final double ignoreVersionsAfter)
    '''
def excludeFieldsWithModifiers():
    '''    public GsonBuilder excludeFieldsWithModifiers(final int... modifiers)
    '''
def generateNonExecutableJson():
    '''    public GsonBuilder generateNonExecutableJson()
    '''
def excludeFieldsWithoutExposeAnnotation():
    '''    public GsonBuilder excludeFieldsWithoutExposeAnnotation()
    '''
def serializeNulls():
    '''    public GsonBuilder serializeNulls()
    '''
def enableComplexMapKeySerialization():
    '''    public GsonBuilder enableComplexMapKeySerialization()
    '''
def disableInnerClassSerialization():
    '''    public GsonBuilder disableInnerClassSerialization()
    '''
def setLongSerializationPolicy():
    '''    public GsonBuilder setLongSerializationPolicy(final LongSerializationPolicy serializationPolicy)
    '''
def setFieldNamingPolicy():
    '''    public GsonBuilder setFieldNamingPolicy(final FieldNamingPolicy namingConvention)
    '''
def setFieldNamingStrategy():
    '''    public GsonBuilder setFieldNamingStrategy(final FieldNamingStrategy fieldNamingStrategy)
    '''
def setExclusionStrategies():
    '''    public GsonBuilder setExclusionStrategies(final ExclusionStrategy... strategies)
    '''
def addSerializationExclusionStrategy():
    '''    public GsonBuilder addSerializationExclusionStrategy(final ExclusionStrategy strategy)
    '''
def addDeserializationExclusionStrategy():
    '''    public GsonBuilder addDeserializationExclusionStrategy(final ExclusionStrategy strategy)
    '''
def setPrettyPrinting():
    '''    public GsonBuilder setPrettyPrinting()
    '''
def disableHtmlEscaping():
    '''    public GsonBuilder disableHtmlEscaping()
    '''
def setDateFormat():
    '''    public GsonBuilder setDateFormat(final String pattern)
    public GsonBuilder setDateFormat(final int style)
    public GsonBuilder setDateFormat(final int dateStyle, final int timeStyle)
    '''
def registerTypeAdapter():
    '''    public GsonBuilder registerTypeAdapter(final Type type, final Object typeAdapter)
    '''
def registerTypeAdapterFactory():
    '''    public GsonBuilder registerTypeAdapterFactory(final TypeAdapterFactory factory)
    '''
def registerTypeHierarchyAdapter():
    '''    public GsonBuilder registerTypeHierarchyAdapter(final Class<?> baseType, final Object typeAdapter)
    '''
def serializeSpecialFloatingPointValues():
    '''    public GsonBuilder serializeSpecialFloatingPointValues()
    '''
def create():
    '''    public Gson create()
    '''
