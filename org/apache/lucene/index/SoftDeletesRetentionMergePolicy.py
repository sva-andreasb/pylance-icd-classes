def ():
    '''returns SoftDeletesRetentionMergePolicy\n\n
    (final String field, final Supplier<Query> retentionQuerySupplier, final MergePolicy in)\n
    '''
def wrapForMerge():
    '''returns CodecReader\n\n
    wrapForMerge(final CodecReader reader)\n
    '''
def keepFullyDeletedSegment():
    '''returns boolean\n\n
    keepFullyDeletedSegment(final IOSupplier<CodecReader> readerIOSupplier)\n
    '''
def get():
    '''returns boolean\n\n
    get(final int index)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def numDeletesToMerge():
    '''returns int\n\n
    numDeletesToMerge(final SegmentCommitInfo info, final int delCount, final IOSupplier<CodecReader> readerSupplier)\n
    '''
