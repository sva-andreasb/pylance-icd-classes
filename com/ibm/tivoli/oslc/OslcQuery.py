def OslcQuery():
'''public OslcQuery(final String queryClause)
public OslcQuery(final String queryClause, final String orderByClause, final String searchTerms)
public OslcQuery(final Map<String, String[]> queryParams)
'''
pass
def init():
'''public void init(final Map<String, String[]> queryParams)
'''
pass
def getQueryParam():
'''public String[] getQueryParam(final String paramName)
'''
pass
def setTemplatePageSize():
'''public void setTemplatePageSize(final int tPageSize)
'''
pass
def setTemplateSelect():
'''public void setTemplateSelect(final String tSelect)
'''
pass
def setTemplateSavedQuery():
'''public void setTemplateSavedQuery(final String tSavedQuery)
'''
pass
def getOslcWhere():
'''public List<IOslcTerm> getOslcWhere()
'''
pass
def getOslcSearchTerm():
'''public List<String> getOslcSearchTerm()
'''
pass
def getOslcProperties():
'''public List<IOslcProperty> getOslcProperties()
'''
pass
def getOslcSelect():
'''public List<IOslcProperty> getOslcSelect()
'''
pass
def getOslcOrderBy():
'''public List<IOslcSortTerm> getOslcOrderBy()
'''
pass
def getOslcPrefixMap():
'''public Map<String, String> getOslcPrefixMap()
'''
pass
def isPagingEnabled():
'''public boolean isPagingEnabled()
'''
pass
def getPageSize():
'''public int getPageSize()
'''
pass
def getPageNumber():
'''public int getPageNumber()
'''
pass
def applyQueryTemplate():
'''public void applyQueryTemplate(final String owner, final String osname)
'''
pass
def getSearchAttributes():
'''public String getSearchAttributes()
'''
pass
def getTimeLineAttribute():
'''public String getTimeLineAttribute()
'''
pass
def whereTerm():
'''public void whereTerm(final String identifier, final String operator, final String value)
public void whereTerm(final String identifier, final String[] values)
'''
pass
def whereScopedTerm():
'''public void whereScopedTerm(final String identifier, final List<IOslcTerm> terms)
'''
pass
def selectProperty():
'''public void selectProperty(final String identifier)
'''
pass
def selectNestedProperty():
'''public void selectNestedProperty(final String identifier, final List<IOslcProperty> properties)
'''
pass
def searchTerm():
'''public void searchTerm(final String term)
'''
pass
def orderBySortTerm():
'''public void orderBySortTerm(final String sortOrder, final String identifier)
'''
pass
def orderByScopedSortTerm():
'''public void orderByScopedSortTerm(final String identifier, final List<IOslcSortTerm> sortTerms)
'''
pass
