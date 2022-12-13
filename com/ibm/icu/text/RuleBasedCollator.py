def RuleBasedCollator():
    '''public RuleBasedCollator(final String rules)
    '''
def clone():
    '''public Object clone()
    '''
def getCollationElementIterator():
    '''public CollationElementIterator getCollationElementIterator(final String source)
    public CollationElementIterator getCollationElementIterator(final CharacterIterator source)
    public CollationElementIterator getCollationElementIterator(final UCharacterIterator source)
    '''
def isFrozen():
    '''public boolean isFrozen()
    '''
def freeze():
    '''public Collator freeze()
    '''
def cloneAsThawed():
    '''public RuleBasedCollator cloneAsThawed()
    '''
def setHiraganaQuaternary():
    '''public void setHiraganaQuaternary(final boolean flag)
    '''
def setHiraganaQuaternaryDefault():
    '''public void setHiraganaQuaternaryDefault()
    '''
def setUpperCaseFirst():
    '''public void setUpperCaseFirst(final boolean upperfirst)
    '''
def setLowerCaseFirst():
    '''public void setLowerCaseFirst(final boolean lowerfirst)
    '''
def setCaseFirstDefault():
    '''public final void setCaseFirstDefault()
    '''
def setAlternateHandlingDefault():
    '''public void setAlternateHandlingDefault()
    '''
def setCaseLevelDefault():
    '''public void setCaseLevelDefault()
    '''
def setDecompositionDefault():
    '''public void setDecompositionDefault()
    '''
def setFrenchCollationDefault():
    '''public void setFrenchCollationDefault()
    '''
def setStrengthDefault():
    '''public void setStrengthDefault()
    '''
def setNumericCollationDefault():
    '''public void setNumericCollationDefault()
    '''
def setFrenchCollation():
    '''public void setFrenchCollation(final boolean flag)
    '''
def setAlternateHandlingShifted():
    '''public void setAlternateHandlingShifted(final boolean shifted)
    '''
def setCaseLevel():
    '''public void setCaseLevel(final boolean flag)
    '''
def setDecomposition():
    '''public void setDecomposition(final int decomposition)
    '''
def setStrength():
    '''public void setStrength(final int newStrength)
    '''
def setMaxVariable():
    '''public RuleBasedCollator setMaxVariable(int group)
    '''
def getMaxVariable():
    '''public int getMaxVariable()
    '''
def setVariableTop():
    '''public int setVariableTop(final String varTop)
    public void setVariableTop(final int varTop)
    '''
def setNumericCollation():
    '''public void setNumericCollation(final boolean flag)
    '''
def setReorderCodes():
    '''public void setReorderCodes(final int... order)
    '''
def getRules():
    '''public String getRules()
    public String getRules(final boolean fullrules)
    '''
def getTailoredSet():
    '''public UnicodeSet getTailoredSet()
    '''
def getContractionsAndExpansions():
    '''public void getContractionsAndExpansions(final UnicodeSet contractions, final UnicodeSet expansions, final boolean addPrefixes)
    '''
def getCollationKey():
    '''public CollationKey getCollationKey(final String source)
    '''
def getRawCollationKey():
    '''public RawCollationKey getRawCollationKey(final String source, final RawCollationKey key)
    '''
def internalGetCEs():
    '''public long[] internalGetCEs(final CharSequence str)
    '''
def getStrength():
    '''public int getStrength()
    '''
def getDecomposition():
    '''public int getDecomposition()
    '''
def isUpperCaseFirst():
    '''public boolean isUpperCaseFirst()
    '''
def isLowerCaseFirst():
    '''public boolean isLowerCaseFirst()
    '''
def isAlternateHandlingShifted():
    '''public boolean isAlternateHandlingShifted()
    '''
def isCaseLevel():
    '''public boolean isCaseLevel()
    '''
def isFrenchCollation():
    '''public boolean isFrenchCollation()
    '''
def isHiraganaQuaternary():
    '''public boolean isHiraganaQuaternary()
    '''
def getVariableTop():
    '''public int getVariableTop()
    '''
def getNumericCollation():
    '''public boolean getNumericCollation()
    '''
def getReorderCodes():
    '''public int[] getReorderCodes()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def compare():
    '''public int compare(final String source, final String target)
    '''
def getVersion():
    '''public VersionInfo getVersion()
    '''
def getUCAVersion():
    '''public VersionInfo getUCAVersion()
    '''
def getLocale():
    '''public ULocale getLocale(final ULocale.Type type)
    '''
