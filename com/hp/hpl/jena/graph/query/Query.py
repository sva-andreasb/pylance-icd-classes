def ():
    '''returns UnboundVariableException\n\n
    ()\n
    (final Graph pattern)\n
    (final Node n)\n
    '''
def addMatch():
    '''returns Query\n\n
    addMatch(final Node s, final Node p, final Node o)\n
    addMatch(final Triple t)\n
    '''
def getPattern():
    '''returns List<Triple>\n\n
    getPattern()\n
    '''
def getConstraints():
    '''returns ExpressionSet\n\n
    getConstraints()\n
    '''
def addConstraint():
    '''returns Query\n\n
    addConstraint(final Expression e)\n
    '''
def executeBindings():
    '''returns ExtendedIterator<Domain>\n\n
    executeBindings(final Graph g, final Node[] results)\n
    executeBindings(final Graph g, final List<Stage> stages, final Node[] results)\n
    executeBindings(final NamedGraphMap args, final Node[] nodes)\n
    executeBindings(final List<Stage> outStages, final NamedGraphMap args, final Node[] nodes)\n
    '''
def args():
    '''returns NamedGraphMap\n\n
    args()\n
    '''
def getSorter():
    '''returns TripleSorter\n\n
    getSorter()\n
    '''
def setTripleSorter():
    '''returns None\n\n
    setTripleSorter(final TripleSorter ts)\n
    '''
def getVariableCount():
    '''returns int\n\n
    getVariableCount()\n
    '''
