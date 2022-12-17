COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloOplRequirementFactoryImpl\n\n
    (final IloCplexSharedDefs defs, final IloCplexController controller)\n
    '''
def forallRangeRequirement():
    '''returns IloForAllRangeRequirement\n\n
    forallRangeRequirement(final String name, final IloForAllRange range, final Object explanation)\n
    '''
def multiForallRangesRequirement():
    '''returns IloMultipleForAllRangesRequirement\n\n
    multiForallRangesRequirement(final String name, final IloForAllRange[] ranges, final Object explanation)\n
    '''
def ctRequirement():
    '''returns IloConstraintRequirement\n\n
    ctRequirement(final String name, final IloConstraint ct, final Object explanation)\n
    '''
def decisionVariable():
    '''returns IloCplexDecisionVariable\n\n
    decisionVariable(final String name, final IloNumExpr expr, final Object explanation)\n
    '''
def decisionValue():
    '''returns IloCplexEvaluatedDecisionVariable\n\n
    decisionValue(final String name, final double value, final Object explanation)\n
    '''
