def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef term)\n
    '''
def seekExact():
    '''returns None\n\n
    seekExact(final long ord)\n
    seekExact(final BytesRef term, final TermState state)\n
    '''
def term():
    '''returns BytesRef\n\n
    term()\n
    '''
def docFreq():
    '''returns int\n\n
    docFreq()\n
    '''
def totalTermFreq():
    '''returns long\n\n
    totalTermFreq()\n
    '''
def ord():
    '''returns long\n\n
    ord()\n
    '''
def postings():
    '''returns PostingsEnum\n\n
    postings(final PostingsEnum reuse, final int flags)\n
    '''
def impacts():
    '''returns ImpactsEnum\n\n
    impacts(final int flags)\n
    '''
def next():
    '''returns BytesRef\n\n
    next()\n
    '''
def termState():
    '''returns TermState\n\n
    termState()\n
    '''
