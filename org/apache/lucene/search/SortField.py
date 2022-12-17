def ():
    '''returns SortField\n\n
    (final String field, final Type type)\n
    (final String field, final Type type, final boolean reverse)\n
    (final String field, final FieldComparatorSource comparator)\n
    (final String field, final FieldComparatorSource comparator, final boolean reverse)\n
    '''
def getMissingValue():
    '''returns Object\n\n
    getMissingValue()\n
    '''
def setMissingValue():
    '''returns None\n\n
    setMissingValue(final Object missingValue)\n
    '''
def getField():
    '''returns String\n\n
    getField()\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getReverse():
    '''returns boolean\n\n
    getReverse()\n
    '''
def getComparatorSource():
    '''returns FieldComparatorSource\n\n
    getComparatorSource()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def setBytesComparator():
    '''returns None\n\n
    setBytesComparator(final Comparator<BytesRef> b)\n
    '''
def getBytesComparator():
    '''returns Comparator<BytesRef>\n\n
    getBytesComparator()\n
    '''
def rewrite():
    '''returns SortField\n\n
    rewrite(final IndexSearcher searcher)\n
    '''
def needsScores():
    '''returns boolean\n\n
    needsScores()\n
    '''
