def ():
    '''returns TVFields\n\n
    (final Directory d, final SegmentInfo si, final String segmentSuffix, final FieldInfos fn, final IOContext context, final String formatName, final CompressionMode compressionMode)\n
    (final int[] fieldNums, final int[] fieldFlags, final int[] fieldNumOffs, final int[] numTerms, final int[] fieldLengths, final int[][] prefixLengths, final int[][] suffixLengths, final int[][] termFreqs, final int[][] positionIndex, final int[][] positions, final int[][] startOffsets, final int[][] lengths, final BytesRef payloadBytes, final int[][] payloadIndex, final BytesRef suffixBytes)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def clone():
    '''returns TermVectorsReader\n\n
    clone()\n
    '''
def get():
    '''returns Fields\n\n
    get(final int doc)\n
    '''
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    '''
def getChildResources():
    '''returns Collection<Accountable>\n\n
    getChildResources()\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def iterator():
    '''returns TermsEnum\n\n
    iterator()\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns BytesRef\n\n
    next()\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def terms():
    '''returns Terms\n\n
    terms(final String field)\n
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
def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef text)\n
    '''
def seekExact():
    '''returns None\n\n
    seekExact(final long ord)\n
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
def impacts():
    '''returns ImpactsEnum\n\n
    impacts(final int flags)\n
    '''
def reset():
    '''returns None\n\n
    reset(final int freq, final int positionIndex, final int[] positions, final int[] startOffsets, final int[] lengths, final BytesRef payloads, final int[] payloadIndex)\n
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
def freq():
    '''returns int\n\n
    freq()\n
    '''
def docID():
    '''returns int\n\n
    docID()\n
    '''
def nextDoc():
    '''returns int\n\n
    nextDoc()\n
    '''
def advance():
    '''returns int\n\n
    advance(final int target)\n
    '''
def cost():
    '''returns long\n\n
    cost()\n
    '''
