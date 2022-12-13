def isDone():
    '''    public final synchronized boolean isDone()
    '''
def waitForCompletion():
    '''    public void waitForCompletion()
    '''
def waitForException():
    '''    public AmazonClientException waitForException()
    '''
def getDescription():
    '''    public String getDescription()
    '''
def getState():
    '''    public synchronized TransferState getState()
    '''
def setState():
    '''    public void setState(final TransferState state)
    '''
def notifyStateChangeListeners():
    '''    public void notifyStateChangeListeners(final TransferState state)
    '''
def addProgressListener():
    '''    public synchronized void addProgressListener(final ProgressListener listener)
    public synchronized void addProgressListener(final com.amazonaws.services.s3.model.ProgressListener listener)
    '''
def removeProgressListener():
    '''    public synchronized void removeProgressListener(final ProgressListener listener)
    public synchronized void removeProgressListener(final com.amazonaws.services.s3.model.ProgressListener listener)
    '''
def addStateChangeListener():
    '''    public synchronized void addStateChangeListener(final TransferStateChangeListener listener)
    '''
def removeStateChangeListener():
    '''    public synchronized void removeStateChangeListener(final TransferStateChangeListener listener)
    '''
def getProgress():
    '''    public TransferProgress getProgress()
    '''
def setMonitor():
    '''    public void setMonitor(final TransferMonitor monitor)
    '''
def getMonitor():
    '''    public TransferMonitor getMonitor()
    '''
