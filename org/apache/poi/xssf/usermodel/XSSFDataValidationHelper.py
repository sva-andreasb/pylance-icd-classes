def ():
    '''returns XSSFDataValidationHelper\n\n
    (final XSSFSheet xssfSheet)\n
    '''
def createDateConstraint():
    '''returns DataValidationConstraint\n\n
    createDateConstraint(final int operatorType, final String formula1, final String formula2, final String dateFormat)\n
    '''
def createDecimalConstraint():
    '''returns DataValidationConstraint\n\n
    createDecimalConstraint(final int operatorType, final String formula1, final String formula2)\n
    '''
def createExplicitListConstraint():
    '''returns DataValidationConstraint\n\n
    createExplicitListConstraint(final String[] listOfValues)\n
    '''
def createFormulaListConstraint():
    '''returns DataValidationConstraint\n\n
    createFormulaListConstraint(final String listFormula)\n
    '''
def createNumericConstraint():
    '''returns DataValidationConstraint\n\n
    createNumericConstraint(final int validationType, final int operatorType, final String formula1, final String formula2)\n
    '''
def createIntegerConstraint():
    '''returns DataValidationConstraint\n\n
    createIntegerConstraint(final int operatorType, final String formula1, final String formula2)\n
    '''
def createTextLengthConstraint():
    '''returns DataValidationConstraint\n\n
    createTextLengthConstraint(final int operatorType, final String formula1, final String formula2)\n
    '''
def createTimeConstraint():
    '''returns DataValidationConstraint\n\n
    createTimeConstraint(final int operatorType, final String formula1, final String formula2)\n
    '''
def createCustomConstraint():
    '''returns DataValidationConstraint\n\n
    createCustomConstraint(final String formula)\n
    '''
def createValidation():
    '''returns DataValidation\n\n
    createValidation(final DataValidationConstraint constraint, final CellRangeAddressList cellRangeAddressList)\n
    '''
