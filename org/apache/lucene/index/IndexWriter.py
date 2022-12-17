MAX_DOCS = "int  2147483519"
MAX_POSITION = "int  2147483519"
WRITE_LOCK_NAME = "String  \"write.lock\""
SOURCE = "String  \"source\""
SOURCE_MERGE = "String  \"merge\""
SOURCE_FLUSH = "String  \"flush\""
SOURCE_ADDINDEXES_READERS = "String  \"addIndexes(CodecReader...)\""
MAX_TERM_LENGTH = "int  32766"
def numDeletedDocs():
    '''returns int\n\n
    numDeletedDocs(final SegmentCommitInfo info)\n
    '''
def ():
    '''returns IndexWriter\n\n
    (final Directory d, final IndexWriterConfig conf)\n
    '''
def deleteUnusedFiles():
    '''returns None\n\n
    deleteUnusedFiles(final Collection<String> files)\n
    '''
def flushFailed():
    '''returns None\n\n
    flushFailed(final SegmentInfo info)\n
    '''
def afterSegmentsFlushed():
    '''returns None\n\n
    afterSegmentsFlushed()\n
    '''
def onTragicEvent():
    '''returns None\n\n
    onTragicEvent(final Throwable event, final String message)\n
    '''
def onDeletesApplied():
    '''returns None\n\n
    onDeletesApplied()\n
    '''
def onTicketBacklog():
    '''returns None\n\n
    onTicketBacklog()\n
    '''
def getConfig():
    '''returns LiveIndexWriterConfig\n\n
    getConfig()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getDirectory():
    '''returns Directory\n\n
    getDirectory()\n
    '''
def getInfoStream():
    '''returns InfoStream\n\n
    getInfoStream()\n
    '''
def getAnalyzer():
    '''returns Analyzer\n\n
    getAnalyzer()\n
    '''
def addDocument():
    '''returns long\n\n
    addDocument(final Iterable<? extends IndexableField> doc)\n
    '''
def addDocuments():
    '''returns long\n\n
    addDocuments(final Iterable<? extends Iterable<? extends IndexableField>> docs)\n
    '''
def updateDocuments():
    '''returns long\n\n
    updateDocuments(final Term delTerm, final Iterable<? extends Iterable<? extends IndexableField>> docs)\n
    '''
def softUpdateDocuments():
    '''returns long\n\n
    softUpdateDocuments(final Term term, final Iterable<? extends Iterable<? extends IndexableField>> docs, final Field... softDeletes)\n
    '''
def deleteDocuments():
    '''returns long\n\n
    deleteDocuments(final Term... terms)\n
    deleteDocuments(final Query... queries)\n
    '''
def updateDocument():
    '''returns long\n\n
    updateDocument(final Term term, final Iterable<? extends IndexableField> doc)\n
    '''
def softUpdateDocument():
    '''returns long\n\n
    softUpdateDocument(final Term term, final Iterable<? extends IndexableField> doc, final Field... softDeletes)\n
    '''
def updateNumericDocValue():
    '''returns long\n\n
    updateNumericDocValue(final Term term, final String field, final long value)\n
    '''
def updateBinaryDocValue():
    '''returns long\n\n
    updateBinaryDocValue(final Term term, final String field, final BytesRef value)\n
    '''
def updateDocValues():
    '''returns long\n\n
    updateDocValues(final Term term, final Field... updates)\n
    '''
def getFieldNames():
    '''returns Set<String>\n\n
    getFieldNames()\n
    '''
def forceMerge():
    '''returns None\n\n
    forceMerge(final int maxNumSegments)\n
    forceMerge(final int maxNumSegments, final boolean doWait)\n
    '''
def forceMergeDeletes():
    '''returns None\n\n
    forceMergeDeletes(final boolean doWait)\n
    forceMergeDeletes()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def deleteAll():
    '''returns long\n\n
    deleteAll()\n
    '''
def addIndexes():
    '''returns long\n\n
    addIndexes(final Directory... dirs)\n
    addIndexes(final CodecReader... readers)\n
    '''
def merge():
    '''returns None\n\n
    merge(final MergePolicy.OneMerge merge)\n
    '''
def get():
    '''returns boolean\n\n
    get(final int index)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def getTragicException():
    '''returns Throwable\n\n
    getTragicException()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def getMaxCompletedSequenceNumber():
    '''returns long\n\n
    getMaxCompletedSequenceNumber()\n
    '''
