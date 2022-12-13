def solve():
'''public static double solve(final UnivariateFunction function, final double x0, final double x1)
public static double solve(final UnivariateFunction function, final double x0, final double x1, final double absoluteAccuracy)
'''
pass
def forceSide():
'''public static double forceSide(final int maxEval, final UnivariateFunction f, final BracketedUnivariateSolver<UnivariateFunction> bracketing, final double baseRoot, final double min, final double max, final AllowedSolution allowedSolution)
'''
pass
def bracket():
'''public static double[] bracket(final UnivariateFunction function, final double initial, final double lowerBound, final double upperBound)
public static double[] bracket(final UnivariateFunction function, final double initial, final double lowerBound, final double upperBound, final int maximumIterations)
public static double[] bracket(final UnivariateFunction function, final double initial, final double lowerBound, final double upperBound, final double q, final double r, final int maximumIterations)
'''
pass
def midpoint():
'''public static double midpoint(final double a, final double b)
'''
pass
def isBracketing():
'''public static boolean isBracketing(final UnivariateFunction function, final double lower, final double upper)
'''
pass
def isSequence():
'''public static boolean isSequence(final double start, final double mid, final double end)
'''
pass
def verifyInterval():
'''public static void verifyInterval(final double lower, final double upper)
'''
pass
def verifySequence():
'''public static void verifySequence(final double lower, final double initial, final double upper)
'''
pass
def verifyBracketing():
'''public static void verifyBracketing(final UnivariateFunction function, final double lower, final double upper)
'''
pass
