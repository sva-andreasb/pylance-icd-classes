def ObjectMapper():
    '''    public ObjectMapper()
    public ObjectMapper(final JsonFactory jf)
    public ObjectMapper(final JsonFactory jf, final DefaultSerializerProvider sp, final DefaultDeserializationContext dc)
    '''
def copy():
    '''    public ObjectMapper copy()
    '''
def version():
    '''    public Version version()
    '''
def registerModule():
    '''    public ObjectMapper registerModule(final Module module)
    '''
def getMapperVersion():
    '''    public Version getMapperVersion()
    '''
def getOwner():
    '''    public <C extends ObjectCodec> C getOwner()
    '''
def getTypeFactory():
    '''    public TypeFactory getTypeFactory()
    public TypeFactory getTypeFactory()
    '''
def isEnabled():
    '''    public boolean isEnabled(final MapperFeature f)
    public boolean isEnabled(final DeserializationFeature f)
    public boolean isEnabled(final SerializationFeature f)
    public boolean isEnabled(final JsonFactory.Feature f)
    public boolean isEnabled(final JsonParser.Feature f)
    public boolean isEnabled(final JsonGenerator.Feature f)
    public boolean isEnabled(final MapperFeature f)
    public boolean isEnabled(final SerializationFeature f)
    public boolean isEnabled(final DeserializationFeature f)
    public boolean isEnabled(final JsonParser.Feature f)
    public boolean isEnabled(final JsonGenerator.Feature f)
    public boolean isEnabled(final JsonFactory.Feature f)
    '''
def configOverride():
    '''    public MutableConfigOverride configOverride(final Class<?> type)
    public MutableConfigOverride configOverride(final Class<?> type)
    '''
def addDeserializers():
    '''    public void addDeserializers(final Deserializers d)
    '''
def addKeyDeserializers():
    '''    public void addKeyDeserializers(final KeyDeserializers d)
    '''
def addBeanDeserializerModifier():
    '''    public void addBeanDeserializerModifier(final BeanDeserializerModifier modifier)
    '''
def addSerializers():
    '''    public void addSerializers(final Serializers s)
    '''
def addKeySerializers():
    '''    public void addKeySerializers(final Serializers s)
    '''
def addBeanSerializerModifier():
    '''    public void addBeanSerializerModifier(final BeanSerializerModifier modifier)
    '''
def addAbstractTypeResolver():
    '''    public void addAbstractTypeResolver(final AbstractTypeResolver resolver)
    '''
def addTypeModifier():
    '''    public void addTypeModifier(final TypeModifier modifier)
    '''
def addValueInstantiators():
    '''    public void addValueInstantiators(final ValueInstantiators instantiators)
    '''
def setClassIntrospector():
    '''    public void setClassIntrospector(final ClassIntrospector ci)
    '''
def insertAnnotationIntrospector():
    '''    public void insertAnnotationIntrospector(final AnnotationIntrospector ai)
    '''
def appendAnnotationIntrospector():
    '''    public void appendAnnotationIntrospector(final AnnotationIntrospector ai)
    '''
def registerSubtypes():
    '''    public void registerSubtypes(final Class<?>... subtypes)
    public void registerSubtypes(final NamedType... subtypes)
    public void registerSubtypes(final Collection<Class<?>> subtypes)
    public void registerSubtypes(final Class<?>... classes)
    public void registerSubtypes(final NamedType... types)
    public void registerSubtypes(final Collection<Class<?>> subtypes)
    '''
def setMixInAnnotations():
    '''    public void setMixInAnnotations(final Class<?> target, final Class<?> mixinSource)
    public void setMixInAnnotations(final Map<Class<?>, Class<?>> sourceMixins)
    '''
def addDeserializationProblemHandler():
    '''    public void addDeserializationProblemHandler(final DeserializationProblemHandler handler)
    '''
def setNamingStrategy():
    '''    public void setNamingStrategy(final PropertyNamingStrategy naming)
    '''
def registerModules():
    '''    public ObjectMapper registerModules(final Module... modules)
    public ObjectMapper registerModules(final Iterable<? extends Module> modules)
    '''
