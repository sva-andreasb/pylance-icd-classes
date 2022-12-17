FRENCH_COLLATION_ = "int  0"
ALTERNATE_HANDLING_ = "int  1"
CASE_FIRST_ = "int  2"
CASE_LEVEL_ = "int  3"
NORMALIZATION_MODE_ = "int  4"
STRENGTH_ = "int  5"
HIRAGANA_QUATERNARY_MODE_ = "int  6"
LIMIT_ = "int  29"
DEFAULT_ = "int  -1"
PRIMARY_ = "int  0"
SECONDARY_ = "int  1"
TERTIARY_ = "int  2"
DEFAULT_STRENGTH_ = "int  2"
CE_STRENGTH_LIMIT_ = "int  3"
QUATERNARY_ = "int  3"
IDENTICAL_ = "int  15"
STRENGTH_LIMIT_ = "int  16"
OFF_ = "int  16"
ON_ = "int  17"
SHIFTED_ = "int  20"
NON_IGNORABLE_ = "int  21"
LOWER_FIRST_ = "int  24"
UPPER_FIRST_ = "int  25"
def ():
    '''returns RuleBasedCollator\n\n
    (final String rules)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getCollationElementIterator():
    '''returns CollationElementIterator\n\n
    getCollationElementIterator(final String source)\n
    getCollationElementIterator(final CharacterIterator source)\n
    getCollationElementIterator(final UCharacterIterator source)\n
    '''
def setHiraganaQuaternary():
    '''returns None\n\n
    setHiraganaQuaternary(final boolean flag)\n
    '''
def setHiraganaQuaternaryDefault():
    '''returns None\n\n
    setHiraganaQuaternaryDefault()\n
    '''
def setUpperCaseFirst():
    '''returns None\n\n
    setUpperCaseFirst(final boolean upperfirst)\n
    '''
def setLowerCaseFirst():
    '''returns None\n\n
    setLowerCaseFirst(final boolean lowerfirst)\n
    '''
def setAlternateHandlingDefault():
    '''returns None\n\n
    setAlternateHandlingDefault()\n
    '''
def setCaseLevelDefault():
    '''returns None\n\n
    setCaseLevelDefault()\n
    '''
def setDecompositionDefault():
    '''returns None\n\n
    setDecompositionDefault()\n
    '''
def setFrenchCollationDefault():
    '''returns None\n\n
    setFrenchCollationDefault()\n
    '''
def setStrengthDefault():
    '''returns None\n\n
    setStrengthDefault()\n
    '''
def setNumericCollationDefault():
    '''returns None\n\n
    setNumericCollationDefault()\n
    '''
def setFrenchCollation():
    '''returns None\n\n
    setFrenchCollation(final boolean flag)\n
    '''
def setAlternateHandlingShifted():
    '''returns None\n\n
    setAlternateHandlingShifted(final boolean shifted)\n
    '''
def setCaseLevel():
    '''returns None\n\n
    setCaseLevel(final boolean flag)\n
    '''
def setStrength():
    '''returns None\n\n
    setStrength(final int newStrength)\n
    '''
def setVariableTop():
    '''returns None\n\n
    setVariableTop(final String varTop)\n
    setVariableTop(final int varTop)\n
    '''
def setNumericCollation():
    '''returns None\n\n
    setNumericCollation(final boolean flag)\n
    '''
def getRules():
    '''returns String\n\n
    getRules()\n
    getRules(final boolean fullrules)\n
    '''
def getTailoredSet():
    '''returns UnicodeSet\n\n
    getTailoredSet()\n
    '''
def getContractionsAndExpansions():
    '''returns None\n\n
    getContractionsAndExpansions(final UnicodeSet contractions, final UnicodeSet expansions, final boolean addPrefixes)\n
    '''
def getCollationKey():
    '''returns CollationKey\n\n
    getCollationKey(final String source)\n
    '''
def getRawCollationKey():
    '''returns RawCollationKey\n\n
    getRawCollationKey(String source, RawCollationKey key)\n
    '''
def isUpperCaseFirst():
    '''returns boolean\n\n
    isUpperCaseFirst()\n
    '''
def isLowerCaseFirst():
    '''returns boolean\n\n
    isLowerCaseFirst()\n
    '''
def isAlternateHandlingShifted():
    '''returns boolean\n\n
    isAlternateHandlingShifted()\n
    '''
def isCaseLevel():
    '''returns boolean\n\n
    isCaseLevel()\n
    '''
def isFrenchCollation():
    '''returns boolean\n\n
    isFrenchCollation()\n
    '''
def isHiraganaQuaternary():
    '''returns boolean\n\n
    isHiraganaQuaternary()\n
    '''
def getVariableTop():
    '''returns int\n\n
    getVariableTop()\n
    '''
def getNumericCollation():
    '''returns boolean\n\n
    getNumericCollation()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def compare():
    '''returns int\n\n
    compare(final String source, final String target)\n
    '''
def getVersion():
    '''returns VersionInfo\n\n
    getVersion()\n
    '''
def getUCAVersion():
    '''returns VersionInfo\n\n
    getUCAVersion()\n
    '''
