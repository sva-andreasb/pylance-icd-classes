def LocalBulletinBoardStateManager():
    '''public LocalBulletinBoardStateManager(final CoordinatorImpl coordinator, final String dcsMember, final MessageCache messageCache, final Set coreGroupMembers, final Version version, final Set configuredBridges)
    '''
def updateCoreGroupMembership():
    '''public synchronized void updateCoreGroupMembership(final Set members)
    '''
def installNewView():
    '''public synchronized void installNewView(final String[] members, final boolean isGSRViewChange, final boolean allBridgesDied, final Set bridgesInNewView)
    '''
def bridgeStateUnsynchronized():
    '''public synchronized void bridgeStateUnsynchronized(final Set bridgesRunningInLocalAPG)
    '''
def bridgeStateSynchronized():
    '''public synchronized void bridgeStateSynchronized(final Set subjectsCurrentlyOwned)
    '''
def suspendBridgeUpdates():
    '''public void suspendBridgeUpdates()
    '''
def resumeBridgeUpdates():
    '''public synchronized void resumeBridgeUpdates()
    '''
def requestCurrentSubjectState():
    '''public synchronized SubjectValue[] requestCurrentSubjectState(final SubjectSubscriptionImpl subscription)
    '''
def getAllState():
    '''public void getAllState(final ReportClusterProcessStateMsg[] messages)
    public void getAllState(final ReportStateMsg[] messages)
    '''
def processGlobalStateRebuildMsg():
    '''public synchronized void processGlobalStateRebuildMsg(final BulletinBoardSubscriberUpdateMsg message, final int coordinatorIndex, final int numberActiveCoordinators)
    public synchronized void processGlobalStateRebuildMsg(final SubscriberUpdateMsg message, final int coordinatorIndex, final int numberActiveCoordinators, final boolean ongoingFSR)
    '''
def processBridgeRebuildMsg():
    '''public synchronized void processBridgeRebuildMsg(final SubscriberUpdateMsg message, final int coordinatorIndex, final int numberActiveCoordinators)
    '''
def processSubjectUpdates():
    '''public synchronized void processSubjectUpdates(final BulletinBoardSubscriberUpdateMsg message, final boolean rebuild)
    public synchronized void processSubjectUpdates(final SubscriberUpdateMsg message)
    '''
def SubscriberList():
    '''public SubscriberList(final SubjectInfoImpl subject)
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
def toString():
    '''public String toString()
    '''
def alarm():
    '''public void alarm(final Object alarmContext)
    '''
