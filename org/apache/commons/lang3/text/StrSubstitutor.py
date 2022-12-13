DEFAULT_ESCAPE = "char  '$'"
def replace():
'''public static <V> String replace(final Object source, final Map<String, V> valueMap)
public static <V> String replace(final Object source, final Map<String, V> valueMap, final String prefix, final String suffix)
public static String replace(final Object source, final Properties valueProperties)
public String replace(final String source)
public String replace(final String source, final int offset, final int length)
public String replace(final char[] source)
public String replace(final char[] source, final int offset, final int length)
public String replace(final StringBuffer source)
public String replace(final StringBuffer source, final int offset, final int length)
public String replace(final CharSequence source)
public String replace(final CharSequence source, final int offset, final int length)
public String replace(final StrBuilder source)
public String replace(final StrBuilder source, final int offset, final int length)
public String replace(final Object source)
'''
pass
def replaceSystemProperties():
'''public static String replaceSystemProperties(final Object source)
'''
pass
def StrSubstitutor():
'''public StrSubstitutor()
public <V> StrSubstitutor(final Map<String, V> valueMap)
public <V> StrSubstitutor(final Map<String, V> valueMap, final String prefix, final String suffix)
public <V> StrSubstitutor(final Map<String, V> valueMap, final String prefix, final String suffix, final char escape)
public <V> StrSubstitutor(final Map<String, V> valueMap, final String prefix, final String suffix, final char escape, final String valueDelimiter)
public StrSubstitutor(final StrLookup<?> variableResolver)
public StrSubstitutor(final StrLookup<?> variableResolver, final String prefix, final String suffix, final char escape)
public StrSubstitutor(final StrLookup<?> variableResolver, final String prefix, final String suffix, final char escape, final String valueDelimiter)
public StrSubstitutor(final StrLookup<?> variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape)
public StrSubstitutor(final StrLookup<?> variableResolver, final StrMatcher prefixMatcher, final StrMatcher suffixMatcher, final char escape, final StrMatcher valueDelimiterMatcher)
'''
pass
def replaceIn():
'''public boolean replaceIn(final StringBuffer source)
public boolean replaceIn(final StringBuffer source, final int offset, final int length)
public boolean replaceIn(final StringBuilder source)
public boolean replaceIn(final StringBuilder source, final int offset, final int length)
public boolean replaceIn(final StrBuilder source)
public boolean replaceIn(final StrBuilder source, final int offset, final int length)
'''
pass
def getEscapeChar():
'''public char getEscapeChar()
'''
pass
def setEscapeChar():
'''public void setEscapeChar(final char escapeCharacter)
'''
pass
def getVariablePrefixMatcher():
'''public StrMatcher getVariablePrefixMatcher()
'''
pass
def setVariablePrefixMatcher():
'''public StrSubstitutor setVariablePrefixMatcher(final StrMatcher prefixMatcher)
'''
pass
def setVariablePrefix():
'''public StrSubstitutor setVariablePrefix(final char prefix)
public StrSubstitutor setVariablePrefix(final String prefix)
'''
pass
def getVariableSuffixMatcher():
'''public StrMatcher getVariableSuffixMatcher()
'''
pass
def setVariableSuffixMatcher():
'''public StrSubstitutor setVariableSuffixMatcher(final StrMatcher suffixMatcher)
'''
pass
def setVariableSuffix():
'''public StrSubstitutor setVariableSuffix(final char suffix)
public StrSubstitutor setVariableSuffix(final String suffix)
'''
pass
def getValueDelimiterMatcher():
'''public StrMatcher getValueDelimiterMatcher()
'''
pass
def setValueDelimiterMatcher():
'''public StrSubstitutor setValueDelimiterMatcher(final StrMatcher valueDelimiterMatcher)
'''
pass
def setValueDelimiter():
'''public StrSubstitutor setValueDelimiter(final char valueDelimiter)
public StrSubstitutor setValueDelimiter(final String valueDelimiter)
'''
pass
def setVariableResolver():
'''public void setVariableResolver(final StrLookup<?> variableResolver)
'''
pass
def isEnableSubstitutionInVariables():
'''public boolean isEnableSubstitutionInVariables()
'''
pass
def setEnableSubstitutionInVariables():
'''public void setEnableSubstitutionInVariables(final boolean enableSubstitutionInVariables)
'''
pass
