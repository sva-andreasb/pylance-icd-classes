def ():
    '''returns FilterPostingsEnum\n\n
    (final LeafReader in)\n
    (final Fields in)\n
    (final Terms in)\n
    (final TermsEnum in)\n
    (final PostingsEnum in)\n
    '''
def getLiveDocs():
    '''returns Bits\n\n
    getLiveDocs()\n
    '''
def getFieldInfos():
    '''returns FieldInfos\n\n
    getFieldInfos()\n
    '''
def getPointValues():
    '''returns PointValues\n\n
    getPointValues(final String field)\n
    '''
def getTermVectors():
    '''returns Fields\n\n
    getTermVectors(final int docID)\n
    '''
def numDocs():
    '''returns int\n\n
    numDocs()\n
    '''
def maxDoc():
    '''returns int\n\n
    maxDoc()\n
    '''
def document():
    '''returns None\n\n
    document(final int docID, final StoredFieldVisitor visitor)\n
    '''
def terms():
    '''returns Terms\n\n
    terms(final String field)\n
    terms(final String field)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getNumericDocValues():
    '''returns NumericDocValues\n\n
    getNumericDocValues(final String field)\n
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
def getNormValues():
    '''returns NumericDocValues\n\n
    getNormValues(final String field)\n
    '''
def getMetaData():
    '''returns LeafMetaData\n\n
    getMetaData()\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def getDelegate():
    '''returns LeafReader\n\n
    getDelegate()\n
    '''
def iterator():
    '''returns TermsEnum\n\n
    iterator()\n
    iterator()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    size()\n
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
def getStats():
    '''returns Object\n\n
    getStats()\n
    '''
def attributes():
    '''returns AttributeSource\n\n
    attributes()\n
    '''
def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef text)\n
    '''
def seekExact():
    '''returns None\n\n
    seekExact(final BytesRef text)\n
    seekExact(final long ord)\n
    seekExact(final BytesRef term, final TermState state)\n
    '''
def next():
    '''returns BytesRef\n\n
    next()\n
    '''
def term():
    '''returns BytesRef\n\n
    term()\n
    '''
def ord():
    '''returns long\n\n
    ord()\n
    '''
def docFreq():
    '''returns int\n\n
    docFreq()\n
    '''
def totalTermFreq():
    '''returns long\n\n
    totalTermFreq()\n
    '''
def postings():
    '''returns PostingsEnum\n\n
    postings(final PostingsEnum reuse, final int flags)\n
    '''
def impacts():
    '''returns ImpactsEnum\n\n
    impacts(final int flags)\n
    '''
def termState():
    '''returns TermState\n\n
    termState()\n
    '''
def docID():
    '''returns int\n\n
    docID()\n
    '''
def freq():
    '''returns int\n\n
    freq()\n
    '''
def nextDoc():
    '''returns int\n\n
    nextDoc()\n
    '''
def advance():
    '''returns int\n\n
    advance(final int target)\n
    '''
def nextPosition():
    '''returns int\n\n
    nextPosition()\n
    '''
def startOffset():
    '''returns int\n\n
    startOffset()\n
    '''
def endOffset():
    '''returns int\n\n
    endOffset()\n
    '''
def getPayload():
    '''returns BytesRef\n\n
    getPayload()\n
    '''
def cost():
    '''returns long\n\n
    cost()\n
    '''
