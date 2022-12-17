def ():
    '''returns Normalizer2WithImpl\n\n
    (final Normalizer2Impl ni)\n
    '''
def normalize():
    '''returns Appendable\n\n
    normalize(final CharSequence src, final StringBuilder dest)\n
    normalize(final CharSequence src, final Appendable dest)\n
    '''
def normalizeSecondAndAppend():
    '''returns StringBuilder\n\n
    normalizeSecondAndAppend(final StringBuilder first, final CharSequence second)\n
    normalizeSecondAndAppend(final StringBuilder first, final CharSequence second, final boolean doNormalize)\n
    '''
def append():
    '''returns StringBuilder\n\n
    append(final StringBuilder first, final CharSequence second)\n
    '''
def getDecomposition():
    '''returns String\n\n
    getDecomposition(final int c)\n
    '''
def getRawDecomposition():
    '''returns String\n\n
    getRawDecomposition(final int c)\n
    '''
def composePair():
    '''returns int\n\n
    composePair(final int a, final int b)\n
    '''
def getCombiningClass():
    '''returns int\n\n
    getCombiningClass(final int c)\n
    '''
def isNormalized():
    '''returns boolean\n\n
    isNormalized(final CharSequence s)\n
    '''
