ISNULL = "String  \"0\""
ISNOTNULL = "String  \"1\""
def ():
    '''returns MAXTableDomain\n\n
    (final MboValue mbv)\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def action():
    '''returns None\n\n
    action()\n
    '''
def chooseActualDomainValues():
    '''returns None\n\n
    chooseActualDomainValues()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String where)\n
    getMboSet(final String where, String identifier)\n
    getMboSet()\n
    '''
def hasList():
    '''returns boolean\n\n
    hasList()\n
    '''
def getList():
    '''returns MboSetRemote\n\n
    getList()\n
    '''
def setRelationship():
    '''returns None\n\n
    setRelationship(final String objectName, final String whereClause)\n
    '''
def setListCriteria():
    '''returns None\n\n
    setListCriteria(final String listWhere)\n
    '''
def setListOrderBy():
    '''returns None\n\n
    setListOrderBy(final String orderBy)\n
    '''
def setErrorMessage():
    '''returns None\n\n
    setErrorMessage(final String eg, final String ek)\n
    '''
def getListCriteria():
    '''returns String\n\n
    getListCriteria()\n
    '''
def setValueFromLookup():
    '''returns None\n\n
    setValueFromLookup(final MboRemote sourceMbo, final long accessModifier)\n
    setValueFromLookup(final MboRemote sourceMbo)\n
    '''
def setLookupKeyMapInOrder():
    '''returns None\n\n
    setLookupKeyMapInOrder(final String[] targetKeys, final String[] sourceKeys)\n
    setLookupKeyMapInOrder(final String[][] map)\n
    '''
def setKeyMap():
    '''returns None\n\n
    setKeyMap(final String sourceMboName, final String[] targetKeys, final String[] sourceKeys)\n
    '''
def addToLookupMapCache():
    '''returns None\n\n
    addToLookupMapCache(final String source, final String[][] map)\n
    '''
def setMultiKeyWhereForLookup():
    '''returns None\n\n
    setMultiKeyWhereForLookup(final String w)\n
    '''
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final String value, final boolean exact)\n
    '''
def smartFillWithoutReset():
    '''returns MboSetRemote\n\n
    smartFillWithoutReset(final String value, final boolean exact)\n
    '''
def smartFind():
    '''returns MboSetRemote\n\n
    smartFind(final String value, final boolean exact)\n
    smartFind(final String sourceObj, final String value, final boolean exact)\n
    '''
def smartFindWithoutReset():
    '''returns MboSetRemote\n\n
    smartFindWithoutReset(final String value, final boolean exact)\n
    '''
def getMatchingAttr():
    '''returns String\n\n
    getMatchingAttr()\n
    getMatchingAttr(final String sourceObjectName)\n
    '''
def addConditionalListWhere():
    '''returns None\n\n
    addConditionalListWhere(final String attribute, final String condition, final String where)\n
    '''
def clearConditionalListWhere():
    '''returns None\n\n
    clearConditionalListWhere()\n
    '''
def evalConditionalWhere():
    '''returns String\n\n
    evalConditionalWhere(final ArrayList conditionalWhereList)\n
    '''
