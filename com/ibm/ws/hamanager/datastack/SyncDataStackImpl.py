def ():
    '''returns SyncDataStackImpl\n\n
    (final DCS dcs, final DCSPlugin plugin, final String name, final String dsType, final boolean usesVS, final HAGroupImpl haGroup, final CoreStackInfoImpl csi, final Map fdParms, final String[] members, final DataStackCallback callback, final SyncDataReqCallback sdrcallback)\n
    '''
def requestData():
    '''returns byte[]\n\n
    requestData(final byte[] requestMsg, final long timeout)\n
    requestData(final GroupMemberId target, final byte[] requestMsg, final long timeout)\n
    '''
def hasData():
    '''returns boolean\n\n
    hasData(final DCSMessage dcsReqMsg)\n
    '''
def getData():
    '''returns DCSMessage\n\n
    getData(final DCSMessage dcsReqMsg)\n
    '''
