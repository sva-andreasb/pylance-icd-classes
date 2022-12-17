def ():
    '''returns Builder\n\n
    (final LogContext logContext, final int node)\n
    ()\n
    '''
def newBuilder():
    '''returns Builder\n\n
    newBuilder()\n
    '''
def handleResponse():
    '''returns boolean\n\n
    handleResponse(final FetchResponse response)\n
    '''
def handleError():
    '''returns None\n\n
    handleError(final Throwable t)\n
    '''
def toForget():
    '''returns List<TopicPartition>\n\n
    toForget()\n
    '''
def metadata():
    '''returns FetchMetadata\n\n
    metadata()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def add():
    '''returns None\n\n
    add(final TopicPartition topicPartition, final FetchRequest.PartitionData data)\n
    '''
def build():
    '''returns FetchRequestData\n\n
    build()\n
    '''
