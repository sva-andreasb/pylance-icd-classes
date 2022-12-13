def JobExecutorImpl():
'''public JobExecutorImpl(final ExecutorService service, final long interval, final long timeout, final int retry, final long retryDelay)
'''
pass
def getExecutionDetails():
'''public JobExecutionDetails getExecutionDetails()
'''
pass
def setExecutionDetails():
'''public void setExecutionDetails(final JobExecutionDetails executionDetails)
'''
pass
def start():
'''public void start()
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def create():
'''public Future<JobResponse> create(final JobRequest request, final JobCallback callback)
'''
pass
def submit():
'''public Future<JobResponse> submit(final JobRequest request, final JobCallback callback)
'''
pass
def monitor():
'''public Future<JobResponse> monitor(final JobRequest request, final String jobid, final JobCallback callback)
'''
pass
def execute():
'''public Future<JobResponse> execute(final JobRequest request, final JobCallback callback)
public Future<JobResponse> execute(final JobRequest request)
'''
pass
def executeMain():
'''public Future<JobResponse> executeMain(final JobRequest request, final JobCallback callback, final boolean create, final boolean submit, final boolean monitor)
'''
pass
def call():
'''public JobResponse call()
'''
pass
def RetryLoop():
'''public RetryLoop()
'''
pass
def next():
'''public void next()
'''
pass
def exception():
'''public void exception(final OperationException e)
'''
pass
