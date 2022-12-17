def ():
    '''returns FilterSortedSetDocValues\n\n
    (final SortedSetDocValues in)\n
    '''
def advanceExact():
    '''returns boolean\n\n
    advanceExact(final int target)\n
    '''
def nextOrd():
    '''returns long\n\n
    nextOrd()\n
    '''
def lookupOrd():
    '''returns BytesRef\n\n
    lookupOrd(final long ord)\n
    '''
def getValueCount():
    '''returns long\n\n
    getValueCount()\n
    '''
def lookupTerm():
    '''returns long\n\n
    lookupTerm(final BytesRef key)\n
    '''
def termsEnum():
    '''returns TermsEnum\n\n
    termsEnum()\n
    '''
def intersect():
    '''returns TermsEnum\n\n
    intersect(final CompiledAutomaton automaton)\n
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
