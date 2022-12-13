def OslcQuery():
    '''    public OslcQuery(final String queryClause)
    public OslcQuery(final String queryClause, final String orderByClause, final String searchTerms)
    public OslcQuery(final Map<String, String[]> queryParams)
    '''
def init():
    '''    public void init(final Map<String, String[]> queryParams)
    '''
def getQueryParam():
    '''    public String[] getQueryParam(final String paramName)
    '''
def setTemplatePageSize():
    '''    public void setTemplatePageSize(final int tPageSize)
    '''
def setTemplateSelect():
    '''    public void setTemplateSelect(final String tSelect)
    '''
def setTemplateSavedQuery():
    '''    public void setTemplateSavedQuery(final String tSavedQuery)
    '''
def getOslcWhere():
    '''    public List<IOslcTerm> getOslcWhere()
    '''
def getOslcSearchTerm():
    '''    public List<String> getOslcSearchTerm()
    '''
def getOslcProperties():
    '''    public List<IOslcProperty> getOslcProperties()
    '''
def getOslcSelect():
    '''    public List<IOslcProperty> getOslcSelect()
    '''
def getOslcOrderBy():
    '''    public List<IOslcSortTerm> getOslcOrderBy()
    '''
def getOslcPrefixMap():
    '''    public Map<String, String> getOslcPrefixMap()
    '''
def isPagingEnabled():
    '''    public boolean isPagingEnabled()
    '''
def getPageSize():
    '''    public int getPageSize()
    '''
def getPageNumber():
    '''    public int getPageNumber()
    '''
def applyQueryTemplate():
    '''    public void applyQueryTemplate(final String owner, final String osname)
    '''
def getSearchAttributes():
    '''    public String getSearchAttributes()
    '''
def getTimeLineAttribute():
    '''    public String getTimeLineAttribute()
    '''
def whereTerm():
    '''    public void whereTerm(final String identifier, final String operator, final String value)
    public void whereTerm(final String identifier, final String[] values)
    '''
def whereScopedTerm():
    '''    public void whereScopedTerm(final String identifier, final List<IOslcTerm> terms)
    '''
def selectProperty():
    '''    public void selectProperty(final String identifier)
    '''
def selectNestedProperty():
    '''    public void selectNestedProperty(final String identifier, final List<IOslcProperty> properties)
    '''
def searchTerm():
    '''    public void searchTerm(final String term)
    '''
def orderBySortTerm():
    '''    public void orderBySortTerm(final String sortOrder, final String identifier)
    '''
def orderByScopedSortTerm():
    '''    public void orderByScopedSortTerm(final String identifier, final List<IOslcSortTerm> sortTerms)
    '''
