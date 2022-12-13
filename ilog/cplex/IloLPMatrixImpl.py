def getNcols():
    '''    public int getNcols()
    '''
def getNrows():
    '''    public int getNrows()
    '''
def getNNZs():
    '''    public int getNNZs()
    '''
def getCols():
    '''    public void getCols(final int begin, final int num, final int[][] ind, final double[][] val)
    '''
def getRows():
    '''    public void getRows(final int start, final int num, final double[] lb, final double[] ub, final int[][] ind, final double[][] val)
    '''
def getNZ():
    '''    public double getNZ(final int row, final int column)
    '''
def getIndex():
    '''    public int getIndex(final ilog.concert.IloRange rng)
    public int getIndex(final ilog.concert.IloNumVar var)
    '''
def getNumVarsO():
    '''    public IloNumVarArray getNumVarsO()
    '''
def addRow():
    '''    public int addRow(final double lb, final double ub, final int[] ind, final double[] val)
    public int addRow(final ilog.concert.IloRange rng)
    '''
def addRows():
    '''    public int addRows(final double[] lb, final double[] ub, final int[][] ind, final double[][] val)
    public int addRows(final ilog.concert.IloRange[] rng)
    public int addRows(final ilog.concert.IloRange[] rng, final int start, final int num)
    '''
def removeRow():
    '''    public void removeRow(final int ind)
    '''
def removeRows():
    '''    public void removeRows(final int start, final int num)
    public void removeRows(final int[] ind)
    public void removeRows(final int[] ind, final int start, final int num)
    '''
def addColumn():
    '''    public int addColumn(final ilog.concert.IloNumVar var, final int[] ind, final double[] val)
    public int addColumn(final ilog.concert.IloNumVar var)
    '''
def addCols():
    '''    public int addCols(final ilog.concert.IloNumVar[] var, final int[][] indices, final double[][] values)
    public int addCols(final ilog.concert.IloNumVar[] var)
    public int addCols(final ilog.concert.IloNumVar[] var, final int start, final int num)
    '''
def removeColumn():
    '''    public void removeColumn(final int ind)
    '''
def removeCols():
    '''    public void removeCols(final int begin, final int num)
    public void removeCols(final int[] ind)
    public void removeCols(final int[] ind, final int start, final int num)
    '''
def clear():
    '''    public void clear()
    '''
def setNZ():
    '''    public void setNZ(final int rowind, final int colind, final double val)
    '''
def setNZs():
    '''    public void setNZs(final int[] rowind, final int[] colind, final double[] val)
    '''
def getName():
    '''    public String getName()
    '''
def setName():
    '''    public void setName(final String arg0)
    '''
def needCopy():
    '''    public void needCopy(final IloCopyManager.Check check)
    '''
def makeCopy():
    '''    public IloCopyable makeCopy(final IloCopyManager copy)
    '''
def getCopy():
    '''    public IloCopyable getCopy(final IloCopyable arg0)
    '''
def makeColumnArray():
    '''    public IloColumnArray makeColumnArray(final int num, final int[][] ind, final double[][] val)
    '''
def install():
    '''    public void install(final ilog.concert.IloNumVar[] var)
    '''
def getSize():
    '''    public int getSize()
    '''
