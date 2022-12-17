COMMIT_JOB = "String  \"SKDCOMMITJOB\""
VALIDATION_JOB = "String  \"SKDVALIDATIONJOB\""
SUCCESS = "int  0"
START = "int  1"
FAIL = "int  2"
def asyncProcess():
    '''returns None\n\n
    asyncProcess(final MXServer server, final String jobName, final String jobQueueNum, final String Object, final UserInfo ui, final String whereClause, final HashMap<String, MaxType> params)\n
    asyncProcess(final String jobName, final String jobQueueNum, final String Object, final UserInfo ui, final String whereClause, final HashMap<String, MaxType> params)\n
    '''
