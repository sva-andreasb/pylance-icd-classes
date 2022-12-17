def ():
    '''returns LRUQueryCache\n\n
    (final int maxSize, final long maxRamBytesUsed, final Predicate<LeafReaderContext> leavesToCache, final float skipCacheFactor)\n
    (final int maxSize, final long maxRamBytesUsed)\n
    '''
def clearCoreCacheKey():
    '''returns None\n\n
    clearCoreCacheKey(final Object coreKey)\n
    '''
def clearQuery():
    '''returns None\n\n
    clearQuery(final Query query)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def doCache():
    '''returns Weight\n\n
    doCache(Weight weight, final QueryCachingPolicy policy)\n
    '''
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    ramBytesUsed()\n
    '''
def getChildResources():
    '''returns Collection<Accountable>\n\n
    getChildResources()\n
    '''
def setScorer():
    '''returns None\n\n
    setScorer(final Scorable scorer)\n
    setScorer(final Scorable scorer)\n
    '''
def collect():
    '''returns None\n\n
    collect(final int doc)\n
    collect(final int doc)\n
    '''
def test():
    '''returns boolean\n\n
    test(final LeafReaderContext context)\n
    '''
def extractTerms():
    '''returns None\n\n
    extractTerms(final Set<Term> terms)\n
    '''
def matches():
    '''returns Matches\n\n
    matches(final LeafReaderContext context, final int doc)\n
    '''
def scorerSupplier():
    '''returns ScorerSupplier\n\n
    scorerSupplier(final LeafReaderContext context)\n
    '''
def get():
    '''returns Scorer\n\n
    get(final long leadCost)\n
    get(final long LeadCost)\n
    '''
def cost():
    '''returns long\n\n
    cost()\n
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
def bulkScorer():
    '''returns BulkScorer\n\n
    bulkScorer(final LeafReaderContext context)\n
    '''
