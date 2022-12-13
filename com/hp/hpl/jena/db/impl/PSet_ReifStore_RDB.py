def storeReifStmt():
    '''public void storeReifStmt(final Node n, final Triple t, final IDBID my_GID)
    '''
def deleteReifStmt():
    '''public void deleteReifStmt(final Node n, final Triple t, final IDBID my_GID)
    '''
def findReifStmt():
    '''public ResultSetReifIterator findReifStmt(final Node stmtURI, final boolean hasType, final IDBID graphID, final boolean getTriples)
    '''
def findReifTripleMatch():
    '''public ResultSetReifIterator findReifTripleMatch(final TripleMatch t, final IDBID graphID)
    '''
def findReifStmtURIByTriple():
    '''public ExtendedIterator<Node> findReifStmtURIByTriple(final Triple t, final IDBID my_GID)
    '''
def storeFrag():
    '''public void storeFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)
    '''
def updateOneFrag():
    '''public void updateOneFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final boolean nullify, final IDBID my_GID)
    '''
def nullifyFrag():
    '''public void nullifyFrag(final Node stmtURI, final ReificationStatementMask fragMask, final IDBID my_GID)
    '''
def updateFrag():
    '''public void updateFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)
    '''
def findFrag():
    '''public ResultSetReifIterator findFrag(final Node stmtURI, final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)
    '''
def deleteFrag():
    '''public void deleteFrag(final Triple frag, final ReificationStatementMask fragMask, final IDBID my_GID)
    '''
def map1():
    '''public Node map1(final List<String> l)
    '''
