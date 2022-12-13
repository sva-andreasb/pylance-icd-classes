def version():
'''public Version version()
'''
pass
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
pass
def withFeatures():
'''public ObjectWriter withFeatures(final SerializationFeature... features)
public ObjectWriter withFeatures(final JsonGenerator.Feature... features)
public ObjectWriter withFeatures(final FormatFeature... features)
'''
pass
def without():
'''public ObjectWriter without(final SerializationFeature feature)
public ObjectWriter without(final SerializationFeature first, final SerializationFeature... other)
public ObjectWriter without(final JsonGenerator.Feature feature)
public ObjectWriter without(final FormatFeature feature)
'''
pass
def withoutFeatures():
'''public ObjectWriter withoutFeatures(final SerializationFeature... features)
public ObjectWriter withoutFeatures(final JsonGenerator.Feature... features)
public ObjectWriter withoutFeatures(final FormatFeature... features)
'''
pass
def forType():
'''public ObjectWriter forType(final JavaType rootType)
public ObjectWriter forType(final Class<?> rootType)
public ObjectWriter forType(final TypeReference<?> rootType)
'''
pass
def withType():
'''public ObjectWriter withType(final JavaType rootType)
public ObjectWriter withType(final Class<?> rootType)
public ObjectWriter withType(final TypeReference<?> rootType)
'''
pass
def withDefaultPrettyPrinter():
'''public ObjectWriter withDefaultPrettyPrinter()
'''
pass
def withRootName():
'''public ObjectWriter withRootName(final String rootName)
public ObjectWriter withRootName(final PropertyName rootName)
'''
pass
def withoutRootName():
'''public ObjectWriter withoutRootName()
'''
pass
def withSchema():
'''public ObjectWriter withSchema(final FormatSchema schema)
'''
pass
def withView():
'''public ObjectWriter withView(final Class<?> view)
'''
pass
def withAttributes():
'''public ObjectWriter withAttributes(final Map<?, ?> attrs)
'''
pass
def withAttribute():
'''public ObjectWriter withAttribute(final Object key, final Object value)
'''
pass
def withoutAttribute():
'''public ObjectWriter withoutAttribute(final Object key)
'''
pass
def withRootValueSeparator():
'''public ObjectWriter withRootValueSeparator(final String sep)
public ObjectWriter withRootValueSeparator(final SerializableString sep)
public GeneratorSettings withRootValueSeparator(final String sep)
public GeneratorSettings withRootValueSeparator(final SerializableString sep)
'''
pass
def writeValues():
'''public SequenceWriter writeValues(final File out)
public SequenceWriter writeValues(final JsonGenerator gen)
public SequenceWriter writeValues(final Writer out)
public SequenceWriter writeValues(final OutputStream out)
public SequenceWriter writeValues(final DataOutput out)
'''
pass
def writeValuesAsArray():
'''public SequenceWriter writeValuesAsArray(final File out)
public SequenceWriter writeValuesAsArray(final JsonGenerator gen)
public SequenceWriter writeValuesAsArray(final Writer out)
public SequenceWriter writeValuesAsArray(final OutputStream out)
public SequenceWriter writeValuesAsArray(final DataOutput out)
'''
pass
def isEnabled():
'''public boolean isEnabled(final SerializationFeature f)
public boolean isEnabled(final MapperFeature f)
public boolean isEnabled(final JsonParser.Feature f)
public boolean isEnabled(final JsonGenerator.Feature f)
'''
pass
def getConfig():
'''public SerializationConfig getConfig()
'''
pass
def getFactory():
'''public JsonFactory getFactory()
'''
pass
def getTypeFactory():
'''public TypeFactory getTypeFactory()
'''
pass
def hasPrefetchedSerializer():
'''public boolean hasPrefetchedSerializer()
'''
pass
def getAttributes():
'''public ContextAttributes getAttributes()
'''
pass
def writeValue():
'''public void writeValue(final JsonGenerator gen, final Object value)
public void writeValue(final File resultFile, final Object value)
public void writeValue(final OutputStream out, final Object value)
public void writeValue(final Writer w, final Object value)
public void writeValue(final DataOutput out, final Object value)
'''
pass
def writeValueAsString():
'''public String writeValueAsString(final Object value)
'''
pass
def writeValueAsBytes():
'''public byte[] writeValueAsBytes(final Object value)
'''
pass
def acceptJsonFormatVisitor():
'''public void acceptJsonFormatVisitor(final JavaType type, final JsonFormatVisitorWrapper visitor)
public void acceptJsonFormatVisitor(final Class<?> rawType, final JsonFormatVisitorWrapper visitor)
'''
pass
def canSerialize():
'''public boolean canSerialize(final Class<?> type)
public boolean canSerialize(final Class<?> type, final AtomicReference<Throwable> cause)
'''
pass
def GeneratorSettings():
'''public GeneratorSettings(final PrettyPrinter pp, final FormatSchema sch, final CharacterEscapes esc, final SerializableString rootSep)
'''
pass
def initialize():
'''public void initialize(final JsonGenerator gen)
'''
pass
def forRootType():
'''public Prefetch forRootType(final ObjectWriter parent, final JavaType newType)
'''
pass
def getValueSerializer():
'''public final JsonSerializer<Object> getValueSerializer()
'''
pass
def getTypeSerializer():
'''public final TypeSerializer getTypeSerializer()
'''
pass
def hasSerializer():
'''public boolean hasSerializer()
'''
pass
def serialize():
'''public void serialize(final JsonGenerator gen, final Object value, final DefaultSerializerProvider prov)
'''
pass
