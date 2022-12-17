def ():
    '''returns MaxMessageHandle\n\n
    ()\n
    (final int maxMessagesPerRead)\n
    ()\n
    '''
def maxMessagesPerRead():
    '''returns MaxMessagesRecvByteBufAllocator\n\n
    maxMessagesPerRead()\n
    maxMessagesPerRead(final int maxMessagesPerRead)\n
    '''
def respectMaybeMoreData():
    '''returns DefaultMaxMessagesRecvByteBufAllocator\n\n
    respectMaybeMoreData(final boolean respectMaybeMoreData)\n
    '''
def get():
    '''returns boolean\n\n
    get()\n
    '''
def reset():
    '''returns None\n\n
    reset(final ChannelConfig config)\n
    '''
def allocate():
    '''returns ByteBuf\n\n
    allocate(final ByteBufAllocator alloc)\n
    '''
def lastBytesRead():
    '''returns None\n\n
    lastBytesRead(final int bytes)\n
    '''
def continueReading():
    '''returns boolean\n\n
    continueReading()\n
    continueReading(final UncheckedBooleanSupplier maybeMoreDataSupplier)\n
    '''
def readComplete():
    '''returns None\n\n
    readComplete()\n
    '''
def attemptedBytesRead():
    '''returns None\n\n
    attemptedBytesRead()\n
    attemptedBytesRead(final int bytes)\n
    '''
