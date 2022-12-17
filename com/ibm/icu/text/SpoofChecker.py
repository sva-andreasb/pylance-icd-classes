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
    '''returns RestrictionLevel\n\n
    getRestrictionLevel()\n
    '''
def getChecks():
    '''returns int\n\n
    getChecks()\n
    '''
def getAllowedLocales():
    '''returns Set<ULocale>\n\n
    getAllowedLocales()\n
    '''
def getAllowedJavaLocales():
    '''returns Set<Locale>\n\n
    getAllowedJavaLocales()\n
    '''
def getAllowedChars():
    '''returns UnicodeSet\n\n
    getAllowedChars()\n
    '''
def failsChecks():
    '''returns boolean\n\n
    failsChecks(final String text, final CheckResult checkResult)\n
    failsChecks(final String text)\n
    '''
def areConfusable():
    '''returns int\n\n
    areConfusable(final String s1, final String s2)\n
    '''
def getSkeleton():
    '''returns String\n\n
    getSkeleton(final CharSequence str)\n
    getSkeleton(final int type, final String id)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def ():
    '''returns CheckResult\n\n
    ()\n
    (final SpoofChecker src)\n
    ()\n
    ()\n
    '''
def build():
    '''returns SpoofChecker\n\n
    build()\n
    '''
def setData():
    '''returns Builder\n\n
    setData(final Reader confusables)\n
    setData(final Reader confusables, final Reader confusablesWholeScript)\n
    '''
def setChecks():
    '''returns Builder\n\n
    setChecks(final int checks)\n
    '''
def setAllowedLocales():
    '''returns Builder\n\n
    setAllowedLocales(final Set<ULocale> locales)\n
    '''
def setAllowedJavaLocales():
    '''returns Builder\n\n
    setAllowedJavaLocales(final Set<Locale> locales)\n
    '''
def setAllowedChars():
    '''returns Builder\n\n
    setAllowedChars(final UnicodeSet chars)\n
    '''
def setRestrictionLevel():
    '''returns Builder\n\n
    setRestrictionLevel(final RestrictionLevel restrictionLevel)\n
    '''
def compare():
    '''returns int\n\n
    compare(final SPUString sL, final SPUString sR)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getByIndex():
    '''returns SPUString\n\n
    getByIndex(final int index)\n
    '''
def addString():
    '''returns SPUString\n\n
    addString(final String src)\n
    '''
def sort():
    '''returns None\n\n
    sort()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def confusableLookup():
    '''returns None\n\n
    confusableLookup(final int inChar, final StringBuilder dest)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def codePointAt():
    '''returns int\n\n
    codePointAt(final int index)\n
    '''
def appendValueTo():
    '''returns None\n\n
    appendValueTo(final int index, final StringBuilder dest)\n
    '''
def isDataVersionAcceptable():
    '''returns boolean\n\n
    isDataVersionAcceptable(final byte[] version)\n
    '''
def and():
    '''returns None\n\n
    and(final int script)\n
    '''
def setAll():
    '''returns None\n\n
    setAll()\n
    '''
def isFull():
    '''returns boolean\n\n
    isFull()\n
    '''
def appendStringTo():
    '''returns None\n\n
    appendStringTo(final StringBuilder sb)\n
    '''
