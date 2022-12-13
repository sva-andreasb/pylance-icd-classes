FILTER_TYPE_CHILDVERSION = "String  \"CHILDVERSION\""
FILTER_TYPE_CHILDRELEASE = "String  \"CHILDRELEASE\""
FILTER_TYPE_PARENTRELATION = "String  \"PARENTRELATION\""
FILTER_TYPE_CHILDRELATION = "String  \"CHILDRELATION\""
FILTER_TYPE_CONVERSIONVARIANT = "String  \"CONVERSIONVARIANT\""
def SoftwareCatalog():
    '''    public SoftwareCatalog(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def setNameAndTypeReadOnly():
    '''    public void setNameAndTypeReadOnly()
    '''
def add():
    '''    public void add()
    '''
def toBeSaved():
    '''    public boolean toBeSaved()
    '''
def generateUniqueId():
    '''    public String generateUniqueId()
    public static String generateUniqueId(String swname, String version, String release, String manufacturer, final String unknownString)
    '''
def modify():
    '''    public void modify()
    '''
def save():
    '''    public void save()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def undelete():
    '''    public void undelete()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def getVuiExhibitID():
    '''    public String getVuiExhibitID()
    '''
def getParent():
    '''    public SoftwareCatalogRemote getParent()
    '''
def getFilterClause():
    '''    public static String getFilterClause(final String requestedType)
    '''
def combineSubClauses():
    '''    public static String combineSubClauses(final String[] subClauses)
    '''
def getCatalogRecord():
    '''    public static MboRemote getCatalogRecord(final long tloamsoftwareid, final UserInfo userInfo)
    '''
