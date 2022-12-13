def writeDataToQueue():
'''public void writeDataToQueue(final MXTransaction mxtran, final String sender, final Map<String, ExternalDataInfo> finalData, final UserInfo userInfo)
public void writeDataToQueue(final MXTransaction mxtran, final String sender, final Map<String, ExternalDataInfo> finalData, final boolean isEvent, final UserInfo userInfo)
'''
pass
def writeDataToQueueIn():
'''public void writeDataToQueueIn(final byte[] data, final Map<String, String> properties, final boolean compress)
public void writeDataToQueueIn(final byte[] data, final String sender, final String ifaceName)
public void writeDataToQueueIn(final byte[] data, final String sender, final String ifaceName, final String loginId)
public void writeDataToQueueIn(final byte[] data, final Map<String, String> properties)
'''
pass
def writeToMessageProvider():
'''public boolean writeToMessageProvider(final byte[] extData, final Map<String, String> properties, final String kafkatopic, final String kafkaprovider, final boolean compress)
'''
pass
def writeToQueue():
'''public void writeToQueue(final byte[] extData, final Map<String, String> properties, final String queueName)
public void writeToQueue(final byte[] extData, final Map<String, String> properties, final String queueName, final boolean compress)
'''
pass
