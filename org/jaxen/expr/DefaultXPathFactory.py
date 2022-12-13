def createXPath():
'''public XPathExpr createXPath(final Expr rootExpr)
'''
pass
def createPathExpr():
'''public PathExpr createPathExpr(final FilterExpr filterExpr, final LocationPath locationPath)
'''
pass
def createRelativeLocationPath():
'''public LocationPath createRelativeLocationPath()
'''
pass
def createAbsoluteLocationPath():
'''public LocationPath createAbsoluteLocationPath()
'''
pass
def createOrExpr():
'''public BinaryExpr createOrExpr(final Expr lhs, final Expr rhs)
'''
pass
def createAndExpr():
'''public BinaryExpr createAndExpr(final Expr lhs, final Expr rhs)
'''
pass
def createEqualityExpr():
'''public BinaryExpr createEqualityExpr(final Expr lhs, final Expr rhs, final int equalityOperator)
'''
pass
def createRelationalExpr():
'''public BinaryExpr createRelationalExpr(final Expr lhs, final Expr rhs, final int relationalOperator)
'''
pass
def createAdditiveExpr():
'''public BinaryExpr createAdditiveExpr(final Expr lhs, final Expr rhs, final int additiveOperator)
'''
pass
def createMultiplicativeExpr():
'''public BinaryExpr createMultiplicativeExpr(final Expr lhs, final Expr rhs, final int multiplicativeOperator)
'''
pass
def createUnaryExpr():
'''public Expr createUnaryExpr(final Expr expr, final int unaryOperator)
'''
pass
def createUnionExpr():
'''public UnionExpr createUnionExpr(final Expr lhs, final Expr rhs)
'''
pass
def createFilterExpr():
'''public FilterExpr createFilterExpr(final Expr expr)
'''
pass
def createFunctionCallExpr():
'''public FunctionCallExpr createFunctionCallExpr(final String prefix, final String functionName)
'''
pass
def createNumberExpr():
'''public NumberExpr createNumberExpr(final int number)
public NumberExpr createNumberExpr(final double number)
'''
pass
def createLiteralExpr():
'''public LiteralExpr createLiteralExpr(final String literal)
'''
pass
def createVariableReferenceExpr():
'''public VariableReferenceExpr createVariableReferenceExpr(final String prefix, final String variable)
'''
pass
def createNameStep():
'''public Step createNameStep(final int axis, final String prefix, final String localName)
'''
pass
def createTextNodeStep():
'''public Step createTextNodeStep(final int axis)
'''
pass
def createCommentNodeStep():
'''public Step createCommentNodeStep(final int axis)
'''
pass
def createAllNodeStep():
'''public Step createAllNodeStep(final int axis)
'''
pass
def createProcessingInstructionNodeStep():
'''public Step createProcessingInstructionNodeStep(final int axis, final String piName)
'''
pass
def createPredicate():
'''public Predicate createPredicate(final Expr predicateExpr)
'''
pass
def createPredicateSet():
'''public PredicateSet createPredicateSet()
'''
pass
