SCOPE_ENVIRONMENT = "int  0"
SCOPE_TEMPLATE = "int  1"
SCOPE_CONFIGURATION = "int  2"
def CustomAttribute():
    '''    public CustomAttribute(final int scope)
    '''
def get():
    '''    public final Object get(final Environment env)
    public final Object get()
    public final Object get(final Template template)
    public final Object get(final Configuration cfg)
    '''
def set():
    '''    public final void set(final Object value, final Environment env)
    public final void set(final Object value)
    public final void set(final Object value, final Template template)
    public final void set(final Object value, final Configuration cfg)
    '''
