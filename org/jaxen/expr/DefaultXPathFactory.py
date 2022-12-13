def createXPath():
    '''public XPathExpr createXPath(final Expr rootExpr)
    '''
def createPathExpr():
    '''public PathExpr createPathExpr(final FilterExpr filterExpr, final LocationPath locationPath)
    '''
def createRelativeLocationPath():
    '''public LocationPath createRelativeLocationPath()
    '''
def createAbsoluteLocationPath():
    '''public LocationPath createAbsoluteLocationPath()
    '''
def createOrExpr():
    '''public BinaryExpr createOrExpr(final Expr lhs, final Expr rhs)
    '''
def createAndExpr():
    '''public BinaryExpr createAndExpr(final Expr lhs, final Expr rhs)
    '''
def createEqualityExpr():
    '''public BinaryExpr createEqualityExpr(final Expr lhs, final Expr rhs, final int equalityOperator)
    '''
def createRelationalExpr():
    '''public BinaryExpr createRelationalExpr(final Expr lhs, final Expr rhs, final int relationalOperator)
    '''
def createAdditiveExpr():
    '''public BinaryExpr createAdditiveExpr(final Expr lhs, final Expr rhs, final int additiveOperator)
    '''
def createMultiplicativeExpr():
    '''public BinaryExpr createMultiplicativeExpr(final Expr lhs, final Expr rhs, final int multiplicativeOperator)
    '''
def createUnaryExpr():
    '''public Expr createUnaryExpr(final Expr expr, final int unaryOperator)
    '''
def createUnionExpr():
    '''public UnionExpr createUnionExpr(final Expr lhs, final Expr rhs)
    '''
def createFilterExpr():
    '''public FilterExpr createFilterExpr(final Expr expr)
    '''
def createFunctionCallExpr():
    '''public FunctionCallExpr createFunctionCallExpr(final String prefix, final String functionName)
    '''
def createNumberExpr():
    '''public NumberExpr createNumberExpr(final int number)
    public NumberExpr createNumberExpr(final double number)
    '''
def createLiteralExpr():
    '''public LiteralExpr createLiteralExpr(final String literal)
    '''
def createVariableReferenceExpr():
    '''public VariableReferenceExpr createVariableReferenceExpr(final String prefix, final String variable)
    '''
def createNameStep():
    '''public Step createNameStep(final int axis, final String prefix, final String localName)
    '''
def createTextNodeStep():
    '''public Step createTextNodeStep(final int axis)
    '''
def createCommentNodeStep():
    '''public Step createCommentNodeStep(final int axis)
    '''
def createAllNodeStep():
    '''public Step createAllNodeStep(final int axis)
    '''
def createProcessingInstructionNodeStep():
    '''public Step createProcessingInstructionNodeStep(final int axis, final String piName)
    '''
def createPredicate():
    '''public Predicate createPredicate(final Expr predicateExpr)
    '''
def createPredicateSet():
    '''public PredicateSet createPredicateSet()
    '''
