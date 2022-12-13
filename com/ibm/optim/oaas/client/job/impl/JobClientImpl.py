def JobClientImpl():
    '''public JobClientImpl(final CloseableHttpClient client, final String url, final String token)
    public JobClientImpl(final CloseableHttpClient client, final String url, final String clientid, final String secret)
    '''
def getExecutionDetails():
    '''public JobExecutionDetails getExecutionDetails()
    '''
def setExecutionDetails():
    '''public void setExecutionDetails(final JobExecutionDetails executionDetails)
    '''
def deleteAllJobs():
    '''public void deleteAllJobs()
    '''
def getAllJobs():
    '''public List<JobImpl> getAllJobs()
    '''
def createJob():
    '''public String createJob(final JobCreationData data)
    '''
def submitJob():
    '''public String submitJob(final JobCreationData data, final Object... atts)
    '''
def copyJob():
    '''public String copyJob(final String jobid, final JobCreationData data, final boolean shallow)
    '''
def recreateJob():
    '''public String recreateJob(final String jobid, final JobCreationData data, final boolean execute)
    '''
def getJob():
    '''public JobImpl getJob(final String id)
    '''
def deleteJob():
    '''public boolean deleteJob(final String id)
    '''
def getJobExecutionStatus():
    '''public JobExecutionStatus getJobExecutionStatus(final String id)
    '''
def executeJob():
    '''public void executeJob(final String id)
    '''
def abortJob():
    '''public void abortJob(final String id)
    '''
def killJob():
    '''public void killJob(final String id)
    '''
def getJobAttachments():
    '''public List<JobAttachmentImpl> getJobAttachments(final String id)
    public List<JobAttachmentImpl> getJobAttachments(final String id, final JobAttachmentType type)
    '''
def deleteJobAttachments():
    '''public void deleteJobAttachments(final String id)
    '''
def createJobAttachment():
    '''public String createJobAttachment(final String id, final JobAttachmentCreationData att)
    '''
def getJobAttachment():
    '''public JobAttachmentImpl getJobAttachment(final String id, final String attid)
    '''
def deleteJobAttachment():
    '''public boolean deleteJobAttachment(final String id, final String attid)
    '''
def uploadJobAttachment():
    '''public void uploadJobAttachment(final String id, final String attid, final File archive)
    public void uploadJobAttachment(final String id, final String attid, final InputStream archive)
    public void uploadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final Object obj)
    public void uploadJobAttachment(final String id, final String attid, final AttachmentContentWriter writer)
    '''
def downloadJobAttachment():
    '''public void downloadJobAttachment(final String id, final String attid, final File archive)
    public void downloadJobAttachment(final String id, final String attid, final OutputStream stream)
    public InputStream downloadJobAttachment(final String id, final String attid)
    public <T> T downloadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final TypeReference<T> type)
    public <T> T downloadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final Class<T> type)
    '''
def downloadLog():
    '''public void downloadLog(final String id, final File archive)
    public void downloadLog(final String id, final OutputStream stream)
    public InputStream downloadLog(final String id)
    '''
def getFailureInfo():
    '''public JobFailureInfo getFailureInfo(final String id)
    '''
def getJobLogItems():
    '''public List<JobLogItemImpl> getJobLogItems(final String jobid)
    public List<JobLogItemImpl> getJobLogItems(final String jobid, final long start)
    '''
def newJobCreationData():
    '''public JobCreationDataImpl newJobCreationData()
    '''
def newInputJobAttachment():
    '''public JobAttachmentImpl newInputJobAttachment(final String name)
    '''
def newRequest():
    '''public JobRequestBuilderImpl newRequest()
    '''
def dropAll():
    '''public void dropAll()
    '''
def InternalCustomEntity():
    '''public InternalCustomEntity(final AttachmentContentWriter entity)
    '''
def isRepeatable():
    '''public boolean isRepeatable()
    '''
def getContentLength():
    '''public long getContentLength()
    '''
def isStreaming():
    '''public boolean isStreaming()
    '''
def getContent():
    '''public InputStream getContent()
    '''
def writeTo():
    '''public void writeTo(final OutputStream outstream)
    '''
