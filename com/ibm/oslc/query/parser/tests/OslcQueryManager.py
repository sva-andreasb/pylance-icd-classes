def OslcQueryManager():
    '''public OslcQueryManager()
    public OslcQueryManager(final boolean verbose)
    '''
def getWhereQueryParameter():
    '''public String getWhereQueryParameter()
    '''
def getSearchTermsQueryParameter():
    '''public String getSearchTermsQueryParameter()
    '''
def getOrderByQueryParameter():
    '''public String getOrderByQueryParameter()
    '''
def getSelectQueryParameter():
    '''public String getSelectQueryParameter()
    '''
def whereTerm():
    '''public void whereTerm(final String identifier, final String operator, final String value)
    public void whereTerm(final String identifier, final String[] values)
    '''
def whereScopedTerm():
    '''public void whereScopedTerm(final String identifier, final List<IOslcTerm> terms)
    '''
def selectProperty():
    '''public void selectProperty(final String identifier)
    '''
def selectNestedProperty():
    '''public void selectNestedProperty(final String identifier, final List<IOslcProperty> properties)
    '''
def searchTerm():
    '''public void searchTerm(final String searchTerm)
    '''
def orderBySortTerm():
    '''public void orderBySortTerm(final String sortOrder, final String identifier)
    '''
def orderByScopedSortTerm():
    '''public void orderByScopedSortTerm(final String identifier, final List<IOslcSortTerm> sortTerms)
    '''
