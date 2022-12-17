def ():
    '''returns SingleServerDataStackImpl\n\n
    (final String name, final DataStackCallback callback, final HAGroupImpl haGroup)\n
    (final String name, final DataStackCallback callback, final SyncDataReqCallback sdrcallback, final HAGroupImpl haGroup)\n
    '''
def getDataStackName():
    '''returns String\n\n
    getDataStackName()\n
    '''
def terminateDataStack():
    '''returns None\n\n
    terminateDataStack()\n
    '''
def requestData():
    '''returns byte[]\n\n
    requestData(final byte[] requestMsg, final long timeout)\n
    requestData(final GroupMemberId target, final byte[] requestMsg, final long timeout)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
