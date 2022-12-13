def TransformSDB():
    '''public TransformSDB(final SDBRequest request, final QuadBlockCompiler quadBlockCompiler)
    '''
def transform():
    '''public Op transform(final OpBGP opBGP)
    public Op transform(final OpQuadPattern quadPattern)
    public Op transform(final OpJoin opJoin, final Op left, final Op right)
    public Op transform(final OpLeftJoin opJoin, final Op left, final Op right)
    public Op transform(final OpFilter opFilter, final Op op)
    public Op transform(final OpTable opTable)
    public Op transform(final OpDistinct opDistinct, final Op subOp)
    public Op transform(final OpProject opProject, final Op subOp)
    public Op transform(final OpService opService, final Op subOp)
    public Op transform(final OpSlice opSlice, final Op subOp)
    public Op transform(final OpDatasetNames opDatasetNames)
    '''
def sub():
    '''public static Op sub(final Op1 op)
    '''
def isProject():
    '''public static boolean isProject(final Op op)
    '''
def asProject():
    '''public static OpProject asProject(final Op op)
    '''
def isDistinct():
    '''public static boolean isDistinct(final Op op)
    '''
def asDistinct():
    '''public static OpDistinct asDistinct(final Op op)
    '''
def isReduced():
    '''public static boolean isReduced(final Op op)
    '''
def asReduced():
    '''public static OpReduced asReduced(final Op op)
    '''
def isOrder():
    '''public static boolean isOrder(final Op op)
    '''
def asOrder():
    '''public static OpOrder asOrder(final Op op)
    '''
def isSlice():
    '''public static boolean isSlice(final Op op)
    '''
def asSlice():
    '''public static OpSlice asSlice(final Op op)
    '''
