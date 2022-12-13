def MessageErrorHandler():
    '''    public MessageErrorHandler(final String queue)
    '''
def initializeEmailInfo():
    '''    public void initializeEmailInfo()
    '''
def getErrorMsgForSeqQueue():
    '''    public JMSData getErrorMsgForSeqQueue(final String queueName)
    '''
def canProcess():
    '''    public int canProcess(final Map<String, String> properties)
    '''
def handleError():
    '''    public boolean handleError(final Exception t, final Map<String, String> msgProperties)
    '''
def getCorrectedFile():
    '''    public JMSData getCorrectedFile(final JMSData data)
    '''
def success():
    '''    public void success(final JMSData data)
    '''
def getJMSData():
    '''    public JMSData getJMSData(final Map<String, String> msgProperties)
    '''
def emailError():
    '''    public void emailError(final Exception t, final String uniqueId)
    '''
def emailToBeSent():
    '''    public boolean emailToBeSent(final Map<String, String> msgProperties)
    '''
def setMaxTryCount():
    '''    public void setMaxTryCount(final int newMaxTryCount)
    '''
