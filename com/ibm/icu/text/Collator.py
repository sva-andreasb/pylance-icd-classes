PRIMARY = "int 0"
SECONDARY = "int 1"
TERTIARY = "int 2"
QUATERNARY = "int 3"
IDENTICAL = "int 15"
FULL_DECOMPOSITION = "int 15"
NO_DECOMPOSITION = "int 16"
CANONICAL_DECOMPOSITION = "int 17"
DEFAULT = "int -1"
NONE = "int 103"
OTHERS = "int 103"
SPACE = "int 4096"
FIRST = "int 4096"
PUNCTUATION = "int 4097"
SYMBOL = "int 4098"
CURRENCY = "int 4099"
DIGIT = "int 4100"
LIMIT = "int 4101"
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final String source, final String target)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def setStrength():
'''public void setStrength(final int newStrength)
'''
pass
def setStrength2():
'''public Collator setStrength2(final int newStrength)
'''
pass
def setDecomposition():
'''public void setDecomposition(final int decomposition)
'''
pass
def setReorderCodes():
'''public void setReorderCodes(final int... order)
'''
pass
def getInstance():
'''public static final Collator getInstance()
public static final Collator getInstance(ULocale locale)
public static final Collator getInstance(final Locale locale)
'''
pass
def clone():
'''public Object clone()
'''
pass
def registerInstance():
'''public static final Object registerInstance(final Collator collator, final ULocale locale)
'''
pass
def registerFactory():
'''public static final Object registerFactory(final CollatorFactory factory)
'''
pass
def unregister():
'''public static final boolean unregister(final Object registryKey)
'''
pass
def getAvailableLocales():
'''public static Locale[] getAvailableLocales()
'''
pass
def getAvailableULocales():
'''public static final ULocale[] getAvailableULocales()
'''
pass
def getKeywords():
'''public static final String[] getKeywords()
'''
pass
def getKeywordValues():
'''public static final String[] getKeywordValues(final String keyword)
'''
pass
def getKeywordValuesForLocale():
'''public static final String[] getKeywordValuesForLocale(final String key, final ULocale locale, final boolean commonlyUsed)
'''
pass
def getFunctionalEquivalent():
'''public static final ULocale getFunctionalEquivalent(final String keyword, final ULocale locID, final boolean[] isAvailable)
public static final ULocale getFunctionalEquivalent(final String keyword, final ULocale locID)
'''
pass
def getDisplayName():
'''public static String getDisplayName(final Locale objectLocale, final Locale displayLocale)
public static String getDisplayName(final ULocale objectLocale, final ULocale displayLocale)
public static String getDisplayName(final Locale objectLocale)
public static String getDisplayName(final ULocale objectLocale)
public String getDisplayName(final Locale objectLocale, final Locale displayLocale)
public String getDisplayName(final ULocale objectLocale, final ULocale displayLocale)
'''
pass
def getStrength():
'''public int getStrength()
'''
pass
def getDecomposition():
'''public int getDecomposition()
'''
pass
def getTailoredSet():
'''public UnicodeSet getTailoredSet()
'''
pass
def compare():
'''public int compare(final Object source, final Object target)
'''
pass
def setMaxVariable():
'''public Collator setMaxVariable(final int group)
'''
pass
def getMaxVariable():
'''public int getMaxVariable()
'''
pass
def getReorderCodes():
'''public int[] getReorderCodes()
'''
pass
def getEquivalentReorderCodes():
'''public static int[] getEquivalentReorderCodes(final int reorderCode)
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public Collator freeze()
'''
pass
def cloneAsThawed():
'''public Collator cloneAsThawed()
'''
pass
def getLocale():
'''public ULocale getLocale(final ULocale.Type type)
'''
pass
def visible():
'''public boolean visible()
'''
pass
def createCollator():
'''public Collator createCollator(final ULocale loc)
public Collator createCollator(final Locale loc)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
