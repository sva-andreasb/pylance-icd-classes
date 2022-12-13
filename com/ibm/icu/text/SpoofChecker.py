SINGLE_SCRIPT_CONFUSABLE = "int  1"
MIXED_SCRIPT_CONFUSABLE = "int  2"
WHOLE_SCRIPT_CONFUSABLE = "int  4"
CONFUSABLE = "int  7"
ANY_CASE = "int  8"
RESTRICTION_LEVEL = "int  16"
SINGLE_SCRIPT = "int  16"
INVISIBLE = "int  32"
CHAR_LIMIT = "int  64"
MIXED_NUMBERS = "int  128"
HIDDEN_OVERLAY = "int  256"
ALL_CHECKS = "int  -1"
FORMAT_VERSION = "int  2"
def getRestrictionLevel():
    '''    public RestrictionLevel getRestrictionLevel()
    '''
def getChecks():
    '''    public int getChecks()
    '''
def getAllowedLocales():
    '''    public Set<ULocale> getAllowedLocales()
    '''
def getAllowedJavaLocales():
    '''    public Set<Locale> getAllowedJavaLocales()
    '''
def getAllowedChars():
    '''    public UnicodeSet getAllowedChars()
    '''
def failsChecks():
    '''    public boolean failsChecks(final String text, final CheckResult checkResult)
    public boolean failsChecks(final String text)
    '''
def areConfusable():
    '''    public int areConfusable(final String s1, final String s2)
    '''
def getSkeleton():
    '''    public String getSkeleton(final CharSequence str)
    public String getSkeleton(final int type, final String id)
    '''
def equals():
    '''    public boolean equals(final Object other)
    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def Builder():
    '''    public Builder()
    public Builder(final SpoofChecker src)
    '''
def build():
    '''    public SpoofChecker build()
    '''
def setData():
    '''    public Builder setData(final Reader confusables)
    public Builder setData(final Reader confusables, final Reader confusablesWholeScript)
    '''
def setChecks():
    '''    public Builder setChecks(final int checks)
    '''
def setAllowedLocales():
    '''    public Builder setAllowedLocales(final Set<ULocale> locales)
    '''
def setAllowedJavaLocales():
    '''    public Builder setAllowedJavaLocales(final Set<Locale> locales)
    '''
def setAllowedChars():
    '''    public Builder setAllowedChars(final UnicodeSet chars)
    '''
def setRestrictionLevel():
    '''    public Builder setRestrictionLevel(final RestrictionLevel restrictionLevel)
    '''
def buildConfusableData():
    '''    public static void buildConfusableData(final Reader confusables, final SpoofData dest)
    '''
def compare():
    '''    public int compare(final SPUString sL, final SPUString sR)
    '''
def SPUStringPool():
    '''    public SPUStringPool()
    '''
def size():
    '''    public int size()
    '''
def getByIndex():
    '''    public SPUString getByIndex(final int index)
    '''
def addString():
    '''    public SPUString addString(final String src)
    '''
def sort():
    '''    public void sort()
    '''
def CheckResult():
    '''    public CheckResult()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def keyToCodePoint():
    '''    public static final int keyToCodePoint(final int key)
    '''
def keyToLength():
    '''    public static final int keyToLength(final int key)
    '''
def codePointAndLengthToKey():
    '''    public static final int codePointAndLengthToKey(final int codePoint, final int length)
    '''
def getDefault():
    '''    public static SpoofData getDefault()
    '''
def confusableLookup():
    '''    public void confusableLookup(final int inChar, final StringBuilder dest)
    '''
def length():
    '''    public int length()
    '''
def codePointAt():
    '''    public int codePointAt(final int index)
    '''
def appendValueTo():
    '''    public void appendValueTo(final int index, final StringBuilder dest)
    '''
def isDataVersionAcceptable():
    '''    public boolean isDataVersionAcceptable(final byte[] version)
    '''
def and():
    '''    public void and(final int script)
    '''
def setAll():
    '''    public void setAll()
    '''
def isFull():
    '''    public boolean isFull()
    '''
def appendStringTo():
    '''    public void appendStringTo(final StringBuilder sb)
    '''
