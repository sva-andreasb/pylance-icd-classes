def getClassIdentifier():
    '''public Map getClassIdentifier()
    '''
def getInstanceIdentifier():
    '''public Map getInstanceIdentifier()
    '''
def getHAGroup():
    '''public HAGroup getHAGroup()
    '''
def getMemberName():
    '''public GroupMemberId getMemberName()
    '''
def createInstance():
    '''public Agent createInstance(final Map agentId, final String channelName)
    '''
def getClassMembers():
    '''public GroupMemberId[] getClassMembers()
    '''
def sendMessage():
    '''public void sendMessage(final MsgQoS qos, final GroupMemberId destination, final byte[] msg)
    public void sendMessage(final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)
    public void sendMessage(final MsgQoS qos, final byte[] msg)
    '''
def remove():
    '''public synchronized void remove()
    '''
def isAlive():
    '''public boolean isAlive(final GroupName gn)
    '''
def memberDeactivate():
    '''public void memberDeactivate(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)
    '''
def memberIsActivated():
    '''public void memberIsActivated(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)
    '''
def memberMayActivate():
    '''public void memberMayActivate(final GroupName groupName)
    '''
def memberMayActivateCancelled():
    '''public void memberMayActivateCancelled(final GroupName groupName)
    '''
def onMessage():
    '''public void onMessage(final GroupMemberId sender, final byte[] msg)
    '''
def membershipChanged():
    '''public void membershipChanged(final GroupName groupName, final GroupMemberId[] members)
    '''
def dataStackMessageReceived():
    '''public void dataStackMessageReceived(final GroupMemberId sender, final String channel, final byte[] message)
    '''
def dataStackMembershipChanged():
    '''public void dataStackMembershipChanged(final GroupMemberId[] members)
    '''
def dataStackTerminated():
    '''public void dataStackTerminated()
    '''
def dataStackEvent():
    '''public void dataStackEvent(final DataStackEvent event)
    '''
def dataStackViewAboutToChange():
    '''public void dataStackViewAboutToChange()
    '''
def toString():
    '''public String toString()
    '''
def doCallback():
    '''public void doCallback()
    '''
def getQueue():
    '''public int getQueue(final int numberOfQueues)
    '''
def getUserClassName():
    '''public String getUserClassName()
    '''
