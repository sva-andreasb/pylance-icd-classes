def Lucene84PostingsWriter():
    '''    public Lucene84PostingsWriter(final SegmentWriteState state)
    '''
def init():
    '''    public void init(final IndexOutput termsOut, final SegmentWriteState state)
    '''
def setField():
    '''    public void setField(final FieldInfo fieldInfo)
    '''
def startTerm():
    '''    public void startTerm(final NumericDocValues norms)
    '''
def startDoc():
    '''    public void startDoc(final int docID, final int termDocFreq)
    '''
def addPosition():
    '''    public void addPosition(final int position, final BytesRef payload, final int startOffset, final int endOffset)
    '''
def finishDoc():
    '''    public void finishDoc()
    '''
def finishTerm():
    '''    public void finishTerm(final BlockTermState _state)
    '''
def encodeTerm():
    '''    public void encodeTerm(final DataOutput out, final FieldInfo fieldInfo, final BlockTermState _state, final boolean absolute)
    '''
def close():
    '''    public void close()
    '''
