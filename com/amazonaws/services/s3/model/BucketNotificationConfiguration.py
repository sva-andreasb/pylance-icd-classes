def ():
    '''returns TopicConfiguration\n\n
    ()\n
    (final String name, final NotificationConfiguration notificationConfiguration)\n
    (final Collection<TopicConfiguration> topicConfigurations)\n
    (final String topic, final String event)\n
    '''
def withNotificationConfiguration():
    '''returns BucketNotificationConfiguration\n\n
    withNotificationConfiguration(final Map<String, NotificationConfiguration> notificationConfiguration)\n
    '''
def addConfiguration():
    '''returns BucketNotificationConfiguration\n\n
    addConfiguration(final String name, final NotificationConfiguration notificationConfiguration)\n
    '''
def setConfigurations():
    '''returns None\n\n
    setConfigurations(final Map<String, NotificationConfiguration> configurations)\n
    '''
def getConfigurationByName():
    '''returns NotificationConfiguration\n\n
    getConfigurationByName(final String name)\n
    '''
def removeConfiguration():
    '''returns NotificationConfiguration\n\n
    removeConfiguration(final String name)\n
    '''
def withTopicConfigurations():
    '''returns BucketNotificationConfiguration\n\n
    withTopicConfigurations(final TopicConfiguration... topicConfigurations)\n
    '''
def setTopicConfigurations():
    '''returns None\n\n
    setTopicConfigurations(final Collection<TopicConfiguration> topicConfigurations)\n
    '''
def getTopicConfigurations():
    '''returns List<TopicConfiguration>\n\n
    getTopicConfigurations()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getTopic():
    '''returns String\n\n
    getTopic()\n
    '''
def getEvent():
    '''returns String\n\n
    getEvent()\n
    '''
