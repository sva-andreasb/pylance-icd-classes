def CompressingTermVectorsReader():
    '''public CompressingTermVectorsReader(final Directory d, final SegmentInfo si, final String segmentSuffix, final FieldInfos fn, final IOContext context, final String formatName, final CompressionMode compressionMode)
    '''
def close():
    '''public void close()
    '''
def clone():
    '''public TermVectorsReader clone()
    '''
def get():
    '''public Fields get(final int doc)
    '''
def ramBytesUsed():
    '''public long ramBytesUsed()
    '''
def getChildResources():
    '''public Collection<Accountable> getChildResources()
    '''
def checkIntegrity():
    '''public void checkIntegrity()
    '''
def toString():
    '''public String toString()
    '''
def TVFields():
    '''public TVFields(final int[] fieldNums, final int[] fieldFlags, final int[] fieldNumOffs, final int[] numTerms, final int[] fieldLengths, final int[][] prefixLengths, final int[][] suffixLengths, final int[][] termFreqs, final int[][] positionIndex, final int[][] positions, final int[][] startOffsets, final int[][] lengths, final BytesRef payloadBytes, final int[][] payloadIndex, final BytesRef suffixBytes)
    '''
def iterator():
    '''public Iterator<String> iterator()
    public TermsEnum iterator()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public String next()
    public BytesRef next()
    '''
def remove():
    '''public void remove()
    '''
def terms():
    '''public Terms terms(final String field)
    '''
def size():
    '''public int size()
    public long size()
    '''
def getSumTotalTermFreq():
    '''public long getSumTotalTermFreq()
    '''
def getSumDocFreq():
    '''public long getSumDocFreq()
    '''
def getDocCount():
    '''public int getDocCount()
    '''
def hasFreqs():
    '''public boolean hasFreqs()
    '''
def hasOffsets():
    '''public boolean hasOffsets()
    '''
def hasPositions():
    '''public boolean hasPositions()
    '''
def hasPayloads():
    '''public boolean hasPayloads()
    '''
def seekCeil():
    '''public SeekStatus seekCeil(final BytesRef text)
    '''
def seekExact():
    '''public void seekExact(final long ord)
    '''
def term():
    '''public BytesRef term()
    '''
def ord():
    '''public long ord()
    '''
def docFreq():
    '''public int docFreq()
    '''
def totalTermFreq():
    '''public long totalTermFreq()
    '''
def postings():
    '''public final PostingsEnum postings(final PostingsEnum reuse, final int flags)
    '''
def impacts():
    '''public ImpactsEnum impacts(final int flags)
    '''
def reset():
    '''public void reset(final int freq, final int positionIndex, final int[] positions, final int[] startOffsets, final int[] lengths, final BytesRef payloads, final int[] payloadIndex)
    '''
def nextPosition():
    '''public int nextPosition()
    '''
def startOffset():
    '''public int startOffset()
    '''
def endOffset():
    '''public int endOffset()
    '''
def getPayload():
    '''public BytesRef getPayload()
    '''
def freq():
    '''public int freq()
    '''
def docID():
    '''public int docID()
    '''
def nextDoc():
    '''public int nextDoc()
    '''
def advance():
    '''public int advance(final int target)
    '''
def cost():
    '''public long cost()
    '''
