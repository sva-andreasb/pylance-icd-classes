def DeserializationConfig():
    '''    public DeserializationConfig(final BaseSettings base, final SubtypeResolver str, final SimpleMixInResolver mixins, final RootNameLookup rootNames, final ConfigOverrides configOverrides)
    '''
def with():
    '''    public DeserializationConfig with(final SubtypeResolver str)
    public DeserializationConfig with(final ContextAttributes attrs)
    public DeserializationConfig with(final DeserializationFeature feature)
    public DeserializationConfig with(final DeserializationFeature first, final DeserializationFeature... features)
    public DeserializationConfig with(final JsonParser.Feature feature)
    public DeserializationConfig with(final FormatFeature feature)
    public DeserializationConfig with(final JsonNodeFactory f)
    '''
def withRootName():
    '''    public DeserializationConfig withRootName(final PropertyName rootName)
    '''
def withView():
    '''    public DeserializationConfig withView(final Class<?> view)
    '''
def withFeatures():
    '''    public DeserializationConfig withFeatures(final DeserializationFeature... features)
    public DeserializationConfig withFeatures(final JsonParser.Feature... features)
    public DeserializationConfig withFeatures(final FormatFeature... features)
    '''
def without():
    '''    public DeserializationConfig without(final DeserializationFeature feature)
    public DeserializationConfig without(final DeserializationFeature first, final DeserializationFeature... features)
    public DeserializationConfig without(final JsonParser.Feature feature)
    public DeserializationConfig without(final FormatFeature feature)
    '''
def withoutFeatures():
    '''    public DeserializationConfig withoutFeatures(final DeserializationFeature... features)
    public DeserializationConfig withoutFeatures(final JsonParser.Feature... features)
    public DeserializationConfig withoutFeatures(final FormatFeature... features)
    '''
def withHandler():
    '''    public DeserializationConfig withHandler(final DeserializationProblemHandler h)
    '''
def withNoProblemHandlers():
    '''    public DeserializationConfig withNoProblemHandlers()
    '''
def initialize():
    '''    public void initialize(final JsonParser p)
    '''
def useRootWrapping():
    '''    public boolean useRootWrapping()
    '''
def isEnabled():
    '''    public final boolean isEnabled(final DeserializationFeature f)
    public final boolean isEnabled(final JsonParser.Feature f, final JsonFactory factory)
    '''
def hasDeserializationFeatures():
    '''    public final boolean hasDeserializationFeatures(final int featureMask)
    '''
def hasSomeOfFeatures():
    '''    public final boolean hasSomeOfFeatures(final int featureMask)
    '''
def getDeserializationFeatures():
    '''    public final int getDeserializationFeatures()
    '''
def requiresFullValue():
    '''    public final boolean requiresFullValue()
    '''
def getProblemHandlers():
    '''    public LinkedNode<DeserializationProblemHandler> getProblemHandlers()
    '''
def getNodeFactory():
    '''    public final JsonNodeFactory getNodeFactory()
    '''
def introspect():
    '''    public <T extends BeanDescription> T introspect(final JavaType type)
    '''
def introspectForCreation():
    '''    public <T extends BeanDescription> T introspectForCreation(final JavaType type)
    '''
def introspectForBuilder():
    '''    public <T extends BeanDescription> T introspectForBuilder(final JavaType type)
    '''
def findTypeDeserializer():
    '''    public TypeDeserializer findTypeDeserializer(final JavaType baseType)
    '''
