WRITE_MODE = "int  1"
DIFFERED_CHANGES_MODE = "int  2"
DIRECT_ACCESS_MODE = "int  4"
ONLY_SAVE_MODIFICATIONS_MODE = "int  8"
def IlvFormModel():
    '''public IlvFormModel(final int c)
    public IlvFormModel(final IlvSettings ilvSettings, final int n)
    public IlvFormModel(final IlvSettings ilvSettings)
    public IlvFormModel()
    '''
def commit():
    '''public void commit()
    public void commit(final IlvSettings ilvSettings)
    '''
def cancelModifications():
    '''public void cancelModifications()
    public void cancelModifications()
    '''
def getWritableModel():
    '''public IlvSettings getWritableModel()
    public IlvSettings getWritableModel()
    '''
def addModel():
    '''public void addModel(final IlvSettings ilvSettings, final String s)
    public void addModel(final IlvSettingsElement ilvSettingsElement, final String s)
    public void addModel(final IlvSettingsElement ilvSettingsElement)
    '''
def getParent():
    '''public Object getParent(final Object o)
    '''
def getChildren():
    '''public Object[] getChildren(final Object o)
    '''
def getAttributeValue():
    '''public Object getAttributeValue(final Object o, final String s)
    '''
def getType():
    '''public String getType(final Object o)
    '''
def getAttributes():
    '''public String[] getAttributes(final Object o)
    '''
def addXMLFile():
    '''public void addXMLFile(final URL url, final String s)
    '''
def addBeanObjects():
    '''public void addBeanObjects(final Object[] array, final String s)
    '''
def getAllSettings():
    '''public IlvSettings getAllSettings()
    '''
def getModelCount():
    '''public final int getModelCount()
    '''
def getModel():
    '''public final IlvSettings getModel(final int n)
    public final IlvSettings getModel(final String s)
    public IlvSettings getModel()
    '''
def removeModel():
    '''public boolean removeModel(final IlvSettings ilvSettings)
    public boolean removeModel(final String s)
    '''
def dump():
    '''public void dump()
    public void dump()
    '''
def ModelManager():
    '''public ModelManager(final String s)
    public ModelManager()
    '''
def getID():
    '''public Object getID(final Object o)
    '''
def ModelNode():
    '''public ModelNode(final IlvSettings a, final String c, final IlvSettings ilvSettings, final int n)
    '''
def getId():
    '''public String getId()
    '''
