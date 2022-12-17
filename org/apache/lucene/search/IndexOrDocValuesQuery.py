def ():
    '''returns IndexOrDocValuesQuery\n\n
    (final Query indexQuery, final Query dvQuery)\n
    '''
def getIndexQuery():
    '''returns Query\n\n
    getIndexQuery()\n
    '''
def getRandomAccessQuery():
    '''returns Query\n\n
    getRandomAccessQuery()\n
    '''
def toString():
    '''returns String\n\n
    toString(final String field)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def rewrite():
    '''returns Query\n\n
    rewrite(final IndexReader reader)\n
    '''
def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    '''
def createWeight():
    '''returns Weight\n\n
    createWeight(final IndexSearcher searcher, final ScoreMode scoreMode, final float boost)\n
    '''
def extractTerms():
    '''returns None\n\n
    extractTerms(final Set<Term> terms)\n
    '''
def matches():
    '''returns Matches\n\n
    matches(final LeafReaderContext context, final int doc)\n
    '''
def explain():
    '''returns Explanation\n\n
    explain(final LeafReaderContext context, final int doc)\n
    '''
def bulkScorer():
    '''returns BulkScorer\n\n
    bulkScorer(final LeafReaderContext context)\n
    '''
def scorerSupplier():
    '''returns ScorerSupplier\n\n
    scorerSupplier(final LeafReaderContext context)\n
    '''
def get():
    '''returns Scorer\n\n
    get(final long leadCost)\n
    '''
def cost():
    '''returns long\n\n
    cost()\n
    '''
def scorer():
    '''returns Scorer\n\n
    scorer(final LeafReaderContext context)\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable(final LeafReaderContext ctx)\n
    '''
