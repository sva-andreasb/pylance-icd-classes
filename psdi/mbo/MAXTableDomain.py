ISNULL = "String  \"0\""
ISNOTNULL = "String  \"1\""
def MAXTableDomain():
    '''    public MAXTableDomain(final MboValue mbv)
    '''
def validate():
    '''    public void validate()
    '''
def action():
    '''    public void action()
    '''
def chooseActualDomainValues():
    '''    public void chooseActualDomainValues()
    '''
def getMboSet():
    '''    public MboSetRemote getMboSet(final String where)
    public MboSetRemote getMboSet(final String where, String identifier)
    public MboSetRemote getMboSet()
    '''
def hasList():
    '''    public boolean hasList()
    '''
def getList():
    '''    public MboSetRemote getList()
    '''
def setRelationship():
    '''    public void setRelationship(final String objectName, final String whereClause)
    '''
def setListCriteria():
    '''    public void setListCriteria(final String listWhere)
    '''
def setListOrderBy():
    '''    public void setListOrderBy(final String orderBy)
    '''
def setErrorMessage():
    '''    public void setErrorMessage(final String eg, final String ek)
    '''
def getListCriteria():
    '''    public String getListCriteria()
    '''
def setValueFromLookup():
    '''    public void setValueFromLookup(final MboRemote sourceMbo, final long accessModifier)
    public void setValueFromLookup(final MboRemote sourceMbo)
    '''
def setLookupKeyMapInOrder():
    '''    public void setLookupKeyMapInOrder(final String[] targetKeys, final String[] sourceKeys)
    public void setLookupKeyMapInOrder(final String[][] map)
    '''
def setKeyMap():
    '''    public void setKeyMap(final String sourceMboName, final String[] targetKeys, final String[] sourceKeys)
    '''
def addToLookupMapCache():
    '''    public void addToLookupMapCache(final String source, final String[][] map)
    '''
def setAllAttrsNullable():
    '''    public final void setAllAttrsNullable()
    '''
def setNotAllowNullAttrs():
    '''    public final void setNotAllowNullAttrs(final String[] attrs)
    '''
def setMultiKeyWhereForLookup():
    '''    public void setMultiKeyWhereForLookup(final String w)
    '''
def smartFill():
    '''    public MboSetRemote smartFill(final String value, final boolean exact)
    '''
def smartFillWithoutReset():
    '''    public MboSetRemote smartFillWithoutReset(final String value, final boolean exact)
    '''
def smartFind():
    '''    public MboSetRemote smartFind(final String value, final boolean exact)
    public MboSetRemote smartFind(final String sourceObj, final String value, final boolean exact)
    '''
def smartFindWithoutReset():
    '''    public MboSetRemote smartFindWithoutReset(final String value, final boolean exact)
    '''
def getMatchingAttr():
    '''    public String getMatchingAttr()
    public String getMatchingAttr(final String sourceObjectName)
    '''
def addConditionalListWhere():
    '''    public void addConditionalListWhere(final String attribute, final String condition, final String where)
    '''
def clearConditionalListWhere():
    '''    public void clearConditionalListWhere()
    '''
def evalConditionalWhere():
    '''    public String evalConditionalWhere(final ArrayList conditionalWhereList)
    '''
