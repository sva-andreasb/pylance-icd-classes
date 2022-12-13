def MessageErrorHandler():
'''public MessageErrorHandler(final String queue)
'''
pass
def initializeEmailInfo():
'''public void initializeEmailInfo()
'''
pass
def getErrorMsgForSeqQueue():
'''public JMSData getErrorMsgForSeqQueue(final String queueName)
'''
pass
def canProcess():
'''public int canProcess(final Map<String, String> properties)
'''
pass
def handleError():
'''public boolean handleError(final Exception t, final Map<String, String> msgProperties)
'''
pass
def getCorrectedFile():
'''public JMSData getCorrectedFile(final JMSData data)
'''
pass
def success():
'''public void success(final JMSData data)
'''
pass
def getJMSData():
'''public JMSData getJMSData(final Map<String, String> msgProperties)
'''
pass
def emailError():
'''public void emailError(final Exception t, final String uniqueId)
'''
pass
def emailToBeSent():
'''public boolean emailToBeSent(final Map<String, String> msgProperties)
'''
pass
def setMaxTryCount():
'''public void setMaxTryCount(final int newMaxTryCount)
'''
pass
