def compose():
    '''    public static UnivariateFunction compose(final UnivariateFunction... f)
    public static UnivariateDifferentiableFunction compose(final UnivariateDifferentiableFunction... f)
    public static DifferentiableUnivariateFunction compose(final DifferentiableUnivariateFunction... f)
    '''
def value():
    '''    public double value(final double x)
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
def derivative():
    '''    public UnivariateFunction derivative()
    public UnivariateFunction derivative()
    public UnivariateFunction derivative()
    public UnivariateFunction derivative()
    '''
def add():
    '''    public static UnivariateFunction add(final UnivariateFunction... f)
    public static UnivariateDifferentiableFunction add(final UnivariateDifferentiableFunction... f)
    public static DifferentiableUnivariateFunction add(final DifferentiableUnivariateFunction... f)
    '''
def multiply():
    '''    public static UnivariateFunction multiply(final UnivariateFunction... f)
    public static UnivariateDifferentiableFunction multiply(final UnivariateDifferentiableFunction... f)
    public static DifferentiableUnivariateFunction multiply(final DifferentiableUnivariateFunction... f)
    '''
def combine():
    '''    public static UnivariateFunction combine(final BivariateFunction combiner, final UnivariateFunction f, final UnivariateFunction g)
    '''
def collector():
    '''    public static MultivariateFunction collector(final BivariateFunction combiner, final UnivariateFunction f, final double initialValue)
    public static MultivariateFunction collector(final BivariateFunction combiner, final double initialValue)
    '''
def fix1stArgument():
    '''    public static UnivariateFunction fix1stArgument(final BivariateFunction f, final double fixed)
    '''
def fix2ndArgument():
    '''    public static UnivariateFunction fix2ndArgument(final BivariateFunction f, final double fixed)
    '''
def sample():
    '''    public static double[] sample(final UnivariateFunction f, final double min, final double max, final int n)
    '''
def toDifferentiableUnivariateFunction():
    '''    public static DifferentiableUnivariateFunction toDifferentiableUnivariateFunction(final UnivariateDifferentiableFunction f)
    '''
def toUnivariateDifferential():
    '''    public static UnivariateDifferentiableFunction toUnivariateDifferential(final DifferentiableUnivariateFunction f)
    '''
def toDifferentiableMultivariateFunction():
    '''    public static DifferentiableMultivariateFunction toDifferentiableMultivariateFunction(final MultivariateDifferentiableFunction f)
    '''
def partialDerivative():
    '''    public MultivariateFunction partialDerivative(final int k)
    '''
def gradient():
    '''    public MultivariateVectorFunction gradient()
    '''
def toMultivariateDifferentiableFunction():
    '''    public static MultivariateDifferentiableFunction toMultivariateDifferentiableFunction(final DifferentiableMultivariateFunction f)
    '''
def toDifferentiableMultivariateVectorFunction():
    '''    public static DifferentiableMultivariateVectorFunction toDifferentiableMultivariateVectorFunction(final MultivariateDifferentiableVectorFunction f)
    '''
def jacobian():
    '''    public MultivariateMatrixFunction jacobian()
    '''
def toMultivariateDifferentiableVectorFunction():
    '''    public static MultivariateDifferentiableVectorFunction toMultivariateDifferentiableVectorFunction(final DifferentiableMultivariateVectorFunction f)
    '''
