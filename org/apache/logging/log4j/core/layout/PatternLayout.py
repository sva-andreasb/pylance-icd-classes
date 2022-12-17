DEFAULT_CONVERSION_PATTERN = "String  \"%m%n\""
TTCC_CONVERSION_PATTERN = "String  \"%r [%t] %p %c %notEmpty{%x }- %m%n\""
SIMPLE_CONVERSION_PATTERN = "String  \"%d [%t] %p %c - %m%n\""
KEY = "String  \"Converter\""
def requiresLocation():
    '''returns boolean\n\n
    requiresLocation()\n
    requiresLocation()\n
    requiresLocation()\n
    requiresLocation()\n
    requiresLocation()\n
    '''
def getConversionPattern():
    '''returns String\n\n
    getConversionPattern()\n
    '''
def toSerializable():
    '''returns StringBuilder\n\n
    toSerializable(final LogEvent event)\n
    toSerializable(final LogEvent event)\n
    toSerializable(final LogEvent event, final StringBuilder buffer)\n
    toSerializable(final LogEvent event)\n
    toSerializable(final LogEvent event, final StringBuilder buffer)\n
    toSerializable(final LogEvent event)\n
    toSerializable(final LogEvent event, final StringBuilder buf)\n
    toSerializable(final LogEvent event)\n
    toSerializable(final LogEvent event, final StringBuilder buffer)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LogEvent event, final StringBuilder stringBuilder)\n
    '''
def encode():
    '''returns None\n\n
    encode(final LogEvent event, final ByteBufferDestination destination)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def getEventSerializer():
    '''returns Serializer\n\n
    getEventSerializer()\n
    '''
def build():
    '''returns PatternLayout\n\n
    build()\n
    build()\n
    '''
def setConfiguration():
    '''returns SerializerBuilder\n\n
    setConfiguration(final Configuration configuration)\n
    '''
def setReplace():
    '''returns SerializerBuilder\n\n
    setReplace(final RegexReplacement replace)\n
    '''
def setPattern():
    '''returns SerializerBuilder\n\n
    setPattern(final String pattern)\n
    '''
def setDefaultPattern():
    '''returns SerializerBuilder\n\n
    setDefaultPattern(final String defaultPattern)\n
    '''
def setPatternSelector():
    '''returns SerializerBuilder\n\n
    setPatternSelector(final PatternSelector patternSelector)\n
    '''
def setAlwaysWriteExceptions():
    '''returns SerializerBuilder\n\n
    setAlwaysWriteExceptions(final boolean alwaysWriteExceptions)\n
    '''
def setDisableAnsi():
    '''returns SerializerBuilder\n\n
    setDisableAnsi(final boolean disableAnsi)\n
    '''
def setNoConsoleNoAnsi():
    '''returns SerializerBuilder\n\n
    setNoConsoleNoAnsi(final boolean noConsoleNoAnsi)\n
    '''
def withPattern():
    '''returns Builder\n\n
    withPattern(final String pattern)\n
    '''
def withPatternSelector():
    '''returns Builder\n\n
    withPatternSelector(final PatternSelector patternSelector)\n
    '''
def withConfiguration():
    '''returns Builder\n\n
    withConfiguration(final Configuration configuration)\n
    '''
def withRegexReplacement():
    '''returns Builder\n\n
    withRegexReplacement(final RegexReplacement regexReplacement)\n
    '''
def withCharset():
    '''returns Builder\n\n
    withCharset(final Charset charset)\n
    '''
def withAlwaysWriteExceptions():
    '''returns Builder\n\n
    withAlwaysWriteExceptions(final boolean alwaysWriteExceptions)\n
    '''
def withDisableAnsi():
    '''returns Builder\n\n
    withDisableAnsi(final boolean disableAnsi)\n
    '''
def withNoConsoleNoAnsi():
    '''returns Builder\n\n
    withNoConsoleNoAnsi(final boolean noConsoleNoAnsi)\n
    '''
def withHeader():
    '''returns Builder\n\n
    withHeader(final String header)\n
    '''
def withFooter():
    '''returns Builder\n\n
    withFooter(final String footer)\n
    '''
