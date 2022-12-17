def getSourceText():
    '''returns CharacterIterator\n\n
    getSourceText()\n
    '''
def getParsingStream():
    '''returns ParsingStream\n\n
    getParsingStream()\n
    '''
def setBreakIteratorByLocaleString():
    '''returns None\n\n
    setBreakIteratorByLocaleString(final String s)\n
    '''
def setBreakIteratorByFilename():
    '''returns None\n\n
    setBreakIteratorByFilename(final String s)\n
    '''
def setProcessingMode():
    '''returns None\n\n
    setProcessingMode(final int processingMode)\n
    '''
def setCaseStrictMode():
    '''returns None\n\n
    setCaseStrictMode(final boolean caseStrictMode)\n
    '''
def setGuessingMode():
    '''returns None\n\n
    setGuessingMode(final int guessingMode)\n
    '''
def setTransliteratorRuleByFilename():
    '''returns None\n\n
    setTransliteratorRuleByFilename(final String transliteratorRuleFile)\n
    '''
def setDictionaries():
    '''returns None\n\n
    setDictionaries(final Dictionary[] array, final Dictionary[] array2, final Dictionary[] array3)\n
    setDictionaries(final Dictionary[] array, final Dictionary[] array2, final Dictionary[] array3, final Dictionary[] array4)\n
    '''
def open():
    '''returns None\n\n
    open(final Dictionary[] array)\n
    open(final Dictionary[] array, final int n)\n
    open(final Dictionary[] array, final int n, final int hints, final int flagSpec)\n
    open(final int n, final int hints, final int flagSpec)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def processTextMW():
    '''returns ParsingStream\n\n
    processTextMW(final CharacterIterator characterIterator, final ParsingStream parsingStream)\n
    processTextMW(final CharacterIterator characterIterator, final ClassificationParsingStream classificationParsingStream)\n
    '''
def processText():
    '''returns ParsingStream\n\n
    processText(final CharacterIterator characterIterator, final ParsingStream plps)\n
    '''
def getLocale():
    '''returns String\n\n
    getLocale()\n
    '''
def getBrkLocale():
    '''returns String\n\n
    getBrkLocale()\n
    '''
def getBreakIterator():
    '''returns RuleBasedBreakIterator\n\n
    getBreakIterator()\n
    '''
