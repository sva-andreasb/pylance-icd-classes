def findMerges():
    '''returns MergeSpecification\n\n
    findMerges(final MergeTrigger mergeTrigger, final SegmentInfos segmentInfos, final MergeContext mergeContext)\n
    '''
def findForcedMerges():
    '''returns MergeSpecification\n\n
    findForcedMerges(final SegmentInfos segmentInfos, final int maxSegmentCount, final Map<SegmentCommitInfo, Boolean> segmentsToMerge, final MergeContext mergeContext)\n
    '''
def findForcedDeletesMerges():
    '''returns MergeSpecification\n\n
    findForcedDeletesMerges(final SegmentInfos segmentInfos, final MergeContext mergeContext)\n
    '''
def useCompoundFile():
    '''returns boolean\n\n
    useCompoundFile(final SegmentInfos segments, final SegmentCommitInfo newSegment, final MergeContext mergeContext)\n
    '''
def getNoCFSRatio():
    '''returns double\n\n
    getNoCFSRatio()\n
    '''
def getMaxCFSSegmentSizeMB():
    '''returns double\n\n
    getMaxCFSSegmentSizeMB()\n
    '''
def setMaxCFSSegmentSizeMB():
    '''returns None\n\n
    setMaxCFSSegmentSizeMB(final double v)\n
    '''
def setNoCFSRatio():
    '''returns None\n\n
    setNoCFSRatio(final double noCFSRatio)\n
    '''
def keepFullyDeletedSegment():
    '''returns boolean\n\n
    keepFullyDeletedSegment(final IOSupplier<CodecReader> readerIOSupplier)\n
    '''
def numDeletesToMerge():
    '''returns int\n\n
    numDeletesToMerge(final SegmentCommitInfo info, final int delCount, final IOSupplier<CodecReader> readerSupplier)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
