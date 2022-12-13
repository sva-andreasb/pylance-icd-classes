PRIVATE_USE_EXTENSION = "char  'x'"
UNICODE_LOCALE_EXTENSION = "char  'u'"
def forLocale():
    '''public static ULocale forLocale(final Locale loc)
    '''
def ULocale():
    '''public ULocale(final String localeID)
    public ULocale(final String a, final String b)
    public ULocale(final String a, final String b, final String c)
    '''
def createCanonical():
    '''public static ULocale createCanonical(final String nonCanonicalID)
    public static ULocale createCanonical(final ULocale locale)
    '''
def toLocale():
    '''public Locale toLocale()
    public static Locale toLocale(final ULocale uloc)
    '''
def getDefault():
    '''public static ULocale getDefault()
    public static ULocale getDefault(final Category category)
    public static Locale getDefault(final Category category)
    '''
def setDefault():
    '''public static synchronized void setDefault(final ULocale newLocale)
    public static synchronized void setDefault(final Category category, final ULocale newLocale)
    public static void setDefault(final Category category, final Locale newLocale)
    '''
def clone():
    '''public Object clone()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def compareTo():
    '''public int compareTo(final ULocale other)
    '''
def getAvailableLocales():
    '''public static ULocale[] getAvailableLocales()
    '''
def getAvailableLocalesByType():
    '''public static Collection<ULocale> getAvailableLocalesByType(final AvailableType type)
    '''
def getISOCountries():
    '''public static String[] getISOCountries()
    '''
def getISOLanguages():
    '''public static String[] getISOLanguages()
    '''
def getLanguage():
    '''public String getLanguage()
    public static String getLanguage(final String localeID)
    '''
def getScript():
    '''public String getScript()
    public static String getScript(final String localeID)
    '''
def getCountry():
    '''public String getCountry()
    public static String getCountry(final String localeID)
    '''
def getRegionForSupplementalData():
    '''public static String getRegionForSupplementalData(final ULocale locale, final boolean inferRegion)
    '''
def getVariant():
    '''public String getVariant()
    public static String getVariant(final String localeID)
    '''
def getFallback():
    '''public static String getFallback(final String localeID)
    public ULocale getFallback()
    '''
def getBaseName():
    '''public String getBaseName()
    public static String getBaseName(final String localeID)
    '''
def getName():
    '''public String getName()
    public static String getName(final String localeID)
    '''
def toString():
    '''public String toString()
    '''
def getKeywords():
    '''public Iterator<String> getKeywords()
    public static Iterator<String> getKeywords(final String localeID)
    '''
def getKeywordValue():
    '''public String getKeywordValue(final String keywordName)
    public static String getKeywordValue(final String localeID, final String keywordName)
    '''
def canonicalize():
    '''public static String canonicalize(final String localeID)
    '''
def setKeywordValue():
    '''public ULocale setKeywordValue(final String keyword, final String value)
    public static String setKeywordValue(final String localeID, final String keyword, final String value)
    '''
def getISO3Language():
    '''public String getISO3Language()
    public static String getISO3Language(final String localeID)
    '''
def getISO3Country():
    '''public String getISO3Country()
    public static String getISO3Country(final String localeID)
    '''
def isRightToLeft():
    '''public boolean isRightToLeft()
    '''
def getDisplayLanguage():
    '''public String getDisplayLanguage()
    public String getDisplayLanguage(final ULocale displayLocale)
    public static String getDisplayLanguage(final String localeID, final String displayLocaleID)
    public static String getDisplayLanguage(final String localeID, final ULocale displayLocale)
    '''
def getDisplayLanguageWithDialect():
    '''public String getDisplayLanguageWithDialect()
    public String getDisplayLanguageWithDialect(final ULocale displayLocale)
    public static String getDisplayLanguageWithDialect(final String localeID, final String displayLocaleID)
    public static String getDisplayLanguageWithDialect(final String localeID, final ULocale displayLocale)
    '''
def getDisplayScript():
    '''public String getDisplayScript()
    public String getDisplayScript(final ULocale displayLocale)
    public static String getDisplayScript(final String localeID, final String displayLocaleID)
    public static String getDisplayScript(final String localeID, final ULocale displayLocale)
    '''
def getDisplayScriptInContext():
    '''public String getDisplayScriptInContext()
    public String getDisplayScriptInContext(final ULocale displayLocale)
    public static String getDisplayScriptInContext(final String localeID, final String displayLocaleID)
    public static String getDisplayScriptInContext(final String localeID, final ULocale displayLocale)
    '''
def getDisplayCountry():
    '''public String getDisplayCountry()
    public String getDisplayCountry(final ULocale displayLocale)
    public static String getDisplayCountry(final String localeID, final String displayLocaleID)
    public static String getDisplayCountry(final String localeID, final ULocale displayLocale)
    '''
def getDisplayVariant():
    '''public String getDisplayVariant()
    public String getDisplayVariant(final ULocale displayLocale)
    public static String getDisplayVariant(final String localeID, final String displayLocaleID)
    public static String getDisplayVariant(final String localeID, final ULocale displayLocale)
    '''
def getDisplayKeyword():
    '''public static String getDisplayKeyword(final String keyword)
    public static String getDisplayKeyword(final String keyword, final String displayLocaleID)
    public static String getDisplayKeyword(final String keyword, final ULocale displayLocale)
    '''
def getDisplayKeywordValue():
    '''public String getDisplayKeywordValue(final String keyword)
    public String getDisplayKeywordValue(final String keyword, final ULocale displayLocale)
    public static String getDisplayKeywordValue(final String localeID, final String keyword, final String displayLocaleID)
    public static String getDisplayKeywordValue(final String localeID, final String keyword, final ULocale displayLocale)
    '''
def getDisplayName():
    '''public String getDisplayName()
    public String getDisplayName(final ULocale displayLocale)
    public static String getDisplayName(final String localeID, final String displayLocaleID)
    public static String getDisplayName(final String localeID, final ULocale displayLocale)
    '''
def getDisplayNameWithDialect():
    '''public String getDisplayNameWithDialect()
    public String getDisplayNameWithDialect(final ULocale displayLocale)
    public static String getDisplayNameWithDialect(final String localeID, final String displayLocaleID)
    public static String getDisplayNameWithDialect(final String localeID, final ULocale displayLocale)
    '''
def getCharacterOrientation():
    '''public String getCharacterOrientation()
    '''
def getLineOrientation():
    '''public String getLineOrientation()
    '''
def acceptLanguage():
    '''public static ULocale acceptLanguage(final String acceptLanguageList, final ULocale[] availableLocales, final boolean[] fallback)
    public static ULocale acceptLanguage(final ULocale[] acceptLanguageList, final ULocale[] availableLocales, final boolean[] fallback)
    public static ULocale acceptLanguage(final String acceptLanguageList, final boolean[] fallback)
    public static ULocale acceptLanguage(final ULocale[] acceptLanguageList, final boolean[] fallback)
    '''
def addLikelySubtags():
    '''public static ULocale addLikelySubtags(final ULocale loc)
    '''
def minimizeSubtags():
    '''public static ULocale minimizeSubtags(final ULocale loc)
    public static ULocale minimizeSubtags(final ULocale loc, final Minimize fieldToFavor)
    '''
def getExtension():
    '''public String getExtension(final char key)
    '''
def getExtensionKeys():
    '''public Set<Character> getExtensionKeys()
    '''
def getUnicodeLocaleAttributes():
    '''public Set<String> getUnicodeLocaleAttributes()
    '''
def getUnicodeLocaleType():
    '''public String getUnicodeLocaleType(final String key)
    '''
def getUnicodeLocaleKeys():
    '''public Set<String> getUnicodeLocaleKeys()
    '''
def toLanguageTag():
    '''public String toLanguageTag()
    '''
def forLanguageTag():
    '''public static ULocale forLanguageTag(final String languageTag)
    '''
def toUnicodeLocaleKey():
    '''public static String toUnicodeLocaleKey(final String keyword)
    '''
def toUnicodeLocaleType():
    '''public static String toUnicodeLocaleType(final String keyword, final String value)
    '''
def toLegacyKey():
    '''public static String toLegacyKey(final String keyword)
    '''
def toLegacyType():
    '''public static String toLegacyType(final String keyword, final String value)
    '''
def Builder():
    '''public Builder()
    '''
def setLocale():
    '''public Builder setLocale(final ULocale locale)
    '''
def setLanguageTag():
    '''public Builder setLanguageTag(final String languageTag)
    '''
def setLanguage():
    '''public Builder setLanguage(final String language)
    '''
def setScript():
    '''public Builder setScript(final String script)
    '''
def setRegion():
    '''public Builder setRegion(final String region)
    '''
def setVariant():
    '''public Builder setVariant(final String variant)
    '''
def setExtension():
    '''public Builder setExtension(final char key, final String value)
    '''
def setUnicodeLocaleKeyword():
    '''public Builder setUnicodeLocaleKeyword(final String key, final String type)
    '''
def addUnicodeLocaleAttribute():
    '''public Builder addUnicodeLocaleAttribute(final String attribute)
    '''
def removeUnicodeLocaleAttribute():
    '''public Builder removeUnicodeLocaleAttribute(final String attribute)
    '''
def clear():
    '''public Builder clear()
    '''
def clearExtensions():
    '''public Builder clearExtensions()
    '''
def build():
    '''public ULocale build()
    '''
def hasLocaleCategories():
    '''public static boolean hasLocaleCategories()
    '''
def toULocale():
    '''public static ULocale toULocale(final Locale loc)
    '''
