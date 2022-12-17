def ():
    '''returns MicService\n\n
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
def getPrimaryInfo():
    '''returns MosDetailInfo\n\n
    getPrimaryInfo(final String mosName)\n
    '''
def getMicSetInfo():
    '''returns MicSetInfo\n\n
    getMicSetInfo(final String mosName, final String objname)\n
    '''
def routeData():
    '''returns byte[]\n\n
    routeData(final byte[] data, final String endPointName, final Map<String, ?> metaData)\n
    '''
def callIntegrityChecker():
    '''returns None\n\n
    callIntegrityChecker(final Map options)\n
    '''
def validateFormula():
    '''returns None\n\n
    validateFormula(final String objectName, final UserInfo info, final String formula)\n
    '''
def tryObjectStructure():
    '''returns None\n\n
    tryObjectStructure(final String mosName, final String where, final UserInfo userInfo)\n
    '''
def getIntegrationDD():
    '''returns ObjectStructureCache\n\n
    getIntegrationDD()\n
    '''
def processObjectStructureService():
    '''returns byte[]\n\n
    processObjectStructureService(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans)\n
    processObjectStructureService(final Document doc, final String mosName, String messageType, final UserInfo info, final MXTransaction trans)\n
    '''
def processOSLCJSON():
    '''returns long\n\n
    processOSLCJSON(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo)\n
    '''
def processOSLC():
    '''returns long\n\n
    processOSLC(final byte[] in, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format)\n
    '''
def isValidUseWith():
    '''returns boolean\n\n
    isValidUseWith(final String useWith)\n
    '''
def processOSLCAsJSON():
    '''returns long\n\n
    processOSLCAsJSON(JSONArtifact jsonData, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format, final OslcRequest oslcRequest)\n
    processOSLCAsJSON(final JSONArtifact jsonData, final String mosName, final String messageType, final UserInfo info, final MXTransaction trans, final MboRemote mbo, final String format)\n
    '''
def loadData():
    '''returns byte[]\n\n
    loadData(final byte[] in, final UserInfo info, final MXTransaction trans, final Map defaults)\n
    '''
def internalProcessData():
    '''returns byte[]\n\n
    internalProcessData(final byte[] in, final UserInfo info, final MXTransaction trans)\n
    '''
def refreshIntegrationDD():
    '''returns None\n\n
    refreshIntegrationDD()\n
    '''
def getMEAProperty():
    '''returns String\n\n
    getMEAProperty(final String propertyName)\n
    '''
def generateMOSServiceSchema():
    '''returns None\n\n
    generateMOSServiceSchema(final String mosName, final boolean forceGenerate)\n
    '''
def getObjectStructureInfo():
    '''returns MosInfo\n\n
    getObjectStructureInfo(final String objectStructureName)\n
    '''
def resetWorkscapelayoutCards():
    '''returns None\n\n
    resetWorkscapelayoutCards(final UserInfo info)\n
    '''
def viewQueueData():
    '''returns None\n\n
    viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly, final List<String> viewFilesList)\n
    viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo, final boolean countOnly)\n
    viewQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)\n
    '''
def deleteQueueData():
    '''returns int\n\n
    deleteQueueData(final String queueName, final String selector, final int count, final UserInfo userInfo)\n
    '''
def loadSystemData():
    '''returns None\n\n
    loadSystemData(final String directory, final String intLevel, final UserInfo userInfo)\n
    '''
def processExternalData():
    '''returns byte[]\n\n
    processExternalData(final byte[] data, final String sender, final String serviceName, final UserInfo info, final MXTransaction trans)\n
    processExternalData(final byte[] data, final String sender, final String serviceName, final UserInfo info, final MXTransaction trans, final boolean fromQueue)\n
    '''
def deleteErrorFileAndTableRow():
    '''returns None\n\n
    deleteErrorFileAndTableRow(final Map<String, String> propMap, final boolean inbound, final String queueName, final UserInfo userInfo)\n
    '''
def internalProcessExternalData():
    '''returns byte[]\n\n
    internalProcessExternalData(final byte[] data, final String sender, final String ifaceName, final UserInfo info, final MXTransaction trans)\n
    '''
def exportData():
    '''returns None\n\n
    exportData(final String interfaceName, final String sender, final String where, final UserInfo userInfo, final int maxcount)\n
    exportData(final String ifaceName, final String sender, final String where, final String orderBy, final int batchSize, final UserInfo userInfo, final int maxcount)\n
    '''
def query():
    '''returns byte[]\n\n
    query(final byte[] queryXml, final String serviceName, final String extSystem, final UserInfo userInfo)\n
    query(final Document data, final String serviceName, final String extSystem, final UserInfo userInfo)\n
    query(final byte[] queryXml, final String mosName, final UserInfo userInfo)\n
    query(final Document queryXml, final String mosName, final UserInfo userInfo)\n
    '''
def processJMSRecovery():
    '''returns None\n\n
    processJMSRecovery(final String queueName, final UserInfo userInfo)\n
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
    bidiTransformData(final Map<String, ?> metaData, final byte[] data)\n
    '''
def getBidiData():
    '''returns byte[]\n\n
    getBidiData(final byte[] responseBody, final String bidiFormat)\n
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
def getLaunchURL():
    '''returns String\n\n
    getLaunchURL(final String launchEntryName, final MboRemote mainMbo)\n
    '''
def checkStatus():
    '''returns boolean\n\n
    checkStatus(final StructureData irData, final String extSystem, final String sendListName, final String orgId, final String siteId, final boolean sendUpdates)\n
    '''
