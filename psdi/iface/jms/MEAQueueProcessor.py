def writeDataToQueue():
    '''returns None\n\n
    writeDataToQueue(final MXTransaction mxtran, final String sender, final Map<String, ExternalDataInfo> finalData, final UserInfo userInfo)\n
    writeDataToQueue(final MXTransaction mxtran, final String sender, final Map<String, ExternalDataInfo> finalData, final boolean isEvent, final UserInfo userInfo)\n
    '''
def writeDataToQueueIn():
    '''returns None\n\n
    writeDataToQueueIn(final byte[] data, final Map<String, String> properties, final boolean compress)\n
    writeDataToQueueIn(final byte[] data, final String sender, final String ifaceName)\n
    writeDataToQueueIn(final byte[] data, final String sender, final String ifaceName, final String loginId)\n
    writeDataToQueueIn(final byte[] data, final Map<String, String> properties)\n
    '''
def writeToMessageProvider():
    '''returns boolean\n\n
    writeToMessageProvider(final byte[] extData, final Map<String, String> properties, final String kafkatopic, final String kafkaprovider, final boolean compress)\n
    '''
def writeToQueue():
    '''returns None\n\n
    writeToQueue(final byte[] extData, final Map<String, String> properties, final String queueName)\n
    writeToQueue(final byte[] extData, final Map<String, String> properties, final String queueName, final boolean compress)\n
    '''
