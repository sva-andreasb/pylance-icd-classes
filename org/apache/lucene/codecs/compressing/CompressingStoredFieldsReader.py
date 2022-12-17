def ():
    '''returns CompressingStoredFieldsReader\n\n
    (final Directory d, final SegmentInfo si, final String segmentSuffix, final FieldInfos fn, final IOContext context, final String formatName, final CompressionMode compressionMode)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def visitDocument():
    '''returns None\n\n
    visitDocument(final int docID, final StoredFieldVisitor visitor)\n
    '''
def clone():
    '''returns StoredFieldsReader\n\n
    clone()\n
    '''
def getMergeInstance():
    '''returns StoredFieldsReader\n\n
    getMergeInstance()\n
    '''
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    '''
def getChildResources():
    '''returns Collection<Accountable>\n\n
    getChildResources()\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def readByte():
    '''returns byte\n\n
    readByte()\n
    '''
def readBytes():
    '''returns None\n\n
    readBytes(final byte[] b, int offset, int len)\n
    '''
