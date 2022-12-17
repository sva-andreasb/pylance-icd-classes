def ():
    '''returns FilteredTermsEnum\n\n
    (final TermsEnum tenum)\n
    (final TermsEnum tenum, final boolean startWithSeek)\n
    '''
def attributes():
    '''returns AttributeSource\n\n
    attributes()\n
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
def seekExact():
    '''returns None\n\n
    seekExact(final BytesRef term)\n
    seekExact(final long ord)\n
    seekExact(final BytesRef term, final TermState state)\n
    '''
def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef term)\n
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
def termState():
    '''returns TermState\n\n
    termState()\n
    '''
def next():
    '''returns BytesRef\n\n
    next()\n
    '''
