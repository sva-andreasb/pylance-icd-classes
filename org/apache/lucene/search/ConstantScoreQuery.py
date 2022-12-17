def ():
    '''returns ConstantBulkScorer\n\n
    (final Query query)\n
    (final BulkScorer bulkScorer, final Weight weight, final float theScore)\n
    '''
def getQuery():
    '''returns Query\n\n
    getQuery()\n
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
    cost()\n
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
def score():
    '''returns float\n\n
    score(final LeafCollector collector, final Bits acceptDocs, final int min, final int max)\n
    score()\n
    '''
def setScorer():
    '''returns None\n\n
    setScorer(final Scorable scorer)\n
    '''
