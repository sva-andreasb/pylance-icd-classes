def ():
    '''returns Lucene84PostingsWriter\n\n
    (final SegmentWriteState state)\n
    '''
def init():
    '''returns None\n\n
    init(final IndexOutput termsOut, final SegmentWriteState state)\n
    '''
def setField():
    '''returns None\n\n
    setField(final FieldInfo fieldInfo)\n
    '''
def startTerm():
    '''returns None\n\n
    startTerm(final NumericDocValues norms)\n
    '''
def startDoc():
    '''returns None\n\n
    startDoc(final int docID, final int termDocFreq)\n
    '''
def addPosition():
    '''returns None\n\n
    addPosition(final int position, final BytesRef payload, final int startOffset, final int endOffset)\n
    '''
def finishDoc():
    '''returns None\n\n
    finishDoc()\n
    '''
def finishTerm():
    '''returns None\n\n
    finishTerm(final BlockTermState _state)\n
    '''
def encodeTerm():
    '''returns None\n\n
    encodeTerm(final DataOutput out, final FieldInfo fieldInfo, final BlockTermState _state, final boolean absolute)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
