def ():
    '''returns JFrostParser\n\n
    (final String loc, final TokenFactory tf, final boolean indexing)\n
    '''
def preProcess():
    '''returns None\n\n
    preProcess(final Reader input)\n
    '''
def reset():
    '''returns None\n\n
    reset(final UniLexAnalyzer analyzer)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def createStd():
    '''returns None\n\n
    createStd(final int p, final int begin, final int end, final GlossCollection gc)\n
    '''
def createUnknown():
    '''returns None\n\n
    createUnknown(final int p, final int begin, final int end, final int wclass)\n
    '''
def createBreakpoint():
    '''returns None\n\n
    createBreakpoint(final int p, final int pos, final int bType)\n
    '''
def createPunctuation():
    '''returns None\n\n
    createPunctuation(final int p, final int begin, final int end, final int flags)\n
    '''
def startGroup():
    '''returns int\n\n
    startGroup(final int begin, final int end, final int type)\n
    '''
def closeGroup():
    '''returns None\n\n
    closeGroup(final int decompGroupN)\n
    '''
def fork():
    '''returns None\n\n
    fork()\n
    '''
def addToFork():
    '''returns None\n\n
    addToFork()\n
    '''
def mergeRoutes():
    '''returns None\n\n
    mergeRoutes(final int num_routes)\n
    '''
def createFragment():
    '''returns None\n\n
    createFragment(final int begin, final int end, final GlossCollection gc, final int position)\n
    createFragment(final int begin, final int end, final int wclass, final int position)\n
    '''
