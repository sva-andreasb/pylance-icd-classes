def ():
    '''returns PerThisOrTargetPointcutVisitor\n\n
    (final boolean isTarget, final ResolvedType fromAspectType)\n
    '''
def getPerTypePointcut():
    '''returns TypePattern\n\n
    getPerTypePointcut(final Pointcut perClausePointcut)\n
    '''
def visit():
    '''returns Object\n\n
    visit(final WithinPointcut node, final Object data)\n
    visit(final WithincodePointcut node, final Object data)\n
    visit(final WithinAnnotationPointcut node, final Object data)\n
    visit(final WithinCodeAnnotationPointcut node, final Object data)\n
    visit(final KindedPointcut node, final Object data)\n
    visit(final AndPointcut node, final Object data)\n
    visit(final OrPointcut node, final Object data)\n
    visit(final NotPointcut node, final Object data)\n
    visit(final ThisOrTargetAnnotationPointcut node, final Object data)\n
    visit(final ThisOrTargetPointcut node, final Object data)\n
    visit(final ReferencePointcut node, final Object data)\n
    visit(final IfPointcut node, final Object data)\n
    visit(final HandlerPointcut node, final Object data)\n
    visit(final CflowPointcut node, final Object data)\n
    visit(final ConcreteCflowPointcut node, final Object data)\n
    visit(final ArgsPointcut node, final Object data)\n
    visit(final ArgsAnnotationPointcut node, final Object data)\n
    visit(final AnnotationPointcut node, final Object data)\n
    visit(final Pointcut.MatchesNothingPointcut node, final Object data)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
