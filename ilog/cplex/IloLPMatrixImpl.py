def getNcols():
'''public int getNcols()
'''
pass
def getNrows():
'''public int getNrows()
'''
pass
def getNNZs():
'''public int getNNZs()
'''
pass
def getCols():
'''public void getCols(final int begin, final int num, final int[][] ind, final double[][] val)
'''
pass
def getRows():
'''public void getRows(final int start, final int num, final double[] lb, final double[] ub, final int[][] ind, final double[][] val)
'''
pass
def getNZ():
'''public double getNZ(final int row, final int column)
'''
pass
def getIndex():
'''public int getIndex(final ilog.concert.IloRange rng)
public int getIndex(final ilog.concert.IloNumVar var)
'''
pass
def getNumVarsO():
'''public IloNumVarArray getNumVarsO()
'''
pass
def addRow():
'''public int addRow(final double lb, final double ub, final int[] ind, final double[] val)
public int addRow(final ilog.concert.IloRange rng)
'''
pass
def addRows():
'''public int addRows(final double[] lb, final double[] ub, final int[][] ind, final double[][] val)
public int addRows(final ilog.concert.IloRange[] rng)
public int addRows(final ilog.concert.IloRange[] rng, final int start, final int num)
'''
pass
def removeRow():
'''public void removeRow(final int ind)
'''
pass
def removeRows():
'''public void removeRows(final int start, final int num)
public void removeRows(final int[] ind)
public void removeRows(final int[] ind, final int start, final int num)
'''
pass
def addColumn():
'''public int addColumn(final ilog.concert.IloNumVar var, final int[] ind, final double[] val)
public int addColumn(final ilog.concert.IloNumVar var)
'''
pass
def addCols():
'''public int addCols(final ilog.concert.IloNumVar[] var, final int[][] indices, final double[][] values)
public int addCols(final ilog.concert.IloNumVar[] var)
public int addCols(final ilog.concert.IloNumVar[] var, final int start, final int num)
'''
pass
def removeColumn():
'''public void removeColumn(final int ind)
'''
pass
def removeCols():
'''public void removeCols(final int begin, final int num)
public void removeCols(final int[] ind)
public void removeCols(final int[] ind, final int start, final int num)
'''
pass
def clear():
'''public void clear()
'''
pass
def setNZ():
'''public void setNZ(final int rowind, final int colind, final double val)
'''
pass
def setNZs():
'''public void setNZs(final int[] rowind, final int[] colind, final double[] val)
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String arg0)
'''
pass
def needCopy():
'''public void needCopy(final IloCopyManager.Check check)
'''
pass
def makeCopy():
'''public IloCopyable makeCopy(final IloCopyManager copy)
'''
pass
def getCopy():
'''public IloCopyable getCopy(final IloCopyable arg0)
'''
pass
def makeColumnArray():
'''public IloColumnArray makeColumnArray(final int num, final int[][] ind, final double[][] val)
'''
pass
def install():
'''public void install(final ilog.concert.IloNumVar[] var)
'''
pass
def getSize():
'''public int getSize()
'''
pass
