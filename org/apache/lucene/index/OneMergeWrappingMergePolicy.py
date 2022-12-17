def ():
    '''returns OneMergeWrappingMergePolicy\n\n
    (final MergePolicy in, final UnaryOperator<OneMerge> wrapOneMerge)\n
    '''
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
