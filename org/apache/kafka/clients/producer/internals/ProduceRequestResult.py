def ():
    '''returns ProduceRequestResult\n\n
    (final TopicPartition topicPartition)\n
    '''
def set():
    '''returns None\n\n
    set(final long baseOffset, final long logAppendTime, final RuntimeException error)\n
    '''
def done():
    '''returns None\n\n
    done()\n
    '''
def await():
    '''returns boolean\n\n
    await()\n
    await(final long timeout, final TimeUnit unit)\n
    '''
def baseOffset():
    '''returns long\n\n
    baseOffset()\n
    '''
def hasLogAppendTime():
    '''returns boolean\n\n
    hasLogAppendTime()\n
    '''
def logAppendTime():
    '''returns long\n\n
    logAppendTime()\n
    '''
def error():
    '''returns RuntimeException\n\n
    error()\n
    '''
def topicPartition():
    '''returns TopicPartition\n\n
    topicPartition()\n
    '''
def completed():
    '''returns boolean\n\n
    completed()\n
    '''
