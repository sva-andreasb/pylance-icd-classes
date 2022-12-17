DEFAULT_ESCAPE = "char  '$'"
DEFAULT_VALUE_DELIMITER_STRING = "String  \":-\""
ESCAPE_DELIMITER_STRING = "String  \":\\-\""
def ():
    '''returns StrSubstitutor\n\n
    ()\n
    (final Map<String, String> valueMap)\n
    (final Map<String, String> valueMap, final String prefix, final String suffix)\n
    (final Map<String, String> valueMap, final String prefix, final String suffix, final char escape)\n
    (final Map<String, String> valueMap, final String prefix, final String suffix, final char escape, final String valueDelimiter)\n
    (final Properties properties)\n
    (final StrLookup variableResolver)\n
    (final StrLookup variableResolver, final String prefix, final String suffix, final char escape)\n
    (final StrLookup variableResolver, final String prefix, final String suffix, final char escape, final String valueDelimiter)\n
    (final StrLookup variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape)\n
    (final StrLookup variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape, final StrMatcher valueDelimiterMatcher)\n
    (final StrLookup variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape, final StrMatcher valueDelimiterMatcher, final StrMatcher valueEscapeMatcher)\n
    '''
def replace():
    '''returns String\n\n
    replace(final String source)\n
    replace(final LogEvent event, final String source)\n
    replace(final String source, final int offset, final int length)\n
    replace(final LogEvent event, final String source, final int offset, final int length)\n
    replace(final char[] source)\n
    replace(final LogEvent event, final char[] source)\n
    replace(final char[] source, final int offset, final int length)\n
    replace(final LogEvent event, final char[] source, final int offset, final int length)\n
    replace(final StringBuffer source)\n
    replace(final LogEvent event, final StringBuffer source)\n
    replace(final StringBuffer source, final int offset, final int length)\n
    replace(final LogEvent event, final StringBuffer source, final int offset, final int length)\n
    replace(final StringBuilder source)\n
    replace(final LogEvent event, final StringBuilder source)\n
    replace(final StringBuilder source, final int offset, final int length)\n
    replace(final LogEvent event, final StringBuilder source, final int offset, final int length)\n
    replace(final Object source)\n
    replace(final LogEvent event, final Object source)\n
    '''
def replaceIn():
    '''returns boolean\n\n
    replaceIn(final StringBuffer source)\n
    replaceIn(final StringBuffer source, final int offset, final int length)\n
    replaceIn(final LogEvent event, final StringBuffer source, final int offset, final int length)\n
    replaceIn(final StringBuilder source)\n
    replaceIn(final LogEvent event, final StringBuilder source)\n
    replaceIn(final StringBuilder source, final int offset, final int length)\n
    replaceIn(final LogEvent event, final StringBuilder source, final int offset, final int length)\n
    '''
def getEscapeChar():
    '''returns char\n\n
    getEscapeChar()\n
    '''
def setEscapeChar():
    '''returns None\n\n
    setEscapeChar(final char escapeCharacter)\n
    '''
def getVariablePrefixMatcher():
    '''returns StrMatcher\n\n
    getVariablePrefixMatcher()\n
    '''
def setVariablePrefixMatcher():
    '''returns StrSubstitutor\n\n
    setVariablePrefixMatcher(final StrMatcher prefixMatcher)\n
    '''
def setVariablePrefix():
    '''returns StrSubstitutor\n\n
    setVariablePrefix(final char prefix)\n
    setVariablePrefix(final String prefix)\n
    '''
def getVariableSuffixMatcher():
    '''returns StrMatcher\n\n
    getVariableSuffixMatcher()\n
    '''
def setVariableSuffixMatcher():
    '''returns StrSubstitutor\n\n
    setVariableSuffixMatcher(final StrMatcher suffixMatcher)\n
    '''
def setVariableSuffix():
    '''returns StrSubstitutor\n\n
    setVariableSuffix(final char suffix)\n
    setVariableSuffix(final String suffix)\n
    '''
def getValueDelimiterMatcher():
    '''returns StrMatcher\n\n
    getValueDelimiterMatcher()\n
    '''
def setValueDelimiterMatcher():
    '''returns StrSubstitutor\n\n
    setValueDelimiterMatcher(final StrMatcher valueDelimiterMatcher)\n
    '''
def setValueDelimiter():
    '''returns StrSubstitutor\n\n
    setValueDelimiter(final char valueDelimiter)\n
    setValueDelimiter(final String valueDelimiter)\n
    '''
def getVariableResolver():
    '''returns StrLookup\n\n
    getVariableResolver()\n
    '''
def setVariableResolver():
    '''returns None\n\n
    setVariableResolver(final StrLookup variableResolver)\n
    '''
def isEnableSubstitutionInVariables():
    '''returns boolean\n\n
    isEnableSubstitutionInVariables()\n
    '''
def setEnableSubstitutionInVariables():
    '''returns None\n\n
    setEnableSubstitutionInVariables(final boolean enableSubstitutionInVariables)\n
    '''
def appendWithSeparators():
    '''returns None\n\n
    appendWithSeparators(final StringBuilder sb, final Iterable<?> iterable, String separator)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setConfiguration():
    '''returns None\n\n
    setConfiguration(final Configuration configuration)\n
    '''
