def createXPath():
    '''returns XPathExpr\n\n
    createXPath(final Expr rootExpr)\n
    '''
def createPathExpr():
    '''returns PathExpr\n\n
    createPathExpr(final FilterExpr filterExpr, final LocationPath locationPath)\n
    '''
def createRelativeLocationPath():
    '''returns LocationPath\n\n
    createRelativeLocationPath()\n
    '''
def createAbsoluteLocationPath():
    '''returns LocationPath\n\n
    createAbsoluteLocationPath()\n
    '''
def createOrExpr():
    '''returns BinaryExpr\n\n
    createOrExpr(final Expr lhs, final Expr rhs)\n
    '''
def createAndExpr():
    '''returns BinaryExpr\n\n
    createAndExpr(final Expr lhs, final Expr rhs)\n
    '''
def createEqualityExpr():
    '''returns BinaryExpr\n\n
    createEqualityExpr(final Expr lhs, final Expr rhs, final int equalityOperator)\n
    '''
def createRelationalExpr():
    '''returns BinaryExpr\n\n
    createRelationalExpr(final Expr lhs, final Expr rhs, final int relationalOperator)\n
    '''
def createAdditiveExpr():
    '''returns BinaryExpr\n\n
    createAdditiveExpr(final Expr lhs, final Expr rhs, final int additiveOperator)\n
    '''
def createMultiplicativeExpr():
    '''returns BinaryExpr\n\n
    createMultiplicativeExpr(final Expr lhs, final Expr rhs, final int multiplicativeOperator)\n
    '''
def createUnaryExpr():
    '''returns Expr\n\n
    createUnaryExpr(final Expr expr, final int unaryOperator)\n
    '''
def createUnionExpr():
    '''returns UnionExpr\n\n
    createUnionExpr(final Expr lhs, final Expr rhs)\n
    '''
def createFilterExpr():
    '''returns FilterExpr\n\n
    createFilterExpr(final Expr expr)\n
    '''
def createFunctionCallExpr():
    '''returns FunctionCallExpr\n\n
    createFunctionCallExpr(final String prefix, final String functionName)\n
    '''
def createNumberExpr():
    '''returns NumberExpr\n\n
    createNumberExpr(final int number)\n
    createNumberExpr(final double number)\n
    '''
def createLiteralExpr():
    '''returns LiteralExpr\n\n
    createLiteralExpr(final String literal)\n
    '''
def createVariableReferenceExpr():
    '''returns VariableReferenceExpr\n\n
    createVariableReferenceExpr(final String prefix, final String variable)\n
    '''
def createNameStep():
    '''returns Step\n\n
    createNameStep(final int axis, final String prefix, final String localName)\n
    '''
def createTextNodeStep():
    '''returns Step\n\n
    createTextNodeStep(final int axis)\n
    '''
def createCommentNodeStep():
    '''returns Step\n\n
    createCommentNodeStep(final int axis)\n
    '''
def createAllNodeStep():
    '''returns Step\n\n
    createAllNodeStep(final int axis)\n
    '''
def createProcessingInstructionNodeStep():
    '''returns Step\n\n
    createProcessingInstructionNodeStep(final int axis, final String piName)\n
    '''
def createPredicate():
    '''returns Predicate\n\n
    createPredicate(final Expr predicateExpr)\n
    '''
def createPredicateSet():
    '''returns PredicateSet\n\n
    createPredicateSet()\n
    '''
