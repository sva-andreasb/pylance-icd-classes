def JFrostParser():
    '''public JFrostParser(final String loc, final TokenFactory tf, final boolean indexing)
    '''
def preProcess():
    '''public void preProcess(final Reader input)
    '''
def reset():
    '''public void reset(final UniLexAnalyzer analyzer)
    '''
def close():
    '''public void close()
    '''
def createStd():
    '''public void createStd(final int p, final int begin, final int end, final GlossCollection gc)
    '''
def createUnknown():
    '''public void createUnknown(final int p, final int begin, final int end, final int wclass)
    '''
def createBreakpoint():
    '''public void createBreakpoint(final int p, final int pos, final int bType)
    '''
def createPunctuation():
    '''public void createPunctuation(final int p, final int begin, final int end, final int flags)
    '''
def startGroup():
    '''public int startGroup(final int begin, final int end, final int type)
    '''
def closeGroup():
    '''public void closeGroup(final int decompGroupN)
    '''
def fork():
    '''public void fork()
    '''
def addToFork():
    '''public void addToFork()
    '''
def mergeRoutes():
    '''public void mergeRoutes(final int num_routes)
    '''
def createFragment():
    '''public void createFragment(final int begin, final int end, final GlossCollection gc, final int position)
    public void createFragment(final int begin, final int end, final int wclass, final int position)
    '''
