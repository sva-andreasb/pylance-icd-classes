PRIVATE_USE_EXTENSION = "char 'x'"
UNICODE_LOCALE_EXTENSION = "char 'u'"
def forLocale():
'''public static ULocale forLocale(final Locale loc)
'''
pass
def ULocale():
'''public ULocale(final String localeID)
public ULocale(final String a, final String b)
public ULocale(final String a, final String b, final String c)
'''
pass
def createCanonical():
'''public static ULocale createCanonical(final String nonCanonicalID)
public static ULocale createCanonical(final ULocale locale)
'''
pass
def toLocale():
'''public Locale toLocale()
public static Locale toLocale(final ULocale uloc)
'''
pass
def getDefault():
'''public static ULocale getDefault()
public static ULocale getDefault(final Category category)
public static Locale getDefault(final Category category)
'''
pass
def setDefault():
'''public static synchronized void setDefault(final ULocale newLocale)
public static synchronized void setDefault(final Category category, final ULocale newLocale)
public static void setDefault(final Category category, final Locale newLocale)
'''
pass
def clone():
'''public Object clone()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def compareTo():
'''public int compareTo(final ULocale other)
'''
pass
def getAvailableLocales():
'''public static ULocale[] getAvailableLocales()
'''
pass
def getAvailableLocalesByType():
'''public static Collection<ULocale> getAvailableLocalesByType(final AvailableType type)
'''
pass
def getISOCountries():
'''public static String[] getISOCountries()
'''
pass
def getISOLanguages():
'''public static String[] getISOLanguages()
'''
pass
def getLanguage():
'''public String getLanguage()
public static String getLanguage(final String localeID)
'''
pass
def getScript():
'''public String getScript()
public static String getScript(final String localeID)
'''
pass
def getCountry():
'''public String getCountry()
public static String getCountry(final String localeID)
'''
pass
def getRegionForSupplementalData():
'''public static String getRegionForSupplementalData(final ULocale locale, final boolean inferRegion)
'''
pass
def getVariant():
'''public String getVariant()
public static String getVariant(final String localeID)
'''
pass
def getFallback():
'''public static String getFallback(final String localeID)
public ULocale getFallback()
'''
pass
def getBaseName():
'''public String getBaseName()
public static String getBaseName(final String localeID)
'''
pass
def getName():
'''public String getName()
public static String getName(final String localeID)
'''
pass
def toString():
'''public String toString()
'''
pass
def getKeywords():
'''public Iterator<String> getKeywords()
public static Iterator<String> getKeywords(final String localeID)
'''
pass
def getKeywordValue():
'''public String getKeywordValue(final String keywordName)
public static String getKeywordValue(final String localeID, final String keywordName)
'''
pass
def canonicalize():
'''public static String canonicalize(final String localeID)
'''
pass
def setKeywordValue():
'''public ULocale setKeywordValue(final String keyword, final String value)
public static String setKeywordValue(final String localeID, final String keyword, final String value)
'''
pass
def getISO3Language():
'''public String getISO3Language()
public static String getISO3Language(final String localeID)
'''
pass
def getISO3Country():
'''public String getISO3Country()
public static String getISO3Country(final String localeID)
'''
pass
def isRightToLeft():
'''public boolean isRightToLeft()
'''
pass
def getDisplayLanguage():
'''public String getDisplayLanguage()
public String getDisplayLanguage(final ULocale displayLocale)
public static String getDisplayLanguage(final String localeID, final String displayLocaleID)
public static String getDisplayLanguage(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayLanguageWithDialect():
'''public String getDisplayLanguageWithDialect()
public String getDisplayLanguageWithDialect(final ULocale displayLocale)
public static String getDisplayLanguageWithDialect(final String localeID, final String displayLocaleID)
public static String getDisplayLanguageWithDialect(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayScript():
'''public String getDisplayScript()
public String getDisplayScript(final ULocale displayLocale)
public static String getDisplayScript(final String localeID, final String displayLocaleID)
public static String getDisplayScript(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayScriptInContext():
'''public String getDisplayScriptInContext()
public String getDisplayScriptInContext(final ULocale displayLocale)
public static String getDisplayScriptInContext(final String localeID, final String displayLocaleID)
public static String getDisplayScriptInContext(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayCountry():
'''public String getDisplayCountry()
public String getDisplayCountry(final ULocale displayLocale)
public static String getDisplayCountry(final String localeID, final String displayLocaleID)
public static String getDisplayCountry(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayVariant():
'''public String getDisplayVariant()
public String getDisplayVariant(final ULocale displayLocale)
public static String getDisplayVariant(final String localeID, final String displayLocaleID)
public static String getDisplayVariant(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayKeyword():
'''public static String getDisplayKeyword(final String keyword)
public static String getDisplayKeyword(final String keyword, final String displayLocaleID)
public static String getDisplayKeyword(final String keyword, final ULocale displayLocale)
'''
pass
def getDisplayKeywordValue():
'''public String getDisplayKeywordValue(final String keyword)
public String getDisplayKeywordValue(final String keyword, final ULocale displayLocale)
public static String getDisplayKeywordValue(final String localeID, final String keyword, final String displayLocaleID)
public static String getDisplayKeywordValue(final String localeID, final String keyword, final ULocale displayLocale)
'''
pass
def getDisplayName():
'''public String getDisplayName()
public String getDisplayName(final ULocale displayLocale)
public static String getDisplayName(final String localeID, final String displayLocaleID)
public static String getDisplayName(final String localeID, final ULocale displayLocale)
'''
pass
def getDisplayNameWithDialect():
'''public String getDisplayNameWithDialect()
public String getDisplayNameWithDialect(final ULocale displayLocale)
public static String getDisplayNameWithDialect(final String localeID, final String displayLocaleID)
public static String getDisplayNameWithDialect(final String localeID, final ULocale displayLocale)
'''
pass
def getCharacterOrientation():
'''public String getCharacterOrientation()
'''
pass
def getLineOrientation():
'''public String getLineOrientation()
'''
pass
def acceptLanguage():
'''public static ULocale acceptLanguage(final String acceptLanguageList, final ULocale[] availableLocales, final boolean[] fallback)
public static ULocale acceptLanguage(final ULocale[] acceptLanguageList, final ULocale[] availableLocales, final boolean[] fallback)
public static ULocale acceptLanguage(final String acceptLanguageList, final boolean[] fallback)
public static ULocale acceptLanguage(final ULocale[] acceptLanguageList, final boolean[] fallback)
'''
pass
def addLikelySubtags():
'''public static ULocale addLikelySubtags(final ULocale loc)
'''
pass
def minimizeSubtags():
'''public static ULocale minimizeSubtags(final ULocale loc)
public static ULocale minimizeSubtags(final ULocale loc, final Minimize fieldToFavor)
'''
pass
def getExtension():
'''public String getExtension(final char key)
'''
pass
def getExtensionKeys():
'''public Set<Character> getExtensionKeys()
'''
pass
def getUnicodeLocaleAttributes():
'''public Set<String> getUnicodeLocaleAttributes()
'''
pass
def getUnicodeLocaleType():
'''public String getUnicodeLocaleType(final String key)
'''
pass
def getUnicodeLocaleKeys():
'''public Set<String> getUnicodeLocaleKeys()
'''
pass
def toLanguageTag():
'''public String toLanguageTag()
'''
pass
def forLanguageTag():
'''public static ULocale forLanguageTag(final String languageTag)
'''
pass
def toUnicodeLocaleKey():
'''public static String toUnicodeLocaleKey(final String keyword)
'''
pass
def toUnicodeLocaleType():
'''public static String toUnicodeLocaleType(final String keyword, final String value)
'''
pass
def toLegacyKey():
'''public static String toLegacyKey(final String keyword)
'''
pass
def toLegacyType():
'''public static String toLegacyType(final String keyword, final String value)
'''
pass
def Builder():
'''public Builder()
'''
pass
def setLocale():
'''public Builder setLocale(final ULocale locale)
'''
pass
def setLanguageTag():
'''public Builder setLanguageTag(final String languageTag)
'''
pass
def setLanguage():
'''public Builder setLanguage(final String language)
'''
pass
def setScript():
'''public Builder setScript(final String script)
'''
pass
def setRegion():
'''public Builder setRegion(final String region)
'''
pass
def setVariant():
'''public Builder setVariant(final String variant)
'''
pass
def setExtension():
'''public Builder setExtension(final char key, final String value)
'''
pass
def setUnicodeLocaleKeyword():
'''public Builder setUnicodeLocaleKeyword(final String key, final String type)
'''
pass
def addUnicodeLocaleAttribute():
'''public Builder addUnicodeLocaleAttribute(final String attribute)
'''
pass
def removeUnicodeLocaleAttribute():
'''public Builder removeUnicodeLocaleAttribute(final String attribute)
'''
pass
def clear():
'''public Builder clear()
'''
pass
def clearExtensions():
'''public Builder clearExtensions()
'''
pass
def build():
'''public ULocale build()
'''
pass
def hasLocaleCategories():
'''public static boolean hasLocaleCategories()
'''
pass
def toULocale():
'''public static ULocale toULocale(final Locale loc)
'''
pass
