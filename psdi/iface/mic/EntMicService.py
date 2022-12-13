def EntMicService():
    '''    public EntMicService()
    public EntMicService(final MXServer mxServer)
    '''
def configure():
    '''    public void configure(final Properties configData)
    '''
def init():
    '''    public void init()
    '''
def query():
    '''    public byte[] query(final byte[] data, final String serviceName, final String extSystem, final UserInfo userInfo)
    public byte[] query(final Document data, final String serviceName, final String extSystem, final UserInfo userInfo)
    public byte[] query(final byte[] queryXml, final String mosName, final UserInfo userInfo)
    public byte[] query(final Document queryXml, final String mosName, final UserInfo userInfo)
    '''
def deleteQueueData():
    '''    public int deleteQueueData(final String queueName, String selector, final int count, UserInfo userInfo)
    '''
def tryObjectStructure():
    '''    public void tryObjectStructure(final String mosName, final String where, final UserInfo userInfo)
    '''
def deleteErrorFileAndTableRow():
    '''    public void deleteErrorFileAndTableRow(final Map<String, String> propMap, final boolean inbound, final String queueName, final UserInfo userInfo)
    '''
def processJMSRecovery():
    '''    public void processJMSRecovery(final String queueName, final UserInfo userInfo)
    '''
def viewQueueData():
    '''    public int viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly)
    public int viewQueueData(final String queueName, String selector, final int count, final UserInfo userInfo, final boolean countOnly, final List<String> viewFilesList)
    public void viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)
    '''
def viewQueueDataApi():
    '''    public void viewQueueDataApi(final String queueName, final String selector, final int count, final UserInfo userInfo)
    '''
def setIfaceTableUserInfo():
    '''    public void setIfaceTableUserInfo(final UserInfo info)
    '''
def getIfaceTableUserInfo():
    '''    public synchronized UserInfo getIfaceTableUserInfo()
    '''
def exportData():
    '''    public void exportData(final String ifaceName, final String sender, final String where, final UserInfo userInfo, final int maxcount)
    public void exportData(final String ifaceName, final String sender, final String where, final String orderBy, final int pageSize, final UserInfo userInfo, int maxcount)
    '''
def loadSystemData():
    '''    public void loadSystemData(final String directory, final String intLevel, final UserInfo userInfo)
    '''
def processExternalData():
    '''    public byte[] processExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)
    public byte[] processExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo userInfo, final MXTransaction trans, final boolean fromQueue)
    '''
def processDataIn():
    '''    public byte[] processDataIn(final StructureData irData, final EnterpriseServiceInfo detailInfo, final String extSystem, final UserInfo info, final MXTransaction mxTrans)
    '''
def internalProcessExternalData():
    '''    public byte[] internalProcessExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)
    '''
def getOSNameForIfaceTable():
    '''    public String getOSNameForIfaceTable(final String entityName)
    '''
def populateQueueList():
    '''    public List<String> populateQueueList(final HashSet<String> validateAgainst, final String nqDescription)
    '''
def getTargetWindow():
    '''    public String[] getTargetWindow(final String launchEntryName, final MboRemote mainMbo)
    '''
def invokeChannel():
    '''    public void invokeChannel(final String channelName, final MboRemote mbo)
    '''
def wsinteraction():
    '''    public void wsinteraction(final String interactionName, final MboRemote mbo)
    '''
def bidiTransformData():
    '''    public byte[] bidiTransformData(final Map<String, ?> metaData, byte[] data)
    '''
def getEndPointName():
    '''    public String getEndPointName(final String extSysName, final String pubChannelName)
    '''
def getQueueToWrite():
    '''    public String getQueueToWrite()
    '''
def writeDataToNotificationQueue():
    '''    public void writeDataToNotificationQueue(final MXTransaction mxtran, final String eventForUser, final Map<String, String> properties, final UserInfo userInfo, final byte[] queueData, final String textData, final boolean syntheticEvent)
    '''
def getNormalizedName():
    '''    public String getNormalizedName(final String queueName)
    '''
def getMosNameForPubChannel():
    '''    public String getMosNameForPubChannel(final String channelName)
    '''
def getBidiData():
    '''    public byte[] getBidiData(final byte[] responseBody, final String bidiFormat)
    '''
def getLaunchURL():
    '''    public String getLaunchURL(final String launchEntryName, final MboRemote mainMbo)
    '''
def checkStatus():
    '''    public boolean checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)
    '''
