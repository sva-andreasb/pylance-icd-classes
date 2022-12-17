DEFAULT_ESCAPE = "char  '$'"
def ():
    '''returns StrSubstitutor\n\n
    ()\n
    (final StrLookup<?> variableResolver)\n
    (final StrLookup<?> variableResolver, final String prefix, final String suffix, final char escape)\n
    (final StrLookup<?> variableResolver, final String prefix, final String suffix, final char escape, final String valueDelimiter)\n
    (final StrLookup<?> variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape)\n
    (final StrLookup<?> variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape, final StrMatcher valueDelimiterMatcher)\n
    '''
def StrSubstitutor():
    '''returns <V>\n\n
    StrSubstitutor(final Map<String, V> valueMap)\n
    StrSubstitutor(final Map<String, V> valueMap, final String prefix, final String suffix)\n
    StrSubstitutor(final Map<String, V> valueMap, final String prefix, final String suffix, final char escape)\n
    StrSubstitutor(final Map<String, V> valueMap, final String prefix, final String suffix, final char escape, final String valueDelimiter)\n
    '''
def replace():
    '''returns String\n\n
    replace(final String source)\n
    replace(final String source, final int offset, final int length)\n
    replace(final char[] source)\n
    replace(final char[] source, final int offset, final int length)\n
    replace(final StringBuffer source)\n
    replace(final StringBuffer source, final int offset, final int length)\n
    replace(final CharSequence source)\n
    replace(final CharSequence source, final int offset, final int length)\n
    replace(final StrBuilder source)\n
    replace(final StrBuilder source, final int offset, final int length)\n
    replace(final Object source)\n
    '''
def replaceIn():
    '''returns boolean\n\n
    replaceIn(final StringBuffer source)\n
    replaceIn(final StringBuffer source, final int offset, final int length)\n
    replaceIn(final StringBuilder source)\n
    replaceIn(final StringBuilder source, final int offset, final int length)\n
    replaceIn(final StrBuilder source)\n
    replaceIn(final StrBuilder source, final int offset, final int length)\n
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
def setVariableResolver():
    '''returns None\n\n
    setVariableResolver(final StrLookup<?> variableResolver)\n
    '''
def isEnableSubstitutionInVariables():
    '''returns boolean\n\n
    isEnableSubstitutionInVariables()\n
    '''
def setEnableSubstitutionInVariables():
    '''returns None\n\n
    setEnableSubstitutionInVariables(final boolean enableSubstitutionInVariables)\n
    '''
