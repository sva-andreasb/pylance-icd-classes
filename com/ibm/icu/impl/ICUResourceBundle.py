ICU_BUNDLE = "String  \"data/icudt44b\""
ICU_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b\""
ICU_COLLATION_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/coll\""
ICU_BRKITR_NAME = "String  \"/brkitr\""
ICU_BRKITR_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/brkitr\""
ICU_RBNF_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/rbnf\""
ICU_TRANSLIT_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/translit\""
ICU_LANG_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/lang\""
ICU_CURR_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/curr\""
ICU_REGION_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/region\""
ICU_ZONE_BASE_NAME = "String  \"com/ibm/icu/impl/data/icudt44b/zone\""
FROM_FALLBACK = "int  1"
FROM_ROOT = "int  2"
FROM_DEFAULT = "int  3"
FROM_LOCALE = "int  4"
RES_BOGUS = "int  -1"
ALIAS = "int  3"
TABLE32 = "int  4"
TABLE16 = "int  5"
STRING_V2 = "int  6"
ARRAY16 = "int  9"
def setLoadingStatus():
    '''    public void setLoadingStatus(final int newStatus)
    public void setLoadingStatus(final String requestedLocale)
    '''
def getLoadingStatus():
    '''    public int getLoadingStatus()
    '''
def getResPath():
    '''    public String getResPath()
    '''
def getFunctionalEquivalent():
    '''    public static final ULocale getFunctionalEquivalent(final String baseName, final ClassLoader loader, final String resName, final String keyword, final ULocale locID, final boolean[] isAvailable, final boolean omitDefault)
    '''
def getKeywordValues():
    '''    public static final String[] getKeywordValues(final String baseName, final String keyword)
    '''
def getWithFallback():
    '''    public ICUResourceBundle getWithFallback(final String path)
    '''
def at():
    '''    public ICUResourceBundle at(final int index)
    public ICUResourceBundle at(final String key)
    '''
def findTopLevel():
    '''    public ICUResourceBundle findTopLevel(final int index)
    public ICUResourceBundle findTopLevel(final String aKey)
    '''
def findWithFallback():
    '''    public ICUResourceBundle findWithFallback(final String path)
    '''
def getStringWithFallback():
    '''    public String getStringWithFallback(final String path)
    '''
def getAvailableLocaleNameSet():
    '''    public static Set<String> getAvailableLocaleNameSet(final String bundlePrefix, final ClassLoader loader)
    public static Set<String> getAvailableLocaleNameSet()
    '''
def getFullLocaleNameSet():
    '''    public static Set<String> getFullLocaleNameSet()
    public static Set<String> getFullLocaleNameSet(final String bundlePrefix, final ClassLoader loader)
    '''
def getAvailableULocales():
    '''    public static final ULocale[] getAvailableULocales(final String baseName, final ClassLoader loader)
    public static final ULocale[] getAvailableULocales()
    '''
def getAvailableLocales():
    '''    public static final Locale[] getAvailableLocales(final String baseName, final ClassLoader loader)
    public static final Locale[] getAvailableLocales()
    '''
def getLocaleList():
    '''    public static final Locale[] getLocaleList(final ULocale[] ulocales)
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def run():
    '''    public List<String> run()
    '''
def visit():
    '''    public void visit(final String s)
    '''
def equals():
    '''    public boolean equals(final Object other)
    public boolean equals(final Object rhs)
    '''
def getBundleInstance():
    '''    public static UResourceBundle getBundleInstance(final String baseName, final String localeID, final ClassLoader root, final boolean disableFallback)
    '''
def getFullName():
    '''    public static String getFullName(String baseName, String localeName)
    '''
def createBundle():
    '''    public static ICUResourceBundle createBundle(final String baseName, final String localeID, final ClassLoader root)
    '''
def getULocale():
    '''    public ULocale getULocale()
    '''
def getParent():
    '''    public UResourceBundle getParent()
    '''
def getKey():
    '''    public String getKey()
    '''
def getType():
    '''    public int getType()
    '''
def isAlias():
    '''    public boolean isAlias(final int index)
    public boolean isAlias()
    public boolean isAlias(final String k)
    '''
def getAliasPath():
    '''    public String getAliasPath(final int index)
    public String getAliasPath()
    public String getAliasPath(final String k)
    '''
def getKeysSafe():
    '''    public Enumeration<String> getKeysSafe()
    '''
def hashCode():
    '''    public int hashCode()
    '''
