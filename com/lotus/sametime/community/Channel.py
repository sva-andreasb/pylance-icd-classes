def addChannelListener():
    '''    public synchronized void addChannelListener(final ChannelListener obj)
    '''
def removeChannelListener():
    '''    public synchronized void removeChannelListener(final ChannelListener obj)
    '''
def open():
    '''    public synchronized void open()
    '''
def accept():
    '''    public void accept(final EncLevel encLevel, final byte[] array)
    public void accept(final EncLevel encLevel, final byte[] array, final STUserInstance stUserInstance)
    public synchronized void accept(final EncLevel encLevel, final byte[] array, final byte b)
    public synchronized void accept(final EncLevel encLevel, final byte[] array, final byte priority, final STUserInstance stUserInstance)
    '''
def sendMsg():
    '''    public synchronized void sendMsg(final short n, final byte[] array, final boolean b)
    '''
def close():
    '''    public synchronized void close(final int n, final byte[] array)
    '''
def pend():
    '''    public void pend()
    '''
def getServiceType():
    '''    public int getServiceType()
    '''
def getProtocolType():
    '''    public int getProtocolType()
    '''
def getProtocolVersion():
    '''    public int getProtocolVersion()
    '''
def setProtocolVersion():
    '''    public void setProtocolVersion(final int prVersion)
    '''
def getEncLevel():
    '''    public EncLevel getEncLevel()
    '''
def getCreateData():
    '''    public byte[] getCreateData()
    '''
def getRemoteInfo():
    '''    public STUserInstance getRemoteInfo()
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def isPending():
    '''    public boolean isPending()
    '''
def getPriority():
    '''    public byte getPriority()
    '''
def getToUser():
    '''    public STUser getToUser()
    '''
def getCreator():
    '''    public STUserInstance getCreator()
    '''
