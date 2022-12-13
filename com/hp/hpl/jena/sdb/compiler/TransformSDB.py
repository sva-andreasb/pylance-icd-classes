def TransformSDB():
'''public TransformSDB(final SDBRequest request, final QuadBlockCompiler quadBlockCompiler)
'''
pass
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
pass
def sub():
'''public static Op sub(final Op1 op)
'''
pass
def isProject():
'''public static boolean isProject(final Op op)
'''
pass
def asProject():
'''public static OpProject asProject(final Op op)
'''
pass
def isDistinct():
'''public static boolean isDistinct(final Op op)
'''
pass
def asDistinct():
'''public static OpDistinct asDistinct(final Op op)
'''
pass
def isReduced():
'''public static boolean isReduced(final Op op)
'''
pass
def asReduced():
'''public static OpReduced asReduced(final Op op)
'''
pass
def isOrder():
'''public static boolean isOrder(final Op op)
'''
pass
def asOrder():
'''public static OpOrder asOrder(final Op op)
'''
pass
def isSlice():
'''public static boolean isSlice(final Op op)
'''
pass
def asSlice():
'''public static OpSlice asSlice(final Op op)
'''
pass
