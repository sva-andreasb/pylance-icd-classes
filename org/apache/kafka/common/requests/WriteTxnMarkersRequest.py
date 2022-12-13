def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def WriteTxnMarkersRequest():
    '''public WriteTxnMarkersRequest(final Struct struct, final short version)
    '''
def markers():
    '''public List<TxnMarkerEntry> markers()
    '''
def getErrorResponse():
    '''public WriteTxnMarkersResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''public static WriteTxnMarkersRequest parse(final ByteBuffer buffer, final short version)
    '''
def equals():
    '''public boolean equals(final Object o)
    public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    public int hashCode()
    '''
def TxnMarkerEntry():
    '''public TxnMarkerEntry(final long producerId, final short producerEpoch, final int coordinatorEpoch, final TransactionResult result, final List<TopicPartition> partitions)
    '''
def producerId():
    '''public long producerId()
    '''
def producerEpoch():
    '''public short producerEpoch()
    '''
def coordinatorEpoch():
    '''public int coordinatorEpoch()
    '''
def transactionResult():
    '''public TransactionResult transactionResult()
    '''
def partitions():
    '''public List<TopicPartition> partitions()
    '''
def toString():
    '''public String toString()
    '''
def Builder():
    '''public Builder(final List<TxnMarkerEntry> markers)
    '''
def build():
    '''public WriteTxnMarkersRequest build(final short version)
    '''
