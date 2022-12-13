def getClassIdentifier():
'''public Map getClassIdentifier()
'''
pass
def getInstanceIdentifier():
'''public Map getInstanceIdentifier()
'''
pass
def getHAGroup():
'''public HAGroup getHAGroup()
'''
pass
def getMemberName():
'''public GroupMemberId getMemberName()
'''
pass
def createInstance():
'''public Agent createInstance(final Map agentId, final String channelName)
'''
pass
def getClassMembers():
'''public GroupMemberId[] getClassMembers()
'''
pass
def sendMessage():
'''public void sendMessage(final MsgQoS qos, final GroupMemberId destination, final byte[] msg)
public void sendMessage(final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)
public void sendMessage(final MsgQoS qos, final byte[] msg)
'''
pass
def remove():
'''public synchronized void remove()
'''
pass
def isAlive():
'''public boolean isAlive(final GroupName gn)
'''
pass
def memberDeactivate():
'''public void memberDeactivate(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)
'''
pass
def memberIsActivated():
'''public void memberIsActivated(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)
'''
pass
def memberMayActivate():
'''public void memberMayActivate(final GroupName groupName)
'''
pass
def memberMayActivateCancelled():
'''public void memberMayActivateCancelled(final GroupName groupName)
'''
pass
def onMessage():
'''public void onMessage(final GroupMemberId sender, final byte[] msg)
'''
pass
def membershipChanged():
'''public void membershipChanged(final GroupName groupName, final GroupMemberId[] members)
'''
pass
def dataStackMessageReceived():
'''public void dataStackMessageReceived(final GroupMemberId sender, final String channel, final byte[] message)
'''
pass
def dataStackMembershipChanged():
'''public void dataStackMembershipChanged(final GroupMemberId[] members)
'''
pass
def dataStackTerminated():
'''public void dataStackTerminated()
'''
pass
def dataStackEvent():
'''public void dataStackEvent(final DataStackEvent event)
'''
pass
def dataStackViewAboutToChange():
'''public void dataStackViewAboutToChange()
'''
pass
def toString():
'''public String toString()
'''
pass
def doCallback():
'''public void doCallback()
'''
pass
def getQueue():
'''public int getQueue(final int numberOfQueues)
'''
pass
def getUserClassName():
'''public String getUserClassName()
'''
pass