def getRegisteredModuleIds():
    '''    public Set<Object> getRegisteredModuleIds()
    '''
def findModules():
    '''    public static List<Module> findModules()
    public static List<Module> findModules(final ClassLoader classLoader)
    '''
def run():
    '''    public ServiceLoader<T> run()
    '''
def findAndRegisterModules():
    '''    public ObjectMapper findAndRegisterModules()
    '''
def getSerializationConfig():
    '''    public SerializationConfig getSerializationConfig()
    '''
def getDeserializationConfig():
    '''    public DeserializationConfig getDeserializationConfig()
    '''
def getDeserializationContext():
    '''    public DeserializationContext getDeserializationContext()
    '''
def setSerializerFactory():
    '''    public ObjectMapper setSerializerFactory(final SerializerFactory f)
    '''
def getSerializerFactory():
    '''    public SerializerFactory getSerializerFactory()
    '''
def setSerializerProvider():
    '''    public ObjectMapper setSerializerProvider(final DefaultSerializerProvider p)
    '''
def getSerializerProvider():
    '''    public SerializerProvider getSerializerProvider()
    '''
def getSerializerProviderInstance():
    '''    public SerializerProvider getSerializerProviderInstance()
    '''
def setMixIns():
    '''    public ObjectMapper setMixIns(final Map<Class<?>, Class<?>> sourceMixins)
    '''
def addMixIn():
    '''    public ObjectMapper addMixIn(final Class<?> target, final Class<?> mixinSource)
    '''
def setMixInResolver():
    '''    public ObjectMapper setMixInResolver(final ClassIntrospector.MixInResolver resolver)
    '''
def mixInCount():
    '''    public int mixInCount()
    '''
def addMixInAnnotations():
    '''    public final void addMixInAnnotations(final Class<?> target, final Class<?> mixinSource)
    '''
def setVisibility():
    '''    public ObjectMapper setVisibility(final VisibilityChecker<?> vc)
    public ObjectMapper setVisibility(final PropertyAccessor forMethod, final JsonAutoDetect.Visibility visibility)
    '''
def getSubtypeResolver():
    '''    public SubtypeResolver getSubtypeResolver()
    '''
def setSubtypeResolver():
    '''    public ObjectMapper setSubtypeResolver(final SubtypeResolver str)
    '''
def setAnnotationIntrospector():
    '''    public ObjectMapper setAnnotationIntrospector(final AnnotationIntrospector ai)
    '''
def setAnnotationIntrospectors():
    '''    public ObjectMapper setAnnotationIntrospectors(final AnnotationIntrospector serializerAI, final AnnotationIntrospector deserializerAI)
    '''
def setPropertyNamingStrategy():
    '''    public ObjectMapper setPropertyNamingStrategy(final PropertyNamingStrategy s)
    '''
def getPropertyNamingStrategy():
    '''    public PropertyNamingStrategy getPropertyNamingStrategy()
    '''
def setDefaultPrettyPrinter():
    '''    public ObjectMapper setDefaultPrettyPrinter(final PrettyPrinter pp)
    '''
def setVisibilityChecker():
    '''    public void setVisibilityChecker(final VisibilityChecker<?> vc)
    '''
def setSerializationInclusion():
    '''    public ObjectMapper setSerializationInclusion(final JsonInclude.Include incl)
    '''
def setPropertyInclusion():
    '''    public ObjectMapper setPropertyInclusion(final JsonInclude.Value incl)
    '''
def setDefaultPropertyInclusion():
    '''    public ObjectMapper setDefaultPropertyInclusion(final JsonInclude.Value incl)
    public ObjectMapper setDefaultPropertyInclusion(final JsonInclude.Include incl)
    '''
def setDefaultSetterInfo():
    '''    public ObjectMapper setDefaultSetterInfo(final JsonSetter.Value v)
    '''
def setDefaultVisibility():
    '''    public ObjectMapper setDefaultVisibility(final JsonAutoDetect.Value vis)
    '''
def setDefaultMergeable():
    '''    public ObjectMapper setDefaultMergeable(final Boolean b)
    '''
