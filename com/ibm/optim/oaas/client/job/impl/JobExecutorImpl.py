def ():
    '''returns RetryLoop\n\n
    (final ExecutorService service, final long interval, final long timeout, final int retry, final long retryDelay)\n
    ()\n
    '''
def getExecutionDetails():
    '''returns JobExecutionDetails\n\n
    getExecutionDetails()\n
    '''
def setExecutionDetails():
    '''returns None\n\n
    setExecutionDetails(final JobExecutionDetails executionDetails)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def create():
    '''returns Future<JobResponse>\n\n
    create(final JobRequest request, final JobCallback callback)\n
    '''
def submit():
    '''returns Future<JobResponse>\n\n
    submit(final JobRequest request, final JobCallback callback)\n
    '''
def monitor():
    '''returns Future<JobResponse>\n\n
    monitor(final JobRequest request, final String jobid, final JobCallback callback)\n
    '''
def execute():
    '''returns Future<JobResponse>\n\n
    execute(final JobRequest request, final JobCallback callback)\n
    execute(final JobRequest request)\n
    '''
def executeMain():
    '''returns Future<JobResponse>\n\n
    executeMain(final JobRequest request, final JobCallback callback, final boolean create, final boolean submit, final boolean monitor)\n
    '''
def call():
    '''returns JobResponse\n\n
    call()\n
    '''
def next():
    '''returns None\n\n
    next()\n
    '''
def exception():
    '''returns None\n\n
    exception(final OperationException e)\n
    '''
