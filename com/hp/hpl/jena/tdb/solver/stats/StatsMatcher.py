STATS = "String  \"stats\""
META = "String  \"meta\""
COUNT = "String  \"count\""
weightSP = "double  2.0"
weightPO = "double  10.0"
weightTypeO = "double  1000.0"
weightSP_small = "double  2.0"
weightPO_small = "double  4.0"
weightTypeO_small = "double  40.0"
def ():
    '''returns Pattern\n\n
    ()\n
    (final String filename)\n
    (final Item stats)\n
    (final double w, final Item subj, final Item pred, final Item obj)\n
    '''
def addPatterns():
    '''returns None\n\n
    addPatterns(final Node predicate, final double numProp)\n
    '''
def addPatternsSmall():
    '''returns None\n\n
    addPatternsSmall(final Node predicate, final double numProp)\n
    '''
def addPattern():
    '''returns None\n\n
    addPattern(final Pattern pattern)\n
    addPattern(final Triple triple)\n
    '''
def match():
    '''returns double\n\n
    match(final Triple t)\n
    match(final PatternTriple pTriple)\n
    match(final Item subj, final Item pred, final Item obj)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def printSSE():
    '''returns None\n\n
    printSSE(final PrintStream ps)\n
    '''
def output():
    '''returns None\n\n
    output(final IndentedWriter out)\n
    '''
