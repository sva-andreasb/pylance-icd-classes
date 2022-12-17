def version():
    '''returns Version\n\n
    version()\n
    '''
def with():
    '''returns GeneratorSettings\n\n
    with(final SerializationFeature feature)\n
    with(final SerializationFeature first, final SerializationFeature... other)\n
    with(final JsonGenerator.Feature feature)\n
    with(final FormatFeature feature)\n
    with(final DateFormat df)\n
    with(final FilterProvider filterProvider)\n
    with(final PrettyPrinter pp)\n
    with(final FormatSchema schema)\n
    with(final Locale l)\n
    with(final TimeZone tz)\n
    with(final Base64Variant b64variant)\n
    with(final CharacterEscapes escapes)\n
    with(final JsonFactory f)\n
    with(final ContextAttributes attrs)\n
    with(PrettyPrinter pp)\n
    with(final FormatSchema sch)\n
    with(final CharacterEscapes esc)\n
    '''
def withFeatures():
    '''returns ObjectWriter\n\n
    withFeatures(final SerializationFeature... features)\n
    withFeatures(final JsonGenerator.Feature... features)\n
    withFeatures(final FormatFeature... features)\n
    '''
def without():
    '''returns ObjectWriter\n\n
    without(final SerializationFeature feature)\n
    without(final SerializationFeature first, final SerializationFeature... other)\n
    without(final JsonGenerator.Feature feature)\n
    without(final FormatFeature feature)\n
    '''
def withoutFeatures():
    '''returns ObjectWriter\n\n
    withoutFeatures(final SerializationFeature... features)\n
    withoutFeatures(final JsonGenerator.Feature... features)\n
    withoutFeatures(final FormatFeature... features)\n
    '''
def forType():
    '''returns ObjectWriter\n\n
    forType(final JavaType rootType)\n
    forType(final Class<?> rootType)\n
    forType(final TypeReference<?> rootType)\n
    '''
def withType():
    '''returns ObjectWriter\n\n
    withType(final JavaType rootType)\n
    withType(final Class<?> rootType)\n
    withType(final TypeReference<?> rootType)\n
    '''
def withDefaultPrettyPrinter():
    '''returns ObjectWriter\n\n
    withDefaultPrettyPrinter()\n
    '''
def withRootName():
    '''returns ObjectWriter\n\n
    withRootName(final String rootName)\n
    withRootName(final PropertyName rootName)\n
    '''
def withoutRootName():
    '''returns ObjectWriter\n\n
    withoutRootName()\n
    '''
def withSchema():
    '''returns ObjectWriter\n\n
    withSchema(final FormatSchema schema)\n
    '''
def withView():
    '''returns ObjectWriter\n\n
    withView(final Class<?> view)\n
    '''
def withAttributes():
    '''returns ObjectWriter\n\n
    withAttributes(final Map<?, ?> attrs)\n
    '''
def withAttribute():
    '''returns ObjectWriter\n\n
    withAttribute(final Object key, final Object value)\n
    '''
def withoutAttribute():
    '''returns ObjectWriter\n\n
    withoutAttribute(final Object key)\n
    '''
def withRootValueSeparator():
    '''returns GeneratorSettings\n\n
    withRootValueSeparator(final String sep)\n
    withRootValueSeparator(final SerializableString sep)\n
    withRootValueSeparator(final String sep)\n
    withRootValueSeparator(final SerializableString sep)\n
    '''
def writeValues():
    '''returns SequenceWriter\n\n
    writeValues(final File out)\n
    writeValues(final JsonGenerator gen)\n
    writeValues(final Writer out)\n
    writeValues(final OutputStream out)\n
    writeValues(final DataOutput out)\n
    '''
def writeValuesAsArray():
    '''returns SequenceWriter\n\n
    writeValuesAsArray(final File out)\n
    writeValuesAsArray(final JsonGenerator gen)\n
    writeValuesAsArray(final Writer out)\n
    writeValuesAsArray(final OutputStream out)\n
    writeValuesAsArray(final DataOutput out)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final SerializationFeature f)\n
    isEnabled(final MapperFeature f)\n
    isEnabled(final JsonParser.Feature f)\n
    isEnabled(final JsonGenerator.Feature f)\n
    '''
def getConfig():
    '''returns SerializationConfig\n\n
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
def hasPrefetchedSerializer():
    '''returns boolean\n\n
    hasPrefetchedSerializer()\n
    '''
def getAttributes():
    '''returns ContextAttributes\n\n
    getAttributes()\n
    '''
def writeValue():
    '''returns None\n\n
    writeValue(final JsonGenerator gen, final Object value)\n
    writeValue(final File resultFile, final Object value)\n
    writeValue(final OutputStream out, final Object value)\n
    writeValue(final Writer w, final Object value)\n
    writeValue(final DataOutput out, final Object value)\n
    '''
def writeValueAsString():
    '''returns String\n\n
    writeValueAsString(final Object value)\n
    '''
def writeValueAsBytes():
    '''returns byte[]\n\n
    writeValueAsBytes(final Object value)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JavaType type, final JsonFormatVisitorWrapper visitor)\n
    acceptJsonFormatVisitor(final Class<?> rawType, final JsonFormatVisitorWrapper visitor)\n
    '''
def canSerialize():
    '''returns boolean\n\n
    canSerialize(final Class<?> type)\n
    canSerialize(final Class<?> type, final AtomicReference<Throwable> cause)\n
    '''
def ():
    '''returns GeneratorSettings\n\n
    (final PrettyPrinter pp, final FormatSchema sch, final CharacterEscapes esc, final SerializableString rootSep)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final JsonGenerator gen)\n
    '''
def forRootType():
    '''returns Prefetch\n\n
    forRootType(final ObjectWriter parent, final JavaType newType)\n
    '''
def hasSerializer():
    '''returns boolean\n\n
    hasSerializer()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator gen, final Object value, final DefaultSerializerProvider prov)\n
    '''
