def ():
    '''returns LeafSlice\n\n
    (final IndexReader r)\n
    (final IndexReader r, final Executor executor)\n
    (final IndexReaderContext context, final Executor executor)\n
    (final IndexReaderContext context)\n
    (final LeafReaderContext... leaves)\n
    '''
def setQueryCache():
    '''returns None\n\n
    setQueryCache(final QueryCache queryCache)\n
    '''
def getQueryCache():
    '''returns QueryCache\n\n
    getQueryCache()\n
    '''
def setQueryCachingPolicy():
    '''returns None\n\n
    setQueryCachingPolicy(final QueryCachingPolicy queryCachingPolicy)\n
    '''
def getQueryCachingPolicy():
    '''returns QueryCachingPolicy\n\n
    getQueryCachingPolicy()\n
    '''
def getIndexReader():
    '''returns IndexReader\n\n
    getIndexReader()\n
    '''
def doc():
    '''returns Document\n\n
    doc(final int docID)\n
    doc(final int docID, final StoredFieldVisitor fieldVisitor)\n
    doc(final int docID, final Set<String> fieldsToLoad)\n
    '''
def setSimilarity():
    '''returns None\n\n
    setSimilarity(final Similarity similarity)\n
    '''
def getSimilarity():
    '''returns Similarity\n\n
    getSimilarity()\n
    '''
def count():
    '''returns int\n\n
    count(Query query)\n
    '''
def newCollector():
    '''returns TopFieldCollector\n\n
    newCollector()\n
    newCollector()\n
    newCollector()\n
    '''
def reduce():
    '''returns TopFieldDocs\n\n
    reduce(final Collection<TotalHitCountCollector> collectors)\n
    reduce(final Collection<TopScoreDocCollector> collectors)\n
    reduce(final Collection<TopFieldCollector> collectors)\n
    '''
def getSlices():
    '''returns LeafSlice[]\n\n
    getSlices()\n
    '''
def searchAfter():
    '''returns TopFieldDocs\n\n
    searchAfter(final ScoreDoc after, final Query query, final int numHits)\n
    searchAfter(final ScoreDoc after, final Query query, final int n, final Sort sort)\n
    searchAfter(final ScoreDoc after, final Query query, final int numHits, final Sort sort, final boolean doDocScores)\n
    '''
def search():
    '''returns TopFieldDocs\n\n
    search(final Query query, final int n)\n
    search(Query query, final Collector results)\n
    search(final Query query, final int n, final Sort sort, final boolean doDocScores)\n
    search(final Query query, final int n, final Sort sort)\n
    '''
def rewrite():
    '''returns Query\n\n
    rewrite(final Query original)\n
    '''
def explain():
    '''returns Explanation\n\n
    explain(Query query, final int doc)\n
    '''
def createWeight():
    '''returns Weight\n\n
    createWeight(final Query query, final ScoreMode scoreMode, final float boost)\n
    '''
def getTopReaderContext():
    '''returns IndexReaderContext\n\n
    getTopReaderContext()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def termStatistics():
    '''returns TermStatistics\n\n
    termStatistics(final Term term, final int docFreq, final long totalTermFreq)\n
    '''
def collectionStatistics():
    '''returns CollectionStatistics\n\n
    collectionStatistics(final String field)\n
    '''
def getExecutor():
    '''returns Executor\n\n
    getExecutor()\n
    '''
