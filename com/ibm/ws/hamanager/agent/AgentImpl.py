def getAgentClass():
'''public AgentClass getAgentClass()
'''
pass
def getInstanceId():
'''public Map getInstanceId()
'''
pass
def getPrimaryId():
'''public GroupMemberId getPrimaryId()
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
def isPrimary():
'''public boolean isPrimary()
'''
pass
def destroy():
'''public synchronized void destroy()
'''
pass
def destroySecondary():
'''public synchronized void destroySecondary()
'''
pass
def getMembers():
'''public GroupMemberId[] getMembers()
'''
pass
def sendMessage():
'''public void sendMessage(final MsgQoS qos, final GroupMemberId destination, final byte[] msg)
public void sendMessage(final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)
public void sendMessage(final MsgQoS qos, final byte[] msg)
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
'''public synchronized void onMessage(final GroupMemberId sender, final byte[] msg)
'''
pass
def membershipChanged():
'''public void membershipChanged(final GroupName groupName, final GroupMemberId[] members)
'''
pass
def toString():
'''public String toString()
'''
pass