def enableDefaultTyping():
    '''    public ObjectMapper enableDefaultTyping()
    public ObjectMapper enableDefaultTyping(final DefaultTyping dti)
    public ObjectMapper enableDefaultTyping(final DefaultTyping applicability, final JsonTypeInfo.As includeAs)
    '''
def enableDefaultTypingAsProperty():
    '''    public ObjectMapper enableDefaultTypingAsProperty(final DefaultTyping applicability, final String propertyName)
    '''
def disableDefaultTyping():
    '''    public ObjectMapper disableDefaultTyping()
    '''
def setDefaultTyping():
    '''    public ObjectMapper setDefaultTyping(final TypeResolverBuilder<?> typer)
    '''
def setTypeFactory():
    '''    public ObjectMapper setTypeFactory(final TypeFactory f)
    '''
def constructType():
    '''    public JavaType constructType(final Type t)
    '''
def getNodeFactory():
    '''    public JsonNodeFactory getNodeFactory()
    '''
def setNodeFactory():
    '''    public ObjectMapper setNodeFactory(final JsonNodeFactory f)
    '''
def addHandler():
    '''    public ObjectMapper addHandler(final DeserializationProblemHandler h)
    '''
def clearProblemHandlers():
    '''    public ObjectMapper clearProblemHandlers()
    '''
def setConfig():
    '''    public ObjectMapper setConfig(final DeserializationConfig config)
    public ObjectMapper setConfig(final SerializationConfig config)
    '''
def setFilters():
    '''    public void setFilters(final FilterProvider filterProvider)
    '''
def setFilterProvider():
    '''    public ObjectMapper setFilterProvider(final FilterProvider filterProvider)
    '''
def setBase64Variant():
    '''    public ObjectMapper setBase64Variant(final Base64Variant v)
    '''
def getFactory():
    '''    public JsonFactory getFactory()
    '''
def getJsonFactory():
    '''    public JsonFactory getJsonFactory()
    '''
def setDateFormat():
    '''    public ObjectMapper setDateFormat(final DateFormat dateFormat)
    '''
def getDateFormat():
    '''    public DateFormat getDateFormat()
    '''
def setHandlerInstantiator():
    '''    public Object setHandlerInstantiator(final HandlerInstantiator hi)
    '''
def setInjectableValues():
    '''    public ObjectMapper setInjectableValues(final InjectableValues injectableValues)
    '''
def getInjectableValues():
    '''    public InjectableValues getInjectableValues()
    '''
def setLocale():
    '''    public ObjectMapper setLocale(final Locale l)
    '''
def setTimeZone():
    '''    public ObjectMapper setTimeZone(final TimeZone tz)
    '''
def configure():
    '''    public ObjectMapper configure(final MapperFeature f, final boolean state)
    public ObjectMapper configure(final SerializationFeature f, final boolean state)
    public ObjectMapper configure(final DeserializationFeature f, final boolean state)
    public ObjectMapper configure(final JsonParser.Feature f, final boolean state)
    public ObjectMapper configure(final JsonGenerator.Feature f, final boolean state)
    '''
def enable():
    '''    public ObjectMapper enable(final MapperFeature... f)
    public ObjectMapper enable(final SerializationFeature f)
    public ObjectMapper enable(final SerializationFeature first, final SerializationFeature... f)
    public ObjectMapper enable(final DeserializationFeature feature)
    public ObjectMapper enable(final DeserializationFeature first, final DeserializationFeature... f)
    public ObjectMapper enable(final JsonParser.Feature... features)
    public ObjectMapper enable(final JsonGenerator.Feature... features)
    '''
def disable():
    '''    public ObjectMapper disable(final MapperFeature... f)
    public ObjectMapper disable(final SerializationFeature f)
    public ObjectMapper disable(final SerializationFeature first, final SerializationFeature... f)
    public ObjectMapper disable(final DeserializationFeature feature)
    public ObjectMapper disable(final DeserializationFeature first, final DeserializationFeature... f)
    public ObjectMapper disable(final JsonParser.Feature... features)
    public ObjectMapper disable(final JsonGenerator.Feature... features)
    '''
