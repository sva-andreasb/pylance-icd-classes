def EntMicService():
'''public EntMicService()
public EntMicService(final MXServer mxServer)
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
def query():
'''public byte[] query(final byte[] data, final String serviceName, final String extSystem, final UserInfo userInfo)
public byte[] query(final Document data, final String serviceName, final String extSystem, final UserInfo userInfo)
public byte[] query(final byte[] queryXml, final String mosName, final UserInfo userInfo)
public byte[] query(final Document queryXml, final String mosName, final UserInfo userInfo)
'''
pass
def deleteQueueData():
'''public int deleteQueueData(final String queueName, String selector, final int count, UserInfo userInfo)
'''
pass
def tryObjectStructure():
'''public void tryObjectStructure(final String mosName, final String where, final UserInfo userInfo)
'''
pass
def deleteErrorFileAndTableRow():
'''public void deleteErrorFileAndTableRow(final Map<String, String> propMap, final boolean inbound, final String queueName, final UserInfo userInfo)
'''
pass
def processJMSRecovery():
'''public void processJMSRecovery(final String queueName, final UserInfo userInfo)
'''
pass
def viewQueueData():
'''public int viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly)
public int viewQueueData(final String queueName, String selector, final int count, final UserInfo userInfo, final boolean countOnly, final List<String> viewFilesList)
public void viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)
'''
pass
def viewQueueDataApi():
'''public void viewQueueDataApi(final String queueName, final String selector, final int count, final UserInfo userInfo)
'''
pass
def setIfaceTableUserInfo():
'''public void setIfaceTableUserInfo(final UserInfo info)
'''
pass
def getIfaceTableUserInfo():
'''public synchronized UserInfo getIfaceTableUserInfo()
'''
pass
def exportData():
'''public void exportData(final String ifaceName, final String sender, final String where, final UserInfo userInfo, final int maxcount)
public void exportData(final String ifaceName, final String sender, final String where, final String orderBy, final int pageSize, final UserInfo userInfo, int maxcount)
'''
pass
def loadSystemData():
'''public void loadSystemData(final String directory, final String intLevel, final UserInfo userInfo)
'''
pass
def processExternalData():
'''public byte[] processExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)
public byte[] processExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo userInfo, final MXTransaction trans, final boolean fromQueue)
'''
pass
def processDataIn():
'''public byte[] processDataIn(final StructureData irData, final EnterpriseServiceInfo detailInfo, final String extSystem, final UserInfo info, final MXTransaction mxTrans)
'''
pass
def internalProcessExternalData():
'''public byte[] internalProcessExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)
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
'''public byte[] bidiTransformData(final Map<String, ?> metaData, byte[] data)
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
def getBidiData():
'''public byte[] getBidiData(final byte[] responseBody, final String bidiFormat)
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
