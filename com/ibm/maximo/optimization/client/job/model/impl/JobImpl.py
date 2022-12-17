TYPE = "String  \"job\""
def ():
    '''returns JobImpl\n\n
    ()\n
    '''
def getInitialQueueIndex():
    '''returns Integer\n\n
    getInitialQueueIndex()\n
    '''
def setInitialQueueIndex():
    '''returns None\n\n
    setInitialQueueIndex(final Integer initialQueueIndex)\n
    '''
def getCurrentQueueIndex():
    '''returns Integer\n\n
    getCurrentQueueIndex()\n
    '''
def setCurrentQueueIndex():
    '''returns None\n\n
    setCurrentQueueIndex(final Integer currentQueueIndex)\n
    '''
def getMerged():
    '''returns List<String>\n\n
    getMerged()\n
    '''
def addToMerged():
    '''returns None\n\n
    addToMerged(final List<String> tomerge)\n
    '''
def getUnmergedConflicts():
    '''returns List<String>\n\n
    getUnmergedConflicts()\n
    '''
def needMerge():
    '''returns boolean\n\n
    needMerge()\n
    '''
def getApiKey():
    '''returns String\n\n
    getApiKey()\n
    '''
def setApiKey():
    '''returns None\n\n
    setApiKey(final String apiKey)\n
    '''
def getModelName():
    '''returns String\n\n
    getModelName()\n
    '''
def setModelName():
    '''returns None\n\n
    setModelName(final String modelName)\n
    '''
def getModelVersion():
    '''returns int\n\n
    getModelVersion()\n
    '''
def setModelVersion():
    '''returns None\n\n
    setModelVersion(final int modelVersion)\n
    '''
def getModelVersionUsed():
    '''returns int\n\n
    getModelVersionUsed()\n
    '''
def setModelVersionUsed():
    '''returns None\n\n
    setModelVersionUsed(final int modelVersionUsed)\n
    '''
def getExecutionStatus():
    '''returns JobExecutionStatus\n\n
    getExecutionStatus()\n
    '''
def setExecutionStatus():
    '''returns None\n\n
    setExecutionStatus(final JobExecutionStatus status)\n
    '''
def getCreatedAt():
    '''returns Date\n\n
    getCreatedAt()\n
    '''
def setCreatedAt():
    '''returns None\n\n
    setCreatedAt(final Date createdAt)\n
    '''
def getStartedAt():
    '''returns Date\n\n
    getStartedAt()\n
    '''
def setStartedAt():
    '''returns None\n\n
    setStartedAt(final Date startedAt)\n
    '''
def getEndedAt():
    '''returns Date\n\n
    getEndedAt()\n
    '''
def setEndedAt():
    '''returns None\n\n
    setEndedAt(final Date endedAt)\n
    '''
def getEndRecordedAt():
    '''returns Date\n\n
    getEndRecordedAt()\n
    '''
def setEndRecordedAt():
    '''returns None\n\n
    setEndRecordedAt(final Date endRecordedAt)\n
    '''
def getUpdatedAt():
    '''returns Date\n\n
    getUpdatedAt()\n
    '''
def setUpdatedAt():
    '''returns None\n\n
    setUpdatedAt(final Date updatedAt)\n
    '''
def getParameters():
    '''returns JobParameters\n\n
    getParameters()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final String name, final String value)\n
    '''
def setParameters():
    '''returns None\n\n
    setParameters(final Map<String, String> parameters)\n
    setParameters(final JobParameters parameters)\n
    '''
def getProcessingOwner():
    '''returns String\n\n
    getProcessingOwner()\n
    '''
def setProcessingOwner():
    '''returns None\n\n
    setProcessingOwner(final String owner)\n
    '''
def getLastProcessingOwner():
    '''returns String\n\n
    getLastProcessingOwner()\n
    '''
def getOwner():
    '''returns String\n\n
    getOwner()\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final String owner)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getAttachments():
    '''returns List<JobAttachment>\n\n
    getAttachments()\n
    '''
def getImplAttachments():
    '''returns List<JobAttachmentImpl>\n\n
    getImplAttachments()\n
    '''
def setAttachments():
    '''returns None\n\n
    setAttachments(final List<JobAttachmentImpl> attachments)\n
    '''
def getAttachment():
    '''returns JobAttachmentImpl\n\n
    getAttachment(final String name)\n
    '''
def getAttachmentsProperties():
    '''returns JobAttachmentsProperties\n\n
    getAttachmentsProperties()\n
    '''
def setAttachmentsProperties():
    '''returns None\n\n
    setAttachmentsProperties(final JobAttachmentsProperties attachmentsProperties)\n
    '''
def getFailureInfo():
    '''returns JobFailureInfoImpl\n\n
    getFailureInfo()\n
    '''
def setFailureInfo():
    '''returns None\n\n
    setFailureInfo(final JobFailureInfoImpl failure)\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def setLanguage():
    '''returns None\n\n
    setLanguage(final String language)\n
    '''
def setSystemDetails():
    '''returns None\n\n
    setSystemDetails(final Map<String, String> details)\n
    '''
def setDetails():
    '''returns None\n\n
    setDetails(final Map<String, String> details)\n
    '''
def getSolveStatus():
    '''returns JobSolveStatus\n\n
    getSolveStatus()\n
    '''
