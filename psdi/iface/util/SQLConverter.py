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
def SQLConverter():
    '''public SQLConverter()
    '''
def convert():
    '''public byte[] convert(final Map<String, String[]> queryParams, final UserInfo userInfo)
    '''
def convertData():
    '''public byte[] convertData(final String data)
    public byte[] convertData(final String data, final UserInfo userInfo)
    public byte[] convertData(final String data, final Connection con, final String schemaOwner)
    '''
def convertInteraction():
    '''public String convertInteraction(final String data)
    '''
def convertJSONResource():
    '''public String convertJSONResource(final String data)
    '''
def convertJSONMap():
    '''public String convertJSONMap(final String data)
    '''
def convertArtifacts():
    '''public String convertArtifacts(final String data)
    '''
def convertMEAArtifacts():
    '''public String convertMEAArtifacts(final String data)
    '''
def convertTable():
    '''public String convertTable(final String data)
    '''
def writeDBCObjects():
    '''public int writeDBCObjects(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo)
    '''
def writeDBCUI():
    '''public int writeDBCUI(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo, final boolean addHeader)
    '''
def writeDBCPublishChannel():
    '''public int writeDBCPublishChannel(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, String extSystem)
    '''
def writeDBCEnterpriseService():
    '''public int writeDBCEnterpriseService(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, String extSystem)
    '''
def writeDBCRules():
    '''public int writeDBCRules(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, final String useWith)
    '''
def writeDBCEndPoint():
    '''public int writeDBCEndPoint(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
    '''
def writeDBCInvokeChannel():
    '''public int writeDBCInvokeChannel(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
    '''
def writeDBCExternalSystem():
    '''public int writeDBCExternalSystem(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
    '''
def writeDBCWSRegistry():
    '''public int writeDBCWSRegistry(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
    '''
def writeDBCObjectStructure():
    '''public int writeDBCObjectStructure(final PrintStream out, final SQLConverterUtil util, int numLines, String whereClause, final String grantApp)
    '''
def writeDBCOslcResource():
    '''public int writeDBCOslcResource(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause)
    '''
def writeDBCScript():
    '''public int writeDBCScript(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause)
    '''
def writeDBCJSONResource():
    '''public int writeDBCJSONResource(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause, final String resourceType)
    '''
def writeDBCJSONMap():
    '''public int writeDBCJSONMap(final PrintStream out, final SQLConverterUtil util, int numLines)
    '''
def convertBYOSArtifacts():
    '''public String convertBYOSArtifacts(final String data)
    '''
def convertTenant():
    '''public String convertTenant(final String data)
    '''
def writeDBCInteractionMap():
    '''public int writeDBCInteractionMap(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo)
    '''
def writeDBCInteraction():
    '''public void writeDBCInteraction(PrintStream out, final SQLConverterUtil util, int numLines, final String name)
    '''
def writeDBCWorkCenter():
    '''public String writeDBCWorkCenter(final String data)
    '''
def writeDBCOSWorkCenter():
    '''public void writeDBCOSWorkCenter(final String input)
    '''
def writeDBCOSWorkCenterAuth():
    '''public void writeDBCOSWorkCenterAuth(final String osString, final String workCenter, final String groupName, final String dir, final boolean addWCAuth)
    '''
def writeDBCWorkCenterGroup():
    '''public void writeDBCWorkCenterGroup(final String workCenter, final String groupName, final String description)
    '''
def writeDBCWorkCenterUser():
    '''public void writeDBCWorkCenterUser(final String workCenter, final String groupName, final String userId)
    '''
def writeDBCWorkCenterAuth():
    '''public void writeDBCWorkCenterAuth(final String workCenter, final String groupName, final List<Element> groupData)
    '''
def recordStart():
    '''public void recordStart()
    '''
def recordEnd():
    '''public String recordEnd(final String rest)
    '''
