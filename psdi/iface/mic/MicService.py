def MicService():
'''public MicService()
public MicService(final MXServer mxServer)
'''
pass
def configure():
'''public void configure(final Properties configData)
'''
pass
def init():
'''public void init()
'''
pass
def getPrimaryInfo():
'''public MosDetailInfo getPrimaryInfo(final String mosName)
'''
pass
def getMicSetInfo():
'''public MicSetInfo getMicSetInfo(final String mosName, final String objname)
'''
pass
def routeData():
'''public byte[] routeData(final byte[] data, final String endPointName, final Map<String, ?> metaData)
'''
pass
def callIntegrityChecker():
'''public void callIntegrityChecker(final Map options)
'''
pass
def validateFormula():
'''public void validateFormula(final String objectName, final UserInfo info, final String formula)
'''
pass
def tryObjectStructure():
'''public void tryObjectStructure(final String mosName, final String where, final UserInfo userInfo)
'''
pass
def getNewUserInfo():
'''public synchronized UserInfo getNewUserInfo()
'''
pass
def getMonitorUserInfo():
'''public synchronized UserInfo getMonitorUserInfo()
'''
pass
def getIntegrationDD():
'''public ObjectStructureCache getIntegrationDD()
'''
pass
def processObjectStructureService():
'''public byte[] processObjectStructureService(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans)
public byte[] processObjectStructureService(final Document doc, final String mosName, String messageType, final UserInfo info, final MXTransaction trans)
'''
pass
def processOSLCJSON():
'''public long processOSLCJSON(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo)
'''
pass
def processOSLC():
'''public long processOSLC(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format)
'''
pass
def isValidUseWith():
'''public boolean isValidUseWith(final String useWith)
'''
pass
def processOSLCAsJSON():
'''public long processOSLCAsJSON(JSONArtifact jsonData, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format, final OslcRequest oslcRequest)
public long processOSLCAsJSON(final JSONArtifact jsonData, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format)
'''
pass
def loadData():
'''public byte[] loadData(final byte[] in, final UserInfo info, final MXTransaction trans, final Map defaults)
'''
pass
def internalProcessData():
'''public byte[] internalProcessData(final byte[] in, final UserInfo info, final MXTransaction trans)
'''
pass
def refreshIntegrationDD():
'''public void refreshIntegrationDD()
'''
pass
def getMicServiceInitDone():
'''public static boolean getMicServiceInitDone()
'''
pass
def getMEAProperty():
'''public String getMEAProperty(final String propertyName)
'''
pass
def generateMOSServiceSchema():
'''public void generateMOSServiceSchema(final String mosName, final boolean forceGenerate)
'''
pass
def getObjectStructureInfo():
'''public MosInfo getObjectStructureInfo(final String objectStructureName)
'''
pass
def resetWorkscapelayoutCards():
'''public void resetWorkscapelayoutCards(final UserInfo info)
'''
pass
def viewQueueData():
'''public int viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly, final List<String> viewFilesList)
public int viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly)
public void viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)
'''
pass
def deleteQueueData():
'''public int deleteQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)
'''
pass
def loadSystemData():
'''public void loadSystemData(final String directory, final String intLevel, final UserInfo userInfo)
'''
pass
def processExternalData():
'''public byte[] processExternalData(final byte[] data, final String sender, final String serviceName, final UserInfo info, final MXTransaction trans)
public byte[] processExternalData(final byte[] data, final String sender, final String serviceName, final UserInfo info, final MXTransaction trans, final boolean fromQueue)
'''
pass
def deleteErrorFileAndTableRow():
'''public void deleteErrorFileAndTableRow(final Map<String, String> propMap, final boolean inbound, final String queueName, final UserInfo userInfo)
'''
pass
def internalProcessExternalData():
'''public byte[] internalProcessExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)
'''
pass
def exportData():
'''public void exportData(final String interfaceName, final String sender, final String where, final UserInfo userInfo, final int maxcount)
public void exportData(final String ifaceName, final String sender, final String where, final String orderBy, final int batchSize, final UserInfo userInfo, final int maxcount)
'''
pass
def query():
'''public byte[] query(final byte[] queryXml, final String serviceName, final String extSystem, final UserInfo userInfo)
public byte[] query(final Document data, final String serviceName, final String extSystem, final UserInfo userInfo)
public byte[] query(final byte[] queryXml, final String mosName, final UserInfo userInfo)
public byte[] query(final Document queryXml, final String mosName, final UserInfo userInfo)
'''
pass
def processJMSRecovery():
'''public void processJMSRecovery(final String queueName, final UserInfo userInfo)
'''
pass
def getOSNameForIfaceTable():
'''public String getOSNameForIfaceTable(final String entityName)
'''
pass
def populateQueueList():
'''public List<String> populateQueueList(final HashSet<String> validateAgainst, final String nqDescription)
'''
pass
def getTargetWindow():
'''public String[] getTargetWindow(final String launchEntryName, final MboRemote mainMbo)
'''
pass
def invokeChannel():
'''public void invokeChannel(final String channelName, final MboRemote mbo)
'''
pass
def wsinteraction():
'''public void wsinteraction(final String interactionName, final MboRemote mbo)
'''
pass
def bidiTransformData():
'''public byte[] bidiTransformData(final Map<String, ?> metaData, final byte[] data)
'''
pass
def getBidiData():
'''public byte[] getBidiData(final byte[] responseBody, final String bidiFormat)
'''
pass
def getEndPointName():
'''public String getEndPointName(final String extSysName, final String pubChannelName)
'''
pass
def getQueueToWrite():
'''public String getQueueToWrite()
'''
pass
def writeDataToNotificationQueue():
'''public void writeDataToNotificationQueue(final MXTransaction mxtran, final String eventForUser, final Map<String, String> properties, final UserInfo userInfo, final byte[] queueData, final String textData, final boolean syntheticEvent)
'''
pass
def getNormalizedName():
'''public String getNormalizedName(final String queueName)
'''
pass
def getMosNameForPubChannel():
'''public String getMosNameForPubChannel(final String channelName)
'''
pass
def getLaunchURL():
'''public String getLaunchURL(final String launchEntryName, final MboRemote mainMbo)
'''
pass
def checkStatus():
'''public boolean checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)
'''
pass
def getRowStampMap():
'''public Map<String, Object> getRowStampMap()
'''
pass