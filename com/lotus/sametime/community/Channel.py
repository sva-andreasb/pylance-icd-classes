def addChannelListener():
'''public synchronized void addChannelListener(final ChannelListener obj)
'''
pass
def removeChannelListener():
'''public synchronized void removeChannelListener(final ChannelListener obj)
'''
pass
def open():
'''public synchronized void open()
'''
pass
def accept():
'''public void accept(final EncLevel encLevel, final byte[] array)
public void accept(final EncLevel encLevel, final byte[] array, final STUserInstance stUserInstance)
public synchronized void accept(final EncLevel encLevel, final byte[] array, final byte b)
public synchronized void accept(final EncLevel encLevel, final byte[] array, final byte priority, final STUserInstance stUserInstance)
'''
pass
def sendMsg():
'''public synchronized void sendMsg(final short n, final byte[] array, final boolean b)
'''
pass
def close():
'''public synchronized void close(final int n, final byte[] array)
'''
pass
def pend():
'''public void pend()
'''
pass
def getServiceType():
'''public int getServiceType()
'''
pass
def getProtocolType():
'''public int getProtocolType()
'''
pass
def getProtocolVersion():
'''public int getProtocolVersion()
'''
pass
def setProtocolVersion():
'''public void setProtocolVersion(final int prVersion)
'''
pass
def getEncLevel():
'''public EncLevel getEncLevel()
'''
pass
def getCreateData():
'''public byte[] getCreateData()
'''
pass
def getRemoteInfo():
'''public STUserInstance getRemoteInfo()
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def isPending():
'''public boolean isPending()
'''
pass
def getPriority():
'''public byte getPriority()
'''
pass
def getToUser():
'''public STUser getToUser()
'''
pass
def getCreator():
'''public STUserInstance getCreator()
'''
pass
