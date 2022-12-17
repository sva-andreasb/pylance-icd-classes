def ():
    '''returns MessageErrorHandler\n\n
    (final String queue)\n
    '''
def initializeEmailInfo():
    '''returns None\n\n
    initializeEmailInfo()\n
    '''
def getErrorMsgForSeqQueue():
    '''returns JMSData\n\n
    getErrorMsgForSeqQueue(final String queueName)\n
    '''
def canProcess():
    '''returns int\n\n
    canProcess(final Map<String, String> properties)\n
    '''
def handleError():
    '''returns boolean\n\n
    handleError(final Exception t, final Map<String, String> msgProperties)\n
    '''
def getCorrectedFile():
    '''returns JMSData\n\n
    getCorrectedFile(final JMSData data)\n
    '''
def success():
    '''returns None\n\n
    success(final JMSData data)\n
    '''
def getJMSData():
    '''returns JMSData\n\n
    getJMSData(final Map<String, String> msgProperties)\n
    '''
def emailError():
    '''returns None\n\n
    emailError(final Exception t, final String uniqueId)\n
    '''
def emailToBeSent():
    '''returns boolean\n\n
    emailToBeSent(final Map<String, String> msgProperties)\n
    '''
def setMaxTryCount():
    '''returns None\n\n
    setMaxTryCount(final int newMaxTryCount)\n
    '''
