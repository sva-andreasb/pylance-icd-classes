def DeserializationConfig():
'''public DeserializationConfig(final BaseSettings base, final SubtypeResolver str, final SimpleMixInResolver mixins, final RootNameLookup rootNames, final ConfigOverrides configOverrides)
'''
pass
def with():
'''public DeserializationConfig with(final SubtypeResolver str)
public DeserializationConfig with(final ContextAttributes attrs)
public DeserializationConfig with(final DeserializationFeature feature)
public DeserializationConfig with(final DeserializationFeature first, final DeserializationFeature... features)
public DeserializationConfig with(final JsonParser.Feature feature)
public DeserializationConfig with(final FormatFeature feature)
public DeserializationConfig with(final JsonNodeFactory f)
'''
pass
def withRootName():
'''public DeserializationConfig withRootName(final PropertyName rootName)
'''
pass
def withView():
'''public DeserializationConfig withView(final Class<?> view)
'''
pass
def withFeatures():
'''public DeserializationConfig withFeatures(final DeserializationFeature... features)
public DeserializationConfig withFeatures(final JsonParser.Feature... features)
public DeserializationConfig withFeatures(final FormatFeature... features)
'''
pass
def without():
'''public DeserializationConfig without(final DeserializationFeature feature)
public DeserializationConfig without(final DeserializationFeature first, final DeserializationFeature... features)
public DeserializationConfig without(final JsonParser.Feature feature)
public DeserializationConfig without(final FormatFeature feature)
'''
pass
def withoutFeatures():
'''public DeserializationConfig withoutFeatures(final DeserializationFeature... features)
public DeserializationConfig withoutFeatures(final JsonParser.Feature... features)
public DeserializationConfig withoutFeatures(final FormatFeature... features)
'''
pass
def withHandler():
'''public DeserializationConfig withHandler(final DeserializationProblemHandler h)
'''
pass
def withNoProblemHandlers():
'''public DeserializationConfig withNoProblemHandlers()
'''
pass
def initialize():
'''public void initialize(final JsonParser p)
'''
pass
def useRootWrapping():
'''public boolean useRootWrapping()
'''
pass
def isEnabled():
'''public final boolean isEnabled(final DeserializationFeature f)
public final boolean isEnabled(final JsonParser.Feature f, final JsonFactory factory)
'''
pass
def hasDeserializationFeatures():
'''public final boolean hasDeserializationFeatures(final int featureMask)
'''
pass
def hasSomeOfFeatures():
'''public final boolean hasSomeOfFeatures(final int featureMask)
'''
pass
def getDeserializationFeatures():
'''public final int getDeserializationFeatures()
'''
pass
def requiresFullValue():
'''public final boolean requiresFullValue()
'''
pass
def getProblemHandlers():
'''public LinkedNode<DeserializationProblemHandler> getProblemHandlers()
'''
pass
def getNodeFactory():
'''public final JsonNodeFactory getNodeFactory()
'''
pass
def introspect():
'''public <T extends BeanDescription> T introspect(final JavaType type)
'''
pass
def introspectForCreation():
'''public <T extends BeanDescription> T introspectForCreation(final JavaType type)
'''
pass
def introspectForBuilder():
'''public <T extends BeanDescription> T introspectForBuilder(final JavaType type)
'''
pass
def findTypeDeserializer():
'''public TypeDeserializer findTypeDeserializer(final JavaType baseType)
'''
pass
