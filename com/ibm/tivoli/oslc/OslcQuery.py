def ():
    '''returns OslcQuery\n\n
    (final String queryClause)\n
    (final String queryClause, final String orderByClause, final String searchTerms)\n
    (final Map<String, String[]> queryParams)\n
    '''
def init():
    '''returns None\n\n
    init(final Map<String, String[]> queryParams)\n
    '''
def getQueryParam():
    '''returns String[]\n\n
    getQueryParam(final String paramName)\n
    '''
def setTemplatePageSize():
    '''returns None\n\n
    setTemplatePageSize(final int tPageSize)\n
    '''
def setTemplateSelect():
    '''returns None\n\n
    setTemplateSelect(final String tSelect)\n
    '''
def setTemplateSavedQuery():
    '''returns None\n\n
    setTemplateSavedQuery(final String tSavedQuery)\n
    '''
def getOslcWhere():
    '''returns List<IOslcTerm>\n\n
    getOslcWhere()\n
    '''
def getOslcSearchTerm():
    '''returns List<String>\n\n
    getOslcSearchTerm()\n
    '''
def getOslcProperties():
    '''returns List<IOslcProperty>\n\n
    getOslcProperties()\n
    '''
def getOslcSelect():
    '''returns List<IOslcProperty>\n\n
    getOslcSelect()\n
    '''
def getOslcOrderBy():
    '''returns List<IOslcSortTerm>\n\n
    getOslcOrderBy()\n
    '''
def isPagingEnabled():
    '''returns boolean\n\n
    isPagingEnabled()\n
    '''
def getPageSize():
    '''returns int\n\n
    getPageSize()\n
    '''
def getPageNumber():
    '''returns int\n\n
    getPageNumber()\n
    '''
def applyQueryTemplate():
    '''returns None\n\n
    applyQueryTemplate(final String owner, final String osname)\n
    '''
def getSearchAttributes():
    '''returns String\n\n
    getSearchAttributes()\n
    '''
def getTimeLineAttribute():
    '''returns String\n\n
    getTimeLineAttribute()\n
    '''
def whereTerm():
    '''returns None\n\n
    whereTerm(final String identifier, final String operator, final String value)\n
    whereTerm(final String identifier, final String[] values)\n
    '''
def whereScopedTerm():
    '''returns None\n\n
    whereScopedTerm(final String identifier, final List<IOslcTerm> terms)\n
    '''
def selectProperty():
    '''returns None\n\n
    selectProperty(final String identifier)\n
    '''
def selectNestedProperty():
    '''returns None\n\n
    selectNestedProperty(final String identifier, final List<IOslcProperty> properties)\n
    '''
def searchTerm():
    '''returns None\n\n
    searchTerm(final String term)\n
    '''
def orderBySortTerm():
    '''returns None\n\n
    orderBySortTerm(final String sortOrder, final String identifier)\n
    '''
def orderByScopedSortTerm():
    '''returns None\n\n
    orderByScopedSortTerm(final String identifier, final List<IOslcSortTerm> sortTerms)\n
    '''
