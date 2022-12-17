def ():
    '''returns DefaultTypeResolverBuilder\n\n
    ()\n
    (final JsonFactory jf)\n
    (final JsonFactory jf, final DefaultSerializerProvider sp, final DefaultDeserializationContext dc)\n
    (final DefaultTyping t)\n
    '''
def copy():
    '''returns ObjectMapper\n\n
    copy()\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def registerModule():
    '''returns ObjectMapper\n\n
    registerModule(final Module module)\n
    '''
def getMapperVersion():
    '''returns Version\n\n
    getMapperVersion()\n
    '''
def getTypeFactory():
    '''returns TypeFactory\n\n
    getTypeFactory()\n
    getTypeFactory()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final MapperFeature f)\n
    isEnabled(final DeserializationFeature f)\n
    isEnabled(final SerializationFeature f)\n
    isEnabled(final JsonFactory.Feature f)\n
    isEnabled(final JsonParser.Feature f)\n
    isEnabled(final JsonGenerator.Feature f)\n
    isEnabled(final MapperFeature f)\n
    isEnabled(final SerializationFeature f)\n
    isEnabled(final DeserializationFeature f)\n
    isEnabled(final JsonParser.Feature f)\n
    isEnabled(final JsonGenerator.Feature f)\n
    isEnabled(final JsonFactory.Feature f)\n
    '''
def configOverride():
    '''returns MutableConfigOverride\n\n
    configOverride(final Class<?> type)\n
    configOverride(final Class<?> type)\n
    '''
def addDeserializers():
    '''returns None\n\n
    addDeserializers(final Deserializers d)\n
    '''
def addKeyDeserializers():
    '''returns None\n\n
    addKeyDeserializers(final KeyDeserializers d)\n
    '''
def addBeanDeserializerModifier():
    '''returns None\n\n
    addBeanDeserializerModifier(final BeanDeserializerModifier modifier)\n
    '''
def addSerializers():
    '''returns None\n\n
    addSerializers(final Serializers s)\n
    '''
def addKeySerializers():
    '''returns None\n\n
    addKeySerializers(final Serializers s)\n
    '''
def addBeanSerializerModifier():
    '''returns None\n\n
    addBeanSerializerModifier(final BeanSerializerModifier modifier)\n
    '''
def addAbstractTypeResolver():
    '''returns None\n\n
    addAbstractTypeResolver(final AbstractTypeResolver resolver)\n
    '''
def addTypeModifier():
    '''returns None\n\n
    addTypeModifier(final TypeModifier modifier)\n
    '''
def addValueInstantiators():
    '''returns None\n\n
    addValueInstantiators(final ValueInstantiators instantiators)\n
    '''
def setClassIntrospector():
    '''returns None\n\n
    setClassIntrospector(final ClassIntrospector ci)\n
    '''
def insertAnnotationIntrospector():
    '''returns None\n\n
    insertAnnotationIntrospector(final AnnotationIntrospector ai)\n
    '''
def appendAnnotationIntrospector():
    '''returns None\n\n
    appendAnnotationIntrospector(final AnnotationIntrospector ai)\n
    '''
def registerSubtypes():
    '''returns None\n\n
    registerSubtypes(final Class<?>... subtypes)\n
    registerSubtypes(final NamedType... subtypes)\n
    registerSubtypes(final Collection<Class<?>> subtypes)\n
    registerSubtypes(final Class<?>... classes)\n
    registerSubtypes(final NamedType... types)\n
    registerSubtypes(final Collection<Class<?>> subtypes)\n
    '''
def setMixInAnnotations():
    '''returns None\n\n
    setMixInAnnotations(final Class<?> target, final Class<?> mixinSource)\n
    setMixInAnnotations(final Map<Class<?>, Class<?>> sourceMixins)\n
    '''
def addDeserializationProblemHandler():
    '''returns None\n\n
    addDeserializationProblemHandler(final DeserializationProblemHandler handler)\n
    '''
def setNamingStrategy():
    '''returns None\n\n
    setNamingStrategy(final PropertyNamingStrategy naming)\n
    '''
def registerModules():
    '''returns ObjectMapper\n\n
    registerModules(final Module... modules)\n
    registerModules(final Iterable<? extends Module> modules)\n
    '''
def getRegisteredModuleIds():
    '''returns Set<Object>\n\n
    getRegisteredModuleIds()\n
    '''
def run():
    '''returns ServiceLoader<T>\n\n
    run()\n
    '''
def findAndRegisterModules():
    '''returns ObjectMapper\n\n
    findAndRegisterModules()\n
    '''
def getSerializationConfig():
    '''returns SerializationConfig\n\n
    getSerializationConfig()\n
    '''
def getDeserializationConfig():
    '''returns DeserializationConfig\n\n
    getDeserializationConfig()\n
    '''
def getDeserializationContext():
    '''returns DeserializationContext\n\n
    getDeserializationContext()\n
    '''
def setSerializerFactory():
    '''returns ObjectMapper\n\n
    setSerializerFactory(final SerializerFactory f)\n
    '''
def getSerializerFactory():
    '''returns SerializerFactory\n\n
    getSerializerFactory()\n
    '''
def setSerializerProvider():
    '''returns ObjectMapper\n\n
    setSerializerProvider(final DefaultSerializerProvider p)\n
    '''
def getSerializerProvider():
    '''returns SerializerProvider\n\n
    getSerializerProvider()\n
    '''
def getSerializerProviderInstance():
    '''returns SerializerProvider\n\n
    getSerializerProviderInstance()\n
    '''
def setMixIns():
    '''returns ObjectMapper\n\n
    setMixIns(final Map<Class<?>, Class<?>> sourceMixins)\n
    '''
def addMixIn():
    '''returns ObjectMapper\n\n
    addMixIn(final Class<?> target, final Class<?> mixinSource)\n
    '''
def setMixInResolver():
    '''returns ObjectMapper\n\n
    setMixInResolver(final ClassIntrospector.MixInResolver resolver)\n
    '''
def mixInCount():
    '''returns int\n\n
    mixInCount()\n
    '''
def setVisibility():
    '''returns ObjectMapper\n\n
    setVisibility(final VisibilityChecker<?> vc)\n
    setVisibility(final PropertyAccessor forMethod, final JsonAutoDetect.Visibility visibility)\n
    '''
def getSubtypeResolver():
    '''returns SubtypeResolver\n\n
    getSubtypeResolver()\n
    '''
def setSubtypeResolver():
    '''returns ObjectMapper\n\n
    setSubtypeResolver(final SubtypeResolver str)\n
    '''
def setAnnotationIntrospector():
    '''returns ObjectMapper\n\n
    setAnnotationIntrospector(final AnnotationIntrospector ai)\n
    '''
def setAnnotationIntrospectors():
    '''returns ObjectMapper\n\n
    setAnnotationIntrospectors(final AnnotationIntrospector serializerAI, final AnnotationIntrospector deserializerAI)\n
    '''
def setPropertyNamingStrategy():
    '''returns ObjectMapper\n\n
    setPropertyNamingStrategy(final PropertyNamingStrategy s)\n
    '''
def getPropertyNamingStrategy():
    '''returns PropertyNamingStrategy\n\n
    getPropertyNamingStrategy()\n
    '''
def setDefaultPrettyPrinter():
    '''returns ObjectMapper\n\n
    setDefaultPrettyPrinter(final PrettyPrinter pp)\n
    '''
def setVisibilityChecker():
    '''returns None\n\n
    setVisibilityChecker(final VisibilityChecker<?> vc)\n
    '''
def setSerializationInclusion():
    '''returns ObjectMapper\n\n
    setSerializationInclusion(final JsonInclude.Include incl)\n
    '''
def setPropertyInclusion():
    '''returns ObjectMapper\n\n
    setPropertyInclusion(final JsonInclude.Value incl)\n
    '''
def setDefaultPropertyInclusion():
    '''returns ObjectMapper\n\n
    setDefaultPropertyInclusion(final JsonInclude.Value incl)\n
    setDefaultPropertyInclusion(final JsonInclude.Include incl)\n
    '''
def setDefaultSetterInfo():
    '''returns ObjectMapper\n\n
    setDefaultSetterInfo(final JsonSetter.Value v)\n
    '''
def setDefaultVisibility():
    '''returns ObjectMapper\n\n
    setDefaultVisibility(final JsonAutoDetect.Value vis)\n
    '''
def setDefaultMergeable():
    '''returns ObjectMapper\n\n
    setDefaultMergeable(final Boolean b)\n
    '''
def enableDefaultTyping():
    '''returns ObjectMapper\n\n
    enableDefaultTyping()\n
    enableDefaultTyping(final DefaultTyping dti)\n
    enableDefaultTyping(final DefaultTyping applicability, final JsonTypeInfo.As includeAs)\n
    '''
def enableDefaultTypingAsProperty():
    '''returns ObjectMapper\n\n
    enableDefaultTypingAsProperty(final DefaultTyping applicability, final String propertyName)\n
    '''
def disableDefaultTyping():
    '''returns ObjectMapper\n\n
    disableDefaultTyping()\n
    '''
def setDefaultTyping():
    '''returns ObjectMapper\n\n
    setDefaultTyping(final TypeResolverBuilder<?> typer)\n
    '''
def setTypeFactory():
    '''returns ObjectMapper\n\n
    setTypeFactory(final TypeFactory f)\n
    '''
def constructType():
    '''returns JavaType\n\n
    constructType(final Type t)\n
    '''
def getNodeFactory():
    '''returns JsonNodeFactory\n\n
    getNodeFactory()\n
    '''
def setNodeFactory():
    '''returns ObjectMapper\n\n
    setNodeFactory(final JsonNodeFactory f)\n
    '''
def addHandler():
    '''returns ObjectMapper\n\n
    addHandler(final DeserializationProblemHandler h)\n
    '''
def clearProblemHandlers():
    '''returns ObjectMapper\n\n
    clearProblemHandlers()\n
    '''
def setConfig():
    '''returns ObjectMapper\n\n
    setConfig(final DeserializationConfig config)\n
    setConfig(final SerializationConfig config)\n
    '''
def setFilters():
    '''returns None\n\n
    setFilters(final FilterProvider filterProvider)\n
    '''
def setFilterProvider():
    '''returns ObjectMapper\n\n
    setFilterProvider(final FilterProvider filterProvider)\n
    '''
def setBase64Variant():
    '''returns ObjectMapper\n\n
    setBase64Variant(final Base64Variant v)\n
    '''
def getFactory():
    '''returns JsonFactory\n\n
    getFactory()\n
    '''
def getJsonFactory():
    '''returns JsonFactory\n\n
    getJsonFactory()\n
    '''
def setDateFormat():
    '''returns ObjectMapper\n\n
    setDateFormat(final DateFormat dateFormat)\n
    '''
def getDateFormat():
    '''returns DateFormat\n\n
    getDateFormat()\n
    '''
def setHandlerInstantiator():
    '''returns Object\n\n
    setHandlerInstantiator(final HandlerInstantiator hi)\n
    '''
def setInjectableValues():
    '''returns ObjectMapper\n\n
    setInjectableValues(final InjectableValues injectableValues)\n
    '''
def getInjectableValues():
    '''returns InjectableValues\n\n
    getInjectableValues()\n
    '''
def setLocale():
    '''returns ObjectMapper\n\n
    setLocale(final Locale l)\n
    '''
def setTimeZone():
    '''returns ObjectMapper\n\n
    setTimeZone(final TimeZone tz)\n
    '''
def configure():
    '''returns ObjectMapper\n\n
    configure(final MapperFeature f, final boolean state)\n
    configure(final SerializationFeature f, final boolean state)\n
    configure(final DeserializationFeature f, final boolean state)\n
    configure(final JsonParser.Feature f, final boolean state)\n
    configure(final JsonGenerator.Feature f, final boolean state)\n
    '''
def enable():
    '''returns ObjectMapper\n\n
    enable(final MapperFeature... f)\n
    enable(final SerializationFeature f)\n
    enable(final SerializationFeature first, final SerializationFeature... f)\n
    enable(final DeserializationFeature feature)\n
    enable(final DeserializationFeature first, final DeserializationFeature... f)\n
    enable(final JsonParser.Feature... features)\n
    enable(final JsonGenerator.Feature... features)\n
    '''
def disable():
    '''returns ObjectMapper\n\n
    disable(final MapperFeature... f)\n
    disable(final SerializationFeature f)\n
    disable(final SerializationFeature first, final SerializationFeature... f)\n
    disable(final DeserializationFeature feature)\n
    disable(final DeserializationFeature first, final DeserializationFeature... f)\n
    disable(final JsonParser.Feature... features)\n
    disable(final JsonGenerator.Feature... features)\n
    '''
def readTree():
    '''returns JsonNode\n\n
    readTree(final InputStream in)\n
    readTree(final Reader r)\n
    readTree(final String content)\n
    readTree(final byte[] content)\n
    readTree(final File file)\n
    readTree(final URL source)\n
    '''
def writeValue():
    '''returns None\n\n
    writeValue(final JsonGenerator g, final Object value)\n
    writeValue(final File resultFile, final Object value)\n
    writeValue(final OutputStream out, final Object value)\n
    writeValue(final DataOutput out, final Object value)\n
    writeValue(final Writer w, final Object value)\n
    '''
def writeTree():
    '''returns None\n\n
    writeTree(final JsonGenerator jgen, final TreeNode rootNode)\n
    writeTree(final JsonGenerator jgen, final JsonNode rootNode)\n
    '''
def createObjectNode():
    '''returns ObjectNode\n\n
    createObjectNode()\n
    '''
def createArrayNode():
    '''returns ArrayNode\n\n
    createArrayNode()\n
    '''
def treeAsTokens():
    '''returns JsonParser\n\n
    treeAsTokens(final TreeNode n)\n
    '''
def canSerialize():
    '''returns boolean\n\n
    canSerialize(final Class<?> type)\n
    canSerialize(final Class<?> type, final AtomicReference<Throwable> cause)\n
    '''
def canDeserialize():
    '''returns boolean\n\n
    canDeserialize(final JavaType type)\n
    canDeserialize(final JavaType type, final AtomicReference<Throwable> cause)\n
    '''
def writeValueAsString():
    '''returns String\n\n
    writeValueAsString(final Object value)\n
    '''
def writeValueAsBytes():
    '''returns byte[]\n\n
    writeValueAsBytes(final Object value)\n
    '''
def writer():
    '''returns ObjectWriter\n\n
    writer()\n
    writer(final SerializationFeature feature)\n
    writer(final SerializationFeature first, final SerializationFeature... other)\n
    writer(final DateFormat df)\n
    writer(PrettyPrinter pp)\n
    writer(final FilterProvider filterProvider)\n
    writer(final FormatSchema schema)\n
    writer(final Base64Variant defaultBase64)\n
    writer(final CharacterEscapes escapes)\n
    writer(final ContextAttributes attrs)\n
    '''
def writerWithView():
    '''returns ObjectWriter\n\n
    writerWithView(final Class<?> serializationView)\n
    '''
def writerFor():
    '''returns ObjectWriter\n\n
    writerFor(final Class<?> rootType)\n
    writerFor(final TypeReference<?> rootType)\n
    writerFor(final JavaType rootType)\n
    '''
def writerWithDefaultPrettyPrinter():
    '''returns ObjectWriter\n\n
    writerWithDefaultPrettyPrinter()\n
    '''
def writerWithType():
    '''returns ObjectWriter\n\n
    writerWithType(final Class<?> rootType)\n
    writerWithType(final TypeReference<?> rootType)\n
    writerWithType(final JavaType rootType)\n
    '''
def reader():
    '''returns ObjectReader\n\n
    reader()\n
    reader(final DeserializationFeature feature)\n
    reader(final DeserializationFeature first, final DeserializationFeature... other)\n
    reader(final JsonNodeFactory f)\n
    reader(final FormatSchema schema)\n
    reader(final InjectableValues injectableValues)\n
    reader(final Base64Variant defaultBase64)\n
    reader(final ContextAttributes attrs)\n
    reader(final JavaType type)\n
    reader(final Class<?> type)\n
    reader(final TypeReference<?> type)\n
    '''
def readerForUpdating():
    '''returns ObjectReader\n\n
    readerForUpdating(final Object valueToUpdate)\n
    '''
def readerFor():
    '''returns ObjectReader\n\n
    readerFor(final JavaType type)\n
    readerFor(final Class<?> type)\n
    readerFor(final TypeReference<?> type)\n
    '''
def readerWithView():
    '''returns ObjectReader\n\n
    readerWithView(final Class<?> view)\n
    '''
def generateJsonSchema():
    '''returns JsonSchema\n\n
    generateJsonSchema(final Class<?> t)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final Class<?> type, final JsonFormatVisitorWrapper visitor)\n
    acceptJsonFormatVisitor(final JavaType type, final JsonFormatVisitorWrapper visitor)\n
    '''
def buildTypeDeserializer():
    '''returns TypeDeserializer\n\n
    buildTypeDeserializer(final DeserializationConfig config, final JavaType baseType, final Collection<NamedType> subtypes)\n
    '''
def buildTypeSerializer():
    '''returns TypeSerializer\n\n
    buildTypeSerializer(final SerializationConfig config, final JavaType baseType, final Collection<NamedType> subtypes)\n
    '''
def useForType():
    '''returns boolean\n\n
    useForType(JavaType t)\n
    '''
