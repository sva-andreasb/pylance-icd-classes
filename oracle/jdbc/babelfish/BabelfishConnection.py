def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String s)\n
    prepareStatement(final String s, final int n)\n
    prepareStatement(final String s, final int[] array)\n
    prepareStatement(final String s, final String[] array)\n
    prepareStatement(final String s, final int n, final int n2)\n
    prepareStatement(final String s, final int n, final int n2, final int n3)\n
    prepareStatement(final String s, final boolean b)\n
    prepareStatement(final String s, final int n, final boolean b)\n
    prepareStatement(final String s, final int[] array, final boolean b)\n
    prepareStatement(final String s, final String[] array, final boolean b)\n
    prepareStatement(final String s, final int n, final int n2, final boolean b)\n
    prepareStatement(final String s, final int n, final int n2, final int n3, final boolean b)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final String s)\n
    prepareCall(final String s, final int n, final int n2)\n
    prepareCall(final String s, final int n, final int n2, final int n3)\n
    prepareCall(final String s, final boolean b)\n
    prepareCall(final String s, final int n, final int n2, final boolean b)\n
    prepareCall(final String s, final int n, final int n2, final int n3, final boolean b)\n
    '''
def nativeSQL():
    '''returns String\n\n
    nativeSQL(final String s)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement()\n
    createStatement(final boolean b)\n
    createStatement(final int n, final int n2)\n
    createStatement(final int n, final int n2, final boolean b)\n
    createStatement(final int n, final int n2, final int n3)\n
    createStatement(final int n, final int n2, final int n3, final boolean b)\n
    '''
