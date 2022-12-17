def ():
    '''returns IntGenerator\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def parseWSDL():
    '''returns None\n\n
    parseWSDL()\n
    '''
def setPortAndOperation():
    '''returns boolean\n\n
    setPortAndOperation()\n
    '''
def viewSchema():
    '''returns None\n\n
    viewSchema()\n
    '''
def viewOptimizedSchemaRequest():
    '''returns None\n\n
    viewOptimizedSchemaRequest(final boolean fill)\n
    '''
def viewOptimizedSchemaResponse():
    '''returns None\n\n
    viewOptimizedSchemaResponse(final boolean fill)\n
    '''
def setRequestArtifacts():
    '''returns None\n\n
    setRequestArtifacts()\n
    '''
def setResponseArtifacts():
    '''returns None\n\n
    setResponseArtifacts()\n
    '''
def fillObjStrUi():
    '''returns None\n\n
    fillObjStrUi(final boolean isReq)\n
    '''
def processnode():
    '''returns None\n\n
    processnode(final WSIOTreeSetRemote treeSet, final LinkedHashMap<String, String> removeMap, final boolean isRequest)\n
    '''
def select():
    '''returns None\n\n
    select()\n
    '''
def unselect():
    '''returns None\n\n
    unselect()\n
    '''
def validateMappings():
    '''returns String\n\n
    validateMappings(final boolean isResponse)\n
    '''
def createIntegrationArtifacts():
    '''returns String\n\n
    createIntegrationArtifacts(final String label, final byte[] presentataion)\n
    '''
def getOBPInfo():
    '''returns OBPInfo\n\n
    getOBPInfo()\n
    '''
def getOBPGenerator():
    '''returns OBPGenerator\n\n
    getOBPGenerator()\n
    '''
def getParentTbName():
    '''returns String\n\n
    getParentTbName(final String hierPath)\n
    '''
def checkMappingObject():
    '''returns None\n\n
    checkMappingObject(final String colsRelation)\n
    '''
def setWSIO():
    '''returns None\n\n
    setWSIO(final WSIO in)\n
    '''
def setWSIOAttribute():
    '''returns None\n\n
    setWSIOAttribute(final WSIOAttribute inAttr)\n
    '''
def getWSIO():
    '''returns WSIO\n\n
    getWSIO()\n
    '''
def getWSIOAttribute():
    '''returns WSIOAttribute\n\n
    getWSIOAttribute()\n
    '''
def fillAttributes():
    '''returns MboSetRemote\n\n
    fillAttributes(final MboRemote parent, final MboRemote thisMbo, final boolean removeExisting)\n
    '''
def logStep():
    '''returns None\n\n
    logStep(final int step, final String label)\n
    '''
def logWSIOStep():
    '''returns None\n\n
    logWSIOStep(final boolean isReq, final String label)\n
    '''
def logMappingStep():
    '''returns None\n\n
    logMappingStep(final boolean isReq, final String label, final String wsioObjectName, final String objectName, final String objectRelationName, final String attributeName, final String locationPath, final String value)\n
    '''
def logCancel():
    '''returns None\n\n
    logCancel()\n
    '''
def logUISelectionStep():
    '''returns None\n\n
    logUISelectionStep(final boolean isReq, final String label)\n
    '''
