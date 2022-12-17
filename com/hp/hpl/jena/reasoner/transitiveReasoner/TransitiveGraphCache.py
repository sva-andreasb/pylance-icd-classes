def ():
    '''returns TransitiveGraphCache\n\n
    (final Node directPredicate, final Node closedPredicate)\n
    '''
def getClosedPredicate():
    '''returns Node\n\n
    getClosedPredicate()\n
    '''
def getDirectPredicate():
    '''returns Node\n\n
    getDirectPredicate()\n
    '''
def visit():
    '''returns List<GraphNode>\n\n
    visit(final GraphNode node, final GraphNode processing, final Set<GraphNode> members, final GraphNode endN)\n
    '''
def removeRelation():
    '''returns None\n\n
    removeRelation(final Triple t)\n
    '''
def findWithContinuation():
    '''returns ExtendedIterator<Triple>\n\n
    findWithContinuation(final TriplePattern pattern, final Finder continuation)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final TriplePattern pattern)\n
    '''
def listAllSubjects():
    '''returns ExtendedIterator<Node>\n\n
    listAllSubjects()\n
    '''
def isSubject():
    '''returns boolean\n\n
    isSubject(final Node node)\n
    '''
def cacheAll():
    '''returns boolean\n\n
    cacheAll(final Finder graph, final Node predicate)\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TriplePattern pattern)\n
    '''
def deepCopy():
    '''returns TransitiveGraphCache\n\n
    deepCopy()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setCaching():
    '''returns None\n\n
    setCaching(final boolean enable)\n
    '''
def dump():
    '''returns String\n\n
    dump()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns Triple\n\n
    next()\n
    next()\n
    '''
