def ():
    '''returns TermStates\n\n
    (final IndexReaderContext context)\n
    (final IndexReaderContext context, final TermState state, final int ord, final int docFreq, final long totalTermFreq)\n
    '''
def wasBuiltFor():
    '''returns boolean\n\n
    wasBuiltFor(final IndexReaderContext context)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def register():
    '''returns None\n\n
    register(final TermState state, final int ord, final int docFreq, final long totalTermFreq)\n
    register(final TermState state, final int ord)\n
    '''
def accumulateStatistics():
    '''returns None\n\n
    accumulateStatistics(final int docFreq, final long totalTermFreq)\n
    '''
def get():
    '''returns TermState\n\n
    get(final LeafReaderContext ctx)\n
    '''
def docFreq():
    '''returns int\n\n
    docFreq()\n
    '''
def totalTermFreq():
    '''returns long\n\n
    totalTermFreq()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def copyFrom():
    '''returns None\n\n
    copyFrom(final TermState other)\n
    '''
