def ():
    '''returns ExitableTermsEnum\n\n
    (final DirectoryReader in, final QueryTimeout queryTimeout)\n
    (final QueryTimeout queryTimeout)\n
    (final LeafReader in, final QueryTimeout queryTimeout)\n
    (final Terms terms, final QueryTimeout queryTimeout)\n
    (final TermsEnum termsEnum, final QueryTimeout queryTimeout)\n
    '''
def getReaderCacheHelper():
    '''returns CacheHelper\n\n
    getReaderCacheHelper()\n
    getReaderCacheHelper()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def wrap():
    '''returns LeafReader\n\n
    wrap(final LeafReader reader)\n
    '''
def getPointValues():
    '''returns PointValues\n\n
    getPointValues(final String field)\n
    '''
def terms():
    '''returns Terms\n\n
    terms(final String field)\n
    '''
def getCoreCacheHelper():
    '''returns CacheHelper\n\n
    getCoreCacheHelper()\n
    '''
def getNumericDocValues():
    '''returns NumericDocValues\n\n
    getNumericDocValues(final String field)\n
    '''
def advance():
    '''returns int\n\n
    advance(final int target)\n
    advance(final int target)\n
    advance(final int target)\n
    advance(final int target)\n
    advance(final int target)\n
    '''
def advanceExact():
    '''returns boolean\n\n
    advanceExact(final int target)\n
    advanceExact(final int target)\n
    advanceExact(final int target)\n
    advanceExact(final int target)\n
    advanceExact(final int target)\n
    '''
def nextDoc():
    '''returns int\n\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    '''
def getBinaryDocValues():
    '''returns BinaryDocValues\n\n
    getBinaryDocValues(final String field)\n
    '''
def getSortedDocValues():
    '''returns SortedDocValues\n\n
    getSortedDocValues(final String field)\n
    '''
def getSortedNumericDocValues():
    '''returns SortedNumericDocValues\n\n
    getSortedNumericDocValues(final String field)\n
    '''
def getSortedSetDocValues():
    '''returns SortedSetDocValues\n\n
    getSortedSetDocValues(final String field)\n
    '''
def intersect():
    '''returns TermsEnum\n\n
    intersect(final IntersectVisitor visitor)\n
    intersect(final CompiledAutomaton compiled, final BytesRef startTerm)\n
    '''
def estimatePointCount():
    '''returns long\n\n
    estimatePointCount(final IntersectVisitor visitor)\n
    '''
def getMinPackedValue():
    '''returns byte[]\n\n
    getMinPackedValue()\n
    '''
def getMaxPackedValue():
    '''returns byte[]\n\n
    getMaxPackedValue()\n
    '''
def getNumDimensions():
    '''returns int\n\n
    getNumDimensions()\n
    '''
def getNumIndexDimensions():
    '''returns int\n\n
    getNumIndexDimensions()\n
    '''
def getBytesPerDimension():
    '''returns int\n\n
    getBytesPerDimension()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def getDocCount():
    '''returns int\n\n
    getDocCount()\n
    '''
def visit():
    '''returns None\n\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    '''
def grow():
    '''returns None\n\n
    grow(final int count)\n
    '''
def iterator():
    '''returns TermsEnum\n\n
    iterator()\n
    '''
def next():
    '''returns BytesRef\n\n
    next()\n
    '''
