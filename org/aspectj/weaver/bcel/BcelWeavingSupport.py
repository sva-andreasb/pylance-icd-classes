def createAdviceMunger():
    '''returns Advice\n\n
    createAdviceMunger(final AjAttribute.AdviceAttribute attribute, final Pointcut pointcut, final Member signature, final ResolvedType concreteAspect)\n
    '''
def makeCflowStackFieldAdder():
    '''returns ConcreteTypeMunger\n\n
    makeCflowStackFieldAdder(final ResolvedMember cflowField)\n
    '''
def makeCflowCounterFieldAdder():
    '''returns ConcreteTypeMunger\n\n
    makeCflowCounterFieldAdder(final ResolvedMember cflowField)\n
    '''
def makePerClauseAspect():
    '''returns ConcreteTypeMunger\n\n
    makePerClauseAspect(final ResolvedType aspect, final PerClause.Kind kind)\n
    '''
def makeCflowAccessVar():
    '''returns Var\n\n
    makeCflowAccessVar(final ResolvedType formalType, final Member cflowField, final int arrayIndex)\n
    '''
def concreteTypeMunger():
    '''returns ConcreteTypeMunger\n\n
    concreteTypeMunger(final ResolvedTypeMunger munger, final ResolvedType aspectType)\n
    '''
def createAccessForInlineMunger():
    '''returns ConcreteTypeMunger\n\n
    createAccessForInlineMunger(final ResolvedType aspect)\n
    '''
