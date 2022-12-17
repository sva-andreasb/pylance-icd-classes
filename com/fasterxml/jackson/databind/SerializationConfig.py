def ():
    '''returns SerializationConfig\n\n
    (final BaseSettings base, final SubtypeResolver str, final SimpleMixInResolver mixins, final RootNameLookup rootNames, final ConfigOverrides configOverrides)\n
    '''
def withRootName():
    '''returns SerializationConfig\n\n
    withRootName(final PropertyName rootName)\n
    '''
def with():
    '''returns SerializationConfig\n\n
    with(final SubtypeResolver str)\n
    with(final ContextAttributes attrs)\n
    with(final DateFormat df)\n
    with(final SerializationFeature feature)\n
    with(final SerializationFeature first, final SerializationFeature... features)\n
    with(final JsonGenerator.Feature feature)\n
    with(final FormatFeature feature)\n
    '''
def withView():
    '''returns SerializationConfig\n\n
    withView(final Class<?> view)\n
    '''
def withFeatures():
    '''returns SerializationConfig\n\n
    withFeatures(final SerializationFeature... features)\n
    withFeatures(final JsonGenerator.Feature... features)\n
    withFeatures(final FormatFeature... features)\n
    '''
def without():
    '''returns SerializationConfig\n\n
    without(final SerializationFeature feature)\n
    without(final SerializationFeature first, final SerializationFeature... features)\n
    without(final JsonGenerator.Feature feature)\n
    without(final FormatFeature feature)\n
    '''
def withoutFeatures():
    '''returns SerializationConfig\n\n
    withoutFeatures(final SerializationFeature... features)\n
    withoutFeatures(final JsonGenerator.Feature... features)\n
    withoutFeatures(final FormatFeature... features)\n
    '''
def withFilters():
    '''returns SerializationConfig\n\n
    withFilters(final FilterProvider filterProvider)\n
    '''
def withPropertyInclusion():
    '''returns SerializationConfig\n\n
    withPropertyInclusion(final JsonInclude.Value incl)\n
    '''
def withDefaultPrettyPrinter():
    '''returns SerializationConfig\n\n
    withDefaultPrettyPrinter(final PrettyPrinter pp)\n
    '''
def constructDefaultPrettyPrinter():
    '''returns PrettyPrinter\n\n
    constructDefaultPrettyPrinter()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final JsonGenerator g)\n
    '''
def useRootWrapping():
    '''returns boolean\n\n
    useRootWrapping()\n
    '''
def getFilterProvider():
    '''returns FilterProvider\n\n
    getFilterProvider()\n
    '''
def getDefaultPrettyPrinter():
    '''returns PrettyPrinter\n\n
    getDefaultPrettyPrinter()\n
    '''
