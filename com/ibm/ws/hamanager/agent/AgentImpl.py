def getAgentClass():
    '''public AgentClass getAgentClass()
    '''
def getInstanceId():
    '''public Map getInstanceId()
    '''
def getPrimaryId():
    '''public GroupMemberId getPrimaryId()
    '''
def getHAGroup():
    '''public HAGroup getHAGroup()
    '''
def getMemberName():
    '''public GroupMemberId getMemberName()
    '''
def isPrimary():
    '''public boolean isPrimary()
    '''
def destroy():
    '''public synchronized void destroy()
    '''
def destroySecondary():
    '''public synchronized void destroySecondary()
    '''
def getMembers():
    '''public GroupMemberId[] getMembers()
    '''
def sendMessage():
    '''public void sendMessage(final MsgQoS qos, final GroupMemberId destination, final byte[] msg)
    public void sendMessage(final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)
    public void sendMessage(final MsgQoS qos, final byte[] msg)
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
    '''public synchronized void onMessage(final GroupMemberId sender, final byte[] msg)
    '''
def membershipChanged():
    '''public void membershipChanged(final GroupName groupName, final GroupMemberId[] members)
    '''
def toString():
    '''public String toString()
    '''
