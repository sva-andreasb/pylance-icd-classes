def memberMayActivate():
    '''returns None\n\n
    memberMayActivate(final byte[] groupNameBytes)\n
    '''
def memberMayActivateCancelled():
    '''returns None\n\n
    memberMayActivateCancelled(final byte[] groupNameBytes)\n
    '''
def memberIsActivated():
    '''returns None\n\n
    memberIsActivated(final byte[] groupNameBytes, final int sequenceNumber)\n
    '''
def memberDeactivate():
    '''returns None\n\n
    memberDeactivate(final byte[] groupNameBytes, final int sequenceNumber)\n
    '''
def membershipChanged():
    '''returns None\n\n
    membershipChanged(final byte[] groupNameBytes, final byte[] membersBytes)\n
    '''
def isAlive():
    '''returns None\n\n
    isAlive(final byte[] groupNameBytes)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final byte[] groupNameBytes, final byte[] groupMemberIdBytes, final byte[] msg)\n
    '''
