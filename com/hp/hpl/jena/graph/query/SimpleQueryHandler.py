def ():
    '''returns SimpleQueryHandler\n\n
    (final Graph graph)\n
    '''
def patternStage():
    '''returns Stage\n\n
    patternStage(final Mapping map, final ExpressionSet constraints, final Triple[] t)\n
    '''
def prepareBindings():
    '''returns BindingQueryPlan\n\n
    prepareBindings(final Query q, final Node[] variables)\n
    '''
def prepareTree():
    '''returns TreeQueryPlan\n\n
    prepareTree(final Graph pattern)\n
    '''
def objectsFor():
    '''returns ExtendedIterator<Node>\n\n
    objectsFor(final Node s, final Node p)\n
    '''
def subjectsFor():
    '''returns ExtendedIterator<Node>\n\n
    subjectsFor(final Node p, final Node o)\n
    '''
def predicatesFor():
    '''returns ExtendedIterator<Node>\n\n
    predicatesFor(final Node s, final Node o)\n
    '''
def containsNode():
    '''returns boolean\n\n
    containsNode(final Node n)\n
    '''
