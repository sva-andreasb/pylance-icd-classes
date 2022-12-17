DISABLE_AUTO_FLUSH = "int  -1"
DEFAULT_MAX_BUFFERED_DELETE_TERMS = "int  -1"
DEFAULT_MAX_BUFFERED_DOCS = "int  -1"
DEFAULT_RAM_BUFFER_SIZE_MB = "double  16.0"
DEFAULT_READER_POOLING = "boolean  true"
DEFAULT_RAM_PER_THREAD_HARD_LIMIT_MB = "int  1945"
DEFAULT_USE_COMPOUND_FILE_SYSTEM = "boolean  true"
DEFAULT_COMMIT_ON_CLOSE = "boolean  true"
def ():
    '''returns IndexWriterConfig\n\n
    ()\n
    (final Analyzer analyzer)\n
    '''
def setOpenMode():
    '''returns IndexWriterConfig\n\n
    setOpenMode(final OpenMode openMode)\n
    '''
def getOpenMode():
    '''returns OpenMode\n\n
    getOpenMode()\n
    '''
def setIndexCreatedVersionMajor():
    '''returns IndexWriterConfig\n\n
    setIndexCreatedVersionMajor(final int indexCreatedVersionMajor)\n
    '''
def setIndexDeletionPolicy():
    '''returns IndexWriterConfig\n\n
    setIndexDeletionPolicy(final IndexDeletionPolicy delPolicy)\n
    '''
def getIndexDeletionPolicy():
    '''returns IndexDeletionPolicy\n\n
    getIndexDeletionPolicy()\n
    '''
def setIndexCommit():
    '''returns IndexWriterConfig\n\n
    setIndexCommit(final IndexCommit commit)\n
    '''
def getIndexCommit():
    '''returns IndexCommit\n\n
    getIndexCommit()\n
    '''
def setSimilarity():
    '''returns IndexWriterConfig\n\n
    setSimilarity(final Similarity similarity)\n
    '''
def getSimilarity():
    '''returns Similarity\n\n
    getSimilarity()\n
    '''
def setMergeScheduler():
    '''returns IndexWriterConfig\n\n
    setMergeScheduler(final MergeScheduler mergeScheduler)\n
    '''
def getMergeScheduler():
    '''returns MergeScheduler\n\n
    getMergeScheduler()\n
    '''
def setCodec():
    '''returns IndexWriterConfig\n\n
    setCodec(final Codec codec)\n
    '''
def getCodec():
    '''returns Codec\n\n
    getCodec()\n
    '''
def getMergePolicy():
    '''returns MergePolicy\n\n
    getMergePolicy()\n
    '''
def setReaderPooling():
    '''returns IndexWriterConfig\n\n
    setReaderPooling(final boolean readerPooling)\n
    '''
def getReaderPooling():
    '''returns boolean\n\n
    getReaderPooling()\n
    '''
def setRAMPerThreadHardLimitMB():
    '''returns IndexWriterConfig\n\n
    setRAMPerThreadHardLimitMB(final int perThreadHardLimitMB)\n
    '''
def getRAMPerThreadHardLimitMB():
    '''returns int\n\n
    getRAMPerThreadHardLimitMB()\n
    '''
def getInfoStream():
    '''returns InfoStream\n\n
    getInfoStream()\n
    '''
def getAnalyzer():
    '''returns Analyzer\n\n
    getAnalyzer()\n
    '''
def getMaxBufferedDocs():
    '''returns int\n\n
    getMaxBufferedDocs()\n
    '''
def getRAMBufferSizeMB():
    '''returns double\n\n
    getRAMBufferSizeMB()\n
    '''
def setInfoStream():
    '''returns IndexWriterConfig\n\n
    setInfoStream(final InfoStream infoStream)\n
    setInfoStream(final PrintStream printStream)\n
    '''
def setMergePolicy():
    '''returns IndexWriterConfig\n\n
    setMergePolicy(final MergePolicy mergePolicy)\n
    '''
def setMaxBufferedDocs():
    '''returns IndexWriterConfig\n\n
    setMaxBufferedDocs(final int maxBufferedDocs)\n
    '''
def setMergedSegmentWarmer():
    '''returns IndexWriterConfig\n\n
    setMergedSegmentWarmer(final IndexWriter.IndexReaderWarmer mergeSegmentWarmer)\n
    '''
def setRAMBufferSizeMB():
    '''returns IndexWriterConfig\n\n
    setRAMBufferSizeMB(final double ramBufferSizeMB)\n
    '''
def setUseCompoundFile():
    '''returns IndexWriterConfig\n\n
    setUseCompoundFile(final boolean useCompoundFile)\n
    '''
def setCommitOnClose():
    '''returns IndexWriterConfig\n\n
    setCommitOnClose(final boolean commitOnClose)\n
    '''
def setIndexSort():
    '''returns IndexWriterConfig\n\n
    setIndexSort(final Sort sort)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setCheckPendingFlushUpdate():
    '''returns IndexWriterConfig\n\n
    setCheckPendingFlushUpdate(final boolean checkPendingFlushOnUpdate)\n
    '''
def setSoftDeletesField():
    '''returns IndexWriterConfig\n\n
    setSoftDeletesField(final String softDeletesField)\n
    '''
def setReaderAttributes():
    '''returns IndexWriterConfig\n\n
    setReaderAttributes(final Map<String, String> readerAttributes)\n
    '''
