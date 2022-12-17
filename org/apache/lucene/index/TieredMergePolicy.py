DEFAULT_NO_CFS_RATIO = "double  0.1"
def ():
    '''returns TieredMergePolicy\n\n
    ()\n
    '''
def setMaxMergeAtOnce():
    '''returns TieredMergePolicy\n\n
    setMaxMergeAtOnce(final int v)\n
    '''
def getMaxMergeAtOnce():
    '''returns int\n\n
    getMaxMergeAtOnce()\n
    '''
def setMaxMergeAtOnceExplicit():
    '''returns TieredMergePolicy\n\n
    setMaxMergeAtOnceExplicit(final int v)\n
    '''
def getMaxMergeAtOnceExplicit():
    '''returns int\n\n
    getMaxMergeAtOnceExplicit()\n
    '''
def setMaxMergedSegmentMB():
    '''returns TieredMergePolicy\n\n
    setMaxMergedSegmentMB(double v)\n
    '''
def getMaxMergedSegmentMB():
    '''returns double\n\n
    getMaxMergedSegmentMB()\n
    '''
def setDeletesPctAllowed():
    '''returns TieredMergePolicy\n\n
    setDeletesPctAllowed(final double v)\n
    '''
def getDeletesPctAllowed():
    '''returns double\n\n
    getDeletesPctAllowed()\n
    '''
def setFloorSegmentMB():
    '''returns TieredMergePolicy\n\n
    setFloorSegmentMB(double v)\n
    '''
def getFloorSegmentMB():
    '''returns double\n\n
    getFloorSegmentMB()\n
    '''
def setForceMergeDeletesPctAllowed():
    '''returns TieredMergePolicy\n\n
    setForceMergeDeletesPctAllowed(final double v)\n
    '''
def getForceMergeDeletesPctAllowed():
    '''returns double\n\n
    getForceMergeDeletesPctAllowed()\n
    '''
def setSegmentsPerTier():
    '''returns TieredMergePolicy\n\n
    setSegmentsPerTier(final double v)\n
    '''
def getSegmentsPerTier():
    '''returns double\n\n
    getSegmentsPerTier()\n
    '''
def findMerges():
    '''returns MergeSpecification\n\n
    findMerges(final MergeTrigger mergeTrigger, final SegmentInfos infos, final MergeContext mergeContext)\n
    '''
def getScore():
    '''returns double\n\n
    getScore()\n
    '''
def getExplanation():
    '''returns String\n\n
    getExplanation()\n
    '''
def findForcedMerges():
    '''returns MergeSpecification\n\n
    findForcedMerges(final SegmentInfos infos, final int maxSegmentCount, final Map<SegmentCommitInfo, Boolean> segmentsToMerge, final MergeContext mergeContext)\n
    '''
def findForcedDeletesMerges():
    '''returns MergeSpecification\n\n
    findForcedDeletesMerges(final SegmentInfos infos, final MergeContext mergeContext)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
