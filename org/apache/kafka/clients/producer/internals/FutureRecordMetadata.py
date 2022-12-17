def ():
    '''returns FutureRecordMetadata\n\n
    (final ProduceRequestResult result, final long relativeOffset, final long createTimestamp, final Long checksum, final int serializedKeySize, final int serializedValueSize)\n
    '''
def cancel():
    '''returns boolean\n\n
    cancel(final boolean interrupt)\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def get():
    '''returns RecordMetadata\n\n
    get()\n
    get(final long timeout, final TimeUnit unit)\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
