def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    visit(final DocIdSetIterator iterator, final byte[] packedValue)\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    visit(final DocIdSetIterator iterator, final byte[] packedValue)\n
    '''
def grow():
    '''returns None\n\n
    grow(final int count)\n
    '''
def scorerSupplier():
    '''returns ScorerSupplier\n\n
    scorerSupplier(final LeafReaderContext context)\n
    '''
def get():
    '''returns Scorer\n\n
    get(final long leadCost)\n
    get(final long leadCost)\n
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
def getField():
    '''returns String\n\n
    getField()\n
    '''
def getNumDims():
    '''returns int\n\n
    getNumDims()\n
    '''
def getBytesPerDim():
    '''returns int\n\n
    getBytesPerDim()\n
    '''
def getLowerPoint():
    '''returns byte[]\n\n
    getLowerPoint()\n
    '''
def getUpperPoint():
    '''returns byte[]\n\n
    getUpperPoint()\n
    '''
