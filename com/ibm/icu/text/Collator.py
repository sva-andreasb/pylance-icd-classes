PRIMARY = "int  0"
SECONDARY = "int  1"
TERTIARY = "int  2"
QUATERNARY = "int  3"
IDENTICAL = "int  15"
FULL_DECOMPOSITION = "int  15"
NO_DECOMPOSITION = "int  16"
CANONICAL_DECOMPOSITION = "int  17"
DEFAULT = "int  -1"
NONE = "int  103"
OTHERS = "int  103"
SPACE = "int  4096"
FIRST = "int  4096"
PUNCTUATION = "int  4097"
SYMBOL = "int  4098"
CURRENCY = "int  4099"
DIGIT = "int  4100"
LIMIT = "int  4101"
def equals():
    '''public boolean equals(final Object obj)
    public boolean equals(final String source, final String target)
    '''
def hashCode():
    '''public int hashCode()
    '''
def setStrength():
    '''public void setStrength(final int newStrength)
    '''
def setStrength2():
    '''public Collator setStrength2(final int newStrength)
    '''
def setDecomposition():
    '''public void setDecomposition(final int decomposition)
    '''
def setReorderCodes():
    '''public void setReorderCodes(final int... order)
    '''
def getInstance():
    '''public static final Collator getInstance()
    public static final Collator getInstance(ULocale locale)
    public static final Collator getInstance(final Locale locale)
    '''
def clone():
    '''public Object clone()
    '''
def registerInstance():
    '''public static final Object registerInstance(final Collator collator, final ULocale locale)
    '''
def registerFactory():
    '''public static final Object registerFactory(final CollatorFactory factory)
    '''
def unregister():
    '''public static final boolean unregister(final Object registryKey)
    '''
def getAvailableLocales():
    '''public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''public static final ULocale[] getAvailableULocales()
    '''
def getKeywords():
    '''public static final String[] getKeywords()
    '''
def getKeywordValues():
    '''public static final String[] getKeywordValues(final String keyword)
    '''
def getKeywordValuesForLocale():
    '''public static final String[] getKeywordValuesForLocale(final String key, final ULocale locale, final boolean commonlyUsed)
    '''
def getFunctionalEquivalent():
    '''public static final ULocale getFunctionalEquivalent(final String keyword, final ULocale locID, final boolean[] isAvailable)
    public static final ULocale getFunctionalEquivalent(final String keyword, final ULocale locID)
    '''
def getDisplayName():
    '''public static String getDisplayName(final Locale objectLocale, final Locale displayLocale)
    public static String getDisplayName(final ULocale objectLocale, final ULocale displayLocale)
    public static String getDisplayName(final Locale objectLocale)
    public static String getDisplayName(final ULocale objectLocale)
    public String getDisplayName(final Locale objectLocale, final Locale displayLocale)
    public String getDisplayName(final ULocale objectLocale, final ULocale displayLocale)
    '''
def getStrength():
    '''public int getStrength()
    '''
def getDecomposition():
    '''public int getDecomposition()
    '''
def getTailoredSet():
    '''public UnicodeSet getTailoredSet()
    '''
def compare():
    '''public int compare(final Object source, final Object target)
    '''
def setMaxVariable():
    '''public Collator setMaxVariable(final int group)
    '''
def getMaxVariable():
    '''public int getMaxVariable()
    '''
def getReorderCodes():
    '''public int[] getReorderCodes()
    '''
def getEquivalentReorderCodes():
    '''public static int[] getEquivalentReorderCodes(final int reorderCode)
    '''
def isFrozen():
    '''public boolean isFrozen()
    '''
def freeze():
    '''public Collator freeze()
    '''
def cloneAsThawed():
    '''public Collator cloneAsThawed()
    '''
def getLocale():
    '''public ULocale getLocale(final ULocale.Type type)
    '''
def visible():
    '''public boolean visible()
    '''
def createCollator():
    '''public Collator createCollator(final ULocale loc)
    public Collator createCollator(final Locale loc)
    '''
def put():
    '''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
