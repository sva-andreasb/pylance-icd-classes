def ():
    '''returns DisjunctionMaxWeight\n\n
    (final Collection<Query> disjuncts, final float tieBreakerMultiplier)\n
    (final IndexSearcher searcher, final ScoreMode scoreMode, final float boost)\n
    '''
def iterator():
    '''returns Iterator<Query>\n\n
    iterator()\n
    '''
def getDisjuncts():
    '''returns List<Query>\n\n
    getDisjuncts()\n
    '''
def getTieBreakerMultiplier():
    '''returns float\n\n
    getTieBreakerMultiplier()\n
    '''
def createWeight():
    '''returns Weight\n\n
    createWeight(final IndexSearcher searcher, final ScoreMode scoreMode, final float boost)\n
    '''
def rewrite():
    '''returns Query\n\n
    rewrite(final IndexReader reader)\n
    '''
def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    '''
def toString():
    '''returns String\n\n
    toString(final String field)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def extractTerms():
    '''returns None\n\n
    extractTerms(final Set<Term> terms)\n
    '''
def matches():
    '''returns Matches\n\n
    matches(final LeafReaderContext context, final int doc)\n
    '''
def scorer():
    '''returns Scorer\n\n
    scorer(final LeafReaderContext context)\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable(final LeafReaderContext ctx)\n
    '''
def explain():
    '''returns Explanation\n\n
    explain(final LeafReaderContext context, final int doc)\n
    '''
