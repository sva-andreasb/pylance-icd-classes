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
def BIMViewer():
    '''public BIMViewer()
    '''
def instantiatedatasrc():
    '''public void instantiatedatasrc()
    '''
def handleEvent():
    '''public int handleEvent(final String methodName, final WebClientEvent event)
    '''
def initialize():
    '''public void initialize()
    '''
def render():
    '''public int render()
    '''
def checkVisibility():
    '''public int checkVisibility()
    '''
def eventSelect():
    '''public int eventSelect()
    '''
def eventRezise():
    '''public void eventRezise()
    '''
def eventReziseDlg():
    '''public void eventReziseDlg()
    '''
def jspGetMultiSelection():
    '''public Set<String> jspGetMultiSelection()
    '''
def jspGetCurrentDataMM():
    '''public String jspGetCurrentDataMM()
    '''
def jspGetCurrentDataFrame():
    '''public String jspGetCurrentDataFrame()
    '''
def jspScript():
    '''public String jspScript(final String id)
    '''
def scriptResize():
    '''public String scriptResize()
    '''
def jspGetScriptModelList():
    '''public String jspGetScriptModelList()
    '''
def scriptFooter():
    '''public String scriptFooter()
    '''
def jspGetRezieOption():
    '''public int jspGetRezieOption()
    '''
def jspGetRezieDlgOption():
    '''public int jspGetRezieDlgOption()
    '''
def jspGetStatusUpdate():
    '''public String jspGetStatusUpdate()
    '''
def jspGetViewerTop():
    '''public int jspGetViewerTop()
    '''
def jspHasStatusUpdate():
    '''public boolean jspHasStatusUpdate()
    '''
def getAppType():
    '''public int getAppType()
    '''
def getBackgroundColor():
    '''public String getBackgroundColor()
    '''
def getBoarderColor():
    '''public String getBoarderColor()
    '''
def getForegroundColor():
    '''public String getForegroundColor()
    '''
def getHighlightColor():
    '''public String getHighlightColor()
    '''
def getBinding():
    '''public String getBinding()
    '''
def getCurrentSelection():
    '''public Set<String> getCurrentSelection()
    '''
def getHeight():
    '''public int getHeight()
    '''
def getControlTop():
    '''public int getControlTop()
    '''
def getControlLeft():
    '''public int getControlLeft()
    '''
def getMboKey():
    '''public String getMboKey()
    '''
def getLeftOffset():
    '''public int getLeftOffset()
    '''
def getLookupValue():
    '''public String getLookupValue()
    '''
def getMxVersion():
    '''public int getMxVersion()
    '''
def getRecordType():
    '''public int getRecordType()
    '''
def getSiteId():
    '''public String getSiteId()
    '''
def getValue():
    '''public String getValue()
    '''
def getViewerType():
    '''public String getViewerType()
    '''
def getWidth():
    '''public String getWidth()
    '''
def isForceUpdate():
    '''public boolean isForceUpdate()
    '''
def isHasMultiSelect():
    '''public boolean isHasMultiSelect()
    '''
def isModelListChanged():
    '''public boolean isModelListChanged()
    '''
def isMultiSelectAllowed():
    '''public boolean isMultiSelectAllowed()
    '''
def isSelectionValid():
    '''public boolean isSelectionValid()
    '''
def forceUpdate():
    '''public void forceUpdate()
    '''
def setModelListChanged():
    '''public void setModelListChanged(final boolean state)
    '''
def isValueChanged():
    '''public boolean isValueChanged()
    '''
def setValueChanged():
    '''public void setValueChanged(final boolean state)
    '''
def isControlVisible():
    '''public boolean isControlVisible()
    '''
def setControlVisible():
    '''public void setControlVisible(final boolean vis)
    '''
def setMultiSelect():
    '''public void setMultiSelect(final String modelLocation, final Set<String> selection)
    '''
def lookupLocation():
    '''public LocationRemote lookupLocation(final String location)
    public static LocationRemote lookupLocation(final MboRemote mbo, final String location, final String siteId)
    '''
def lookupLocationFromModelId():
    '''public LocationRemote lookupLocationFromModelId(final String modelId)
    public LocationRemote lookupLocationFromModelId(final String modelLocation, final String modelId)
    public LocationRemote lookupLocationFromModelId(final String modelLocation, final String modelId, final String siteId)
    '''
def lookupLocationModelId():
    '''public String lookupLocationModelId(final String location, final String siteId)
    '''
def lookupLocationFromWO():
    '''public String lookupLocationFromWO(final String woKey, final String siteId)
    '''
def findByRenderId():
    '''public static BaseInstance findByRenderId(final BaseInstance root, final String renderId)
    '''
def lookupLocations():
    '''public static LocationSetRemote lookupLocations(final MboRemote mbo, final String location, final String siteId)
    '''
def lookupAssetsAtLocation():
    '''public static MboSetRemote lookupAssetsAtLocation(final MboRemote locationMbo)
    '''
