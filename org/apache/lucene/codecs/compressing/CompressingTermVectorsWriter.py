def CompressingTermVectorsWriter():
'''public CompressingTermVectorsWriter(final Directory directory, final SegmentInfo si, final String segmentSuffix, final IOContext context, final String formatName, final CompressionMode compressionMode, final int chunkSize, final int blockShift)
'''
pass
def close():
'''public void close()
'''
pass
def startDocument():
'''public void startDocument(final int numVectorFields)
'''
pass
def finishDocument():
'''public void finishDocument()
'''
pass
def startField():
'''public void startField(final FieldInfo info, final int numTerms, final boolean positions, final boolean offsets, final boolean payloads)
'''
pass
def finishField():
'''public void finishField()
'''
pass
def startTerm():
'''public void startTerm(final BytesRef term, final int freq)
'''
pass
def addPosition():
'''public void addPosition(final int position, final int startOffset, final int endOffset, final BytesRef payload)
'''
pass
def finish():
'''public void finish(final FieldInfos fis, final int numDocs)
'''
pass
def addProx():
'''public void addProx(final int numProx, final DataInput positions, final DataInput offsets)
'''
pass
def merge():
'''public int merge(final MergeState mergeState)
'''
pass
