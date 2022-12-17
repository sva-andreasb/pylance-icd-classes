def ():
    '''returns EntMicService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def configure():
    '''returns None\n\n
    configure(final Properties configData)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def query():
    '''returns byte[]\n\n
    query(final byte[] data, final String serviceName, final String extSystem, final UserInfo userInfo)\n
    query(final Document data, final String serviceName, final String extSystem, final UserInfo userInfo)\n
    query(final byte[] queryXml, final String mosName, final UserInfo userInfo)\n
    query(final Document queryXml, final String mosName, final UserInfo userInfo)\n
    '''
def deleteQueueData():
    '''returns int\n\n
    deleteQueueData(final String queueName, String selector, final int count, UserInfo userInfo)\n
    '''
def tryObjectStructure():
    '''returns None\n\n
    tryObjectStructure(final String mosName, final String where, final UserInfo userInfo)\n
    '''
def deleteErrorFileAndTableRow():
    '''returns None\n\n
    deleteErrorFileAndTableRow(final Map<String, String> propMap, final boolean inbound, final String queueName, final UserInfo userInfo)\n
    '''
def processJMSRecovery():
    '''returns None\n\n
    processJMSRecovery(final String queueName, final UserInfo userInfo)\n
    '''
def viewQueueData():
    '''returns None\n\n
    viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly)\n
    viewQueueData(final String queueName, String selector, final int count, final UserInfo userInfo, final boolean countOnly, final List<String> viewFilesList)\n
    viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)\n
    '''
def viewQueueDataApi():
    '''returns None\n\n
    viewQueueDataApi(final String queueName, final String selector, final int count, final UserInfo userInfo)\n
    '''
def setIfaceTableUserInfo():
    '''returns None\n\n
    setIfaceTableUserInfo(final UserInfo info)\n
    '''
def exportData():
    '''returns None\n\n
    exportData(final String ifaceName, final String sender, final String where, final UserInfo userInfo, final int maxcount)\n
    exportData(final String ifaceName, final String sender, final String where, final String orderBy, final int pageSize, final UserInfo userInfo, int maxcount)\n
    '''
def loadSystemData():
    '''returns None\n\n
    loadSystemData(final String directory, final String intLevel, final UserInfo userInfo)\n
    '''
def processExternalData():
    '''returns byte[]\n\n
    processExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)\n
    processExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo userInfo, final MXTransaction trans, final boolean fromQueue)\n
    '''
def processDataIn():
    '''returns byte[]\n\n
    processDataIn(final StructureData irData, final EnterpriseServiceInfo detailInfo, final String extSystem, final UserInfo info, final MXTransaction mxTrans)\n
    '''
def internalProcessExternalData():
    '''returns byte[]\n\n
    internalProcessExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)\n
    '''
def getOSNameForIfaceTable():
    '''returns String\n\n
    getOSNameForIfaceTable(final String entityName)\n
    '''
def populateQueueList():
    '''returns List<String>\n\n
    populateQueueList(final HashSet<String> validateAgainst, final String nqDescription)\n
    '''
def getTargetWindow():
    '''returns String[]\n\n
    getTargetWindow(final String launchEntryName, final MboRemote mainMbo)\n
    '''
def invokeChannel():
    '''returns None\n\n
    invokeChannel(final String channelName, final MboRemote mbo)\n
    '''
def wsinteraction():
    '''returns None\n\n
    wsinteraction(final String interactionName, final MboRemote mbo)\n
    '''
def bidiTransformData():
    '''returns byte[]\n\n
    bidiTransformData(final Map<String, ?> metaData, byte[] data)\n
    '''
def getEndPointName():
    '''returns String\n\n
    getEndPointName(final String extSysName, final String pubChannelName)\n
    '''
def getQueueToWrite():
    '''returns String\n\n
    getQueueToWrite()\n
    '''
def writeDataToNotificationQueue():
    '''returns None\n\n
    writeDataToNotificationQueue(final MXTransaction mxtran, final String eventForUser, final Map<String, String> properties, final UserInfo userInfo, final byte[] queueData, final String textData, final boolean syntheticEvent)\n
    '''
def getNormalizedName():
    '''returns String\n\n
    getNormalizedName(final String queueName)\n
    '''
def getMosNameForPubChannel():
    '''returns String\n\n
    getMosNameForPubChannel(final String channelName)\n
    '''
def getBidiData():
    '''returns byte[]\n\n
    getBidiData(final byte[] responseBody, final String bidiFormat)\n
    '''
def getLaunchURL():
    '''returns String\n\n
    getLaunchURL(final String launchEntryName, final MboRemote mainMbo)\n
    '''
def checkStatus():
    '''returns boolean\n\n
    checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)\n
    '''
