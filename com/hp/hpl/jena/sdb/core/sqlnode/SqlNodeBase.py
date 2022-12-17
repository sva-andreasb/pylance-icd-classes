def ():
    '''returns SqlNodeBase\n\n
    (final String aliasName)\n
    '''
def isJoin():
    '''returns boolean\n\n
    isJoin()\n
    '''
def isInnerJoin():
    '''returns boolean\n\n
    isInnerJoin()\n
    '''
def isLeftJoin():
    '''returns boolean\n\n
    isLeftJoin()\n
    '''
def asJoin():
    '''returns SqlJoin\n\n
    asJoin()\n
    '''
def asLeftJoin():
    '''returns SqlJoinLeftOuter\n\n
    asLeftJoin()\n
    '''
def asInnerJoin():
    '''returns SqlJoinInner\n\n
    asInnerJoin()\n
    '''
def isRestrict():
    '''returns boolean\n\n
    isRestrict()\n
    '''
def asRestrict():
    '''returns SqlRestrict\n\n
    asRestrict()\n
    '''
def isProject():
    '''returns boolean\n\n
    isProject()\n
    '''
def asProject():
    '''returns SqlProject\n\n
    asProject()\n
    '''
def isDistinct():
    '''returns boolean\n\n
    isDistinct()\n
    '''
def asDistinct():
    '''returns SqlDistinct\n\n
    asDistinct()\n
    '''
def isCoalesce():
    '''returns boolean\n\n
    isCoalesce()\n
    '''
def asCoalesce():
    '''returns SqlCoalesce\n\n
    asCoalesce()\n
    '''
def isTable():
    '''returns boolean\n\n
    isTable()\n
    '''
def asTable():
    '''returns SqlTable\n\n
    asTable()\n
    '''
def isSelectBlock():
    '''returns boolean\n\n
    isSelectBlock()\n
    '''
def asSelectBlock():
    '''returns SqlSelectBlock\n\n
    asSelectBlock()\n
    '''
def output():
    '''returns None\n\n
    output(final IndentedWriter out)\n
    output(final IndentedWriter out, final boolean withAnnotations)\n
    '''
def usesColumn():
    '''returns boolean\n\n
    usesColumn(final SqlColumn c)\n
    '''
def tablesInvolved():
    '''returns Set<SqlTable>\n\n
    tablesInvolved()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
