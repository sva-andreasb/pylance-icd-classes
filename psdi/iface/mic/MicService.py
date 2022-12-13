def MicService():
    '''public MicService()
    public MicService(final MXServer mxServer)
    '''
def configure():
    '''public void configure(final Properties configData)
    '''
def init():
    '''public void init()
    '''
def getPrimaryInfo():
    '''public MosDetailInfo getPrimaryInfo(final String mosName)
    '''
def getMicSetInfo():
    '''public MicSetInfo getMicSetInfo(final String mosName, final String objname)
    '''
def routeData():
    '''public byte[] routeData(final byte[] data, final String endPointName, final Map<String, ?> metaData)
    '''
def callIntegrityChecker():
    '''public void callIntegrityChecker(final Map options)
    '''
def validateFormula():
    '''public void validateFormula(final String objectName, final UserInfo info, final String formula)
    '''
def tryObjectStructure():
    '''public void tryObjectStructure(final String mosName, final String where, final UserInfo userInfo)
    '''
def getNewUserInfo():
    '''public synchronized UserInfo getNewUserInfo()
    '''
def getMonitorUserInfo():
    '''public synchronized UserInfo getMonitorUserInfo()
    '''
def getIntegrationDD():
    '''public ObjectStructureCache getIntegrationDD()
    '''
def processObjectStructureService():
    '''public byte[] processObjectStructureService(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans)
    public byte[] processObjectStructureService(final Document doc, final String mosName, String messageType, final UserInfo info, final MXTransaction trans)
    '''
def processOSLCJSON():
    '''public long processOSLCJSON(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo)
    '''
def processOSLC():
    '''public long processOSLC(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format)
    '''
def isValidUseWith():
    '''public boolean isValidUseWith(final String useWith)
    '''
def processOSLCAsJSON():
    '''public long processOSLCAsJSON(JSONArtifact jsonData, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format, final OslcRequest oslcRequest)
    public long processOSLCAsJSON(final JSONArtifact jsonData, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format)
    '''
def loadData():
    '''public byte[] loadData(final byte[] in, final UserInfo info, final MXTransaction trans, final Map defaults)
    '''
def internalProcessData():
    '''public byte[] internalProcessData(final byte[] in, final UserInfo info, final MXTransaction trans)
    '''
def refreshIntegrationDD():
    '''public void refreshIntegrationDD()
    '''
def getMicServiceInitDone():
    '''public static boolean getMicServiceInitDone()
    '''
def getMEAProperty():
    '''public String getMEAProperty(final String propertyName)
    '''
def generateMOSServiceSchema():
    '''public void generateMOSServiceSchema(final String mosName, final boolean forceGenerate)
    '''
def getObjectStructureInfo():
    '''public MosInfo getObjectStructureInfo(final String objectStructureName)
    '''
def resetWorkscapelayoutCards():
    '''public void resetWorkscapelayoutCards(final UserInfo info)
    '''
def viewQueueData():
    '''public int viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly, final List<String> viewFilesList)
    public int viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly)
    public void viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)
    '''
def deleteQueueData():
    '''public int deleteQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)
    '''
def loadSystemData():
    '''public void loadSystemData(final String directory, final String intLevel, final UserInfo userInfo)
    '''
def processExternalData():
    '''public byte[] processExternalData(final byte[] data, final String sender, final String serviceName, final UserInfo info, final MXTransaction trans)
    public byte[] processExternalData(final byte[] data, final String sender, final String serviceName, final UserInfo info, final MXTransaction trans, final boolean fromQueue)
    '''
def deleteErrorFileAndTableRow():
    '''public void deleteErrorFileAndTableRow(final Map<String, String> propMap, final boolean inbound, final String queueName, final UserInfo userInfo)
    '''
def internalProcessExternalData():
    '''public byte[] internalProcessExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)
    '''
def exportData():
    '''public void exportData(final String interfaceName, final String sender, final String where, final UserInfo userInfo, final int maxcount)
    public void exportData(final String ifaceName, final String sender, final String where, final String orderBy, final int batchSize, final UserInfo userInfo, final int maxcount)
    '''
def query():
    '''public byte[] query(final byte[] queryXml, final String serviceName, final String extSystem, final UserInfo userInfo)
    public byte[] query(final Document data, final String serviceName, final String extSystem, final UserInfo userInfo)
    public byte[] query(final byte[] queryXml, final String mosName, final UserInfo userInfo)
    public byte[] query(final Document queryXml, final String mosName, final UserInfo userInfo)
    '''
def processJMSRecovery():
    '''public void processJMSRecovery(final String queueName, final UserInfo userInfo)
    '''
def getOSNameForIfaceTable():
    '''public String getOSNameForIfaceTable(final String entityName)
    '''
def populateQueueList():
    '''public List<String> populateQueueList(final HashSet<String> validateAgainst, final String nqDescription)
    '''
def getTargetWindow():
    '''public String[] getTargetWindow(final String launchEntryName, final MboRemote mainMbo)
    '''
def invokeChannel():
    '''public void invokeChannel(final String channelName, final MboRemote mbo)
    '''
def wsinteraction():
    '''public void wsinteraction(final String interactionName, final MboRemote mbo)
    '''
def bidiTransformData():
    '''public byte[] bidiTransformData(final Map<String, ?> metaData, final byte[] data)
    '''
def getBidiData():
    '''public byte[] getBidiData(final byte[] responseBody, final String bidiFormat)
    '''
def getEndPointName():
    '''public String getEndPointName(final String extSysName, final String pubChannelName)
    '''
def getQueueToWrite():
    '''public String getQueueToWrite()
    '''
def writeDataToNotificationQueue():
    '''public void writeDataToNotificationQueue(final MXTransaction mxtran, final String eventForUser, final Map<String, String> properties, final UserInfo userInfo, final byte[] queueData, final String textData, final boolean syntheticEvent)
    '''
def getNormalizedName():
    '''public String getNormalizedName(final String queueName)
    '''
def getMosNameForPubChannel():
    '''public String getMosNameForPubChannel(final String channelName)
    '''
def getLaunchURL():
    '''public String getLaunchURL(final String launchEntryName, final MboRemote mainMbo)
    '''
def checkStatus():
    '''public boolean checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)
    '''
def getRowStampMap():
    '''public Map<String, Object> getRowStampMap()
    '''
