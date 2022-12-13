SINGLE_SCRIPT_CONFUSABLE = "int 1"
MIXED_SCRIPT_CONFUSABLE = "int 2"
WHOLE_SCRIPT_CONFUSABLE = "int 4"
CONFUSABLE = "int 7"
ANY_CASE = "int 8"
RESTRICTION_LEVEL = "int 16"
SINGLE_SCRIPT = "int 16"
INVISIBLE = "int 32"
CHAR_LIMIT = "int 64"
MIXED_NUMBERS = "int 128"
HIDDEN_OVERLAY = "int 256"
ALL_CHECKS = "int -1"
FORMAT_VERSION = "int 2"
def getRestrictionLevel():
'''public RestrictionLevel getRestrictionLevel()
'''
pass
def getChecks():
'''public int getChecks()
'''
pass
def getAllowedLocales():
'''public Set<ULocale> getAllowedLocales()
'''
pass
def getAllowedJavaLocales():
'''public Set<Locale> getAllowedJavaLocales()
'''
pass
def getAllowedChars():
'''public UnicodeSet getAllowedChars()
'''
pass
def failsChecks():
'''public boolean failsChecks(final String text, final CheckResult checkResult)
public boolean failsChecks(final String text)
'''
pass
def areConfusable():
'''public int areConfusable(final String s1, final String s2)
'''
pass
def getSkeleton():
'''public String getSkeleton(final CharSequence str)
public String getSkeleton(final int type, final String id)
'''
pass
def equals():
'''public boolean equals(final Object other)
public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def Builder():
'''public Builder()
public Builder(final SpoofChecker src)
'''
pass
def build():
'''public SpoofChecker build()
'''
pass
def setData():
'''public Builder setData(final Reader confusables)
public Builder setData(final Reader confusables, final Reader confusablesWholeScript)
'''
pass
def setChecks():
'''public Builder setChecks(final int checks)
'''
pass
def setAllowedLocales():
'''public Builder setAllowedLocales(final Set<ULocale> locales)
'''
pass
def setAllowedJavaLocales():
'''public Builder setAllowedJavaLocales(final Set<Locale> locales)
'''
pass
def setAllowedChars():
'''public Builder setAllowedChars(final UnicodeSet chars)
'''
pass
def setRestrictionLevel():
'''public Builder setRestrictionLevel(final RestrictionLevel restrictionLevel)
'''
pass
def buildConfusableData():
'''public static void buildConfusableData(final Reader confusables, final SpoofData dest)
'''
pass
def compare():
'''public int compare(final SPUString sL, final SPUString sR)
'''
pass
def SPUStringPool():
'''public SPUStringPool()
'''
pass
def size():
'''public int size()
'''
pass
def getByIndex():
'''public SPUString getByIndex(final int index)
'''
pass
def addString():
'''public SPUString addString(final String src)
'''
pass
def sort():
'''public void sort()
'''
pass
def CheckResult():
'''public CheckResult()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def keyToCodePoint():
'''public static final int keyToCodePoint(final int key)
'''
pass
def keyToLength():
'''public static final int keyToLength(final int key)
'''
pass
def codePointAndLengthToKey():
'''public static final int codePointAndLengthToKey(final int codePoint, final int length)
'''
pass
def getDefault():
'''public static SpoofData getDefault()
'''
pass
def confusableLookup():
'''public void confusableLookup(final int inChar, final StringBuilder dest)
'''
pass
def length():
'''public int length()
'''
pass
def codePointAt():
'''public int codePointAt(final int index)
'''
pass
def appendValueTo():
'''public void appendValueTo(final int index, final StringBuilder dest)
'''
pass
def isDataVersionAcceptable():
'''public boolean isDataVersionAcceptable(final byte[] version)
'''
pass
def and():
'''public void and(final int script)
'''
pass
def setAll():
'''public void setAll()
'''
pass
def isFull():
'''public boolean isFull()
'''
pass
def appendStringTo():
'''public void appendStringTo(final StringBuilder sb)
'''
pass
