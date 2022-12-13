def version():
    '''public Version version()
    '''
def with():
    '''public ObjectWriter with(final SerializationFeature feature)
    public ObjectWriter with(final SerializationFeature first, final SerializationFeature... other)
    public ObjectWriter with(final JsonGenerator.Feature feature)
    public ObjectWriter with(final FormatFeature feature)
    public ObjectWriter with(final DateFormat df)
    public ObjectWriter with(final FilterProvider filterProvider)
    public ObjectWriter with(final PrettyPrinter pp)
    public ObjectWriter with(final FormatSchema schema)
    public ObjectWriter with(final Locale l)
    public ObjectWriter with(final TimeZone tz)
    public ObjectWriter with(final Base64Variant b64variant)
    public ObjectWriter with(final CharacterEscapes escapes)
    public ObjectWriter with(final JsonFactory f)
    public ObjectWriter with(final ContextAttributes attrs)
    public GeneratorSettings with(PrettyPrinter pp)
    public GeneratorSettings with(final FormatSchema sch)
    public GeneratorSettings with(final CharacterEscapes esc)
    '''
def withFeatures():
    '''public ObjectWriter withFeatures(final SerializationFeature... features)
    public ObjectWriter withFeatures(final JsonGenerator.Feature... features)
    public ObjectWriter withFeatures(final FormatFeature... features)
    '''
def without():
    '''public ObjectWriter without(final SerializationFeature feature)
    public ObjectWriter without(final SerializationFeature first, final SerializationFeature... other)
    public ObjectWriter without(final JsonGenerator.Feature feature)
    public ObjectWriter without(final FormatFeature feature)
    '''
def withoutFeatures():
    '''public ObjectWriter withoutFeatures(final SerializationFeature... features)
    public ObjectWriter withoutFeatures(final JsonGenerator.Feature... features)
    public ObjectWriter withoutFeatures(final FormatFeature... features)
    '''
def forType():
    '''public ObjectWriter forType(final JavaType rootType)
    public ObjectWriter forType(final Class<?> rootType)
    public ObjectWriter forType(final TypeReference<?> rootType)
    '''
def withType():
    '''public ObjectWriter withType(final JavaType rootType)
    public ObjectWriter withType(final Class<?> rootType)
    public ObjectWriter withType(final TypeReference<?> rootType)
    '''
def withDefaultPrettyPrinter():
    '''public ObjectWriter withDefaultPrettyPrinter()
    '''
def withRootName():
    '''public ObjectWriter withRootName(final String rootName)
    public ObjectWriter withRootName(final PropertyName rootName)
    '''
def withoutRootName():
    '''public ObjectWriter withoutRootName()
    '''
def withSchema():
    '''public ObjectWriter withSchema(final FormatSchema schema)
    '''
def withView():
    '''public ObjectWriter withView(final Class<?> view)
    '''
def withAttributes():
    '''public ObjectWriter withAttributes(final Map<?, ?> attrs)
    '''
def withAttribute():
    '''public ObjectWriter withAttribute(final Object key, final Object value)
    '''
def withoutAttribute():
    '''public ObjectWriter withoutAttribute(final Object key)
    '''
def withRootValueSeparator():
    '''public ObjectWriter withRootValueSeparator(final String sep)
    public ObjectWriter withRootValueSeparator(final SerializableString sep)
    public GeneratorSettings withRootValueSeparator(final String sep)
    public GeneratorSettings withRootValueSeparator(final SerializableString sep)
    '''
def writeValues():
    '''public SequenceWriter writeValues(final File out)
    public SequenceWriter writeValues(final JsonGenerator gen)
    public SequenceWriter writeValues(final Writer out)
    public SequenceWriter writeValues(final OutputStream out)
    public SequenceWriter writeValues(final DataOutput out)
    '''
def writeValuesAsArray():
    '''public SequenceWriter writeValuesAsArray(final File out)
    public SequenceWriter writeValuesAsArray(final JsonGenerator gen)
    public SequenceWriter writeValuesAsArray(final Writer out)
    public SequenceWriter writeValuesAsArray(final OutputStream out)
    public SequenceWriter writeValuesAsArray(final DataOutput out)
    '''
def isEnabled():
    '''public boolean isEnabled(final SerializationFeature f)
    public boolean isEnabled(final MapperFeature f)
    public boolean isEnabled(final JsonParser.Feature f)
    public boolean isEnabled(final JsonGenerator.Feature f)
    '''
def getConfig():
    '''public SerializationConfig getConfig()
    '''
def getFactory():
    '''public JsonFactory getFactory()
    '''
def getTypeFactory():
    '''public TypeFactory getTypeFactory()
    '''
def hasPrefetchedSerializer():
    '''public boolean hasPrefetchedSerializer()
    '''
def getAttributes():
    '''public ContextAttributes getAttributes()
    '''
def writeValue():
    '''public void writeValue(final JsonGenerator gen, final Object value)
    public void writeValue(final File resultFile, final Object value)
    public void writeValue(final OutputStream out, final Object value)
    public void writeValue(final Writer w, final Object value)
    public void writeValue(final DataOutput out, final Object value)
    '''
def writeValueAsString():
    '''public String writeValueAsString(final Object value)
    '''
def writeValueAsBytes():
    '''public byte[] writeValueAsBytes(final Object value)
    '''
def acceptJsonFormatVisitor():
    '''public void acceptJsonFormatVisitor(final JavaType type, final JsonFormatVisitorWrapper visitor)
    public void acceptJsonFormatVisitor(final Class<?> rawType, final JsonFormatVisitorWrapper visitor)
    '''
def canSerialize():
    '''public boolean canSerialize(final Class<?> type)
    public boolean canSerialize(final Class<?> type, final AtomicReference<Throwable> cause)
    '''
def GeneratorSettings():
    '''public GeneratorSettings(final PrettyPrinter pp, final FormatSchema sch, final CharacterEscapes esc, final SerializableString rootSep)
    '''
def initialize():
    '''public void initialize(final JsonGenerator gen)
    '''
def forRootType():
    '''public Prefetch forRootType(final ObjectWriter parent, final JavaType newType)
    '''
def getValueSerializer():
    '''public final JsonSerializer<Object> getValueSerializer()
    '''
def getTypeSerializer():
    '''public final TypeSerializer getTypeSerializer()
    '''
def hasSerializer():
    '''public boolean hasSerializer()
    '''
def serialize():
    '''public void serialize(final JsonGenerator gen, final Object value, final DefaultSerializerProvider prov)
    '''
