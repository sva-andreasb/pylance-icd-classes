DSTYPE_BASE = "String  \"BASE\""
DSTYPE_SYNC = "String  \"SYNC\""
def ():
    '''returns DataStackImpl\n\n
    (final DCS dcs, final DCSPlugin plugin, final String name, final String dsType, final boolean usesVS, final HAGroupImpl haGroup, final CoreStackInfoImpl csi, final Map fdParms, final String[] members, final DataStackCallback callback)\n
    '''
def getDataStackName():
    '''returns String\n\n
    getDataStackName()\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final DCSMessage dcsMsg)\n
    '''
def removeMembers():
    '''returns None\n\n
    removeMembers(final String[] members)\n
    '''
def check():
    '''returns Throwable\n\n
    check()\n
    '''
def handleViewChangeEvent():
    '''returns None\n\n
    handleViewChangeEvent(final ViewChangeEvent event, final Comparable id)\n
    '''
def notifyEvent():
    '''returns None\n\n
    notifyEvent(final DCSExternalEvent event)\n
    '''
def approvePartialNewView():
    '''returns None\n\n
    approvePartialNewView(final ViewId viewID, final String[] viewMembers, final int context)\n
    '''
