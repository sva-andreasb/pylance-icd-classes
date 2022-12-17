def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final PDQConnection pdqConnection_, final String s)\n
    prepareStatement(final PDQConnection pdqConnection, final String s, final String[] array)\n
    prepareStatement(final PDQConnection pdqConnection, final String s, final int n)\n
    prepareStatement(final PDQConnection pdqConnection, final String s, final int[] array)\n
    prepareStatement(final PDQConnection pdqConnection_, final String s, final int n, final int n2)\n
    prepareStatement(final PDQConnection pdqConnection_, final String s, final int n, final int n2, final int n3)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final PDQConnection pdqConnection_, final String s)\n
    prepareCall(final PDQConnection pdqConnection_, final String s, final int n, final int n2)\n
    prepareCall(final PDQConnection pdqConnection_, final String s, final int n, final int n2, final int n3)\n
    '''
def clearBatch():
    '''returns None\n\n
    clearBatch(final PDQConnection pdqConnection_, final Statement statement, final PreparedStatement preparedStatement, final CallableStatement callableStatement)\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement(final PDQConnection pdqConnection_)\n
    createStatement(final PDQConnection pdqConnection_, final int n, final int n2)\n
    createStatement(final PDQConnection pdqConnection_, final int n, final int n2, final int n3)\n
    '''
