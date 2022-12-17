SERVICE_NAME = "String  \"BIM\""
PROP_NAME_BIM_MODEL_DIR = "String  \"bim.model.dir\""
PROP_NAME_BIM_WORKING_DIR = "String  \"bim.import.dir\""
PROP_NAME_BIM_DOC_DIR = "String  \"bim.import.docdir\""
PROP_NAME_BIM_MODEL_HOST = "String  \"bim.model.hostname\""
PROP_NAME_ACTIVE_VIEWER = "String  \"bim.viewer.active\""
DOMAIN_COBIESHEETTYPE = "String  \"COBIESHEETTYPE\""
IMPORT_SCR_EXCEL = "String  \"EXCEL\""
IMPORT_SCR_CONTACT = "String  \"CONTACT\""
IMPORT_SCR_FACILITY = "String  \"FACILITY\""
IMPORT_SCR_FLOOR = "String  \"FLOOR\""
IMPORT_SCR_SPACE = "String  \"SPACE\""
IMPORT_SCR_ATTRIBUTE = "String  \"ATTRIBUTE\""
IMPORT_SCR_COMPONENT = "String  \"COMPONENT\""
IMPORT_SCR_TYPE = "String  \"TYPE\""
IMPORT_SCR_SYSTEM = "String  \"SYSTEM\""
IMPORT_SCR_ZONE = "String  \"ZONE\""
VERSION_UNKNOWN = "int  -1"
VERSION_LESS_THAN_7116 = "int  0"
VERSION_7116_OR_GREATER = "int  1"
VERSION_75_OR_GREATER = "int  2"
def ():
    '''returns BIMService\n\n
    (final MXServer mxServer)\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getLoaderFactory():
    '''returns Factory\n\n
    getLoaderFactory()\n
    '''
def setFactory():
    '''returns None\n\n
    setFactory(final Factory factory)\n
    '''
def getMaximoVersion():
    '''returns int\n\n
    getMaximoVersion()\n
    '''
def getProject():
    '''returns MboRemote\n\n
    getProject(final UserInfo userInfo, final String attribute, final long key)\n
    '''
def makeDir():
    '''returns None\n\n
    makeDir(final File newDir)\n
    '''
def copyFile():
    '''returns None\n\n
    copyFile(final InputStream is, final String targetDir, final String fileName)\n
    '''
def uploadClassification():
    '''returns None\n\n
    uploadClassification(final OslcRequest request)\n
    '''
def uploadCOBieFile():
    '''returns None\n\n
    uploadCOBieFile(final OslcRequest request)\n
    '''
def startSession():
    '''returns MboRemote\n\n
    startSession(final UserInfo userInfo, final String projectId, final String sessionId, final String siteId)\n
    '''
def startBuildingCommisioning():
    '''returns MboRemote\n\n
    startBuildingCommisioning(final UserInfo userInfo, final String projectId, final String commissioningId)\n
    '''
def startClassificationImport():
    '''returns MboRemote\n\n
    startClassificationImport(final UserInfo userInfo, final String importId, final String fileType)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