def readValue():
    '''    public <T> T readValue(final JsonParser p, final Class<T> valueType)
    public <T> T readValue(final JsonParser p, final TypeReference<?> valueTypeRef)
    public final <T> T readValue(final JsonParser p, final ResolvedType valueType)
    public <T> T readValue(final JsonParser p, final JavaType valueType)
    public <T> T readValue(final File src, final Class<T> valueType)
    public <T> T readValue(final File src, final TypeReference valueTypeRef)
    public <T> T readValue(final File src, final JavaType valueType)
    public <T> T readValue(final URL src, final Class<T> valueType)
    public <T> T readValue(final URL src, final TypeReference valueTypeRef)
    public <T> T readValue(final URL src, final JavaType valueType)
    public <T> T readValue(final String content, final Class<T> valueType)
    public <T> T readValue(final String content, final TypeReference valueTypeRef)
    public <T> T readValue(final String content, final JavaType valueType)
    public <T> T readValue(final Reader src, final Class<T> valueType)
    public <T> T readValue(final Reader src, final TypeReference valueTypeRef)
    public <T> T readValue(final Reader src, final JavaType valueType)
    public <T> T readValue(final InputStream src, final Class<T> valueType)
    public <T> T readValue(final InputStream src, final TypeReference valueTypeRef)
    public <T> T readValue(final InputStream src, final JavaType valueType)
    public <T> T readValue(final byte[] src, final Class<T> valueType)
    public <T> T readValue(final byte[] src, final int offset, final int len, final Class<T> valueType)
    public <T> T readValue(final byte[] src, final TypeReference valueTypeRef)
    public <T> T readValue(final byte[] src, final int offset, final int len, final TypeReference valueTypeRef)
    public <T> T readValue(final byte[] src, final JavaType valueType)
    public <T> T readValue(final byte[] src, final int offset, final int len, final JavaType valueType)
    public <T> T readValue(final DataInput src, final Class<T> valueType)
    public <T> T readValue(final DataInput src, final JavaType valueType)
    '''
def readTree():
    '''    public <T extends TreeNode> T readTree(final JsonParser p)
    public JsonNode readTree(final InputStream in)
    public JsonNode readTree(final Reader r)
    public JsonNode readTree(final String content)
    public JsonNode readTree(final byte[] content)
    public JsonNode readTree(final File file)
    public JsonNode readTree(final URL source)
    '''
def readValues():
    '''    public <T> MappingIterator<T> readValues(final JsonParser p, final ResolvedType valueType)
    public <T> MappingIterator<T> readValues(final JsonParser p, final JavaType valueType)
    public <T> MappingIterator<T> readValues(final JsonParser p, final Class<T> valueType)
    public <T> MappingIterator<T> readValues(final JsonParser p, final TypeReference<?> valueTypeRef)
    '''
def writeValue():
    '''    public void writeValue(final JsonGenerator g, final Object value)
    public void writeValue(final File resultFile, final Object value)
    public void writeValue(final OutputStream out, final Object value)
    public void writeValue(final DataOutput out, final Object value)
    public void writeValue(final Writer w, final Object value)
    '''
def writeTree():
    '''    public void writeTree(final JsonGenerator jgen, final TreeNode rootNode)
    public void writeTree(final JsonGenerator jgen, final JsonNode rootNode)
    '''
def createObjectNode():
    '''    public ObjectNode createObjectNode()
    '''
def createArrayNode():
    '''    public ArrayNode createArrayNode()
    '''
def treeAsTokens():
    '''    public JsonParser treeAsTokens(final TreeNode n)
    '''
def treeToValue():
    '''    public <T> T treeToValue(final TreeNode n, final Class<T> valueType)
    '''
def valueToTree():
    '''    public <T extends JsonNode> T valueToTree(final Object fromValue)
    '''
def canSerialize():
    '''    public boolean canSerialize(final Class<?> type)
    public boolean canSerialize(final Class<?> type, final AtomicReference<Throwable> cause)
    '''
