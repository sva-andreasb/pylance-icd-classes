TYPE = "String  \"job\""
def JobImpl():
    '''public JobImpl()
    '''
def getInitialQueueIndex():
    '''public Integer getInitialQueueIndex()
    '''
def setInitialQueueIndex():
    '''public void setInitialQueueIndex(final Integer initialQueueIndex)
    '''
def getCurrentQueueIndex():
    '''public Integer getCurrentQueueIndex()
    '''
def setCurrentQueueIndex():
    '''public void setCurrentQueueIndex(final Integer currentQueueIndex)
    '''
def getMerged():
    '''public List<String> getMerged()
    '''
def addToMerged():
    '''public void addToMerged(final List<String> tomerge)
    '''
def getUnmergedConflicts():
    '''public List<String> getUnmergedConflicts()
    '''
def needMerge():
    '''public boolean needMerge()
    '''
def getApiKey():
    '''public String getApiKey()
    '''
def setApiKey():
    '''public void setApiKey(final String apiKey)
    '''
def getModelName():
    '''public String getModelName()
    '''
def setModelName():
    '''public void setModelName(final String modelName)
    '''
def getModelVersion():
    '''public int getModelVersion()
    '''
def setModelVersion():
    '''public void setModelVersion(final int modelVersion)
    '''
def getModelVersionUsed():
    '''public int getModelVersionUsed()
    '''
def setModelVersionUsed():
    '''public void setModelVersionUsed(final int modelVersionUsed)
    '''
def getExecutionStatus():
    '''public JobExecutionStatus getExecutionStatus()
    '''
def setExecutionStatus():
    '''public void setExecutionStatus(final JobExecutionStatus status)
    '''
def getCreatedAt():
    '''public Date getCreatedAt()
    '''
def setCreatedAt():
    '''public void setCreatedAt(final Date createdAt)
    '''
def getStartedAt():
    '''public Date getStartedAt()
    '''
def setStartedAt():
    '''public void setStartedAt(final Date startedAt)
    '''
def getEndedAt():
    '''public Date getEndedAt()
    '''
def setEndedAt():
    '''public void setEndedAt(final Date endedAt)
    '''
def getEndRecordedAt():
    '''public Date getEndRecordedAt()
    '''
def setEndRecordedAt():
    '''public void setEndRecordedAt(final Date endRecordedAt)
    '''
def getUpdatedAt():
    '''public Date getUpdatedAt()
    '''
def setUpdatedAt():
    '''public void setUpdatedAt(final Date updatedAt)
    '''
def getParameters():
    '''public JobParameters getParameters()
    '''
def setParameter():
    '''public void setParameter(final String name, final String value)
    '''
def setParameters():
    '''public void setParameters(final Map<String, String> parameters)
    public void setParameters(final JobParameters parameters)
    '''
def getProcessingOwner():
    '''public String getProcessingOwner()
    '''
def setProcessingOwner():
    '''public void setProcessingOwner(final String owner)
    '''
def getLastProcessingOwner():
    '''public String getLastProcessingOwner()
    '''
def getOwner():
    '''public String getOwner()
    '''
def setOwner():
    '''public void setOwner(final String owner)
    '''
def toString():
    '''public String toString()
    '''
def getAttachments():
    '''public List<JobAttachment> getAttachments()
    '''
def getImplAttachments():
    '''public List<JobAttachmentImpl> getImplAttachments()
    '''
def setAttachments():
    '''public void setAttachments(final List<JobAttachmentImpl> attachments)
    '''
def getAttachment():
    '''public JobAttachmentImpl getAttachment(final String name)
    '''
def getAttachmentsProperties():
    '''public JobAttachmentsProperties getAttachmentsProperties()
    '''
def setAttachmentsProperties():
    '''public void setAttachmentsProperties(final JobAttachmentsProperties attachmentsProperties)
    '''
def getFailureInfo():
    '''public JobFailureInfoImpl getFailureInfo()
    '''
def setFailureInfo():
    '''public void setFailureInfo(final JobFailureInfoImpl failure)
    '''
def getLanguage():
    '''public String getLanguage()
    '''
def setLanguage():
    '''public void setLanguage(final String language)
    '''
def getDetails():
    '''public Map<String, String> getDetails()
    '''
def setSystemDetails():
    '''public void setSystemDetails(final Map<String, String> details)
    '''
def getSystemDetails():
    '''public Map<String, String> getSystemDetails()
    '''
