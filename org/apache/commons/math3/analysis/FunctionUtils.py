def compose():
'''public static UnivariateFunction compose(final UnivariateFunction... f)
public static UnivariateDifferentiableFunction compose(final UnivariateDifferentiableFunction... f)
public static DifferentiableUnivariateFunction compose(final DifferentiableUnivariateFunction... f)
'''
pass
def value():
'''public double value(final double x)
public double value(final double t)
public DerivativeStructure value(final DerivativeStructure t)
public double value(final double x)
public double value(final double x)
public double value(final double x)
public double value(final double t)
public DerivativeStructure value(final DerivativeStructure t)
public double value(final double x)
public double value(final double x)
public double value(final double x)
public double value(final double t)
public DerivativeStructure value(final DerivativeStructure t)
public double value(final double x)
public double value(final double x)
public double value(final double x)
public double value(final double[] point)
public double value(final double x)
public double value(final double x)
public double value(final double x)
public double value(final double x)
public double value(final double x)
public DerivativeStructure value(final DerivativeStructure t)
public double value(final double[] x)
public double value(final double[] x)
public double[] value(final double[] x)
public double value(final double[] x)
public DerivativeStructure value(final DerivativeStructure[] t)
public double[] value(final double[] x)
public double[][] value(final double[] x)
public double[] value(final double[] x)
public DerivativeStructure[] value(final DerivativeStructure[] t)
'''
pass
def derivative():
'''public UnivariateFunction derivative()
public UnivariateFunction derivative()
public UnivariateFunction derivative()
public UnivariateFunction derivative()
'''
pass
def add():
'''public static UnivariateFunction add(final UnivariateFunction... f)
public static UnivariateDifferentiableFunction add(final UnivariateDifferentiableFunction... f)
public static DifferentiableUnivariateFunction add(final DifferentiableUnivariateFunction... f)
'''
pass
def multiply():
'''public static UnivariateFunction multiply(final UnivariateFunction... f)
public static UnivariateDifferentiableFunction multiply(final UnivariateDifferentiableFunction... f)
public static DifferentiableUnivariateFunction multiply(final DifferentiableUnivariateFunction... f)
'''
pass
def combine():
'''public static UnivariateFunction combine(final BivariateFunction combiner, final UnivariateFunction f, final UnivariateFunction g)
'''
pass
def collector():
'''public static MultivariateFunction collector(final BivariateFunction combiner, final UnivariateFunction f, final double initialValue)
public static MultivariateFunction collector(final BivariateFunction combiner, final double initialValue)
'''
pass
def fix1stArgument():
'''public static UnivariateFunction fix1stArgument(final BivariateFunction f, final double fixed)
'''
pass
def fix2ndArgument():
'''public static UnivariateFunction fix2ndArgument(final BivariateFunction f, final double fixed)
'''
pass
def sample():
'''public static double[] sample(final UnivariateFunction f, final double min, final double max, final int n)
'''
pass
def toDifferentiableUnivariateFunction():
'''public static DifferentiableUnivariateFunction toDifferentiableUnivariateFunction(final UnivariateDifferentiableFunction f)
'''
pass
def toUnivariateDifferential():
'''public static UnivariateDifferentiableFunction toUnivariateDifferential(final DifferentiableUnivariateFunction f)
'''
pass
def toDifferentiableMultivariateFunction():
'''public static DifferentiableMultivariateFunction toDifferentiableMultivariateFunction(final MultivariateDifferentiableFunction f)
'''
pass
def partialDerivative():
'''public MultivariateFunction partialDerivative(final int k)
'''
pass
def gradient():
'''public MultivariateVectorFunction gradient()
'''
pass
def toMultivariateDifferentiableFunction():
'''public static MultivariateDifferentiableFunction toMultivariateDifferentiableFunction(final DifferentiableMultivariateFunction f)
'''
pass
def toDifferentiableMultivariateVectorFunction():
'''public static DifferentiableMultivariateVectorFunction toDifferentiableMultivariateVectorFunction(final MultivariateDifferentiableVectorFunction f)
'''
pass
def jacobian():
'''public MultivariateMatrixFunction jacobian()
'''
pass
def toMultivariateDifferentiableVectorFunction():
'''public static MultivariateDifferentiableVectorFunction toMultivariateDifferentiableVectorFunction(final DifferentiableMultivariateVectorFunction f)
'''
pass
