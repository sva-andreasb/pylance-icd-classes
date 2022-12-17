LEVEL_LOG_SPAN = "double  0.75"
DEFAULT_MERGE_FACTOR = "int  10"
DEFAULT_MAX_MERGE_DOCS = "int  Integer.MAX_VALUE"
DEFAULT_NO_CFS_RATIO = "double  0.1"
def ():
    '''returns SegmentInfoAndLevel\n\n
    ()\n
    (final SegmentCommitInfo info, final float level)\n
    '''
def getMergeFactor():
    '''returns int\n\n
    getMergeFactor()\n
    '''
def setMergeFactor():
    '''returns None\n\n
    setMergeFactor(final int mergeFactor)\n
    '''
def setCalibrateSizeByDeletes():
    '''returns None\n\n
    setCalibrateSizeByDeletes(final boolean calibrateSizeByDeletes)\n
    '''
def getCalibrateSizeByDeletes():
    '''returns boolean\n\n
    getCalibrateSizeByDeletes()\n
    '''
def findForcedMerges():
    '''returns MergeSpecification\n\n
    findForcedMerges(final SegmentInfos infos, final int maxNumSegments, final Map<SegmentCommitInfo, Boolean> segmentsToMerge, final MergeContext mergeContext)\n
    '''
def findForcedDeletesMerges():
    '''returns MergeSpecification\n\n
    findForcedDeletesMerges(final SegmentInfos segmentInfos, final MergeContext mergeContext)\n
    '''
def findMerges():
    '''returns MergeSpecification\n\n
    findMerges(final MergeTrigger mergeTrigger, final SegmentInfos infos, final MergeContext mergeContext)\n
    '''
def setMaxMergeDocs():
    '''returns None\n\n
    setMaxMergeDocs(final int maxMergeDocs)\n
    '''
def getMaxMergeDocs():
    '''returns int\n\n
    getMaxMergeDocs()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final SegmentInfoAndLevel other)\n
    '''
