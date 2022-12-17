OS_DIR = "String  \"os\""
WORKCENTER_DIR = "String  \"workcenter\""
MEA_DIR = "String  \"mea\""
TABLE_DIR = "String  \"table\""
PUBLISH_CHANNEL_DIR = "String  \"publish\""
SCRIPT_DIR = "String  \"script\""
INVOKE_CHANNEL_DIR = "String  \"invoke\""
ENTERPRICE_SERVICE_DIR = "String  \"eservice\""
END_POINT_DIR = "String  \"endpoint\""
WS_REGISTRY_DIR = "String  \"ws\""
EXTERNAL_SYSTEM_DIR = "String  \"extsystem\""
OSLC_RESOURCE_DIR = "String  \"oslcresource\""
JSON_RESOURCE_DIR = "String  \"jsonresource\""
JSON_MAP_DIR = "String  \"jsonmap\""
RECORD_DIR = "String  \"record\""
TENANT_DIR = "String  \"tenant\""
def ():
    '''returns SQLConverter\n\n
    ()\n
    '''
def convert():
    '''returns byte[]\n\n
    convert(final Map<String, String[]> queryParams, final UserInfo userInfo)\n
    '''
def convertData():
    '''returns byte[]\n\n
    convertData(final String data)\n
    convertData(final String data, final UserInfo userInfo)\n
    convertData(final String data, final Connection con, final String schemaOwner)\n
    '''
def convertInteraction():
    '''returns String\n\n
    convertInteraction(final String data)\n
    '''
def convertJSONResource():
    '''returns String\n\n
    convertJSONResource(final String data)\n
    '''
def convertJSONMap():
    '''returns String\n\n
    convertJSONMap(final String data)\n
    '''
def convertArtifacts():
    '''returns String\n\n
    convertArtifacts(final String data)\n
    '''
def convertMEAArtifacts():
    '''returns String\n\n
    convertMEAArtifacts(final String data)\n
    '''
def convertTable():
    '''returns String\n\n
    convertTable(final String data)\n
    '''
def writeDBCObjects():
    '''returns int\n\n
    writeDBCObjects(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo)\n
    '''
def writeDBCUI():
    '''returns int\n\n
    writeDBCUI(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo, final boolean addHeader)\n
    '''
def writeDBCPublishChannel():
    '''returns int\n\n
    writeDBCPublishChannel(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, String extSystem)\n
    '''
def writeDBCEnterpriseService():
    '''returns int\n\n
    writeDBCEnterpriseService(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, String extSystem)\n
    '''
def writeDBCRules():
    '''returns int\n\n
    writeDBCRules(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, final String useWith)\n
    '''
def writeDBCEndPoint():
    '''returns int\n\n
    writeDBCEndPoint(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)\n
    '''
def writeDBCInvokeChannel():
    '''returns int\n\n
    writeDBCInvokeChannel(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)\n
    '''
def writeDBCExternalSystem():
    '''returns int\n\n
    writeDBCExternalSystem(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)\n
    '''
def writeDBCWSRegistry():
    '''returns int\n\n
    writeDBCWSRegistry(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)\n
    '''
def writeDBCObjectStructure():
    '''returns int\n\n
    writeDBCObjectStructure(final PrintStream out, final SQLConverterUtil util, int numLines, String whereClause, final String grantApp)\n
    '''
def writeDBCOslcResource():
    '''returns int\n\n
    writeDBCOslcResource(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause)\n
    '''
def writeDBCScript():
    '''returns int\n\n
    writeDBCScript(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause)\n
    '''
def writeDBCJSONResource():
    '''returns int\n\n
    writeDBCJSONResource(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause, final String resourceType)\n
    '''
def writeDBCJSONMap():
    '''returns int\n\n
    writeDBCJSONMap(final PrintStream out, final SQLConverterUtil util, int numLines)\n
    '''
def convertBYOSArtifacts():
    '''returns String\n\n
    convertBYOSArtifacts(final String data)\n
    '''
def convertTenant():
    '''returns String\n\n
    convertTenant(final String data)\n
    '''
def writeDBCInteractionMap():
    '''returns int\n\n
    writeDBCInteractionMap(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo)\n
    '''
def writeDBCInteraction():
    '''returns None\n\n
    writeDBCInteraction(PrintStream out, final SQLConverterUtil util, int numLines, final String name)\n
    '''
def writeDBCWorkCenter():
    '''returns String\n\n
    writeDBCWorkCenter(final String data)\n
    '''
def writeDBCOSWorkCenter():
    '''returns None\n\n
    writeDBCOSWorkCenter(final String input)\n
    '''
def writeDBCOSWorkCenterAuth():
    '''returns None\n\n
    writeDBCOSWorkCenterAuth(final String osString, final String workCenter, final String groupName, final String dir, final boolean addWCAuth)\n
    '''
def writeDBCWorkCenterGroup():
    '''returns None\n\n
    writeDBCWorkCenterGroup(final String workCenter, final String groupName, final String description)\n
    '''
def writeDBCWorkCenterUser():
    '''returns None\n\n
    writeDBCWorkCenterUser(final String workCenter, final String groupName, final String userId)\n
    '''
def writeDBCWorkCenterAuth():
    '''returns None\n\n
    writeDBCWorkCenterAuth(final String workCenter, final String groupName, final List<Element> groupData)\n
    '''
def recordStart():
    '''returns None\n\n
    recordStart()\n
    '''
def recordEnd():
    '''returns String\n\n
    recordEnd(final String rest)\n
    '''