def setDetails():
    '''public void setDetails(final Map<String, String> details)
    '''
def getSolveStatus():
    '''public JobSolveStatus getSolveStatus()
    '''
def setSolveStatus():
    '''public void setSolveStatus(final JobSolveStatus solveStatus)
    '''
def getInterruptionStatus():
    '''public JobInterruptionStatus getInterruptionStatus()
    '''
def setInterruptionStatus():
    '''public void setInterruptionStatus(final JobInterruptionStatus interruptionStatus)
    '''
def getInterruptedAt():
    '''public Date getInterruptedAt()
    '''
def setInterruptedAt():
    '''public void setInterruptedAt(final Date interruptedAt)
    '''
def getSubmittedAt():
    '''public Date getSubmittedAt()
    '''
def setSubmittedAt():
    '''public void setSubmittedAt(final Date submittedAt)
    '''
def getSubmittedToProcessorAt():
    '''public Date getSubmittedToProcessorAt()
    '''
def setSubmittedToProcessorAt():
    '''public void setSubmittedToProcessorAt(final Date submittedToProcessorAt)
    '''
def getNbLogItems():
    '''public Long getNbLogItems()
    '''
def setNbLogItems():
    '''public void setNbLogItems(final Long nbLogItems)
    '''
def getSubscription():
    '''public JobSubscriptionImpl getSubscription()
    '''
def setSubscription():
    '''public void setSubscription(final JobSubscriptionImpl subscription)
    '''
def getToken():
    '''public String getToken()
    '''
def setToken():
    '''public void setToken(final String token)
    '''
def getSubscriptionId():
    '''public String getSubscriptionId()
    '''
def getApiClient():
    '''public JobApiClientImpl getApiClient()
    '''
def setApiClient():
    '''public void setApiClient(final JobApiClientImpl apiClient)
    '''
def getSubscriber():
    '''public JobSubscriberImpl getSubscriber()
    '''
def setSubscriber():
    '''public void setSubscriber(final JobSubscriberImpl subscriber)
    '''
def getStorageVersion():
    '''public int getStorageVersion()
    '''
def setStorageVersion():
    '''public void setStorageVersion(final int storageVersion)
    '''
def getEncryptionKeyName():
    '''public String getEncryptionKeyName()
    '''
def setEncryptionKeyName():
    '''public void setEncryptionKeyName(final String encryptionKeyName)
    '''
def getLastDetails():
    '''public JobDetailsImpl getLastDetails()
    '''
def setLastDetails():
    '''public void setLastDetails(final JobDetailsImpl lastDetails)
    '''
def getETag():
    '''public String getETag()
    '''
def isIgnoreJobCount():
    '''public boolean isIgnoreJobCount()
    '''
def setIgnoreJobCount():
    '''public void setIgnoreJobCount(final boolean ignoreJobCount)
    '''
def getEmailForNotification():
    '''public String getEmailForNotification()
    '''
def getCorrelationId():
    '''public String getCorrelationId()
    '''
def setCorrelationId():
    '''public void setCorrelationId(final String correlationId)
    '''
def getLogTail():
    '''public List<String> getLogTail()
    '''
def setLogTail():
    '''public void setLogTail(final List<String> logTail)
    '''
def getJobLog():
    '''public String getJobLog()
    '''
def setJobLog():
    '''public void setJobLog(final String jobLog)
    '''
def getErrorInformation():
    '''public String getErrorInformation()
    '''
def setErrorInformation():
    '''public void setErrorInformation(final String errorInformation)
    '''
def getProjectName():
    '''public String getProjectName()
    '''
def setProjectName():
    '''public void setProjectName(final String projectName)
    '''
def getProjectId():
    '''public ObjectId getProjectId()
    '''
def setProjectId():
    '''public void setProjectId(final ObjectId projectId)
    '''
def getUserName():
    '''public String getUserName()
    '''
def setUserName():
    '''public void setUserName(final String userName)
    '''
def getUserEmail():
    '''public String getUserEmail()
    '''
def setUserEmail():
    '''public void setUserEmail(final String userEmail)
    '''
def getScenarioName():
    '''public String getScenarioName()
    '''
def setScenarioName():
    '''public void setScenarioName(final String scenarioName)
    '''
def getJobSolutionDetails():
    '''public JobSolutionDetails getJobSolutionDetails()
    '''
def setJobSolutionDetails():
    '''public void setJobSolutionDetails(final JobSolutionDetailsImpl jobSolutionDetails)
    '''
