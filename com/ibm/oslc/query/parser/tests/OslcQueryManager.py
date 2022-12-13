def OslcQueryManager():
'''public OslcQueryManager()
public OslcQueryManager(final boolean verbose)
'''
pass
def getWhereQueryParameter():
'''public String getWhereQueryParameter()
'''
pass
def getSearchTermsQueryParameter():
'''public String getSearchTermsQueryParameter()
'''
pass
def getOrderByQueryParameter():
'''public String getOrderByQueryParameter()
'''
pass
def getSelectQueryParameter():
'''public String getSelectQueryParameter()
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
'''public void searchTerm(final String searchTerm)
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
