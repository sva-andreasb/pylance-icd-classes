HAM_CORESTACK_VIEW_CHANGE_INTO_SYNC = "int  0"
HAM_CORESTACK_VIEW_CHANGE_OUTOF_SYNC = "int  1"
FOREIGN_STATE_UNSYNCHRONONIZED_INTO_SYNC = "int  2"
FOREIGN_STATE_UNSYNCHRONONIZED_OUTOF_SYNC = "int  3"
FOREIGN_STATE_SYNCHRONIZED = "int  4"
INITIALIZE_NONBRIDGED_PROCESS = "int  5"
INITIALIZE_BRIDGED_PROCESS_IN_SINGLE_MEMBER_APG = "int  6"
INITIALIZE_BRIDGED_PROCESS_IN_MULTI_MEMBER_APG = "int  7"
def BridgeStateController():
    '''    public BridgeStateController(final BridgeStateManager observer, final Set configuredBridges, final String thisMembersDCSName)
    '''
def bridgeStateSynchronized():
    '''    public void bridgeStateSynchronized()
    '''
def bridgeStateUnsynchronized():
    '''    public synchronized void bridgeStateUnsynchronized(final Set activeBridgeMembers)
    '''
def installNewView():
    '''    public synchronized void installNewView(final String[] members, final boolean isGSRViewChange, final Set bridgesInNewView)
    '''
def CrossCoreStackEvent():
    '''    public CrossCoreStackEvent(final int eventIndex, final boolean isHamGSRViewChange)
    '''
def getEventIndex():
    '''    public int getEventIndex()
    '''
def isLocalViewChangeEvent():
    '''    public boolean isLocalViewChangeEvent()
    '''
def isGSRViewChange():
    '''    public boolean isGSRViewChange()
    '''
def CrossCoreStackStateMachine():
    '''    public CrossCoreStackStateMachine(final BridgeStateManager stateObserver, final int numberOfConfiguredBridges)
    '''
def initializeStateMachine():
    '''    public void initializeStateMachine(final int numberOfConfiguredBridges)
    '''
def processEvent():
    '''    public void processEvent(final CrossCoreStackEvent event)
    '''
