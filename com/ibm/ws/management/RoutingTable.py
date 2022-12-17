INIT_STATE = "int  0"
MONITOR_STATE = "int  1"
RECOVERY_STATE = "int  2"
DISCOVERY_EVENT = "int  0"
REACHABLE_EVENT = "int  1"
NOT_REACHABLE_EVENT = "int  2"
RESET_EVENT = "int  3"
def getProductVersion():
    '''returns String\n\n
    getProductVersion(final String name)\n
    '''
def getParent():
    '''returns AdminClient\n\n
    getParent()\n
    '''
def connectedToParent():
    '''returns boolean\n\n
    connectedToParent(long timeout)\n
    '''
def getSession():
    '''returns Session\n\n
    getSession(final String name)\n
    '''
def getPid():
    '''returns String\n\n
    getPid(final String name)\n
    '''
def setOwnInfo():
    '''returns None\n\n
    setOwnInfo(final ServerInfo self)\n
    '''
def getOwnInfo():
    '''returns ServerInfo\n\n
    getOwnInfo()\n
    '''
def isRoutable():
    '''returns boolean\n\n
    isRoutable(final String name)\n
    '''
def getAdminClients():
    '''returns AdminClient[]\n\n
    getAdminClients()\n
    '''
def getAdminClient():
    '''returns AdminClient\n\n
    getAdminClient(final String name)\n
    getAdminClient(final String name, final String connectorType)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final ServerInfo serverInfo)\n
    '''
def isChildDisabled():
    '''returns boolean\n\n
    isChildDisabled(final String name)\n
    '''
def getDisabledAdminClient():
    '''returns AdminClient\n\n
    getDisabledAdminClient(final String name)\n
    '''
def addParent():
    '''returns None\n\n
    addParent(final ServerInfo serverInfo)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification ntfyObj, final Object handback)\n
    '''
def isXCFGroupMember():
    '''returns boolean\n\n
    isXCFGroupMember(final String memberName)\n
    '''
def getXCFGroupMembers():
    '''returns HashMap\n\n
    getXCFGroupMembers()\n
    '''
def getXCFGroupMember():
    '''returns Long\n\n
    getXCFGroupMember(final String memberName)\n
    '''
def getmyXCFHostCellNode():
    '''returns String\n\n
    getmyXCFHostCellNode()\n
    '''
def addXCFGroupMember():
    '''returns None\n\n
    addXCFGroupMember(final String memberName, final Long context)\n
    '''
def removeXCFGroupMember():
    '''returns None\n\n
    removeXCFGroupMember(final String memberName)\n
    '''
def isXCFMonitorEnabled():
    '''returns boolean\n\n
    isXCFMonitorEnabled()\n
    '''
def checkAdminContext():
    '''returns None\n\n
    checkAdminContext()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def ():
    '''returns StateMachine\n\n
    (final Session session)\n
    ()\n
    ()\n
    ()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def stopMonitor():
    '''returns None\n\n
    stopMonitor(final Accessor accessor)\n
    stopMonitor(final Accessor accessor)\n
    stopMonitor(final Accessor accessor)\n
    '''
def routeAdded():
    '''returns None\n\n
    routeAdded(final Accessor accessor)\n
    routeAdded(final Accessor accessor)\n
    routeAdded(final Accessor accessor)\n
    routeAdded(final Accessor accessor)\n
    '''
def routeRemoved():
    '''returns None\n\n
    routeRemoved(final Accessor accessor)\n
    routeRemoved(final Accessor accessor)\n
    routeRemoved(final Accessor accessor)\n
    routeRemoved(final Accessor accessor)\n
    '''
def startMonitor():
    '''returns None\n\n
    startMonitor(final Accessor accessor)\n
    startMonitor(final Accessor accessor)\n
    startMonitor(final Accessor accessor)\n
    startMonitor(final Accessor accessor)\n
    '''
def transition():
    '''returns None\n\n
    transition(final int event, final Session eventSession, final Accessor accessor, final StateMachineCallback callback)\n
    '''
def getState():
    '''returns int\n\n
    getState()\n
    '''
