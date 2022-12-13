STATS = "String  \"stats\""
META = "String  \"meta\""
COUNT = "String  \"count\""
weightSP = "double  2.0"
weightPO = "double  10.0"
weightTypeO = "double  1000.0"
weightSP_small = "double  2.0"
weightPO_small = "double  4.0"
weightTypeO_small = "double  40.0"
def StatsMatcher():
    '''    public StatsMatcher()
    public StatsMatcher(final String filename)
    public StatsMatcher(final Item stats)
    '''
def addPatterns():
    '''    public void addPatterns(final Node predicate, final double numProp)
    '''
def addPatternsSmall():
    '''    public void addPatternsSmall(final Node predicate, final double numProp)
    '''
def addPattern():
    '''    public void addPattern(final Pattern pattern)
    public void addPattern(final Triple triple)
    '''
def match():
    '''    public double match(final Triple t)
    public double match(final PatternTriple pTriple)
    public double match(final Item subj, final Item pred, final Item obj)
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def printSSE():
    '''    public void printSSE(final PrintStream ps)
    '''
def Pattern():
    '''    public Pattern(final double w, final Item subj, final Item pred, final Item obj)
    '''
def output():
    '''    public void output(final IndentedWriter out)
    '''
