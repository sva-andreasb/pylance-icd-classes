def ():
    '''returns GsonBuilder\n\n
    ()\n
    '''
def setVersion():
    '''returns GsonBuilder\n\n
    setVersion(final double ignoreVersionsAfter)\n
    '''
def excludeFieldsWithModifiers():
    '''returns GsonBuilder\n\n
    excludeFieldsWithModifiers(final int... modifiers)\n
    '''
def generateNonExecutableJson():
    '''returns GsonBuilder\n\n
    generateNonExecutableJson()\n
    '''
def excludeFieldsWithoutExposeAnnotation():
    '''returns GsonBuilder\n\n
    excludeFieldsWithoutExposeAnnotation()\n
    '''
def serializeNulls():
    '''returns GsonBuilder\n\n
    serializeNulls()\n
    '''
def enableComplexMapKeySerialization():
    '''returns GsonBuilder\n\n
    enableComplexMapKeySerialization()\n
    '''
def disableInnerClassSerialization():
    '''returns GsonBuilder\n\n
    disableInnerClassSerialization()\n
    '''
def setLongSerializationPolicy():
    '''returns GsonBuilder\n\n
    setLongSerializationPolicy(final LongSerializationPolicy serializationPolicy)\n
    '''
def setFieldNamingPolicy():
    '''returns GsonBuilder\n\n
    setFieldNamingPolicy(final FieldNamingPolicy namingConvention)\n
    '''
def setFieldNamingStrategy():
    '''returns GsonBuilder\n\n
    setFieldNamingStrategy(final FieldNamingStrategy fieldNamingStrategy)\n
    '''
def setExclusionStrategies():
    '''returns GsonBuilder\n\n
    setExclusionStrategies(final ExclusionStrategy... strategies)\n
    '''
def addSerializationExclusionStrategy():
    '''returns GsonBuilder\n\n
    addSerializationExclusionStrategy(final ExclusionStrategy strategy)\n
    '''
def addDeserializationExclusionStrategy():
    '''returns GsonBuilder\n\n
    addDeserializationExclusionStrategy(final ExclusionStrategy strategy)\n
    '''
def setPrettyPrinting():
    '''returns GsonBuilder\n\n
    setPrettyPrinting()\n
    '''
def disableHtmlEscaping():
    '''returns GsonBuilder\n\n
    disableHtmlEscaping()\n
    '''
def setDateFormat():
    '''returns GsonBuilder\n\n
    setDateFormat(final String pattern)\n
    setDateFormat(final int style)\n
    setDateFormat(final int dateStyle, final int timeStyle)\n
    '''
def registerTypeAdapter():
    '''returns GsonBuilder\n\n
    registerTypeAdapter(final Type type, final Object typeAdapter)\n
    '''
def registerTypeAdapterFactory():
    '''returns GsonBuilder\n\n
    registerTypeAdapterFactory(final TypeAdapterFactory factory)\n
    '''
def registerTypeHierarchyAdapter():
    '''returns GsonBuilder\n\n
    registerTypeHierarchyAdapter(final Class<?> baseType, final Object typeAdapter)\n
    '''
def serializeSpecialFloatingPointValues():
    '''returns GsonBuilder\n\n
    serializeSpecialFloatingPointValues()\n
    '''
def create():
    '''returns Gson\n\n
    create()\n
    '''
