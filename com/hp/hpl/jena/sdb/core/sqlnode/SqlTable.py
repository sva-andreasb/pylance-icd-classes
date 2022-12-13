def SqlTable():
    '''public SqlTable(final String name)
    public SqlTable(final String aliasName, final String tableName)
    '''
def isTable():
    '''public boolean isTable()
    '''
def asTable():
    '''public SqlTable asTable()
    '''
def usesColumn():
    '''public boolean usesColumn(final SqlColumn c)
    '''
def getTableName():
    '''public String getTableName()
    '''
def visit():
    '''public void visit(final SqlNodeVisitor visitor)
    '''
def getIdScope():
    '''public Scope getIdScope()
    '''
def getNodeScope():
    '''public Scope getNodeScope()
    '''
def setIdColumnForVar():
    '''public void setIdColumnForVar(final Var var, final SqlColumn thisCol)
    '''
def setValueColumnForVar():
    '''public void setValueColumnForVar(final Var var, final SqlColumn thisCol)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object other)
    '''
def apply():
    '''public SqlNode apply(final SqlTransform transform)
    '''
def copy():
    '''public SqlNode copy()
    '''
