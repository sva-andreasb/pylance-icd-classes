def getNcols():
    '''returns int\n\n
    getNcols()\n
    '''
def getNrows():
    '''returns int\n\n
    getNrows()\n
    '''
def getNNZs():
    '''returns int\n\n
    getNNZs()\n
    '''
def getCols():
    '''returns None\n\n
    getCols(final int begin, final int num, final int[][] ind, final double[][] val)\n
    '''
def getRows():
    '''returns None\n\n
    getRows(final int start, final int num, final double[] lb, final double[] ub, final int[][] ind, final double[][] val)\n
    '''
def getNZ():
    '''returns double\n\n
    getNZ(final int row, final int column)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final ilog.concert.IloRange rng)\n
    getIndex(final ilog.concert.IloNumVar var)\n
    '''
def getNumVarsO():
    '''returns IloNumVarArray\n\n
    getNumVarsO()\n
    '''
def addRow():
    '''returns int\n\n
    addRow(final double lb, final double ub, final int[] ind, final double[] val)\n
    addRow(final ilog.concert.IloRange rng)\n
    '''
def addRows():
    '''returns int\n\n
    addRows(final double[] lb, final double[] ub, final int[][] ind, final double[][] val)\n
    addRows(final ilog.concert.IloRange[] rng)\n
    addRows(final ilog.concert.IloRange[] rng, final int start, final int num)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final int ind)\n
    '''
def removeRows():
    '''returns None\n\n
    removeRows(final int start, final int num)\n
    removeRows(final int[] ind)\n
    removeRows(final int[] ind, final int start, final int num)\n
    '''
def addColumn():
    '''returns int\n\n
    addColumn(final ilog.concert.IloNumVar var, final int[] ind, final double[] val)\n
    addColumn(final ilog.concert.IloNumVar var)\n
    '''
def addCols():
    '''returns int\n\n
    addCols(final ilog.concert.IloNumVar[] var, final int[][] indices, final double[][] values)\n
    addCols(final ilog.concert.IloNumVar[] var)\n
    addCols(final ilog.concert.IloNumVar[] var, final int start, final int num)\n
    '''
def removeColumn():
    '''returns None\n\n
    removeColumn(final int ind)\n
    '''
def removeCols():
    '''returns None\n\n
    removeCols(final int begin, final int num)\n
    removeCols(final int[] ind)\n
    removeCols(final int[] ind, final int start, final int num)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setNZ():
    '''returns None\n\n
    setNZ(final int rowind, final int colind, final double val)\n
    '''
def setNZs():
    '''returns None\n\n
    setNZs(final int[] rowind, final int[] colind, final double[] val)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String arg0)\n
    '''
def needCopy():
    '''returns None\n\n
    needCopy(final IloCopyManager.Check check)\n
    '''
def makeCopy():
    '''returns IloCopyable\n\n
    makeCopy(final IloCopyManager copy)\n
    '''
def getCopy():
    '''returns IloCopyable\n\n
    getCopy(final IloCopyable arg0)\n
    '''
def makeColumnArray():
    '''returns IloColumnArray\n\n
    makeColumnArray(final int num, final int[][] ind, final double[][] val)\n
    '''
def install():
    '''returns None\n\n
    install(final ilog.concert.IloNumVar[] var)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
