def ():
    '''returns SqlTable\n\n
    (final String name)\n
    (final String aliasName, final String tableName)\n
    '''
def isTable():
    '''returns boolean\n\n
    isTable()\n
    '''
def asTable():
    '''returns SqlTable\n\n
    asTable()\n
    '''
def usesColumn():
    '''returns boolean\n\n
    usesColumn(final SqlColumn c)\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
    '''
def visit():
    '''returns None\n\n
    visit(final SqlNodeVisitor visitor)\n
    '''
def getIdScope():
    '''returns Scope\n\n
    getIdScope()\n
    '''
def getNodeScope():
    '''returns Scope\n\n
    getNodeScope()\n
    '''
def setIdColumnForVar():
    '''returns None\n\n
    setIdColumnForVar(final Var var, final SqlColumn thisCol)\n
    '''
def setValueColumnForVar():
    '''returns None\n\n
    setValueColumnForVar(final Var var, final SqlColumn thisCol)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def apply():
    '''returns SqlNode\n\n
    apply(final SqlTransform transform)\n
    '''
def copy():
    '''returns SqlNode\n\n
    copy()\n
    '''
