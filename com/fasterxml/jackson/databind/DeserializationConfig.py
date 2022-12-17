def ():
    '''returns DeserializationConfig\n\n
    (final BaseSettings base, final SubtypeResolver str, final SimpleMixInResolver mixins, final RootNameLookup rootNames, final ConfigOverrides configOverrides)\n
    '''
def with():
    '''returns DeserializationConfig\n\n
    with(final SubtypeResolver str)\n
    with(final ContextAttributes attrs)\n
    with(final DeserializationFeature feature)\n
    with(final DeserializationFeature first, final DeserializationFeature... features)\n
    with(final JsonParser.Feature feature)\n
    with(final FormatFeature feature)\n
    with(final JsonNodeFactory f)\n
    '''
def withRootName():
    '''returns DeserializationConfig\n\n
    withRootName(final PropertyName rootName)\n
    '''
def withView():
    '''returns DeserializationConfig\n\n
    withView(final Class<?> view)\n
    '''
def withFeatures():
    '''returns DeserializationConfig\n\n
    withFeatures(final DeserializationFeature... features)\n
    withFeatures(final JsonParser.Feature... features)\n
    withFeatures(final FormatFeature... features)\n
    '''
def without():
    '''returns DeserializationConfig\n\n
    without(final DeserializationFeature feature)\n
    without(final DeserializationFeature first, final DeserializationFeature... features)\n
    without(final JsonParser.Feature feature)\n
    without(final FormatFeature feature)\n
    '''
def withoutFeatures():
    '''returns DeserializationConfig\n\n
    withoutFeatures(final DeserializationFeature... features)\n
    withoutFeatures(final JsonParser.Feature... features)\n
    withoutFeatures(final FormatFeature... features)\n
    '''
def withHandler():
    '''returns DeserializationConfig\n\n
    withHandler(final DeserializationProblemHandler h)\n
    '''
def withNoProblemHandlers():
    '''returns DeserializationConfig\n\n
    withNoProblemHandlers()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final JsonParser p)\n
    '''
def useRootWrapping():
    '''returns boolean\n\n
    useRootWrapping()\n
    '''
def getProblemHandlers():
    '''returns LinkedNode<DeserializationProblemHandler>\n\n
    getProblemHandlers()\n
    '''
def findTypeDeserializer():
    '''returns TypeDeserializer\n\n
    findTypeDeserializer(final JavaType baseType)\n
    '''
