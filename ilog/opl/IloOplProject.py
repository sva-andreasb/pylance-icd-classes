def ():
    '''returns IloOplProject\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final String prjPath)\n
    (final IloEnv env, final istream ins, final String name)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def tuneParam():
    '''returns boolean\n\n
    tuneParam(final IloCplex.ParameterSet fixedSet, final IloCplex.ParameterSet resultSet, final IloStringArray runConfigNames)\n
    tuneParam(final IloCplex.ParameterSet fixedSet, final IloCplex.ParameterSet resultSet, final IloStringArray runConfigNames, final IloOplSettings settings)\n
    tuneParam(final IloCplex__ParameterSet fixedSet, final IloCplex__ParameterSet resultSet, final ilog.opl_core.cppimpl.IloStringArray runConfigNames)\n
    tuneParam(final IloCplex__ParameterSet fixedSet, final IloCplex__ParameterSet resultSet, final ilog.opl_core.cppimpl.IloStringArray runConfigNames, final IloOplSettings settings)\n
    tuneParam(final IloCplex__ParameterSet fixedSet, final IloCplex__ParameterSet resultSet, final ilog.opl_core.cppimpl.IloStringArray runConfigNames, final IloOplSettings settings, final IloOplTuningCallback cb)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def makeRunConfiguration():
    '''returns IloOplRunConfiguration\n\n
    makeRunConfiguration()\n
    makeRunConfiguration(final String name)\n
    '''
