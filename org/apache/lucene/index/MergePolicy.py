def ():
    '''returns MergeAbortedException\n\n
    ()\n
    ()\n
    (final List<SegmentCommitInfo> segments)\n
    ()\n
    (final String message, final Directory dir)\n
    (final Throwable exc, final Directory dir)\n
    ()\n
    (final String message)\n
    '''
def useCompoundFile():
    '''returns boolean\n\n
    useCompoundFile(final SegmentInfos infos, final SegmentCommitInfo mergedInfo, final MergeContext mergeContext)\n
    '''
def getNoCFSRatio():
    '''returns double\n\n
    getNoCFSRatio()\n
    '''
def setNoCFSRatio():
    '''returns None\n\n
    setNoCFSRatio(final double noCFSRatio)\n
    '''
def getMaxCFSSegmentSizeMB():
    '''returns double\n\n
    getMaxCFSSegmentSizeMB()\n
    '''
def setMaxCFSSegmentSizeMB():
    '''returns None\n\n
    setMaxCFSSegmentSizeMB(double v)\n
    '''
def keepFullyDeletedSegment():
    '''returns boolean\n\n
    keepFullyDeletedSegment(final IOSupplier<CodecReader> readerIOSupplier)\n
    '''
def numDeletesToMerge():
    '''returns int\n\n
    numDeletesToMerge(final SegmentCommitInfo info, final int delCount, final IOSupplier<CodecReader> readerSupplier)\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    isAborted()\n
    '''
def pauseNanos():
    '''returns None\n\n
    pauseNanos(long pauseNanos, final PauseReason reason, final BooleanSupplier condition)\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
def mergeInit():
    '''returns None\n\n
    mergeInit()\n
    '''
def mergeFinished():
    '''returns None\n\n
    mergeFinished()\n
    '''
def wrapForMerge():
    '''returns CodecReader\n\n
    wrapForMerge(final CodecReader reader)\n
    '''
def setMergeInfo():
    '''returns None\n\n
    setMergeInfo(final SegmentCommitInfo info)\n
    '''
def getMergeInfo():
    '''returns SegmentCommitInfo\n\n
    getMergeInfo()\n
    '''
def segString():
    '''returns String\n\n
    segString()\n
    segString(final Directory dir)\n
    '''
def totalBytesSize():
    '''returns long\n\n
    totalBytesSize()\n
    '''
def totalNumDocs():
    '''returns int\n\n
    totalNumDocs()\n
    '''
def getStoreMergeInfo():
    '''returns MergeInfo\n\n
    getStoreMergeInfo()\n
    '''
def setAborted():
    '''returns None\n\n
    setAborted()\n
    '''
def checkAborted():
    '''returns None\n\n
    checkAborted()\n
    '''
def getMergeProgress():
    '''returns OneMergeProgress\n\n
    getMergeProgress()\n
    '''
def add():
    '''returns None\n\n
    add(final OneMerge merge)\n
    '''
def getDirectory():
    '''returns Directory\n\n
    getDirectory()\n
    '''
