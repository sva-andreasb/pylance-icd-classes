def ():
    '''returns BlockImpactsEverythingEnum\n\n
    (final SegmentReadState state)\n
    (final FieldInfo fieldInfo)\n
    (final FieldInfo fieldInfo)\n
    (final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState)\n
    (final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState)\n
    (final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)\n
    '''
def init():
    '''returns None\n\n
    init(final IndexInput termsIn, final SegmentReadState state)\n
    '''
def newTermState():
    '''returns BlockTermState\n\n
    newTermState()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def decodeTerm():
    '''returns None\n\n
    decodeTerm(final DataInput in, final FieldInfo fieldInfo, final BlockTermState _termState, final boolean absolute)\n
    '''
def postings():
    '''returns PostingsEnum\n\n
    postings(final FieldInfo fieldInfo, final BlockTermState termState, final PostingsEnum reuse, final int flags)\n
    '''
def impacts():
    '''returns ImpactsEnum\n\n
    impacts(final FieldInfo fieldInfo, final BlockTermState state, final int flags)\n
    '''
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def canReuse():
    '''returns boolean\n\n
    canReuse(final IndexInput docIn, final FieldInfo fieldInfo)\n
    canReuse(final IndexInput docIn, final FieldInfo fieldInfo)\n
    '''
def reset():
    '''returns EverythingEnum\n\n
    reset(final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)\n
    reset(final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)\n
    '''
def freq():
    '''returns int\n\n
    freq()\n
    freq()\n
    freq()\n
    freq()\n
    freq()\n
    '''
def nextPosition():
    '''returns int\n\n
    nextPosition()\n
    nextPosition()\n
    nextPosition()\n
    nextPosition()\n
    nextPosition()\n
    '''
def startOffset():
    '''returns int\n\n
    startOffset()\n
    startOffset()\n
    startOffset()\n
    startOffset()\n
    startOffset()\n
    '''
def endOffset():
    '''returns int\n\n
    endOffset()\n
    endOffset()\n
    endOffset()\n
    endOffset()\n
    endOffset()\n
    '''
def getPayload():
    '''returns BytesRef\n\n
    getPayload()\n
    getPayload()\n
    getPayload()\n
    getPayload()\n
    getPayload()\n
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
    '''
def advance():
    '''returns int\n\n
    advance(final int target)\n
    advance(final int target)\n
    advance(final int target)\n
    advance(final int target)\n
    advance(final int target)\n
    '''
def cost():
    '''returns long\n\n
    cost()\n
    cost()\n
    cost()\n
    cost()\n
    cost()\n
    '''
def advanceShallow():
    '''returns None\n\n
    advanceShallow(final int target)\n
    advanceShallow(final int target)\n
    advanceShallow(final int target)\n
    '''
def getImpacts():
    '''returns Impacts\n\n
    getImpacts()\n
    getImpacts()\n
    getImpacts()\n
    '''
