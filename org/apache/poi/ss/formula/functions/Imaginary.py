GROUP1_REAL_SIGN_REGEX = "String  \"([+-]?)\""
GROUP2_REAL_INTEGER_OR_DOUBLE_REGEX = "String  \"([0-9]+\\.[0-9]+|[0-9]*)\""
GROUP3_IMAGINARY_SIGN_REGEX = "String  \"([+-]?)\""
GROUP4_IMAGINARY_INTEGER_OR_DOUBLE_REGEX = "String  \"([0-9]+\\.[0-9]+|[0-9]*)\""
GROUP5_IMAGINARY_GROUP_REGEX = "String  \"([ij]?)\""
GROUP1_REAL_SIGN = "int  1"
GROUP2_IMAGINARY_INTEGER_OR_DOUBLE = "int  2"
GROUP3_IMAGINARY_SIGN = "int  3"
GROUP4_IMAGINARY_INTEGER_OR_DOUBLE = "int  4"
def evaluate():
    '''returns ValueEval\n\n
    evaluate(final int srcRowIndex, final int srcColumnIndex, final ValueEval inumberVE)\n
    evaluate(final ValueEval[] args, final OperationEvaluationContext ec)\n
    '''
