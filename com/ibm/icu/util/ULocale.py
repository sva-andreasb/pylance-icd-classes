PRIVATE_USE_EXTENSION = "char  'x'"
UNICODE_LOCALE_EXTENSION = "char  'u'"
def ():
    '''returns Builder\n\n
    (final String localeID)\n
    (final String a, final String b)\n
    (final String a, final String b, final String c)\n
    (final double theq, final int theserial)\n
    ()\n
    (final boolean isLenientVariant)\n
    '''
def toLocale():
    '''returns Locale\n\n
    toLocale()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def getScript():
    '''returns String\n\n
    getScript()\n
    '''
def getCountry():
    '''returns String\n\n
    getCountry()\n
    '''
def getVariant():
    '''returns String\n\n
    getVariant()\n
    '''
def getFallback():
    '''returns ULocale\n\n
    getFallback()\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getKeywords():
    '''returns Iterator<String>\n\n
    getKeywords()\n
    '''
def getKeywordValue():
    '''returns String\n\n
    getKeywordValue(final String keywordName)\n
    '''
def setKeywordValue():
    '''returns ULocale\n\n
    setKeywordValue(final String keyword, final String value)\n
    '''
def getISO3Language():
    '''returns String\n\n
    getISO3Language()\n
    '''
def getISO3Country():
    '''returns String\n\n
    getISO3Country()\n
    '''
def getDisplayLanguage():
    '''returns String\n\n
    getDisplayLanguage()\n
    getDisplayLanguage(final ULocale displayLocale)\n
    '''
def getDisplayLanguageWithDialect():
    '''returns String\n\n
    getDisplayLanguageWithDialect()\n
    getDisplayLanguageWithDialect(final ULocale displayLocale)\n
    '''
def getDisplayScript():
    '''returns String\n\n
    getDisplayScript()\n
    getDisplayScript(final ULocale displayLocale)\n
    '''
def getDisplayCountry():
    '''returns String\n\n
    getDisplayCountry()\n
    getDisplayCountry(final ULocale displayLocale)\n
    '''
def getDisplayVariant():
    '''returns String\n\n
    getDisplayVariant()\n
    getDisplayVariant(final ULocale displayLocale)\n
    '''
def getDisplayKeywordValue():
    '''returns String\n\n
    getDisplayKeywordValue(final String keyword)\n
    getDisplayKeywordValue(final String keyword, final ULocale displayLocale)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName()\n
    getDisplayName(final ULocale displayLocale)\n
    '''
def getDisplayNameWithDialect():
    '''returns String\n\n
    getDisplayNameWithDialect()\n
    getDisplayNameWithDialect(final ULocale displayLocale)\n
    '''
def getCharacterOrientation():
    '''returns String\n\n
    getCharacterOrientation()\n
    '''
def getLineOrientation():
    '''returns String\n\n
    getLineOrientation()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final ULocaleAcceptLanguageQ other)\n
    '''
def getExtension():
    '''returns String\n\n
    getExtension(final char key)\n
    '''
def getExtensionKeys():
    '''returns Set<Character>\n\n
    getExtensionKeys()\n
    '''
def getUnicodeLocaleType():
    '''returns String\n\n
    getUnicodeLocaleType(final String key)\n
    '''
def getUnicodeLocaleKeys():
    '''returns Set<String>\n\n
    getUnicodeLocaleKeys()\n
    '''
def toLanguageTag():
    '''returns String\n\n
    toLanguageTag()\n
    '''
def isLenientVariant():
    '''returns boolean\n\n
    isLenientVariant()\n
    '''
def setLocale():
    '''returns Builder\n\n
    setLocale(final ULocale locale)\n
    '''
def setLanguageTag():
    '''returns Builder\n\n
    setLanguageTag(final String languageTag)\n
    '''
def setLanguage():
    '''returns Builder\n\n
    setLanguage(final String language)\n
    '''
def setScript():
    '''returns Builder\n\n
    setScript(final String script)\n
    '''
def setRegion():
    '''returns Builder\n\n
    setRegion(final String region)\n
    '''
def setVariant():
    '''returns Builder\n\n
    setVariant(final String variant)\n
    '''
def setExtension():
    '''returns Builder\n\n
    setExtension(final char key, final String value)\n
    '''
def setUnicodeLocaleKeyword():
    '''returns Builder\n\n
    setUnicodeLocaleKeyword(final String key, final String type)\n
    '''
def clear():
    '''returns Builder\n\n
    clear()\n
    '''
def clearExtensions():
    '''returns Builder\n\n
    clearExtensions()\n
    '''
def build():
    '''returns ULocale\n\n
    build()\n
    '''
