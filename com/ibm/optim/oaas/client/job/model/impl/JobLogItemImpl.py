MISSING_TIMEOUT = "long  10000L"
TYPE = "String  \"log\""
def ():
    '''returns JobLogItemImpl\n\n
    ()\n
    '''
def getSeqid():
    '''returns long\n\n
    getSeqid()\n
    '''
def setSeqid():
    '''returns None\n\n
    setSeqid(final long seqid)\n
    '''
def getEngineLogRecords():
    '''returns List<JobLogRecord>\n\n
    getEngineLogRecords()\n
    '''
def getImplEngineLogRecords():
    '''returns List<JobLogRecordImpl>\n\n
    getImplEngineLogRecords()\n
    '''
def setEngineLogRecords():
    '''returns None\n\n
    setEngineLogRecords(final List<JobLogRecordImpl> engineLogRecords)\n
    '''
def addRecord():
    '''returns None\n\n
    addRecord(final Date date, final String level, final String message)\n
    '''
def missing():
    '''returns boolean\n\n
    missing()\n
    '''
def setMising():
    '''returns None\n\n
    setMising(final boolean missing)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    '''
def stop():
    '''returns boolean\n\n
    stop()\n
    '''
def setStop():
    '''returns None\n\n
    setStop(final boolean stop)\n
    '''
