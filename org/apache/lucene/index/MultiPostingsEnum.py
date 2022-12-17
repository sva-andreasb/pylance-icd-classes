def ():
    '''returns MultiPostingsEnum\n\n
    (final MultiTermsEnum parent, final int subReaderCount)\n
    '''
def canReuse():
    '''returns boolean\n\n
    canReuse(final MultiTermsEnum parent)\n
    '''
def reset():
    '''returns MultiPostingsEnum\n\n
    reset(final EnumWithSlice[] subs, final int numSubs)\n
    '''
def getNumSubs():
    '''returns int\n\n
    getNumSubs()\n
    '''
def getSubs():
    '''returns EnumWithSlice[]\n\n
    getSubs()\n
    '''
def freq():
    '''returns int\n\n
    freq()\n
    '''
def docID():
    '''returns int\n\n
    docID()\n
    '''
def advance():
    '''returns int\n\n
    advance(final int target)\n
    '''
def nextDoc():
    '''returns int\n\n
    nextDoc()\n
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
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
