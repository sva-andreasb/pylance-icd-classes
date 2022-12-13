def JobClientImpl():
'''public JobClientImpl(final CloseableHttpClient client, final String url, final String token)
public JobClientImpl(final CloseableHttpClient client, final String url, final String clientid, final String secret)
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
def deleteAllJobs():
'''public void deleteAllJobs()
'''
pass
def getAllJobs():
'''public List<JobImpl> getAllJobs()
'''
pass
def createJob():
'''public String createJob(final JobCreationData data)
'''
pass
def submitJob():
'''public String submitJob(final JobCreationData data, final Object... atts)
'''
pass
def copyJob():
'''public String copyJob(final String jobid, final JobCreationData data, final boolean shallow)
'''
pass
def recreateJob():
'''public String recreateJob(final String jobid, final JobCreationData data, final boolean execute)
'''
pass
def getJob():
'''public JobImpl getJob(final String id)
'''
pass
def deleteJob():
'''public boolean deleteJob(final String id)
'''
pass
def getJobExecutionStatus():
'''public JobExecutionStatus getJobExecutionStatus(final String id)
'''
pass
def executeJob():
'''public void executeJob(final String id)
'''
pass
def abortJob():
'''public void abortJob(final String id)
'''
pass
def killJob():
'''public void killJob(final String id)
'''
pass
def getJobAttachments():
'''public List<JobAttachmentImpl> getJobAttachments(final String id)
public List<JobAttachmentImpl> getJobAttachments(final String id, final JobAttachmentType type)
'''
pass
def deleteJobAttachments():
'''public void deleteJobAttachments(final String id)
'''
pass
def createJobAttachment():
'''public String createJobAttachment(final String id, final JobAttachmentCreationData att)
'''
pass
def getJobAttachment():
'''public JobAttachmentImpl getJobAttachment(final String id, final String attid)
'''
pass
def deleteJobAttachment():
'''public boolean deleteJobAttachment(final String id, final String attid)
'''
pass
def uploadJobAttachment():
'''public void uploadJobAttachment(final String id, final String attid, final File archive)
public void uploadJobAttachment(final String id, final String attid, final InputStream archive)
public void uploadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final Object obj)
public void uploadJobAttachment(final String id, final String attid, final AttachmentContentWriter writer)
'''
pass
def downloadJobAttachment():
'''public void downloadJobAttachment(final String id, final String attid, final File archive)
public void downloadJobAttachment(final String id, final String attid, final OutputStream stream)
public InputStream downloadJobAttachment(final String id, final String attid)
public <T> T downloadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final TypeReference<T> type)
public <T> T downloadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final Class<T> type)
'''
pass
def downloadLog():
'''public void downloadLog(final String id, final File archive)
public void downloadLog(final String id, final OutputStream stream)
public InputStream downloadLog(final String id)
'''
pass
def getFailureInfo():
'''public JobFailureInfo getFailureInfo(final String id)
'''
pass
def getJobLogItems():
'''public List<JobLogItemImpl> getJobLogItems(final String jobid)
public List<JobLogItemImpl> getJobLogItems(final String jobid, final long start)
'''
pass
def newJobCreationData():
'''public JobCreationDataImpl newJobCreationData()
'''
pass
def newInputJobAttachment():
'''public JobAttachmentImpl newInputJobAttachment(final String name)
'''
pass
def newRequest():
'''public JobRequestBuilderImpl newRequest()
'''
pass
def dropAll():
'''public void dropAll()
'''
pass
def InternalCustomEntity():
'''public InternalCustomEntity(final AttachmentContentWriter entity)
'''
pass
def isRepeatable():
'''public boolean isRepeatable()
'''
pass
def getContentLength():
'''public long getContentLength()
'''
pass
def isStreaming():
'''public boolean isStreaming()
'''
pass
def getContent():
'''public InputStream getContent()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream outstream)
'''
pass
