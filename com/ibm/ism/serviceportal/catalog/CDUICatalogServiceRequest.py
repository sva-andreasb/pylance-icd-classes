def CDUICatalogServiceRequest():
    '''    public CDUICatalogServiceRequest(final MboRemote sr)
    '''
def setAttributes():
    '''    public void setAttributes(final List<CDUICatalogAttribute> attributes, final boolean modifyFlags)
    '''
def getAllSpecAttributesName():
    '''    public Set<String> getAllSpecAttributesName()
    '''
def addSpecAttribute():
    '''    public void addSpecAttribute(final String attribute, final String specAttribute)
    '''
def getAttributeData():
    '''    public JSONObject getAttributeData(final CDUICatalogAttribute ca, final boolean paging, final int pageSize, final int pageNum, final String searchValueInTable, final boolean loadDomain)
    '''
def getAllAttributeData():
    '''    public JSONArray getAllAttributeData(final List<CDUICatalogAttribute> attributes)
    '''
def getTableAttributeData():
    '''    public JSONArray getTableAttributeData(final List<CDUICatalogTableAttribute> attributes)
    '''
def saveAttributes():
    '''    public Map<String, String> saveAttributes(final List<CDUICatalogAttribute> attributesToBeSaved, final List<CDUICatalogTableAttribute> tableAttributesToBeSaved)
    '''
def submitAttributes():
    '''    public Map<String, String> submitAttributes(final List<CDUICatalogAttribute> attributesToBeSaved, final List<CDUICatalogTableAttribute> tableAttributesToBeSaved)
    '''
def getSpecAttribute():
    '''    public String getSpecAttribute(final String attributeName)
    '''
def getSR():
    '''    public MboRemote getSR()
    '''
def getSpec():
    '''    public PmScCRSpecRemote getSpec()
    '''
def getCR():
    '''    public PmScCRRemote getCR()
    '''
def initialize():
    '''    public void initialize(final MboRemote sr)
    '''
def getRelativeMboSet():
    '''    public MboSetRemote getRelativeMboSet(final String attribute)
    '''
