def ():
    '''returns SubscriptionState\n\n
    (final OffsetResetStrategy defaultResetStrategy)\n
    '''
def subscribe():
    '''returns None\n\n
    subscribe(final Set<String> topics, final ConsumerRebalanceListener listener)\n
    subscribe(final Pattern pattern, final ConsumerRebalanceListener listener)\n
    '''
def subscribeFromPattern():
    '''returns None\n\n
    subscribeFromPattern(final Set<String> topics)\n
    '''
def groupSubscribe():
    '''returns None\n\n
    groupSubscribe(final Collection<String> topics)\n
    '''
def resetGroupSubscription():
    '''returns None\n\n
    resetGroupSubscription()\n
    '''
def assignFromUser():
    '''returns None\n\n
    assignFromUser(final Set<TopicPartition> partitions)\n
    '''
def assignFromSubscribed():
    '''returns None\n\n
    assignFromSubscribed(final Collection<TopicPartition> assignments)\n
    '''
def hasPatternSubscription():
    '''returns boolean\n\n
    hasPatternSubscription()\n
    '''
def hasNoSubscriptionOrUserAssignment():
    '''returns boolean\n\n
    hasNoSubscriptionOrUserAssignment()\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe()\n
    '''
def subscribedPattern():
    '''returns Pattern\n\n
    subscribedPattern()\n
    '''
def subscription():
    '''returns Set<String>\n\n
    subscription()\n
    '''
def pausedPartitions():
    '''returns Set<TopicPartition>\n\n
    pausedPartitions()\n
    '''
def groupSubscription():
    '''returns Set<String>\n\n
    groupSubscription()\n
    '''
def seek():
    '''returns None\n\n
    seek(final TopicPartition tp, final long offset)\n
    '''
def assignedPartitions():
    '''returns Set<TopicPartition>\n\n
    assignedPartitions()\n
    '''
def fetchablePartitions():
    '''returns List<TopicPartition>\n\n
    fetchablePartitions()\n
    '''
def partitionsAutoAssigned():
    '''returns boolean\n\n
    partitionsAutoAssigned()\n
    '''
def position():
    '''returns Long\n\n
    position(final TopicPartition tp, final long offset)\n
    position(final TopicPartition tp)\n
    '''
def partitionLag():
    '''returns Long\n\n
    partitionLag(final TopicPartition tp, final IsolationLevel isolationLevel)\n
    '''
def updateHighWatermark():
    '''returns None\n\n
    updateHighWatermark(final TopicPartition tp, final long highWatermark)\n
    '''
def updateLastStableOffset():
    '''returns None\n\n
    updateLastStableOffset(final TopicPartition tp, final long lastStableOffset)\n
    '''
def requestOffsetReset():
    '''returns None\n\n
    requestOffsetReset(final TopicPartition partition, final OffsetResetStrategy offsetResetStrategy)\n
    requestOffsetReset(final TopicPartition partition)\n
    '''
def setResetPending():
    '''returns None\n\n
    setResetPending(final Set<TopicPartition> partitions, final long nextAllowResetTimeMs)\n
    '''
def hasDefaultOffsetResetPolicy():
    '''returns boolean\n\n
    hasDefaultOffsetResetPolicy()\n
    '''
def isOffsetResetNeeded():
    '''returns boolean\n\n
    isOffsetResetNeeded(final TopicPartition partition)\n
    '''
def resetStrategy():
    '''returns OffsetResetStrategy\n\n
    resetStrategy(final TopicPartition partition)\n
    '''
def hasAllFetchPositions():
    '''returns boolean\n\n
    hasAllFetchPositions()\n
    '''
def missingFetchPositions():
    '''returns Set<TopicPartition>\n\n
    missingFetchPositions()\n
    '''
def resetMissingPositions():
    '''returns None\n\n
    resetMissingPositions()\n
    '''
def partitionsNeedingReset():
    '''returns Set<TopicPartition>\n\n
    partitionsNeedingReset(final long nowMs)\n
    '''
def isAssigned():
    '''returns boolean\n\n
    isAssigned(final TopicPartition tp)\n
    '''
def isPaused():
    '''returns boolean\n\n
    isPaused(final TopicPartition tp)\n
    '''
def isFetchable():
    '''returns boolean\n\n
    isFetchable(final TopicPartition tp)\n
    '''
def hasValidPosition():
    '''returns boolean\n\n
    hasValidPosition(final TopicPartition tp)\n
    '''
def pause():
    '''returns None\n\n
    pause(final TopicPartition tp)\n
    '''
def resume():
    '''returns None\n\n
    resume(final TopicPartition tp)\n
    '''
def resetFailed():
    '''returns None\n\n
    resetFailed(final Set<TopicPartition> partitions, final long nextRetryTimeMs)\n
    '''
def movePartitionToEnd():
    '''returns None\n\n
    movePartitionToEnd(final TopicPartition tp)\n
    '''
def rebalanceListener():
    '''returns ConsumerRebalanceListener\n\n
    rebalanceListener()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final Listener listener)\n
    '''
def fireOnAssignment():
    '''returns None\n\n
    fireOnAssignment(final Set<TopicPartition> assignment)\n
    '''
