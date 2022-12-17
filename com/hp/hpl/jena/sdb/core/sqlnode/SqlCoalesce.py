def getCoalesceVars():
    '''returns Set<Var>\n\n
    getCoalesceVars()\n
    '''
def getNonCoalesceVars():
    '''returns Set<Var>\n\n
    getNonCoalesceVars()\n
    '''
def isCoalesce():
    '''returns boolean\n\n
    isCoalesce()\n
    '''
def asCoalesce():
    '''returns SqlCoalesce\n\n
    asCoalesce()\n
    '''
def getIdScope():
    '''returns Scope\n\n
    getIdScope()\n
    '''
def getNodeScope():
    '''returns Scope\n\n
    getNodeScope()\n
    '''
def getJoinNode():
    '''returns SqlJoin\n\n
    getJoinNode()\n
    '''
def visit():
    '''returns None\n\n
    visit(final SqlNodeVisitor visitor)\n
    '''
def apply():
    '''returns SqlNode\n\n
    apply(final SqlTransform transform, final SqlNode newSubNode)\n
    '''
def copy():
    '''returns SqlNode\n\n
    copy(final SqlNode subNode)\n
    '''
