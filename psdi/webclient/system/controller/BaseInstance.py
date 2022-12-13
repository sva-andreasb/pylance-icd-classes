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
def getId():
    '''public String getId()
    '''
def getSafeId():
    '''public String getSafeId()
    '''
def setRenderId():
    '''public void setRenderId(final String id)
    '''
def getRenderId():
    '''public String getRenderId()
    '''
def setWebClientSession():
    '''public void setWebClientSession(final WebClientSession wcs)
    '''
def getWebClientSession():
    '''public WebClientSession getWebClientSession()
    '''
def addChild():
    '''public void addChild(final BaseInstance child)
    public void addChild(final BaseInstance child, final int index)
    '''
def getChildren():
    '''public List<BaseInstance> getChildren()
    '''
def clearChildren():
    '''public void clearChildren()
    '''
def getParentInstance():
    '''public BaseInstance getParentInstance()
    '''
def setParent():
    '''public void setParent(final BaseInstance parent)
    '''
def hasLocalProperty():
    '''public boolean hasLocalProperty(final String key)
    '''
def isOnTableRow():
    '''public boolean isOnTableRow()
    '''
def getRowNum():
    '''public String getRowNum()
    '''
def getPropertyNames():
    '''public final String[] getPropertyNames()
    '''
def getProperty():
    '''public String getProperty(final String key)
    '''
def initProperty():
    '''public void initProperty()
    '''
def setProperty():
    '''public boolean setProperty(final String key, final String value, final boolean systemCheck, final boolean showWarnings)
    public void setProperty(final String key, final String value)
    '''
def removeProperty():
    '''public void removeProperty(final String key)
    '''
def getString():
    '''public String getString(final String key)
    '''
def getBoolean():
    '''public boolean getBoolean(final String property)
    '''
def getInt():
    '''public int getInt(final String property, final int defaultValue)
    '''
def getParent():
    '''public ControlHandler getParent()
    '''
def handleEvent():
    '''public int handleEvent(final WebClientEvent event)
    public int handleEvent(final String methodName, final WebClientEvent event)
    '''
def initialize():
    '''public void initialize()
    '''
def getDescriptor():
    '''public BaseDescriptor getDescriptor()
    '''
def setDescriptor():
    '''public void setDescriptor(final BaseDescriptor descriptor)
    '''
def getType():
    '''public String getType()
    '''
def getLocalizedType():
    '''public String getLocalizedType()
    '''
def setType():
    '''public void setType(final String type)
    '''
def getChildCount():
    '''public int getChildCount()
    '''
def setConsiderInDesigner():
    '''public void setConsiderInDesigner(final boolean flag)
    '''
def getConsiderInDesigner():
    '''public boolean getConsiderInDesigner()
    '''
def clearProperties():
    '''public void clearProperties()
    '''
def clone():
    '''public Object clone(final String newId)
    public Object clone(final String newId, final String childIdAppend)
    '''
def cleanup():
    '''public void cleanup()
    '''
def hasPropertyChanged():
    '''public boolean hasPropertyChanged(final String property)
    '''
def hasAnyPropertyChanged():
    '''public boolean hasAnyPropertyChanged()
    '''
def isVisible():
    '''public boolean isVisible()
    '''
def getPage():
    '''public PageInstance getPage()
    '''
def toString():
    '''public String toString()
    '''
def addRefreshListener():
    '''public void addRefreshListener(final String componentId)
    '''
def isDynamicContainer():
    '''public boolean isDynamicContainer()
    '''
def getRefreshListeners():
    '''public String getRefreshListeners()
    '''
def setDynamicContainer():
    '''public void setDynamicContainer(final boolean isDynamic)
    '''
def maintainControlId():
    '''public boolean maintainControlId()
    '''
def getChildIndex():
    '''public int getChildIndex()
    '''
def getIdExtension():
    '''public String getIdExtension()
    '''
def setOnTable():
    '''public void setOnTable(final boolean isOnTable)
    '''
def isOnTable():
    '''public boolean isOnTable()
    '''
