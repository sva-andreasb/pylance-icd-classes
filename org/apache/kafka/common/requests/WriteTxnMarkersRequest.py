def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def WriteTxnMarkersRequest():
'''public WriteTxnMarkersRequest(final Struct struct, final short version)
'''
pass
def markers():
'''public List<TxnMarkerEntry> markers()
'''
pass
def getErrorResponse():
'''public WriteTxnMarkersResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static WriteTxnMarkersRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def equals():
'''public boolean equals(final Object o)
public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def TxnMarkerEntry():
'''public TxnMarkerEntry(final long producerId, final short producerEpoch, final int coordinatorEpoch, final TransactionResult result, final List<TopicPartition> partitions)
'''
pass
def producerId():
'''public long producerId()
'''
pass
def producerEpoch():
'''public short producerEpoch()
'''
pass
def coordinatorEpoch():
'''public int coordinatorEpoch()
'''
pass
def transactionResult():
'''public TransactionResult transactionResult()
'''
pass
def partitions():
'''public List<TopicPartition> partitions()
'''
pass
def toString():
'''public String toString()
'''
pass
def Builder():
'''public Builder(final List<TxnMarkerEntry> markers)
'''
pass
def build():
'''public WriteTxnMarkersRequest build(final short version)
'''
pass
