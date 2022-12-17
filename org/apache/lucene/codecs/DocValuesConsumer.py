def merge():
    '''returns None\n\n
    merge(final MergeState mergeState)\n
    '''
def mergeNumericField():
    '''returns None\n\n
    mergeNumericField(final FieldInfo mergeFieldInfo, final MergeState mergeState)\n
    '''
def getNumeric():
    '''returns NumericDocValues\n\n
    getNumeric(final FieldInfo fieldInfo)\n
    '''
def docID():
    '''returns int\n\n
    docID()\n
    docID()\n
    docID()\n
    docID()\n
    docID()\n
    '''
def nextDoc():
    '''returns int\n\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
    nextDoc()\n
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
def cost():
    '''returns long\n\n
    cost()\n
    cost()\n
    cost()\n
    cost()\n
    cost()\n
    '''
def longValue():
    '''returns long\n\n
    longValue()\n
    '''
def mergeBinaryField():
    '''returns None\n\n
    mergeBinaryField(final FieldInfo mergeFieldInfo, final MergeState mergeState)\n
    '''
def getBinary():
    '''returns BinaryDocValues\n\n
    getBinary(final FieldInfo fieldInfo)\n
    '''
def binaryValue():
    '''returns BytesRef\n\n
    binaryValue()\n
    '''
def mergeSortedNumericField():
    '''returns None\n\n
    mergeSortedNumericField(final FieldInfo mergeFieldInfo, final MergeState mergeState)\n
    '''
def getSortedNumeric():
    '''returns SortedNumericDocValues\n\n
    getSortedNumeric(final FieldInfo fieldInfo)\n
    '''
def docValueCount():
    '''returns int\n\n
    docValueCount()\n
    '''
def nextValue():
    '''returns long\n\n
    nextValue()\n
    '''
def mergeSortedField():
    '''returns None\n\n
    mergeSortedField(final FieldInfo fieldInfo, final MergeState mergeState)\n
    '''
def getSorted():
    '''returns SortedDocValues\n\n
    getSorted(final FieldInfo fieldInfoIn)\n
    '''
def ordValue():
    '''returns int\n\n
    ordValue()\n
    '''
def getValueCount():
    '''returns long\n\n
    getValueCount()\n
    getValueCount()\n
    '''
def lookupOrd():
    '''returns BytesRef\n\n
    lookupOrd(final int ord)\n
    lookupOrd(final long ord)\n
    '''
def termsEnum():
    '''returns TermsEnum\n\n
    termsEnum()\n
    termsEnum()\n
    '''
def mergeSortedSetField():
    '''returns None\n\n
    mergeSortedSetField(final FieldInfo mergeFieldInfo, final MergeState mergeState)\n
    '''
def getSortedSet():
    '''returns SortedSetDocValues\n\n
    getSortedSet(final FieldInfo fieldInfo)\n
    '''
def nextOrd():
    '''returns long\n\n
    nextOrd()\n
    '''
def iterator():
    '''returns Iterator<Number>\n\n
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
def ():
    '''returns SortedSetDocValuesSub\n\n
    (final MergeState.DocMap docMap, final NumericDocValues values)\n
    (final MergeState.DocMap docMap, final BinaryDocValues values)\n
    (final MergeState.DocMap docMap, final SortedNumericDocValues values)\n
    (final MergeState.DocMap docMap, final SortedDocValues values, final LongValues map)\n
    (final MergeState.DocMap docMap, final SortedSetDocValues values, final LongValues map)\n
    '''
def term():
    '''returns BytesRef\n\n
    term()\n
    '''
def ord():
    '''returns long\n\n
    ord()\n
    '''
def attributes():
    '''returns AttributeSource\n\n
    attributes()\n
    '''
def seekExact():
    '''returns None\n\n
    seekExact(final BytesRef text)\n
    seekExact(final long ord)\n
    seekExact(final BytesRef term, final TermState state)\n
    '''
def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef text)\n
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
def toString():
    '''returns String\n\n
    toString()\n
    '''
