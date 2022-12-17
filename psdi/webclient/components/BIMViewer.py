VERSION_LESS_THAN_7116 = "int  0"
VERSION_7116_OR_GREATER = "int  1"
VERSION_75_OR_GREATER = "int  2"
PROP_DATA_ATTRIB = "String  \"dataattribute\""
PROP_MODEL_ATTRIB = "String  \"modelattribute\""
PROP_CTRL_TARGET = "String  \"controltarget\""
FIELD_ASSETUID = "String  \"ASSETUID\""
FIELD_ASSETNUM = "String  \"ASSETNUM\""
FIELD_BUILDINGMODELID = "String  \"BUILDINGMODELID\""
FIELD_ORGID = "String  \"ORGID\""
FIELD_SITEID = "String  \"SITEID\""
FIELD_LOCATION = "String  \"LOCATION\""
FIELD_LOCATIONUID = "String  \"LOCATIONSID\""
FIELD_MODELID = "String  \"MODELID\""
FIELD_NETWORK = "String  \"NETWORK\""
FIELD_PARENT = "String  \"PARENT\""
FIELD_PRIMARYSYSTEM = "String  \"PRIMARYSYSTEM\""
FIELD_SYSTEMID = "String  \"SYSTEMID\""
FIELD_WO_NUM = "String  \"WONUM\""
TABLE_ASSET = "String  \"ASSET\""
TABLE_LOCATIONS = "String  \"LOCATIONS\""
TABLE_WORKORDER = "String  \"WORKORDER\""
TABLE_LOCACCESTOR = "String  \"LOCACCESTOR\""
TABLE_LOCHIERARCHY = "String  \"LOCHIERARCHY\""
TABLE_LOCSYSTEM = "String  \"LOCSYSTEM\""
HOST_PARAM_MARKER = "String  \"<HOSTNAME>\""
ATTRIB_RESIZE = "String  \"bim.resize\""
ATTRIB_RESIZE_DLG = "String  \"bim.resize.dlg\""
TYPE_UNKNOWN = "int  0"
TYPE_ASSET = "int  1"
TYPE_LOCATION = "int  2"
TYPE_LOOKUP = "int  3"
TYPE_WORKORDER = "int  4"
TYPE_MODEL = "int  5"
RECORD_UNKNOWN = "int  0"
RECORD_ASSET = "int  1"
RECORD_LOCATION = "int  2"
RECORD_MODEL = "int  3"
def ():
    '''returns BIMViewer\n\n
    ()\n
    '''
def instantiatedatasrc():
    '''returns None\n\n
    instantiatedatasrc()\n
    '''
