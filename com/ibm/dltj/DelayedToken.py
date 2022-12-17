token_type_close = "int  0"
token_type_std = "int  1"
token_type_unkown = "int  2"
token_type_breakpoint = "int  3"
token_type_punctuation = "int  4"
token_type_reset = "int  5"
token_type_startGroup = "int  6"
token_type_closeGroup = "int  7"
token_type_fork = "int  8"
token_type_addToFork = "int  9"
token_type_mergeRoutes = "int  10"
def ():
    '''returns DelayedToken\n\n
    ()\n
    '''
def tokenUnzip():
    '''returns String[]\n\n
    tokenUnzip(final String s)\n
    '''
def close():
    '''returns String\n\n
    close()\n
    '''
def createStd():
    '''returns String\n\n
    createStd(final int i, final int j, final int k, final GlossCollection e)\n
    '''
def createUnknown():
    '''returns String\n\n
    createUnknown(final int i, final int j, final int k, final int l)\n
    '''
def createBreakpoint():
    '''returns String\n\n
    createBreakpoint(final int i, final int j, final int k)\n
    '''
def createPunctuation():
    '''returns String\n\n
    createPunctuation(final int i, final int j, final int k, final int l)\n
    '''
def reset():
    '''returns String\n\n
    reset(final UniLexAnalyzer e)\n
    '''
def startGroup():
    '''returns String\n\n
    startGroup(final int i, final int j, final int k)\n
    '''
def closeGroup():
    '''returns String\n\n
    closeGroup(final int i)\n
    '''
def fork():
    '''returns String\n\n
    fork()\n
    '''
def addToFork():
    '''returns String\n\n
    addToFork()\n
    '''
def mergeRoutes():
    '''returns String\n\n
    mergeRoutes(final int i)\n
    '''
