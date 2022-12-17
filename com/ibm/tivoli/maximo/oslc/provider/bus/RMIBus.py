MEMBER_CONTEXT = "String  \"members\""
def ():
    '''returns RMIBus\n\n
    ()\n
    '''
def getResource():
    '''returns OslcResourceResponse\n\n
    getResource(final String requestPath, final OslcRequest request)\n
    '''
def getDBInfo():
    '''returns BusResource\n\n
    getDBInfo()\n
    '''
def getMembers():
    '''returns BusResourceCollection\n\n
    getMembers()\n
    '''
def isThisServer():
    '''returns boolean\n\n
    isThisServer(final String serverHost, final String serverName)\n
    '''
def crawlToMember():
    '''returns BusMemberServiceRemote\n\n
    crawlToMember(final String memberId)\n
    '''
