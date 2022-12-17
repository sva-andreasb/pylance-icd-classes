def ():
    '''returns PartitionState\n\n
    ()\n
    (final TopicPartition topicPartition, final S state)\n
    '''
def moveToEnd():
    '''returns None\n\n
    moveToEnd(final TopicPartition topicPartition)\n
    '''
def updateAndMoveToEnd():
    '''returns None\n\n
    updateAndMoveToEnd(final TopicPartition topicPartition, final S state)\n
    '''
def remove():
    '''returns None\n\n
    remove(final TopicPartition topicPartition)\n
    '''
def partitionSet():
    '''returns Set<TopicPartition>\n\n
    partitionSet()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final TopicPartition topicPartition)\n
    '''
def partitionStates():
    '''returns List<PartitionState<S>>\n\n
    partitionStates()\n
    '''
def partitionStateValues():
    '''returns List<S>\n\n
    partitionStateValues()\n
    '''
def stateValue():
    '''returns S\n\n
    stateValue(final TopicPartition topicPartition)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def set():
    '''returns None\n\n
    set(final Map<TopicPartition, S> partitionToState)\n
    '''
def value():
    '''returns S\n\n
    value()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def topicPartition():
    '''returns TopicPartition\n\n
    topicPartition()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
