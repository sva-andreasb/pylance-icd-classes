DEFAULT_ESCAPE = "char  '$'"
DEFAULT_VALUE_DELIMITER_STRING = "String  \":-\""
ESCAPE_DELIMITER_STRING = "String  \":\\-\""
def StrSubstitutor():
    '''    public StrSubstitutor()
    public StrSubstitutor(final Map<String, String> valueMap)
    public StrSubstitutor(final Map<String, String> valueMap, final String prefix, final String suffix)
    public StrSubstitutor(final Map<String, String> valueMap, final String prefix, final String suffix, final char escape)
    public StrSubstitutor(final Map<String, String> valueMap, final String prefix, final String suffix, final char escape, final String valueDelimiter)
    public StrSubstitutor(final Properties properties)
    public StrSubstitutor(final StrLookup variableResolver)
    public StrSubstitutor(final StrLookup variableResolver, final String prefix, final String suffix, final char escape)
    public StrSubstitutor(final StrLookup variableResolver, final String prefix, final String suffix, final char escape, final String valueDelimiter)
    public StrSubstitutor(final StrLookup variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape)
    public StrSubstitutor(final StrLookup variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape, final StrMatcher valueDelimiterMatcher)
    public StrSubstitutor(final StrLookup variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape, final StrMatcher valueDelimiterMatcher, final StrMatcher valueEscapeMatcher)
    '''
def replace():
    '''    public static String replace(final Object source, final Map<String, String> valueMap)
    public static String replace(final Object source, final Map<String, String> valueMap, final String prefix, final String suffix)
    public static String replace(final Object source, final Properties valueProperties)
    public String replace(final String source)
    public String replace(final LogEvent event, final String source)
    public String replace(final String source, final int offset, final int length)
    public String replace(final LogEvent event, final String source, final int offset, final int length)
    public String replace(final char[] source)
    public String replace(final LogEvent event, final char[] source)
    public String replace(final char[] source, final int offset, final int length)
    public String replace(final LogEvent event, final char[] source, final int offset, final int length)
    public String replace(final StringBuffer source)
    public String replace(final LogEvent event, final StringBuffer source)
    public String replace(final StringBuffer source, final int offset, final int length)
    public String replace(final LogEvent event, final StringBuffer source, final int offset, final int length)
    public String replace(final StringBuilder source)
    public String replace(final LogEvent event, final StringBuilder source)
    public String replace(final StringBuilder source, final int offset, final int length)
    public String replace(final LogEvent event, final StringBuilder source, final int offset, final int length)
    public String replace(final Object source)
    public String replace(final LogEvent event, final Object source)
    '''
def replaceIn():
    '''    public boolean replaceIn(final StringBuffer source)
    public boolean replaceIn(final StringBuffer source, final int offset, final int length)
    public boolean replaceIn(final LogEvent event, final StringBuffer source, final int offset, final int length)
    public boolean replaceIn(final StringBuilder source)
    public boolean replaceIn(final LogEvent event, final StringBuilder source)
    public boolean replaceIn(final StringBuilder source, final int offset, final int length)
    public boolean replaceIn(final LogEvent event, final StringBuilder source, final int offset, final int length)
    '''
def getEscapeChar():
    '''    public char getEscapeChar()
    '''
def setEscapeChar():
    '''    public void setEscapeChar(final char escapeCharacter)
    '''
def getVariablePrefixMatcher():
    '''    public StrMatcher getVariablePrefixMatcher()
    '''
def setVariablePrefixMatcher():
    '''    public StrSubstitutor setVariablePrefixMatcher(final StrMatcher prefixMatcher)
    '''
def setVariablePrefix():
    '''    public StrSubstitutor setVariablePrefix(final char prefix)
    public StrSubstitutor setVariablePrefix(final String prefix)
    '''
def getVariableSuffixMatcher():
    '''    public StrMatcher getVariableSuffixMatcher()
    '''
def setVariableSuffixMatcher():
    '''    public StrSubstitutor setVariableSuffixMatcher(final StrMatcher suffixMatcher)
    '''
def setVariableSuffix():
    '''    public StrSubstitutor setVariableSuffix(final char suffix)
    public StrSubstitutor setVariableSuffix(final String suffix)
    '''
def getValueDelimiterMatcher():
    '''    public StrMatcher getValueDelimiterMatcher()
    '''
def setValueDelimiterMatcher():
    '''    public StrSubstitutor setValueDelimiterMatcher(final StrMatcher valueDelimiterMatcher)
    '''
def setValueDelimiter():
    '''    public StrSubstitutor setValueDelimiter(final char valueDelimiter)
    public StrSubstitutor setValueDelimiter(final String valueDelimiter)
    '''
def getVariableResolver():
    '''    public StrLookup getVariableResolver()
    '''
def setVariableResolver():
    '''    public void setVariableResolver(final StrLookup variableResolver)
    '''
def isEnableSubstitutionInVariables():
    '''    public boolean isEnableSubstitutionInVariables()
    '''
def setEnableSubstitutionInVariables():
    '''    public void setEnableSubstitutionInVariables(final boolean enableSubstitutionInVariables)
    '''
def appendWithSeparators():
    '''    public void appendWithSeparators(final StringBuilder sb, final Iterable<?> iterable, String separator)
    '''
def toString():
    '''    public String toString()
    '''
def setConfiguration():
    '''    public void setConfiguration(final Configuration configuration)
    '''
