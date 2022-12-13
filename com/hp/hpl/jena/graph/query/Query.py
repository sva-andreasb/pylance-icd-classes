def Query():
    '''    public Query()
    public Query(final Graph pattern)
    '''
def addMatch():
    '''    public Query addMatch(final Node s, final Node p, final Node o)
    public Query addMatch(final Triple t)
    '''
def getPattern():
    '''    public List<Triple> getPattern()
    '''
def getConstraints():
    '''    public ExpressionSet getConstraints()
    '''
def addConstraint():
    '''    public Query addConstraint(final Expression e)
    '''
def executeBindings():
    '''    public ExtendedIterator<Domain> executeBindings(final Graph g, final Node[] results)
    public ExtendedIterator<Domain> executeBindings(final Graph g, final List<Stage> stages, final Node[] results)
    public ExtendedIterator<Domain> executeBindings(final NamedGraphMap args, final Node[] nodes)
    public ExtendedIterator<Domain> executeBindings(final List<Stage> outStages, final NamedGraphMap args, final Node[] nodes)
    '''
def args():
    '''    public NamedGraphMap args()
    '''
def getSorter():
    '''    public TripleSorter getSorter()
    '''
def setTripleSorter():
    '''    public void setTripleSorter(final TripleSorter ts)
    '''
def getVariableCount():
    '''    public int getVariableCount()
    '''
def UnboundVariableException():
    '''    public UnboundVariableException(final Node n)
    '''
