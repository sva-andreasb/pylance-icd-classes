def accessToken():
    '''public static JSONObject accessToken(final HttpClient client, final CloudEnv env, final String authCode)
    '''
def me():
    '''public static JSONObject me(final HttpClient client, final CloudEnv env)
    '''
def uploadDatasetPublicAPI():
    '''public static String uploadDatasetPublicAPI(final HttpClient client, final CloudEnv env, String datasetID, final File file, final String datasetName, final UploadProgressIndicator uploadIndicator)
    '''
def uploadDatasetPublicAPIUsingSegments():
    '''public static String uploadDatasetPublicAPIUsingSegments(final HttpClient client, final CloudEnv env, String datasetID, final File file, final String datasetName)
    '''
def deleteDatasetPublicApi():
    '''public static boolean deleteDatasetPublicApi(final HttpClient httpClient, final CloudEnv env, final String id)
    '''
def getDatasetCSVPublicApi():
    '''public static boolean getDatasetCSVPublicApi(final HttpClient httpClient, final CloudEnv env, final String id)
    '''
def getDatasetsPublicApi():
    '''public static boolean getDatasetsPublicApi(final HttpClient httpClient, final CloudEnv env)
    '''
def execute():
    '''public static RESTAPIResponse execute(final HttpClient client, final HttpRequestBase method)
    '''
def dumpErrorFile():
    '''public static void dumpErrorFile(final Exception ex, final HttpRequestBase req, final RESTAPIResponse resp)
    '''
