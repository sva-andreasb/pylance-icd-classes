def ():
    '''returns InternalCustomEntity\n\n
    (final CloseableHttpClient client, final String url, final String token)\n
    (final CloseableHttpClient client, final String url, final String clientid, final String secret)\n
    (final AttachmentContentWriter entity)\n
    '''
def getExecutionDetails():
    '''returns JobExecutionDetails\n\n
    getExecutionDetails()\n
    '''
def setExecutionDetails():
    '''returns None\n\n
    setExecutionDetails(final JobExecutionDetails executionDetails)\n
    '''
def deleteAllJobs():
    '''returns None\n\n
    deleteAllJobs()\n
    '''
def getAllJobs():
    '''returns List<JobImpl>\n\n
    getAllJobs()\n
    '''
def createJob():
    '''returns String\n\n
    createJob(final JobCreationData data)\n
    '''
def submitJob():
    '''returns String\n\n
    submitJob(final JobCreationData data, final Object... atts)\n
    '''
def copyJob():
    '''returns String\n\n
    copyJob(final String jobid, final JobCreationData data, final boolean shallow)\n
    '''
def recreateJob():
    '''returns String\n\n
    recreateJob(final String jobid, final JobCreationData data, final boolean execute)\n
    '''
def getJob():
    '''returns JobImpl\n\n
    getJob(final String id)\n
    '''
def deleteJob():
    '''returns boolean\n\n
    deleteJob(final String id)\n
    '''
def getJobExecutionStatus():
    '''returns JobExecutionStatus\n\n
    getJobExecutionStatus(final String id)\n
    '''
def executeJob():
    '''returns None\n\n
    executeJob(final String id)\n
    '''
def abortJob():
    '''returns None\n\n
    abortJob(final String id)\n
    '''
def killJob():
    '''returns None\n\n
    killJob(final String id)\n
    '''
def getJobAttachments():
    '''returns List<JobAttachmentImpl>\n\n
    getJobAttachments(final String id)\n
    getJobAttachments(final String id, final JobAttachmentType type)\n
    '''
def deleteJobAttachments():
    '''returns None\n\n
    deleteJobAttachments(final String id)\n
    '''
def createJobAttachment():
    '''returns String\n\n
    createJobAttachment(final String id, final JobAttachmentCreationData att)\n
    '''
def getJobAttachment():
    '''returns JobAttachmentImpl\n\n
    getJobAttachment(final String id, final String attid)\n
    '''
def deleteJobAttachment():
    '''returns boolean\n\n
    deleteJobAttachment(final String id, final String attid)\n
    '''
def uploadJobAttachment():
    '''returns None\n\n
    uploadJobAttachment(final String id, final String attid, final File archive)\n
    uploadJobAttachment(final String id, final String attid, final InputStream archive)\n
    uploadJobAttachment(final String id, final String attid, final ObjectMapper mapper, final Object obj)\n
    uploadJobAttachment(final String id, final String attid, final AttachmentContentWriter writer)\n
    '''
def downloadJobAttachment():
    '''returns InputStream\n\n
    downloadJobAttachment(final String id, final String attid, final File archive)\n
    downloadJobAttachment(final String id, final String attid, final OutputStream stream)\n
    downloadJobAttachment(final String id, final String attid)\n
    '''
def downloadLog():
    '''returns InputStream\n\n
    downloadLog(final String id, final File archive)\n
    downloadLog(final String id, final OutputStream stream)\n
    downloadLog(final String id)\n
    '''
def getFailureInfo():
    '''returns JobFailureInfo\n\n
    getFailureInfo(final String id)\n
    '''
def getJobLogItems():
    '''returns List<JobLogItemImpl>\n\n
    getJobLogItems(final String jobid)\n
    getJobLogItems(final String jobid, final long start)\n
    '''
def newJobCreationData():
    '''returns JobCreationDataImpl\n\n
    newJobCreationData()\n
    '''
def newInputJobAttachment():
    '''returns JobAttachmentImpl\n\n
    newInputJobAttachment(final String name)\n
    '''
def newRequest():
    '''returns JobRequestBuilderImpl\n\n
    newRequest()\n
    '''
def dropAll():
    '''returns None\n\n
    dropAll()\n
    '''
def isRepeatable():
    '''returns boolean\n\n
    isRepeatable()\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def isStreaming():
    '''returns boolean\n\n
    isStreaming()\n
    '''
def getContent():
    '''returns InputStream\n\n
    getContent()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream outstream)\n
    '''
