def generateUniqueID():
'''public static String generateUniqueID()
'''
pass
def uncompressMessage():
'''public static byte[] uncompressMessage(final byte[] cdata, final int uncompressedLength)
'''
pass
def compressMessage():
'''public static byte[] compressMessage(final byte[] messageBody)
'''
pass
def getProperties():
'''public static Map<String, String> getProperties(final Message msg)
'''
pass
def createJMSData():
'''public static JMSData createJMSData(final Message msg)
'''
pass
def createMessage():
'''public static Message createMessage(final JMSData data, final Session session)
'''
pass
def getQueueEmailInfo():
'''public static QueueEmailInfo getQueueEmailInfo(final QueueConfig queueConfig)
'''
pass
def queueEmailToBeSent():
'''public static boolean queueEmailToBeSent(final Map msgProperties)
'''
pass
def emailQueueError():
'''public static void emailQueueError(final QueueEmailInfo queueEmailInfo, final Exception t, final String errorMsgGroup, final String errorMsgKey, final String queueName)
'''
pass
def getJMSREcoveryFileName():
'''public static String getJMSREcoveryFileName(final Map msgProperties)
'''
pass
def convertBytesToRecoveryData():
'''public static Document convertBytesToRecoveryData(final byte[] data, final Map msgProperties)
'''
pass
def convertRecoveryDataToJMSData():
'''public static JMSData convertRecoveryDataToJMSData(final String filename, final boolean isCompress)
'''
pass
