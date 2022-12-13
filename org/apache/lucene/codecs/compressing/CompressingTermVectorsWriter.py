def CompressingTermVectorsWriter():
    '''public CompressingTermVectorsWriter(final Directory directory, final SegmentInfo si, final String segmentSuffix, final IOContext context, final String formatName, final CompressionMode compressionMode, final int chunkSize, final int blockShift)
    '''
def close():
    '''public void close()
    '''
def startDocument():
    '''public void startDocument(final int numVectorFields)
    '''
def finishDocument():
    '''public void finishDocument()
    '''
def startField():
    '''public void startField(final FieldInfo info, final int numTerms, final boolean positions, final boolean offsets, final boolean payloads)
    '''
def finishField():
    '''public void finishField()
    '''
def startTerm():
    '''public void startTerm(final BytesRef term, final int freq)
    '''
def addPosition():
    '''public void addPosition(final int position, final int startOffset, final int endOffset, final BytesRef payload)
    '''
def finish():
    '''public void finish(final FieldInfos fis, final int numDocs)
    '''
def addProx():
    '''public void addProx(final int numProx, final DataInput positions, final DataInput offsets)
    '''
def merge():
    '''public int merge(final MergeState mergeState)
    '''
