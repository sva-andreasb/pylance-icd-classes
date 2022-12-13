EXCEPTION_NONE = "int  -1"
EXCEPTION_WARNING = "int  0"
EXCEPTION_REQUIREDFIELD = "int  1"
EXCEPTION_YESNOCANCEL = "int  2"
EXCEPTION_ERROR = "int  3"
EXCEPTION_SMARTFILL = "int  4"
EXCEPTION_INFO = "int  5"
NO_PROMPT_WITH_WARNING = "int  0"
PROMPT_WHEN_WARNING_EXIST = "int  1"
FORCE_WARNING_HANDLING = "int  2"
def BaseInstance():
'''public BaseInstance()
'''
pass
def getId():
'''public String getId()
'''
pass
def getSafeId():
'''public String getSafeId()
'''
pass
def setRenderId():
'''public void setRenderId(final String id)
'''
pass
def getRenderId():
'''public String getRenderId()
'''
pass
def setWebClientSession():
'''public void setWebClientSession(final WebClientSession wcs)
'''
pass
def getWebClientSession():
'''public WebClientSession getWebClientSession()
'''
pass
def addChild():
'''public void addChild(final BaseInstance child)
public void addChild(final BaseInstance child, final int index)
'''
pass
def getChildren():
'''public List<BaseInstance> getChildren()
'''
pass
def clearChildren():
'''public void clearChildren()
'''
pass
def getParentInstance():
'''public BaseInstance getParentInstance()
'''
pass
def setParent():
'''public void setParent(final BaseInstance parent)
'''
pass
def hasLocalProperty():
'''public boolean hasLocalProperty(final String key)
'''
pass
def isOnTableRow():
'''public boolean isOnTableRow()
'''
pass
def getRowNum():
'''public String getRowNum()
'''
pass
def getPropertyNames():
'''public final String[] getPropertyNames()
'''
pass
def getProperty():
'''public String getProperty(final String key)
'''
pass
def initProperty():
'''public void initProperty()
'''
pass
def setProperty():
'''public boolean setProperty(final String key, final String value, final boolean systemCheck, final boolean showWarnings)
public void setProperty(final String key, final String value)
'''
pass
def removeProperty():
'''public void removeProperty(final String key)
'''
pass
def getString():
'''public String getString(final String key)
'''
pass
def getBoolean():
'''public boolean getBoolean(final String property)
'''
pass
def getInt():
'''public int getInt(final String property, final int defaultValue)
'''
pass
def getParent():
'''public ControlHandler getParent()
'''
pass
def handleEvent():
'''public int handleEvent(final WebClientEvent event)
public int handleEvent(final String methodName, final WebClientEvent event)
'''
pass
def initialize():
'''public void initialize()
'''
pass
def getDescriptor():
'''public BaseDescriptor getDescriptor()
'''
pass
def setDescriptor():
'''public void setDescriptor(final BaseDescriptor descriptor)
'''
pass
def getType():
'''public String getType()
'''
pass
def getLocalizedType():
'''public String getLocalizedType()
'''
pass
def setType():
'''public void setType(final String type)
'''
pass
def getChildCount():
'''public int getChildCount()
'''
pass
def setConsiderInDesigner():
'''public void setConsiderInDesigner(final boolean flag)
'''
pass
def getConsiderInDesigner():
'''public boolean getConsiderInDesigner()
'''
pass
def clearProperties():
'''public void clearProperties()
'''
pass
def clone():
'''public Object clone(final String newId)
public Object clone(final String newId, final String childIdAppend)
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def hasPropertyChanged():
'''public boolean hasPropertyChanged(final String property)
'''
pass
def hasAnyPropertyChanged():
'''public boolean hasAnyPropertyChanged()
'''
pass
def isVisible():
'''public boolean isVisible()
'''
pass
def getPage():
'''public PageInstance getPage()
'''
pass
def toString():
'''public String toString()
'''
pass
def addRefreshListener():
'''public void addRefreshListener(final String componentId)
'''
pass
def isDynamicContainer():
'''public boolean isDynamicContainer()
'''
pass
def getRefreshListeners():
'''public String getRefreshListeners()
'''
pass
def setDynamicContainer():
'''public void setDynamicContainer(final boolean isDynamic)
'''
pass
def maintainControlId():
'''public boolean maintainControlId()
'''
pass
def getChildIndex():
'''public int getChildIndex()
'''
pass
def getIdExtension():
'''public String getIdExtension()
'''
pass
def setOnTable():
'''public void setOnTable(final boolean isOnTable)
'''
pass
def isOnTable():
'''public boolean isOnTable()
'''
pass
