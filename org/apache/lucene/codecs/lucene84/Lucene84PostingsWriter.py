def Lucene84PostingsWriter():
'''public Lucene84PostingsWriter(final SegmentWriteState state)
'''
pass
def init():
'''public void init(final IndexOutput termsOut, final SegmentWriteState state)
'''
pass
def setField():
'''public void setField(final FieldInfo fieldInfo)
'''
pass
def startTerm():
'''public void startTerm(final NumericDocValues norms)
'''
pass
def startDoc():
'''public void startDoc(final int docID, final int termDocFreq)
'''
pass
def addPosition():
'''public void addPosition(final int position, final BytesRef payload, final int startOffset, final int endOffset)
'''
pass
def finishDoc():
'''public void finishDoc()
'''
pass
def finishTerm():
'''public void finishTerm(final BlockTermState _state)
'''
pass
def encodeTerm():
'''public void encodeTerm(final DataOutput out, final FieldInfo fieldInfo, final BlockTermState _state, final boolean absolute)
'''
pass
def close():
'''public void close()
'''
pass
