def generateUniqueID():
    '''    public static String generateUniqueID()
    '''
def uncompressMessage():
    '''    public static byte[] uncompressMessage(final byte[] cdata, final int uncompressedLength)
    '''
def compressMessage():
    '''    public static byte[] compressMessage(final byte[] messageBody)
    '''
def getProperties():
    '''    public static Map<String, String> getProperties(final Message msg)
    '''
def createJMSData():
    '''    public static JMSData createJMSData(final Message msg)
    '''
def createMessage():
    '''    public static Message createMessage(final JMSData data, final Session session)
    '''
def getQueueEmailInfo():
    '''    public static QueueEmailInfo getQueueEmailInfo(final QueueConfig queueConfig)
    '''
def queueEmailToBeSent():
    '''    public static boolean queueEmailToBeSent(final Map msgProperties)
    '''
def emailQueueError():
    '''    public static void emailQueueError(final QueueEmailInfo queueEmailInfo, final Exception t, final String errorMsgGroup, final String errorMsgKey, final String queueName)
    '''
def getJMSREcoveryFileName():
    '''    public static String getJMSREcoveryFileName(final Map msgProperties)
    '''
def convertBytesToRecoveryData():
    '''    public static Document convertBytesToRecoveryData(final byte[] data, final Map msgProperties)
    '''
def convertRecoveryDataToJMSData():
    '''    public static JMSData convertRecoveryDataToJMSData(final String filename, final boolean isCompress)
    '''
