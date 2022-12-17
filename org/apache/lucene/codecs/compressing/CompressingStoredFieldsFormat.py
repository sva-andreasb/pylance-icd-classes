def ():
    '''returns CompressingStoredFieldsFormat\n\n
    (final String formatName, final CompressionMode compressionMode, final int chunkSize, final int maxDocsPerChunk, final int blockShift)\n
    (final String formatName, final String segmentSuffix, final CompressionMode compressionMode, final int chunkSize, final int maxDocsPerChunk, final int blockShift)\n
    '''
def fieldsReader():
    '''returns StoredFieldsReader\n\n
    fieldsReader(final Directory directory, final SegmentInfo si, final FieldInfos fn, final IOContext context)\n
    '''
def fieldsWriter():
    '''returns StoredFieldsWriter\n\n
    fieldsWriter(final Directory directory, final SegmentInfo si, final IOContext context)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
