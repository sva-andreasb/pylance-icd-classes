def ():
    '''returns ContentManagerServiceStub\n\n
    ()\n
    (final URL endpointURL, final Service service)\n
    (final Service service)\n
    '''
def activate():
    '''returns None\n\n
    activate(final SearchPathSingleObject searchPath)\n
    '''
def activateURI():
    '''returns None\n\n
    activateURI(final String uri)\n
    '''
def add():
    '''returns BaseClass[]\n\n
    add(final SearchPathSingleObject parentPath, final BaseClass[] objects, final AddOptions options)\n
    '''
def addAnnotations():
    '''returns BaseClass[]\n\n
    addAnnotations(final SearchPathSingleObject containerPath, final BaseClass[] objects, final AddOptions options)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final AsynchRequest conversation)\n
    '''
def copy():
    '''returns BaseClass[]\n\n
    copy(final BaseClass[] objects, final SearchPathSingleObject targetPath, final CopyOptions options)\n
    '''
def copyAccount():
    '''returns None\n\n
    copyAccount(final SearchPathSingleObject sourceAccountPath, final SearchPathSingleObject targetAccountPath, final Option[] options)\n
    '''
def copyRename():
    '''returns BaseClass[]\n\n
    copyRename(final BaseClass[] objects, final SearchPathSingleObject targetPath, final String[] newNames, final CopyOptions options)\n
    '''
def delete():
    '''returns int\n\n
    delete(final BaseClass[] objects, final DeleteOptions options)\n
    '''
def deleteAccount():
    '''returns None\n\n
    deleteAccount(final SearchPathSingleObject objectPath, final Option[] options)\n
    '''
def deleteTenants():
    '''returns None\n\n
    deleteTenants(final String[] tenantIDs)\n
    '''
def determineRouting():
    '''returns String\n\n
    determineRouting(final SearchPathSingleObject[] objectPaths)\n
    '''
def getActiveContentManager():
    '''returns String\n\n
    getActiveContentManager()\n
    '''
def getDeploymentOptions():
    '''returns Option[]\n\n
    getDeploymentOptions(final String archive, final Option[] options)\n
    '''
def listArchives():
    '''returns String[]\n\n
    listArchives()\n
    '''
def listTenants():
    '''returns TenantInfo[]\n\n
    listTenants(final ListTenantsOptions options)\n
    '''
def logoff():
    '''returns None\n\n
    logoff()\n
    '''
def logon():
    '''returns None\n\n
    logon(final XmlEncodedXML credentials, final SearchPathSingleObject[] roles)\n
    '''
def move():
    '''returns BaseClass[]\n\n
    move(final BaseClass[] objects, final SearchPathSingleObject targetPath, final MoveOptions options)\n
    '''
def moveRename():
    '''returns BaseClass[]\n\n
    moveRename(final BaseClass[] objects, final SearchPathSingleObject targetPath, final String[] newNames, final MoveOptions options)\n
    '''
def query():
    '''returns BaseClass[]\n\n
    query(final SearchPathMultipleObject searchPath, final PropEnum[] properties, final Sort[] sortBy, final QueryOptions options)\n
    '''
def queryMultiple():
    '''returns QueryReply[]\n\n
    queryMultiple(final QueryRequest[] requests)\n
    '''
def queryMultipleCache():
    '''returns QueryMultipleResult\n\n
    queryMultipleCache(final QueryRequest[] requests, final QueryMultipleOptions options)\n
    '''
def release():
    '''returns None\n\n
    release(final AsynchRequest conversation)\n
    '''
def run():
    '''returns AsynchReply\n\n
    run(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def runSpecification():
    '''returns AsynchReply\n\n
    runSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def selectRoles():
    '''returns None\n\n
    selectRoles(final SearchPathSingleObject[] roles)\n
    '''
def update():
    '''returns BaseClass[]\n\n
    update(final BaseClass[] objects, final UpdateOptions options)\n
    '''
def wait():
    '''returns AsynchReply\n\n
    wait(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
