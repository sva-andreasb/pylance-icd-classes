def SerializationConfig():
    '''    public SerializationConfig(final BaseSettings base, final SubtypeResolver str, final SimpleMixInResolver mixins, final RootNameLookup rootNames, final ConfigOverrides configOverrides)
    '''
def withRootName():
    '''    public SerializationConfig withRootName(final PropertyName rootName)
    '''
def with():
    '''    public SerializationConfig with(final SubtypeResolver str)
    public SerializationConfig with(final ContextAttributes attrs)
    public SerializationConfig with(final DateFormat df)
    public SerializationConfig with(final SerializationFeature feature)
    public SerializationConfig with(final SerializationFeature first, final SerializationFeature... features)
    public SerializationConfig with(final JsonGenerator.Feature feature)
    public SerializationConfig with(final FormatFeature feature)
    '''
def withView():
    '''    public SerializationConfig withView(final Class<?> view)
    '''
def withFeatures():
    '''    public SerializationConfig withFeatures(final SerializationFeature... features)
    public SerializationConfig withFeatures(final JsonGenerator.Feature... features)
    public SerializationConfig withFeatures(final FormatFeature... features)
    '''
def without():
    '''    public SerializationConfig without(final SerializationFeature feature)
    public SerializationConfig without(final SerializationFeature first, final SerializationFeature... features)
    public SerializationConfig without(final JsonGenerator.Feature feature)
    public SerializationConfig without(final FormatFeature feature)
    '''
def withoutFeatures():
    '''    public SerializationConfig withoutFeatures(final SerializationFeature... features)
    public SerializationConfig withoutFeatures(final JsonGenerator.Feature... features)
    public SerializationConfig withoutFeatures(final FormatFeature... features)
    '''
def withFilters():
    '''    public SerializationConfig withFilters(final FilterProvider filterProvider)
    '''
def withPropertyInclusion():
    '''    public SerializationConfig withPropertyInclusion(final JsonInclude.Value incl)
    '''
def withDefaultPrettyPrinter():
    '''    public SerializationConfig withDefaultPrettyPrinter(final PrettyPrinter pp)
    '''
def constructDefaultPrettyPrinter():
    '''    public PrettyPrinter constructDefaultPrettyPrinter()
    '''
def initialize():
    '''    public void initialize(final JsonGenerator g)
    '''
def useRootWrapping():
    '''    public boolean useRootWrapping()
    '''
def isEnabled():
    '''    public final boolean isEnabled(final SerializationFeature f)
    public final boolean isEnabled(final JsonGenerator.Feature f, final JsonFactory factory)
    '''
def hasSerializationFeatures():
    '''    public final boolean hasSerializationFeatures(final int featureMask)
    '''
def getSerializationFeatures():
    '''    public final int getSerializationFeatures()
    '''
def getFilterProvider():
    '''    public FilterProvider getFilterProvider()
    '''
def getDefaultPrettyPrinter():
    '''    public PrettyPrinter getDefaultPrettyPrinter()
    '''
def introspect():
    '''    public <T extends BeanDescription> T introspect(final JavaType type)
    '''
