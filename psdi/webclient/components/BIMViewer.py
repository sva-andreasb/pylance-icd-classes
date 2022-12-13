VERSION_LESS_THAN_7116 = "int  0"
VERSION_7116_OR_GREATER = "int  1"
VERSION_75_OR_GREATER = "int  2"
PROP_DATA_ATTRIB = "String  dataattribute""
PROP_MODEL_ATTRIB = "String  modelattribute""
PROP_CTRL_TARGET = "String  controltarget""
FIELD_ASSETUID = "String  ASSETUID""
FIELD_ASSETNUM = "String  ASSETNUM""
FIELD_BUILDINGMODELID = "String  BUILDINGMODELID""
FIELD_ORGID = "String  ORGID""
FIELD_SITEID = "String  SITEID""
FIELD_LOCATION = "String  LOCATION""
FIELD_LOCATIONUID = "String  LOCATIONSID""
FIELD_MODELID = "String  MODELID""
FIELD_NETWORK = "String  NETWORK""
FIELD_PARENT = "String  PARENT""
FIELD_PRIMARYSYSTEM = "String  PRIMARYSYSTEM""
FIELD_SYSTEMID = "String  SYSTEMID""
FIELD_WO_NUM = "String  WONUM""
TABLE_ASSET = "String  ASSET""
TABLE_LOCATIONS = "String  LOCATIONS""
TABLE_WORKORDER = "String  WORKORDER""
TABLE_LOCACCESTOR = "String  LOCACCESTOR""
TABLE_LOCHIERARCHY = "String  LOCHIERARCHY""
TABLE_LOCSYSTEM = "String  LOCSYSTEM""
HOST_PARAM_MARKER = "String  <HOSTNAME>""
ATTRIB_RESIZE = "String  bim.resize""
ATTRIB_RESIZE_DLG = "String  bim.resize.dlg""
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
pass
def instantiatedatasrc():
'''public void instantiatedatasrc()
'''
pass
def handleEvent():
'''public int handleEvent(final String methodName, final WebClientEvent event)
'''
pass
def initialize():
'''public void initialize()
'''
pass
def render():
'''public int render()
'''
pass
def checkVisibility():
'''public int checkVisibility()
'''
pass
def eventSelect():
'''public int eventSelect()
'''
pass
def eventRezise():
'''public void eventRezise()
'''
pass
def eventReziseDlg():
'''public void eventReziseDlg()
'''
pass
def jspGetMultiSelection():
'''public Set<String> jspGetMultiSelection()
'''
pass
def jspGetCurrentDataMM():
'''public String jspGetCurrentDataMM()
'''
pass
def jspGetCurrentDataFrame():
'''public String jspGetCurrentDataFrame()
'''
pass
def jspScript():
'''public String jspScript(final String id)
'''
pass
def scriptResize():
'''public String scriptResize()
'''
pass
def jspGetScriptModelList():
'''public String jspGetScriptModelList()
'''
pass
def scriptFooter():
'''public String scriptFooter()
'''
pass
def jspGetRezieOption():
'''public int jspGetRezieOption()
'''
pass
def jspGetRezieDlgOption():
'''public int jspGetRezieDlgOption()
'''
pass
def jspGetStatusUpdate():
'''public String jspGetStatusUpdate()
'''
pass
def jspGetViewerTop():
'''public int jspGetViewerTop()
'''
pass
def jspHasStatusUpdate():
'''public boolean jspHasStatusUpdate()
'''
pass
def getAppType():
'''public int getAppType()
'''
pass
def getBackgroundColor():
'''public String getBackgroundColor()
'''
pass
def getBoarderColor():
'''public String getBoarderColor()
'''
pass
def getForegroundColor():
'''public String getForegroundColor()
'''
pass
def getHighlightColor():
'''public String getHighlightColor()
'''
pass
def getBinding():
'''public String getBinding()
'''
pass
def getCurrentSelection():
'''public Set<String> getCurrentSelection()
'''
pass
def getHeight():
'''public int getHeight()
'''
pass
def getControlTop():
'''public int getControlTop()
'''
pass
def getControlLeft():
'''public int getControlLeft()
'''
pass
def getMboKey():
'''public String getMboKey()
'''
pass
def getLeftOffset():
'''public int getLeftOffset()
'''
pass
def getLookupValue():
'''public String getLookupValue()
'''
pass
def getMxVersion():
'''public int getMxVersion()
'''
pass
def getRecordType():
'''public int getRecordType()
'''
pass
def getSiteId():
'''public String getSiteId()
'''
pass
def getValue():
'''public String getValue()
'''
pass
def getViewerType():
'''public String getViewerType()
'''
pass
def getWidth():
'''public String getWidth()
'''
pass
def isForceUpdate():
'''public boolean isForceUpdate()
'''
pass
def isHasMultiSelect():
'''public boolean isHasMultiSelect()
'''
pass
def isModelListChanged():
'''public boolean isModelListChanged()
'''
pass
def isMultiSelectAllowed():
'''public boolean isMultiSelectAllowed()
'''
pass
def isSelectionValid():
'''public boolean isSelectionValid()
'''
pass
def forceUpdate():
'''public void forceUpdate()
'''
pass
def setModelListChanged():
'''public void setModelListChanged(final boolean state)
'''
pass
def isValueChanged():
'''public boolean isValueChanged()
'''
pass
def setValueChanged():
'''public void setValueChanged(final boolean state)
'''
pass
def isControlVisible():
'''public boolean isControlVisible()
'''
pass
def setControlVisible():
'''public void setControlVisible(final boolean vis)
'''
pass
def setMultiSelect():
'''public void setMultiSelect(final String modelLocation, final Set<String> selection)
'''
pass
def lookupLocation():
'''public LocationRemote lookupLocation(final String location)
public static LocationRemote lookupLocation(final MboRemote mbo, final String location, final String siteId)
'''
pass
def lookupLocationFromModelId():
'''public LocationRemote lookupLocationFromModelId(final String modelId)
public LocationRemote lookupLocationFromModelId(final String modelLocation, final String modelId)
public LocationRemote lookupLocationFromModelId(final String modelLocation, final String modelId, final String siteId)
'''
pass
def lookupLocationModelId():
'''public String lookupLocationModelId(final String location, final String siteId)
'''
pass
def lookupLocationFromWO():
'''public String lookupLocationFromWO(final String woKey, final String siteId)
'''
pass
def findByRenderId():
'''public static BaseInstance findByRenderId(final BaseInstance root, final String renderId)
'''
pass
def lookupLocations():
'''public static LocationSetRemote lookupLocations(final MboRemote mbo, final String location, final String siteId)
'''
pass
def lookupAssetsAtLocation():
'''public static MboSetRemote lookupAssetsAtLocation(final MboRemote locationMbo)
'''
pass
