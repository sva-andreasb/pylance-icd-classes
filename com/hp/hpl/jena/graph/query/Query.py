def Query():
'''public Query()
public Query(final Graph pattern)
'''
pass
def addMatch():
'''public Query addMatch(final Node s, final Node p, final Node o)
public Query addMatch(final Triple t)
'''
pass
def getPattern():
'''public List<Triple> getPattern()
'''
pass
def getConstraints():
'''public ExpressionSet getConstraints()
'''
pass
def addConstraint():
'''public Query addConstraint(final Expression e)
'''
pass
def executeBindings():
'''public ExtendedIterator<Domain> executeBindings(final Graph g, final Node[] results)
public ExtendedIterator<Domain> executeBindings(final Graph g, final List<Stage> stages, final Node[] results)
public ExtendedIterator<Domain> executeBindings(final NamedGraphMap args, final Node[] nodes)
public ExtendedIterator<Domain> executeBindings(final List<Stage> outStages, final NamedGraphMap args, final Node[] nodes)
'''
pass
def args():
'''public NamedGraphMap args()
'''
pass
def getSorter():
'''public TripleSorter getSorter()
'''
pass
def setTripleSorter():
'''public void setTripleSorter(final TripleSorter ts)
'''
pass
def getVariableCount():
'''public int getVariableCount()
'''
pass
def UnboundVariableException():
'''public UnboundVariableException(final Node n)
'''
pass
