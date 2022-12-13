def isDone():
'''public final synchronized boolean isDone()
'''
pass
def waitForCompletion():
'''public void waitForCompletion()
'''
pass
def waitForException():
'''public AmazonClientException waitForException()
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def getState():
'''public synchronized TransferState getState()
'''
pass
def setState():
'''public void setState(final TransferState state)
'''
pass
def notifyStateChangeListeners():
'''public void notifyStateChangeListeners(final TransferState state)
'''
pass
def addProgressListener():
'''public synchronized void addProgressListener(final ProgressListener listener)
public synchronized void addProgressListener(final com.amazonaws.services.s3.model.ProgressListener listener)
'''
pass
def removeProgressListener():
'''public synchronized void removeProgressListener(final ProgressListener listener)
public synchronized void removeProgressListener(final com.amazonaws.services.s3.model.ProgressListener listener)
'''
pass
def addStateChangeListener():
'''public synchronized void addStateChangeListener(final TransferStateChangeListener listener)
'''
pass
def removeStateChangeListener():
'''public synchronized void removeStateChangeListener(final TransferStateChangeListener listener)
'''
pass
def getProgress():
'''public TransferProgress getProgress()
'''
pass
def setMonitor():
'''public void setMonitor(final TransferMonitor monitor)
'''
pass
def getMonitor():
'''public TransferMonitor getMonitor()
'''
pass