def handleEvent():
    '''returns int\n\n
    handleEvent(final String methodName, final WebClientEvent event)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def checkVisibility():
    '''returns int\n\n
    checkVisibility()\n
    '''
def eventSelect():
    '''returns int\n\n
    eventSelect()\n
    '''
def eventRezise():
    '''returns None\n\n
    eventRezise()\n
    '''
def eventReziseDlg():
    '''returns None\n\n
    eventReziseDlg()\n
    '''
def jspGetMultiSelection():
    '''returns Set<String>\n\n
    jspGetMultiSelection()\n
    '''
def jspGetCurrentDataMM():
    '''returns String\n\n
    jspGetCurrentDataMM()\n
    '''
def jspGetCurrentDataFrame():
    '''returns String\n\n
    jspGetCurrentDataFrame()\n
    '''
def jspScript():
    '''returns String\n\n
    jspScript(final String id)\n
    '''
def scriptResize():
    '''returns String\n\n
    scriptResize()\n
    '''
def jspGetScriptModelList():
    '''returns String\n\n
    jspGetScriptModelList()\n
    '''
def scriptFooter():
    '''returns String\n\n
    scriptFooter()\n
    '''
def jspGetRezieOption():
    '''returns int\n\n
    jspGetRezieOption()\n
    '''
def jspGetRezieDlgOption():
    '''returns int\n\n
    jspGetRezieDlgOption()\n
    '''
def jspGetStatusUpdate():
    '''returns String\n\n
    jspGetStatusUpdate()\n
    '''
def jspGetViewerTop():
    '''returns int\n\n
    jspGetViewerTop()\n
    '''
def jspHasStatusUpdate():
    '''returns boolean\n\n
    jspHasStatusUpdate()\n
    '''
def getAppType():
    '''returns int\n\n
    getAppType()\n
    '''
def getBackgroundColor():
    '''returns String\n\n
    getBackgroundColor()\n
    '''
def getBoarderColor():
    '''returns String\n\n
    getBoarderColor()\n
    '''
def getForegroundColor():
    '''returns String\n\n
    getForegroundColor()\n
    '''
def getHighlightColor():
    '''returns String\n\n
    getHighlightColor()\n
    '''
def getBinding():
    '''returns String\n\n
    getBinding()\n
    '''
def getCurrentSelection():
    '''returns Set<String>\n\n
    getCurrentSelection()\n
    '''
def getHeight():
    '''returns int\n\n
    getHeight()\n
    '''
def getControlTop():
    '''returns int\n\n
    getControlTop()\n
    '''
def getControlLeft():
    '''returns int\n\n
    getControlLeft()\n
    '''
def getMboKey():
    '''returns String\n\n
    getMboKey()\n
    '''
def getLeftOffset():
    '''returns int\n\n
    getLeftOffset()\n
    '''
def getLookupValue():
    '''returns String\n\n
    getLookupValue()\n
    '''
def getMxVersion():
    '''returns int\n\n
    getMxVersion()\n
    '''
def getRecordType():
    '''returns int\n\n
    getRecordType()\n
    '''
def getSiteId():
    '''returns String\n\n
    getSiteId()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def getViewerType():
    '''returns String\n\n
    getViewerType()\n
    '''
def getWidth():
    '''returns String\n\n
    getWidth()\n
    '''
def isForceUpdate():
    '''returns boolean\n\n
    isForceUpdate()\n
    '''
def isHasMultiSelect():
    '''returns boolean\n\n
    isHasMultiSelect()\n
    '''
def isModelListChanged():
    '''returns boolean\n\n
    isModelListChanged()\n
    '''
def isMultiSelectAllowed():
    '''returns boolean\n\n
    isMultiSelectAllowed()\n
    '''
def isSelectionValid():
    '''returns boolean\n\n
    isSelectionValid()\n
    '''
def forceUpdate():
    '''returns None\n\n
    forceUpdate()\n
    '''
def setModelListChanged():
    '''returns None\n\n
    setModelListChanged(final boolean state)\n
    '''
def isValueChanged():
    '''returns boolean\n\n
    isValueChanged()\n
    '''
def setValueChanged():
    '''returns None\n\n
    setValueChanged(final boolean state)\n
    '''
def isControlVisible():
    '''returns boolean\n\n
    isControlVisible()\n
    '''
def setControlVisible():
    '''returns None\n\n
    setControlVisible(final boolean vis)\n
    '''
def setMultiSelect():
    '''returns None\n\n
    setMultiSelect(final String modelLocation, final Set<String> selection)\n
    '''
def lookupLocation():
    '''returns LocationRemote\n\n
    lookupLocation(final String location)\n
    '''
def lookupLocationFromModelId():
    '''returns LocationRemote\n\n
    lookupLocationFromModelId(final String modelId)\n
    lookupLocationFromModelId(final String modelLocation, final String modelId)\n
    lookupLocationFromModelId(final String modelLocation, final String modelId, final String siteId)\n
    '''
def lookupLocationModelId():
    '''returns String\n\n
    lookupLocationModelId(final String location, final String siteId)\n
    '''
def lookupLocationFromWO():
    '''returns String\n\n
    lookupLocationFromWO(final String woKey, final String siteId)\n
    '''
