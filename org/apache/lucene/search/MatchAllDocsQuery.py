def createWeight():
    '''returns Weight\n\n
    createWeight(final IndexSearcher searcher, final ScoreMode scoreMode, final float boost)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String field)\n
    '''
def scorer():
    '''returns Scorer\n\n
    scorer(final LeafReaderContext context)\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable(final LeafReaderContext ctx)\n
    '''
def bulkScorer():
    '''returns BulkScorer\n\n
    bulkScorer(final LeafReaderContext context)\n
    '''
def score():
    '''returns int\n\n
    score(final LeafCollector collector, final Bits acceptDocs, final int min, int max)\n
    '''
def cost():
    '''returns long\n\n
    cost()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    '''
