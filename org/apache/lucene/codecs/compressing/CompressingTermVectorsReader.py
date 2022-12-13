def CompressingTermVectorsReader():
'''public CompressingTermVectorsReader(final Directory d, final SegmentInfo si, final String segmentSuffix, final FieldInfos fn, final IOContext context, final String formatName, final CompressionMode compressionMode)
'''
pass
def close():
'''public void close()
'''
pass
def clone():
'''public TermVectorsReader clone()
'''
pass
def get():
'''public Fields get(final int doc)
'''
pass
def ramBytesUsed():
'''public long ramBytesUsed()
'''
pass
def getChildResources():
'''public Collection<Accountable> getChildResources()
'''
pass
def checkIntegrity():
'''public void checkIntegrity()
'''
pass
def toString():
'''public String toString()
'''
pass
def TVFields():
'''public TVFields(final int[] fieldNums, final int[] fieldFlags, final int[] fieldNumOffs, final int[] numTerms, final int[] fieldLengths, final int[][] prefixLengths, final int[][] suffixLengths, final int[][] termFreqs, final int[][] positionIndex, final int[][] positions, final int[][] startOffsets, final int[][] lengths, final BytesRef payloadBytes, final int[][] payloadIndex, final BytesRef suffixBytes)
'''
pass
def iterator():
'''public Iterator<String> iterator()
public TermsEnum iterator()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public String next()
public BytesRef next()
'''
pass
def remove():
'''public void remove()
'''
pass
def terms():
'''public Terms terms(final String field)
'''
pass
def size():
'''public int size()
public long size()
'''
pass
def getSumTotalTermFreq():
'''public long getSumTotalTermFreq()
'''
pass
def getSumDocFreq():
'''public long getSumDocFreq()
'''
pass
def getDocCount():
'''public int getDocCount()
'''
pass
def hasFreqs():
'''public boolean hasFreqs()
'''
pass
def hasOffsets():
'''public boolean hasOffsets()
'''
pass
def hasPositions():
'''public boolean hasPositions()
'''
pass
def hasPayloads():
'''public boolean hasPayloads()
'''
pass
def seekCeil():
'''public SeekStatus seekCeil(final BytesRef text)
'''
pass
def seekExact():
'''public void seekExact(final long ord)
'''
pass
def term():
'''public BytesRef term()
'''
pass
def ord():
'''public long ord()
'''
pass
def docFreq():
'''public int docFreq()
'''
pass
def totalTermFreq():
'''public long totalTermFreq()
'''
pass
def postings():
'''public final PostingsEnum postings(final PostingsEnum reuse, final int flags)
'''
pass
def impacts():
'''public ImpactsEnum impacts(final int flags)
'''
pass
def reset():
'''public void reset(final int freq, final int positionIndex, final int[] positions, final int[] startOffsets, final int[] lengths, final BytesRef payloads, final int[] payloadIndex)
'''
pass
def nextPosition():
'''public int nextPosition()
'''
pass
def startOffset():
'''public int startOffset()
'''
pass
def endOffset():
'''public int endOffset()
'''
pass
def getPayload():
'''public BytesRef getPayload()
'''
pass
def freq():
'''public int freq()
'''
pass
def docID():
'''public int docID()
'''
pass
def nextDoc():
'''public int nextDoc()
'''
pass
def advance():
'''public int advance(final int target)
'''
pass
def cost():
'''public long cost()
'''
pass
