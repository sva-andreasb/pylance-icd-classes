def ():
    '''returns PostingsAndFreq\n\n
    (final int slop, final String field, final String... terms)\n
    (final String field, final String... terms)\n
    (final int slop, final String field, final BytesRef... terms)\n
    (final String field, final BytesRef... terms)\n
    ()\n
    (final PostingsEnum postings, final ImpactsEnum impacts, final int position, final Term... terms)\n
    (final PostingsEnum postings, final ImpactsEnum impacts, final int position, final List<Term> terms)\n
    '''
def getSlop():
    '''returns int\n\n
    getSlop()\n
    '''
def getField():
    '''returns String\n\n
    getField()\n
    '''
def getTerms():
    '''returns Term[]\n\n
    getTerms()\n
    '''
def getPositions():
    '''returns int[]\n\n
    getPositions()\n
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
    extractTerms(final Set<Term> queryTerms)\n
    '''
def toString():
    '''returns String\n\n
    toString(final String f)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def setSlop():
    '''returns Builder\n\n
    setSlop(final int slop)\n
    '''
def add():
    '''returns Builder\n\n
    add(final Term term)\n
    add(final Term term, final int position)\n
    '''
def build():
    '''returns PhraseQuery\n\n
    build()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final PostingsAndFreq other)\n
    '''