def setSolveStatus():
    '''returns None\n\n
    setSolveStatus(final JobSolveStatus solveStatus)\n
    '''
def getInterruptionStatus():
    '''returns JobInterruptionStatus\n\n
    getInterruptionStatus()\n
    '''
def setInterruptionStatus():
    '''returns None\n\n
    setInterruptionStatus(final JobInterruptionStatus interruptionStatus)\n
    '''
def getInterruptedAt():
    '''returns Date\n\n
    getInterruptedAt()\n
    '''
def setInterruptedAt():
    '''returns None\n\n
    setInterruptedAt(final Date interruptedAt)\n
    '''
def getSubmittedAt():
    '''returns Date\n\n
    getSubmittedAt()\n
    '''
def setSubmittedAt():
    '''returns None\n\n
    setSubmittedAt(final Date submittedAt)\n
    '''
def getSubmittedToProcessorAt():
    '''returns Date\n\n
    getSubmittedToProcessorAt()\n
    '''
def setSubmittedToProcessorAt():
    '''returns None\n\n
    setSubmittedToProcessorAt(final Date submittedToProcessorAt)\n
    '''
def getNbLogItems():
    '''returns Long\n\n
    getNbLogItems()\n
    '''
def setNbLogItems():
    '''returns None\n\n
    setNbLogItems(final Long nbLogItems)\n
    '''
def getSubscription():
    '''returns JobSubscriptionImpl\n\n
    getSubscription()\n
    '''
def setSubscription():
    '''returns None\n\n
    setSubscription(final JobSubscriptionImpl subscription)\n
    '''
def getToken():
    '''returns String\n\n
    getToken()\n
    '''
def setToken():
    '''returns None\n\n
    setToken(final String token)\n
    '''
def getSubscriptionId():
    '''returns String\n\n
    getSubscriptionId()\n
    '''
def getApiClient():
    '''returns JobApiClientImpl\n\n
    getApiClient()\n
    '''
def setApiClient():
    '''returns None\n\n
    setApiClient(final JobApiClientImpl apiClient)\n
    '''
def getSubscriber():
    '''returns JobSubscriberImpl\n\n
    getSubscriber()\n
    '''
def setSubscriber():
    '''returns None\n\n
    setSubscriber(final JobSubscriberImpl subscriber)\n
    '''
def getStorageVersion():
    '''returns int\n\n
    getStorageVersion()\n
    '''
def setStorageVersion():
    '''returns None\n\n
    setStorageVersion(final int storageVersion)\n
    '''
def getEncryptionKeyName():
    '''returns String\n\n
    getEncryptionKeyName()\n
    '''
def setEncryptionKeyName():
    '''returns None\n\n
    setEncryptionKeyName(final String encryptionKeyName)\n
    '''
def getLastDetails():
    '''returns JobDetailsImpl\n\n
    getLastDetails()\n
    '''
def setLastDetails():
    '''returns None\n\n
    setLastDetails(final JobDetailsImpl lastDetails)\n
    '''
def getETag():
    '''returns String\n\n
    getETag()\n
    '''
def isIgnoreJobCount():
    '''returns boolean\n\n
    isIgnoreJobCount()\n
    '''
def setIgnoreJobCount():
    '''returns None\n\n
    setIgnoreJobCount(final boolean ignoreJobCount)\n
    '''
def getEmailForNotification():
    '''returns String\n\n
    getEmailForNotification()\n
    '''
def getCorrelationId():
    '''returns String\n\n
    getCorrelationId()\n
    '''
def setCorrelationId():
    '''returns None\n\n
    setCorrelationId(final String correlationId)\n
    '''
def getLogTail():
    '''returns List<String>\n\n
    getLogTail()\n
    '''
def setLogTail():
    '''returns None\n\n
    setLogTail(final List<String> logTail)\n
    '''
def getJobLog():
    '''returns String\n\n
    getJobLog()\n
    '''
def setJobLog():
    '''returns None\n\n
    setJobLog(final String jobLog)\n
    '''
def getErrorInformation():
    '''returns String\n\n
    getErrorInformation()\n
    '''
def setErrorInformation():
    '''returns None\n\n
    setErrorInformation(final String errorInformation)\n
    '''
def getProjectName():
    '''returns String\n\n
    getProjectName()\n
    '''
def setProjectName():
    '''returns None\n\n
    setProjectName(final String projectName)\n
    '''
def getProjectId():
    '''returns ObjectId\n\n
    getProjectId()\n
    '''
def setProjectId():
    '''returns None\n\n
    setProjectId(final ObjectId projectId)\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def setUserName():
    '''returns None\n\n
    setUserName(final String userName)\n
    '''
def getUserEmail():
    '''returns String\n\n
    getUserEmail()\n
    '''
def setUserEmail():
    '''returns None\n\n
    setUserEmail(final String userEmail)\n
    '''
def getScenarioName():
    '''returns String\n\n
    getScenarioName()\n
    '''
def setScenarioName():
    '''returns None\n\n
    setScenarioName(final String scenarioName)\n
    '''
def getJobSolutionDetails():
    '''returns JobSolutionDetails\n\n
    getJobSolutionDetails()\n
    '''
def setJobSolutionDetails():
    '''returns None\n\n
    setJobSolutionDetails(final JobSolutionDetailsImpl jobSolutionDetails)\n
    '''
