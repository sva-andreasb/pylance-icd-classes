def isProject():
    '''returns boolean\n\n
    isProject()\n
    '''
def asProject():
    '''returns SqlProject\n\n
    asProject()\n
    '''
def usesColumn():
    '''returns boolean\n\n
    usesColumn(final SqlColumn c)\n
    '''
def getCols():
    '''returns List<ColAlias>\n\n
    getCols()\n
    '''
def visit():
    '''returns None\n\n
    visit(final SqlNodeVisitor visitor)\n
    '''
def apply():
    '''returns SqlNode\n\n
    apply(final SqlTransform transform, final SqlNode subNode)\n
    '''
def copy():
    '''returns SqlNode\n\n
    copy(final SqlNode subNode)\n
    '''
