def ():
    '''returns FuzzyTermsEnum\n\n
    (final Terms terms, final Term term, final int maxEdits, final int prefixLength, final boolean transpositions)\n
    '''
def setMaxNonCompetitiveBoost():
    '''returns None\n\n
    setMaxNonCompetitiveBoost(final float boost)\n
    '''
def getBoost():
    '''returns float\n\n
    getBoost()\n
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
def seekExact():
    '''returns None\n\n
    seekExact(final BytesRef term, final TermState state)\n
    seekExact(final BytesRef text)\n
    seekExact(final long ord)\n
    '''
def termState():
    '''returns TermState\n\n
    termState()\n
    '''
def ord():
    '''returns long\n\n
    ord()\n
    '''
def attributes():
    '''returns AttributeSource\n\n
    attributes()\n
    '''
def seekCeil():
    '''returns SeekStatus\n\n
    seekCeil(final BytesRef text)\n
    '''
def term():
    '''returns BytesRef\n\n
    term()\n
    '''
def getAutomata():
    '''returns CompiledAutomaton[]\n\n
    getAutomata()\n
    '''
def getTermLength():
    '''returns int\n\n
    getTermLength()\n
    '''
def init():
    '''returns None\n\n
    init(final Supplier<FuzzyAutomatonBuilder> supplier)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def reflectWith():
    '''returns None\n\n
    reflectWith(final AttributeReflector reflector)\n
    '''
def copyTo():
    '''returns None\n\n
    copyTo(final AttributeImpl target)\n
    '''
