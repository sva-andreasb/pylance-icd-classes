def IloCplex__BranchCallbackI():
    '''public IloCplex__BranchCallbackI(final long cPtr, final boolean cMemoryOwn)
    '''
def getCPtr():
    '''public static long getCPtr(final IloCplex__BranchCallbackI obj)
    '''
def delete():
    '''public void delete()
    '''
def getNbranches():
    '''public int getNbranches()
    '''
def getBranchType():
    '''public BranchType getBranchType()
    '''
def getBranch():
    '''public double getBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final int i)
    '''
def isIntegerFeasible():
    '''public boolean isIntegerFeasible()
    '''
def makeBranch():
    '''public NodeId makeBranch(final int num, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final int num)
    public NodeId makeBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final IloNumVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloNumVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate)
    public NodeId makeBranch(final IloIntVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloIntVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate)
    public NodeId makeBranch(final IloConstraintArray cons, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraintArray cons, final double objestimate)
    public NodeId makeBranch(final IloConstraint con, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraint con, final double objestimate)
    public NodeId makeBranch(final IloConstraintArray cons, final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraintArray cons, final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final IloConstraintArray cons, final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraintArray cons, final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    '''
def prune():
    '''public void prune()
    '''
def mySwigValue():
    '''public int mySwigValue()
    '''
def swigValue():
    '''public final int swigValue()
    '''
def toString():
    '''public String toString()
    '''
def swigToEnum():
    '''public static BranchType swigToEnum(final int swigValue)
    '''
def BranchType():
    '''public BranchType(final String swigName, final int swigValue)
    '''
