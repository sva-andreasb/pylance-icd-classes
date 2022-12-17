def getMatchCount():
    '''returns int\n\n
    getMatchCount()\n
    '''
def getMatchArray():
    '''returns TermsEnumWithSlice[]\n\n
    getMatchArray()\n
    '''
def ():
    '''returns TermsEnumWithSlice\n\n
    (final ReaderSlice[] slices)\n
    (final TermsEnum termsEnum, final int subIndex)\n
    (final int index, final ReaderSlice subSlice)\n
    '''
def term():
    '''returns BytesRef\n\n
    term()\n
    '''
def reset():
    '''returns None\n\n
    reset(final TermsEnumIndex[] termsEnumsIndex)\n
    reset(final TermsEnum terms, final BytesRef term)\n
    '''
def seekExact():
    '''returns None\n\n
    seekExact(final BytesRef term)\n
    seekExact(final long ord)\n
    '''
def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef term)\n
    '''
def ord():
    '''returns long\n\n
    ord()\n
    '''
def next():
    '''returns BytesRef\n\n
    next()\n
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
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def compare():
    '''returns int\n\n
    compare(final TermsEnumWithSlice o1, final TermsEnumWithSlice o2)\n
    '''
