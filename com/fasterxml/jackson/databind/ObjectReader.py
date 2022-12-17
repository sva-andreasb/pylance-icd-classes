def version():
    '''returns Version\n\n
    version()\n
    '''
def with():
    '''returns ObjectReader\n\n
    with(final DeserializationFeature feature)\n
    with(final DeserializationFeature first, final DeserializationFeature... other)\n
    with(final JsonParser.Feature feature)\n
    with(final FormatFeature feature)\n
    with(final DeserializationConfig config)\n
    with(final InjectableValues injectableValues)\n
    with(final JsonNodeFactory f)\n
    with(final JsonFactory f)\n
    with(final FormatSchema schema)\n
    with(final Locale l)\n
    with(final TimeZone tz)\n
    with(final Base64Variant defaultBase64)\n
    with(final ContextAttributes attrs)\n
    '''
def withFeatures():
    '''returns ObjectReader\n\n
    withFeatures(final DeserializationFeature... features)\n
    withFeatures(final JsonParser.Feature... features)\n
    withFeatures(final FormatFeature... features)\n
    '''
def without():
    '''returns ObjectReader\n\n
    without(final DeserializationFeature feature)\n
    without(final DeserializationFeature first, final DeserializationFeature... other)\n
    without(final JsonParser.Feature feature)\n
    without(final FormatFeature feature)\n
    '''
def withoutFeatures():
    '''returns ObjectReader\n\n
    withoutFeatures(final DeserializationFeature... features)\n
    withoutFeatures(final JsonParser.Feature... features)\n
    withoutFeatures(final FormatFeature... features)\n
    '''
def at():
    '''returns ObjectReader\n\n
    at(final String value)\n
    at(final JsonPointer pointer)\n
    '''
def withRootName():
    '''returns ObjectReader\n\n
    withRootName(final String rootName)\n
    withRootName(final PropertyName rootName)\n
    '''
def withoutRootName():
    '''returns ObjectReader\n\n
    withoutRootName()\n
    '''
def forType():
    '''returns ObjectReader\n\n
    forType(final JavaType valueType)\n
    forType(final Class<?> valueType)\n
    forType(final TypeReference<?> valueTypeRef)\n
    '''
def withType():
    '''returns ObjectReader\n\n
    withType(final JavaType valueType)\n
    withType(final Class<?> valueType)\n
    withType(final Type valueType)\n
    withType(final TypeReference<?> valueTypeRef)\n
    '''
def withValueToUpdate():
    '''returns ObjectReader\n\n
    withValueToUpdate(final Object value)\n
    '''
def withView():
    '''returns ObjectReader\n\n
    withView(final Class<?> activeView)\n
    '''
def withHandler():
    '''returns ObjectReader\n\n
    withHandler(final DeserializationProblemHandler h)\n
    '''
def withFormatDetection():
    '''returns ObjectReader\n\n
    withFormatDetection(final ObjectReader... readers)\n
    withFormatDetection(final DataFormatReaders readers)\n
    '''
def withAttributes():
    '''returns ObjectReader\n\n
    withAttributes(final Map<?, ?> attrs)\n
    '''
def withAttribute():
    '''returns ObjectReader\n\n
    withAttribute(final Object key, final Object value)\n
    '''
def withoutAttribute():
    '''returns ObjectReader\n\n
    withoutAttribute(final Object key)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final DeserializationFeature f)\n
    isEnabled(final MapperFeature f)\n
    isEnabled(final JsonParser.Feature f)\n
    '''
def getConfig():
    '''returns DeserializationConfig\n\n
    getConfig()\n
    '''
def getFactory():
    '''returns JsonFactory\n\n
    getFactory()\n
    '''
def getTypeFactory():
    '''returns TypeFactory\n\n
    getTypeFactory()\n
    '''
def getAttributes():
    '''returns ContextAttributes\n\n
    getAttributes()\n
    '''
def getInjectableValues():
    '''returns InjectableValues\n\n
    getInjectableValues()\n
    '''
def createArrayNode():
    '''returns JsonNode\n\n
    createArrayNode()\n
    '''
def createObjectNode():
    '''returns JsonNode\n\n
    createObjectNode()\n
    '''
def treeAsTokens():
    '''returns JsonParser\n\n
    treeAsTokens(final TreeNode n)\n
    '''
def writeTree():
    '''returns None\n\n
    writeTree(final JsonGenerator g, final TreeNode rootNode)\n
    '''
def readTree():
    '''returns JsonNode\n\n
    readTree(final InputStream in)\n
    readTree(final Reader r)\n
    readTree(final String json)\n
    readTree(final DataInput src)\n
    '''
def writeValue():
    '''returns None\n\n
    writeValue(final JsonGenerator gen, final Object value)\n
    '''
