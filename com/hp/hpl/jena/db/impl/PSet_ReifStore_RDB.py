def storeReifStmt():
    '''returns None\n\n
    storeReifStmt(final Node n, final Triple t, final IDBID my_GID)\n
    '''
def deleteReifStmt():
    '''returns None\n\n
    deleteReifStmt(final Node n, final Triple t, final IDBID my_GID)\n
    '''
def findReifStmt():
    '''returns ResultSetReifIterator\n\n
    findReifStmt(final Node stmtURI, final boolean hasType, final IDBID graphID, final boolean getTriples)\n
    '''
def findReifTripleMatch():
    '''returns ResultSetReifIterator\n\n
    findReifTripleMatch(final TripleMatch t, final IDBID graphID)\n
    '''
def findReifStmtURIByTriple():
    '''returns ExtendedIterator<Node>\n\n
    findReifStmtURIByTriple(final Triple t, final IDBID my_GID)\n
    '''
def storeFrag():
    '''returns None\n\n
    storeFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)\n
    '''
def updateOneFrag():
    '''returns None\n\n
    updateOneFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final boolean nullify, final IDBID my_GID)\n
    '''
def nullifyFrag():
    '''returns None\n\n
    nullifyFrag(final Node stmtURI, final ReificationStatementMask fragMask, final IDBID my_GID)\n
    '''
def updateFrag():
    '''returns None\n\n
    updateFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)\n
    '''
def findFrag():
    '''returns ResultSetReifIterator\n\n
    findFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)\n
    '''
def deleteFrag():
    '''returns None\n\n
    deleteFrag(final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)\n
    '''
def map1():
    '''returns Node\n\n
    map1(final List<String> l)\n
    '''
