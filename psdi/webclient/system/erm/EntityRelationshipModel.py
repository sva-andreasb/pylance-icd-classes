def EntityRelationshipModel():
    '''    public EntityRelationshipModel(final String id)
    public EntityRelationshipModel()
    '''
def getId():
    '''    public String getId()
    '''
def putTopLevelEntity():
    '''    public void putTopLevelEntity(final String datasrc, final UIERMEntity entity)
    '''
def putEntity():
    '''    public void putEntity(final String datasrc, final UIERMEntity entity)
    '''
def getTopLevelEntities():
    '''    public Map<String, UIERMEntity> getTopLevelEntities()
    '''
def findEntity():
    '''    public UIERMEntity findEntity(final String datasrc)
    '''
def generateERMXML():
    '''    public StringBuilder generateERMXML()
    '''
def dialogEntityExists():
    '''    public boolean dialogEntityExists(final String id)
    '''
def hasDialogEntity():
    '''    public boolean hasDialogEntity(final String id)
    '''
def addDialogEntity():
    '''    public void addDialogEntity(final String id)
    '''
def removeDialogEntity():
    '''    public void removeDialogEntity(final String id)
    '''
def setConditionalSigOptions():
    '''    public void setConditionalSigOptions(final List<String> sigOptions)
    '''
def sigOptionHaveCondInputmode():
    '''    public boolean sigOptionHaveCondInputmode(final String sigOption)
    '''
def generateDataStores():
    '''    public void generateDataStores(final Element presentationElement, final MXSession mxSession)
    '''
def generateDataStoresForDialog():
    '''    public synchronized List<DataStoreInfo> generateDataStoresForDialog(final Element el, final MXSession mxSession)
    '''
def addDataStoreInfo():
    '''    public void addDataStoreInfo(final DataStoreInfo dataStoreInfo)
    '''
def getDataStore():
    '''    public DataStoreInfo getDataStore(final String dataStoreId)
    '''
def getDataStoreList():
    '''    public Map<String, DataStoreInfo> getDataStoreList()
    '''
def addToCheckForDataStoresList():
    '''    public void addToCheckForDataStoresList(final UIERMEntity currentEntity)
    '''
def addRepLibraryEntity():
    '''    public void addRepLibraryEntity(final UIERMEntity currentEntity)
    '''
def removeRepLibraryEntitites():
    '''    public void removeRepLibraryEntitites()
    '''
