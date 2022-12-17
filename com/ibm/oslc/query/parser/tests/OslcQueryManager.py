def ():
    '''returns OslcQueryManager\n\n
    ()\n
    (final boolean verbose)\n
    '''
def getWhereQueryParameter():
    '''returns String\n\n
    getWhereQueryParameter()\n
    '''
def getSearchTermsQueryParameter():
    '''returns String\n\n
    getSearchTermsQueryParameter()\n
    '''
def getOrderByQueryParameter():
    '''returns String\n\n
    getOrderByQueryParameter()\n
    '''
def getSelectQueryParameter():
    '''returns String\n\n
    getSelectQueryParameter()\n
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
    searchTerm(final String searchTerm)\n
    '''
def orderBySortTerm():
    '''returns None\n\n
    orderBySortTerm(final String sortOrder, final String identifier)\n
    '''
def orderByScopedSortTerm():
    '''returns None\n\n
    orderByScopedSortTerm(final String identifier, final List<IOslcSortTerm> sortTerms)\n
    '''
