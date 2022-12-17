def rewrite():
    '''returns Query\n\n
    rewrite(final IndexReader reader, final MultiTermQuery query)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString(final String field)\n
    '''
def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    '''
def createWeight():
    '''returns Weight\n\n
    createWeight(final IndexSearcher searcher, final ScoreMode scoreMode, final float boost)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final LeafReaderContext context, final int doc)\n
    matches()\n
    '''
def iterator():
    '''returns TermsEnum\n\n
    iterator()\n
    '''
def getSumTotalTermFreq():
    '''returns long\n\n
    getSumTotalTermFreq()\n
    '''
def getSumDocFreq():
    '''returns long\n\n
    getSumDocFreq()\n
    '''
def getDocCount():
    '''returns int\n\n
    getDocCount()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def hasFreqs():
    '''returns boolean\n\n
    hasFreqs()\n
    '''
def hasOffsets():
    '''returns boolean\n\n
    hasOffsets()\n
    '''
def hasPositions():
    '''returns boolean\n\n
    hasPositions()\n
    '''
def hasPayloads():
    '''returns boolean\n\n
    hasPayloads()\n
    '''
def scorer():
    '''returns Scorer\n\n
    scorer(final LeafReaderContext context)\n
    '''
def matchCost():
    '''returns float\n\n
    matchCost()\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable(final LeafReaderContext ctx)\n
    '''
