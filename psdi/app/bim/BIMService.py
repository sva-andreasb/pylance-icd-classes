SERVICE_NAME = "String  BIM""
PROP_NAME_BIM_MODEL_DIR = "String  bim.model.dir""
PROP_NAME_BIM_WORKING_DIR = "String  bim.import.dir""
PROP_NAME_BIM_DOC_DIR = "String  bim.import.docdir""
PROP_NAME_BIM_MODEL_HOST = "String  bim.model.hostname""
PROP_NAME_ACTIVE_VIEWER = "String  bim.viewer.active""
DOMAIN_COBIESHEETTYPE = "String  COBIESHEETTYPE""
IMPORT_SCR_EXCEL = "String  EXCEL""
IMPORT_SCR_CONTACT = "String  CONTACT""
IMPORT_SCR_FACILITY = "String  FACILITY""
IMPORT_SCR_FLOOR = "String  FLOOR""
IMPORT_SCR_SPACE = "String  SPACE""
IMPORT_SCR_ATTRIBUTE = "String  ATTRIBUTE""
IMPORT_SCR_COMPONENT = "String  COMPONENT""
IMPORT_SCR_TYPE = "String  TYPE""
IMPORT_SCR_SYSTEM = "String  SYSTEM""
IMPORT_SCR_ZONE = "String  ZONE""
VERSION_UNKNOWN = "int  -1"
VERSION_LESS_THAN_7116 = "int  0"
VERSION_7116_OR_GREATER = "int  1"
VERSION_75_OR_GREATER = "int  2"
def BIMService():
'''public BIMService(final MXServer mxServer)
public BIMService()
'''
pass
def init():
'''public void init()
'''
pass
def getLoaderFactory():
'''public Factory getLoaderFactory()
'''
pass
def setFactory():
'''public void setFactory(final Factory factory)
'''
pass
def getMaximoVersion():
'''public int getMaximoVersion()
'''
pass
def getProject():
'''public MboRemote getProject(final UserInfo userInfo, final String attribute, final long key)
'''
pass
def makeDir():
'''public void makeDir(final File newDir)
'''
pass
def copyFile():
'''public void copyFile(final InputStream is, final String targetDir, final String fileName)
'''
pass
def uploadClassification():
'''public void uploadClassification(final OslcRequest request)
'''
pass
def uploadCOBieFile():
'''public void uploadCOBieFile(final OslcRequest request)
'''
pass
def startSession():
'''public MboRemote startSession(final UserInfo userInfo, final String projectId, final String sessionId, final String siteId)
'''
pass
def startBuildingCommisioning():
'''public MboRemote startBuildingCommisioning(final UserInfo userInfo, final String projectId, final String commissioningId)
'''
pass
def startClassificationImport():
'''public MboRemote startClassificationImport(final UserInfo userInfo, final String importId, final String fileType)
'''
pass
def deleteDirecotry():
'''public static void deleteDirecotry(final File file)
'''
pass
def run():
'''public void run()
'''
pass
