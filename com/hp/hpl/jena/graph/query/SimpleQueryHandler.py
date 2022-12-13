def SimpleQueryHandler():
    '''public SimpleQueryHandler(final Graph graph)
    '''
def patternStage():
    '''public Stage patternStage(final Mapping map, final ExpressionSet constraints, final Triple[] t)
    '''
def prepareBindings():
    '''public BindingQueryPlan prepareBindings(final Query q, final Node[] variables)
    '''
def prepareTree():
    '''public TreeQueryPlan prepareTree(final Graph pattern)
    '''
def objectsFor():
    '''public ExtendedIterator<Node> objectsFor(final Node s, final Node p)
    public static ExtendedIterator<Node> objectsFor(final Graph g, final Node s, final Node p)
    '''
def subjectsFor():
    '''public ExtendedIterator<Node> subjectsFor(final Node p, final Node o)
    public static ExtendedIterator<Node> subjectsFor(final Graph g, final Node p, final Node o)
    '''
def predicatesFor():
    '''public ExtendedIterator<Node> predicatesFor(final Node s, final Node o)
    public static ExtendedIterator<Node> predicatesFor(final Graph g, final Node s, final Node o)
    '''
def containsNode():
    '''public boolean containsNode(final Node n)
    '''