def canDeserialize():
    '''    public boolean canDeserialize(final JavaType type)
    public boolean canDeserialize(final JavaType type, final AtomicReference<Throwable> cause)
    '''
def writeValueAsString():
    '''    public String writeValueAsString(final Object value)
    '''
def writeValueAsBytes():
    '''    public byte[] writeValueAsBytes(final Object value)
    '''
def writer():
    '''    public ObjectWriter writer()
    public ObjectWriter writer(final SerializationFeature feature)
    public ObjectWriter writer(final SerializationFeature first, final SerializationFeature... other)
    public ObjectWriter writer(final DateFormat df)
    public ObjectWriter writer(PrettyPrinter pp)
    public ObjectWriter writer(final FilterProvider filterProvider)
    public ObjectWriter writer(final FormatSchema schema)
    public ObjectWriter writer(final Base64Variant defaultBase64)
    public ObjectWriter writer(final CharacterEscapes escapes)
    public ObjectWriter writer(final ContextAttributes attrs)
    '''
def writerWithView():
    '''    public ObjectWriter writerWithView(final Class<?> serializationView)
    '''
def writerFor():
    '''    public ObjectWriter writerFor(final Class<?> rootType)
    public ObjectWriter writerFor(final TypeReference<?> rootType)
    public ObjectWriter writerFor(final JavaType rootType)
    '''
def writerWithDefaultPrettyPrinter():
    '''    public ObjectWriter writerWithDefaultPrettyPrinter()
    '''
def writerWithType():
    '''    public ObjectWriter writerWithType(final Class<?> rootType)
    public ObjectWriter writerWithType(final TypeReference<?> rootType)
    public ObjectWriter writerWithType(final JavaType rootType)
    '''
def reader():
    '''    public ObjectReader reader()
    public ObjectReader reader(final DeserializationFeature feature)
    public ObjectReader reader(final DeserializationFeature first, final DeserializationFeature... other)
    public ObjectReader reader(final JsonNodeFactory f)
    public ObjectReader reader(final FormatSchema schema)
    public ObjectReader reader(final InjectableValues injectableValues)
    public ObjectReader reader(final Base64Variant defaultBase64)
    public ObjectReader reader(final ContextAttributes attrs)
    public ObjectReader reader(final JavaType type)
    public ObjectReader reader(final Class<?> type)
    public ObjectReader reader(final TypeReference<?> type)
    '''
def readerForUpdating():
    '''    public ObjectReader readerForUpdating(final Object valueToUpdate)
    '''
def readerFor():
    '''    public ObjectReader readerFor(final JavaType type)
    public ObjectReader readerFor(final Class<?> type)
    public ObjectReader readerFor(final TypeReference<?> type)
    '''
def readerWithView():
    '''    public ObjectReader readerWithView(final Class<?> view)
    '''
def convertValue():
    '''    public <T> T convertValue(final Object fromValue, final Class<T> toValueType)
    public <T> T convertValue(final Object fromValue, final TypeReference<?> toValueTypeRef)
    public <T> T convertValue(final Object fromValue, final JavaType toValueType)
    '''
def updateValue():
    '''    public <T> T updateValue(final T valueToUpdate, final Object overrides)
    '''
def generateJsonSchema():
    '''    public JsonSchema generateJsonSchema(final Class<?> t)
    '''
def acceptJsonFormatVisitor():
    '''    public void acceptJsonFormatVisitor(final Class<?> type, final JsonFormatVisitorWrapper visitor)
    public void acceptJsonFormatVisitor(final JavaType type, final JsonFormatVisitorWrapper visitor)
    '''
def DefaultTypeResolverBuilder():
    '''    public DefaultTypeResolverBuilder(final DefaultTyping t)
    '''
def buildTypeDeserializer():
    '''    public TypeDeserializer buildTypeDeserializer(final DeserializationConfig config, final JavaType baseType, final Collection<NamedType> subtypes)
    '''
def buildTypeSerializer():
    '''    public TypeSerializer buildTypeSerializer(final SerializationConfig config, final JavaType baseType, final Collection<NamedType> subtypes)
    '''
def useForType():
    '''    public boolean useForType(JavaType t)
    '''
