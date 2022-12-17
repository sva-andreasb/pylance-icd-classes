def ():
    '''returns CompressingTermVectorsWriter\n\n
    (final Directory directory, final SegmentInfo si, final String segmentSuffix, final IOContext context, final String formatName, final CompressionMode compressionMode, final int chunkSize, final int blockShift)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final int numVectorFields)\n
    '''
def finishDocument():
    '''returns None\n\n
    finishDocument()\n
    '''
def startField():
    '''returns None\n\n
    startField(final FieldInfo info, final int numTerms, final boolean positions, final boolean offsets, final boolean payloads)\n
    '''
def finishField():
    '''returns None\n\n
    finishField()\n
    '''
def startTerm():
    '''returns None\n\n
    startTerm(final BytesRef term, final int freq)\n
    '''
def addPosition():
    '''returns None\n\n
    addPosition(final int position, final int startOffset, final int endOffset, final BytesRef payload)\n
    '''
def finish():
    '''returns None\n\n
    finish(final FieldInfos fis, final int numDocs)\n
    '''
def addProx():
    '''returns None\n\n
    addProx(final int numProx, final DataInput positions, final DataInput offsets)\n
    '''
def merge():
    '''returns int\n\n
    merge(final MergeState mergeState)\n
    '''
