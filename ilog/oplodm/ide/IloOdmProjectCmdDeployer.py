COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
RC_OK = "int  0"
def ():
    '''returns IloOdmProjectCmdDeployer\n\n
    ()\n
    '''
def execute():
    '''returns int\n\n
    execute(final String... args)\n
    execute(final List<String> args)\n
    '''
def getAcceptedIssuers():
    '''returns X509Certificate[]\n\n
    getAcceptedIssuers()\n
    '''
def checkServerTrusted():
    '''returns None\n\n
    checkServerTrusted(final X509Certificate[] chain, final String algo)\n
    '''
def checkClientTrusted():
    '''returns None\n\n
    checkClientTrusted(final X509Certificate[] arg0, final String arg1)\n
    '''
def taskSubmitted():
    '''returns None\n\n
    taskSubmitted(final IloTaskEvent evt)\n
    '''
def taskStarted():
    '''returns None\n\n
    taskStarted(final IloTaskEvent evt)\n
    '''
def completionChanged():
    '''returns None\n\n
    completionChanged(final IloTaskCompletionEvent evt)\n
    '''
def taskCompleted():
    '''returns None\n\n
    taskCompleted(final IloTaskEvent evt)\n
    '''
def taskCancelled():
    '''returns None\n\n
    taskCancelled(final IloTaskEvent evt)\n
    '''
def taskCancelledbyOtherUser():
    '''returns None\n\n
    taskCancelledbyOtherUser(final IloTaskEvent evt)\n
    '''
