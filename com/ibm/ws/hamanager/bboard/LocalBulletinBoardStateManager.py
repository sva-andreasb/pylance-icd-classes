def LocalBulletinBoardStateManager():
'''public LocalBulletinBoardStateManager(final CoordinatorImpl coordinator, final String dcsMember, final MessageCache messageCache, final Set coreGroupMembers, final Version version, final Set configuredBridges)
'''
pass
def updateCoreGroupMembership():
'''public synchronized void updateCoreGroupMembership(final Set members)
'''
pass
def installNewView():
'''public synchronized void installNewView(final String[] members, final boolean isGSRViewChange, final boolean allBridgesDied, final Set bridgesInNewView)
'''
pass
def bridgeStateUnsynchronized():
'''public synchronized void bridgeStateUnsynchronized(final Set bridgesRunningInLocalAPG)
'''
pass
def bridgeStateSynchronized():
'''public synchronized void bridgeStateSynchronized(final Set subjectsCurrentlyOwned)
'''
pass
def suspendBridgeUpdates():
'''public void suspendBridgeUpdates()
'''
pass
def resumeBridgeUpdates():
'''public synchronized void resumeBridgeUpdates()
'''
pass
def requestCurrentSubjectState():
'''public synchronized SubjectValue[] requestCurrentSubjectState(final SubjectSubscriptionImpl subscription)
'''
pass
def getAllState():
'''public void getAllState(final ReportClusterProcessStateMsg[] messages)
public void getAllState(final ReportStateMsg[] messages)
'''
pass
def processGlobalStateRebuildMsg():
'''public synchronized void processGlobalStateRebuildMsg(final BulletinBoardSubscriberUpdateMsg message, final int coordinatorIndex, final int numberActiveCoordinators)
public synchronized void processGlobalStateRebuildMsg(final SubscriberUpdateMsg message, final int coordinatorIndex, final int numberActiveCoordinators, final boolean ongoingFSR)
'''
pass
def processBridgeRebuildMsg():
'''public synchronized void processBridgeRebuildMsg(final SubscriberUpdateMsg message, final int coordinatorIndex, final int numberActiveCoordinators)
'''
pass
def processSubjectUpdates():
'''public synchronized void processSubjectUpdates(final BulletinBoardSubscriberUpdateMsg message, final boolean rebuild)
public synchronized void processSubjectUpdates(final SubscriberUpdateMsg message)
'''
pass
def SubscriberList():
'''public SubscriberList(final SubjectInfoImpl subject)
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
def toString():
'''public String toString()
'''
pass
def alarm():
'''public void alarm(final Object alarmContext)
'''
pass
