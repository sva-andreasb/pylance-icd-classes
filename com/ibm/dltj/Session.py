DLTSESSION_LEX = "int  0"
DLTSESSION_SPELL = "int  1"
Delay_sentence = "int  2"
Delay_paragraph = "int  2"
PROCMODE_ALLCASE = "int  1"
PROCMODE_LOWERCASE = "int  3"
PROCMODE_MW_PROCESSING = "int  3"
PROCMODE_MW_BUILDING = "int  4"
def ():
    '''returns Session\n\n
    (final String s)\n
    (final Locale locale)\n
    '''
def setBreakIteratorByLocaleString():
    '''returns None\n\n
    setBreakIteratorByLocaleString(final String breakIteratorByLocaleString)\n
    '''
def setBreakIteratorByFilename():
    '''returns None\n\n
    setBreakIteratorByFilename(final String breakIteratorByFilename)\n
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
    setTransliteratorRuleByFilename(final String transliteratorRuleByFilename)\n
    '''
def setDictionaries():
    '''returns None\n\n
    setDictionaries(final Dictionary[] array, final Dictionary[] array2, final Dictionary[] array3)\n
    setDictionaries(final Dictionary[] array, final Dictionary[] array2, final Dictionary[] array3, final Dictionary[] array4)\n
    '''
def open():
    '''returns None\n\n
    open(final Dictionary[] array, final int n)\n
    open(final Dictionary[] array, final int n, final int n2, final int n3)\n
    open(final int n, final int n2, final int n3)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def valid():
    '''returns boolean\n\n
    valid()\n
    '''
