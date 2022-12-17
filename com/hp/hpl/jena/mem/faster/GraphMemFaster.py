def ():
    '''returns GraphMemFasterStatisticsHandler\n\n
    ()\n
    (final ReificationStyle style)\n
    (final FasterTripleStore store, final Reifier reifier)\n
    '''
def performAdd():
    '''returns None\n\n
    performAdd(final Triple t)\n
    '''
def performDelete():
    '''returns None\n\n
    performDelete(final Triple t)\n
    '''
def graphBaseSize():
    '''returns int\n\n
    graphBaseSize()\n
    '''
def queryHandler():
    '''returns QueryHandler\n\n
    queryHandler()\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final TripleMatch m)\n
    '''
def createApplyer():
    '''returns Applyer\n\n
    createApplyer(final ProcessedTriple pt)\n
    '''
def applyToTriples():
    '''returns None\n\n
    applyToTriples(final Domain d, final Matcher m, final StageElement next)\n
    '''
def graphBaseContains():
    '''returns boolean\n\n
    graphBaseContains(final Triple t)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getStatistic():
    '''returns long\n\n
    getStatistic(final Node S, final Node P, final Node O)\n
    '''
def countsInMap():
    '''returns long\n\n
    countsInMap(final Node a, final NodeToTriplesMapFaster mapA, final Node b, final NodeToTriplesMapFaster mapB)\n
    '''
def countInMap():
    '''returns long\n\n
    countInMap(final Node n, final NodeToTriplesMapFaster map)\n
    '''
