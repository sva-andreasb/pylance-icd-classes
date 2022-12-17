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
def scorer():
    '''returns Scorer\n\n
    scorer(final LeafReaderContext context)\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable(final LeafReaderContext ctx)\n
    '''
def getPackedPoints():
    '''returns Collection<byte[]>\n\n
    getPackedPoints()\n
    '''
def iterator():
    '''returns Iterator<byte[]>\n\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns byte[]\n\n
    next()\n
    '''
def size():
    '''returns int\n\n
    size()\n
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
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    '''
def ():
    '''returns SinglePointVisitor\n\n
    (final PrefixCodedTerms sortedPackedPoints, final DocIdSetBuilder result)\n
    (final DocIdSetBuilder result)\n
    '''
def grow():
    '''returns None\n\n
    grow(final int count)\n
    grow(final int count)\n
    '''
def setPoint():
    '''returns None\n\n
    setPoint(final BytesRef point)\n
    '''
