def ():
    '''returns StreamEncryptionInfo\n\n
    (final InputStream in, final boolean shouldIncludeContinueRecords)\n
    (final RecordInputStream rs, final List<Record> outputRecs)\n
    '''
def nextRecord():
    '''returns Record\n\n
    nextRecord()\n
    '''
def createDecryptingStream():
    '''returns RecordInputStream\n\n
    createDecryptingStream(final InputStream original)\n
    '''
def hasEncryption():
    '''returns boolean\n\n
    hasEncryption()\n
    '''
def getLastRecord():
    '''returns Record\n\n
    getLastRecord()\n
    '''
def hasBOFRecord():
    '''returns boolean\n\n
    hasBOFRecord()\n
    '''
