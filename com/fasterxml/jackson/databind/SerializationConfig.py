def SerializationConfig():
'''public SerializationConfig(final BaseSettings base, final SubtypeResolver str, final SimpleMixInResolver mixins, final RootNameLookup rootNames, final ConfigOverrides configOverrides)
'''
pass
def withRootName():
'''public SerializationConfig withRootName(final PropertyName rootName)
'''
pass
def with():
'''public SerializationConfig with(final SubtypeResolver str)
public SerializationConfig with(final ContextAttributes attrs)
public SerializationConfig with(final DateFormat df)
public SerializationConfig with(final SerializationFeature feature)
public SerializationConfig with(final SerializationFeature first, final SerializationFeature... features)
public SerializationConfig with(final JsonGenerator.Feature feature)
public SerializationConfig with(final FormatFeature feature)
'''
pass
def withView():
'''public SerializationConfig withView(final Class<?> view)
'''
pass
def withFeatures():
'''public SerializationConfig withFeatures(final SerializationFeature... features)
public SerializationConfig withFeatures(final JsonGenerator.Feature... features)
public SerializationConfig withFeatures(final FormatFeature... features)
'''
pass
def without():
'''public SerializationConfig without(final SerializationFeature feature)
public SerializationConfig without(final SerializationFeature first, final SerializationFeature... features)
public SerializationConfig without(final JsonGenerator.Feature feature)
public SerializationConfig without(final FormatFeature feature)
'''
pass
def withoutFeatures():
'''public SerializationConfig withoutFeatures(final SerializationFeature... features)
public SerializationConfig withoutFeatures(final JsonGenerator.Feature... features)
public SerializationConfig withoutFeatures(final FormatFeature... features)
'''
pass
def withFilters():
'''public SerializationConfig withFilters(final FilterProvider filterProvider)
'''
pass
def withPropertyInclusion():
'''public SerializationConfig withPropertyInclusion(final JsonInclude.Value incl)
'''
pass
def withDefaultPrettyPrinter():
'''public SerializationConfig withDefaultPrettyPrinter(final PrettyPrinter pp)
'''
pass
def constructDefaultPrettyPrinter():
'''public PrettyPrinter constructDefaultPrettyPrinter()
'''
pass
def initialize():
'''public void initialize(final JsonGenerator g)
'''
pass
def useRootWrapping():
'''public boolean useRootWrapping()
'''
pass
def isEnabled():
'''public final boolean isEnabled(final SerializationFeature f)
public final boolean isEnabled(final JsonGenerator.Feature f, final JsonFactory factory)
'''
pass
def hasSerializationFeatures():
'''public final boolean hasSerializationFeatures(final int featureMask)
'''
pass
def getSerializationFeatures():
'''public final int getSerializationFeatures()
'''
pass
def getFilterProvider():
'''public FilterProvider getFilterProvider()
'''
pass
def getDefaultPrettyPrinter():
'''public PrettyPrinter getDefaultPrettyPrinter()
'''
pass
def introspect():
'''public <T extends BeanDescription> T introspect(final JavaType type)
'''
pass
