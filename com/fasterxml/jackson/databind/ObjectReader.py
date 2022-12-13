def version():
    '''    public Version version()
    '''
def with():
    '''    public ObjectReader with(final DeserializationFeature feature)
    public ObjectReader with(final DeserializationFeature first, final DeserializationFeature... other)
    public ObjectReader with(final JsonParser.Feature feature)
    public ObjectReader with(final FormatFeature feature)
    public ObjectReader with(final DeserializationConfig config)
    public ObjectReader with(final InjectableValues injectableValues)
    public ObjectReader with(final JsonNodeFactory f)
    public ObjectReader with(final JsonFactory f)
    public ObjectReader with(final FormatSchema schema)
    public ObjectReader with(final Locale l)
    public ObjectReader with(final TimeZone tz)
    public ObjectReader with(final Base64Variant defaultBase64)
    public ObjectReader with(final ContextAttributes attrs)
    '''
def withFeatures():
    '''    public ObjectReader withFeatures(final DeserializationFeature... features)
    public ObjectReader withFeatures(final JsonParser.Feature... features)
    public ObjectReader withFeatures(final FormatFeature... features)
    '''
def without():
    '''    public ObjectReader without(final DeserializationFeature feature)
    public ObjectReader without(final DeserializationFeature first, final DeserializationFeature... other)
    public ObjectReader without(final JsonParser.Feature feature)
    public ObjectReader without(final FormatFeature feature)
    '''
def withoutFeatures():
    '''    public ObjectReader withoutFeatures(final DeserializationFeature... features)
    public ObjectReader withoutFeatures(final JsonParser.Feature... features)
    public ObjectReader withoutFeatures(final FormatFeature... features)
    '''
def at():
    '''    public ObjectReader at(final String value)
    public ObjectReader at(final JsonPointer pointer)
    '''
def withRootName():
    '''    public ObjectReader withRootName(final String rootName)
    public ObjectReader withRootName(final PropertyName rootName)
    '''
def withoutRootName():
    '''    public ObjectReader withoutRootName()
    '''
def forType():
    '''    public ObjectReader forType(final JavaType valueType)
    public ObjectReader forType(final Class<?> valueType)
    public ObjectReader forType(final TypeReference<?> valueTypeRef)
    '''
def withType():
    '''    public ObjectReader withType(final JavaType valueType)
    public ObjectReader withType(final Class<?> valueType)
    public ObjectReader withType(final Type valueType)
    public ObjectReader withType(final TypeReference<?> valueTypeRef)
    '''
def withValueToUpdate():
    '''    public ObjectReader withValueToUpdate(final Object value)
    '''
def withView():
    '''    public ObjectReader withView(final Class<?> activeView)
    '''
def withHandler():
    '''    public ObjectReader withHandler(final DeserializationProblemHandler h)
    '''
def withFormatDetection():
    '''    public ObjectReader withFormatDetection(final ObjectReader... readers)
    public ObjectReader withFormatDetection(final DataFormatReaders readers)
    '''
def withAttributes():
    '''    public ObjectReader withAttributes(final Map<?, ?> attrs)
    '''
def withAttribute():
    '''    public ObjectReader withAttribute(final Object key, final Object value)
    '''
def withoutAttribute():
    '''    public ObjectReader withoutAttribute(final Object key)
    '''
def isEnabled():
    '''    public boolean isEnabled(final DeserializationFeature f)
    public boolean isEnabled(final MapperFeature f)
    public boolean isEnabled(final JsonParser.Feature f)
    '''
def getConfig():
    '''    public DeserializationConfig getConfig()
    '''
def getFactory():
    '''    public JsonFactory getFactory()
    '''
def getTypeFactory():
    '''    public TypeFactory getTypeFactory()
    '''
def getAttributes():
    '''    public ContextAttributes getAttributes()
    '''
def getInjectableValues():
    '''    public InjectableValues getInjectableValues()
    '''
def readValue():
    '''    public <T> T readValue(final JsonParser p)
    public <T> T readValue(final JsonParser p, final Class<T> valueType)
    public <T> T readValue(final JsonParser p, final TypeReference<?> valueTypeRef)
    public <T> T readValue(final JsonParser p, final ResolvedType valueType)
    public <T> T readValue(final JsonParser p, final JavaType valueType)
    public <T> T readValue(final InputStream src)
    public <T> T readValue(final Reader src)
    public <T> T readValue(final String src)
    public <T> T readValue(final byte[] src)
    public <T> T readValue(final byte[] src, final int offset, final int length)
    public <T> T readValue(final File src)
    public <T> T readValue(final URL src)
    public <T> T readValue(final JsonNode src)
    public <T> T readValue(final DataInput src)
    '''
def readValues():
    '''    public <T> Iterator<T> readValues(final JsonParser p, final Class<T> valueType)
    public <T> Iterator<T> readValues(final JsonParser p, final TypeReference<?> valueTypeRef)
    public <T> Iterator<T> readValues(final JsonParser p, final ResolvedType valueType)
    public <T> Iterator<T> readValues(final JsonParser p, final JavaType valueType)
    public <T> MappingIterator<T> readValues(final JsonParser p)
    public <T> MappingIterator<T> readValues(final InputStream src)
    public <T> MappingIterator<T> readValues(final Reader src)
    public <T> MappingIterator<T> readValues(final String json)
    public <T> MappingIterator<T> readValues(final byte[] src, final int offset, final int length)
    public final <T> MappingIterator<T> readValues(final byte[] src)
    public <T> MappingIterator<T> readValues(final File src)
    public <T> MappingIterator<T> readValues(final URL src)
    public <T> MappingIterator<T> readValues(final DataInput src)
    '''
def createArrayNode():
    '''    public JsonNode createArrayNode()
    '''
def createObjectNode():
    '''    public JsonNode createObjectNode()
    '''
def treeAsTokens():
    '''    public JsonParser treeAsTokens(final TreeNode n)
    '''
def readTree():
    '''    public <T extends TreeNode> T readTree(final JsonParser p)
    public JsonNode readTree(final InputStream in)
    public JsonNode readTree(final Reader r)
    public JsonNode readTree(final String json)
    public JsonNode readTree(final DataInput src)
    '''
def writeTree():
    '''    public void writeTree(final JsonGenerator g, final TreeNode rootNode)
    '''
def treeToValue():
    '''    public <T> T treeToValue(final TreeNode n, final Class<T> valueType)
    '''
def writeValue():
    '''    public void writeValue(final JsonGenerator gen, final Object value)
    '''
