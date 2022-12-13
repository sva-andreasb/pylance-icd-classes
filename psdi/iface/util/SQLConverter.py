OS_DIR = "String  os""
WORKCENTER_DIR = "String  workcenter""
MEA_DIR = "String  mea""
TABLE_DIR = "String  table""
PUBLISH_CHANNEL_DIR = "String  publish""
SCRIPT_DIR = "String  script""
INVOKE_CHANNEL_DIR = "String  invoke""
ENTERPRICE_SERVICE_DIR = "String  eservice""
END_POINT_DIR = "String  endpoint""
WS_REGISTRY_DIR = "String  ws""
EXTERNAL_SYSTEM_DIR = "String  extsystem""
OSLC_RESOURCE_DIR = "String  oslcresource""
JSON_RESOURCE_DIR = "String  jsonresource""
JSON_MAP_DIR = "String  jsonmap""
RECORD_DIR = "String  record""
TENANT_DIR = "String  tenant""
def SQLConverter():
'''public SQLConverter()
'''
pass
def convert():
'''public byte[] convert(final Map<String, String[]> queryParams, final UserInfo userInfo)
'''
pass
def convertData():
'''public byte[] convertData(final String data)
public byte[] convertData(final String data, final UserInfo userInfo)
public byte[] convertData(final String data, final Connection con, final String schemaOwner)
'''
pass
def convertInteraction():
'''public String convertInteraction(final String data)
'''
pass
def convertJSONResource():
'''public String convertJSONResource(final String data)
'''
pass
def convertJSONMap():
'''public String convertJSONMap(final String data)
'''
pass
def convertArtifacts():
'''public String convertArtifacts(final String data)
'''
pass
def convertMEAArtifacts():
'''public String convertMEAArtifacts(final String data)
'''
pass
def convertTable():
'''public String convertTable(final String data)
'''
pass
def writeDBCObjects():
'''public int writeDBCObjects(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo)
'''
pass
def writeDBCUI():
'''public int writeDBCUI(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo, final boolean addHeader)
'''
pass
def writeDBCPublishChannel():
'''public int writeDBCPublishChannel(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, String extSystem)
'''
pass
def writeDBCEnterpriseService():
'''public int writeDBCEnterpriseService(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, String extSystem)
'''
pass
def writeDBCRules():
'''public int writeDBCRules(final PrintStream out, final SQLConverterUtil util, int numLines, final String name, final String useWith)
'''
pass
def writeDBCEndPoint():
'''public int writeDBCEndPoint(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
'''
pass
def writeDBCInvokeChannel():
'''public int writeDBCInvokeChannel(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
'''
pass
def writeDBCExternalSystem():
'''public int writeDBCExternalSystem(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
'''
pass
def writeDBCWSRegistry():
'''public int writeDBCWSRegistry(final PrintStream out, final SQLConverterUtil util, int numLines, final String name)
'''
pass
def writeDBCObjectStructure():
'''public int writeDBCObjectStructure(final PrintStream out, final SQLConverterUtil util, int numLines, String whereClause, final String grantApp)
'''
pass
def writeDBCOslcResource():
'''public int writeDBCOslcResource(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause)
'''
pass
def writeDBCScript():
'''public int writeDBCScript(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause)
'''
pass
def writeDBCJSONResource():
'''public int writeDBCJSONResource(final PrintStream out, final SQLConverterUtil util, int numLines, final String whereClause, final String resourceType)
'''
pass
def writeDBCJSONMap():
'''public int writeDBCJSONMap(final PrintStream out, final SQLConverterUtil util, int numLines)
'''
pass
def convertBYOSArtifacts():
'''public String convertBYOSArtifacts(final String data)
'''
pass
def convertTenant():
'''public String convertTenant(final String data)
'''
pass
def writeDBCInteractionMap():
'''public int writeDBCInteractionMap(final PrintStream out, final SQLConverterUtil util, int numLines, final InteractionInfo interactionInfo)
'''
pass
def writeDBCInteraction():
'''public void writeDBCInteraction(PrintStream out, final SQLConverterUtil util, int numLines, final String name)
'''
pass
def writeDBCWorkCenter():
'''public String writeDBCWorkCenter(final String data)
'''
pass
def writeDBCOSWorkCenter():
'''public void writeDBCOSWorkCenter(final String input)
'''
pass
def writeDBCOSWorkCenterAuth():
'''public void writeDBCOSWorkCenterAuth(final String osString, final String workCenter, final String groupName, final String dir, final boolean addWCAuth)
'''
pass
def writeDBCWorkCenterGroup():
'''public void writeDBCWorkCenterGroup(final String workCenter, final String groupName, final String description)
'''
pass
def writeDBCWorkCenterUser():
'''public void writeDBCWorkCenterUser(final String workCenter, final String groupName, final String userId)
'''
pass
def writeDBCWorkCenterAuth():
'''public void writeDBCWorkCenterAuth(final String workCenter, final String groupName, final List<Element> groupData)
'''
pass
def recordStart():
'''public void recordStart()
'''
pass
def recordEnd():
'''public String recordEnd(final String rest)
'''
pass
