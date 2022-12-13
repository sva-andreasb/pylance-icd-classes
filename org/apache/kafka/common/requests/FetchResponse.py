INVALID_HIGHWATERMARK = "long  -1L"
INVALID_LAST_STABLE_OFFSET = "long  -1L"
INVALID_LOG_START_OFFSET = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def FetchResponse():
'''public FetchResponse(final Errors error, final LinkedHashMap<TopicPartition, PartitionData> responseData, final int throttleTimeMs, final int sessionId)
public FetchResponse(final Struct struct)
'''
pass
def toStruct():
'''public Struct toStruct(final short version)
'''
pass
def error():
'''public Errors error()
'''
pass
def responseData():
'''public LinkedHashMap<TopicPartition, PartitionData> responseData()
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def sessionId():
'''public int sessionId()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static FetchResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def sizeOf():
'''public static int sizeOf(final short version, final Iterator<Map.Entry<TopicPartition, PartitionData>> partIterator)
'''
pass
def AbortedTransaction():
'''public AbortedTransaction(final long producerId, final long firstOffset)
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
def toString():
'''public String toString()
public String toString()
'''
pass
def PartitionData():
'''public PartitionData(final Errors error, final long highWatermark, final long lastStableOffset, final long logStartOffset, final List<AbortedTransaction> abortedTransactions, final Records records)
'''
pass
