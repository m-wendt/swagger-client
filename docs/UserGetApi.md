# swagger_client.UserGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_access_code_validate_access_code**](UserGetApi.md#user_access_code_validate_access_code) | **GET** /v3/user/accesscode/verification | Validates the AccessCode
[**user_get**](UserGetApi.md#user_get) | **GET** /v3/user | Endpoint for getting the data of the requesting user.


# **user_access_code_validate_access_code**
> user_access_code_validate_access_code(accesscode=accesscode)

Validates the AccessCode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UserGetApi(swagger_client.ApiClient(configuration))
accesscode = 'accesscode_example' # str |  (optional)

try:
    # Validates the AccessCode
    api_instance.user_access_code_validate_access_code(accesscode=accesscode)
except ApiException as e:
    print("Exception when calling UserGetApi->user_access_code_validate_access_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accesscode** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> SaveTVWebApiResponseModelsUser user_get(fields=fields)

Endpoint for getting the data of the requesting user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UserGetApi(swagger_client.ApiClient(configuration))
fields = ['catchall.haspermission, contract.hasxlpackage, contract.hasxxlpackage, contract.iscancelled, contract.islocked, contract.isrunning, contract.packagename, erotic.isenabled, fullname, guard.isenabled, id, livestreaming.isenabled, playlists.allowed, recordbuffer.followuptime, recordbuffer.leadtime, recordformat.id, recordformat.name, retentiontime.daysdivx, retentiontime.daysh264hd, retentiontime.daysh264mobile, retentiontime.daysh264sd, retentiontime.hasextendedretentiontimepermission'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    catchall.haspermission,    contract.hasxlpackage,    contract.hasxxlpackage,    contract.iscancelled,    contract.islocked,    contract.isrunning,    contract.packagename,    erotic.isenabled,    fullname,    guard.isenabled,    id,    livestreaming.isenabled,    playlists.allowed,    recordbuffer.followuptime,    recordbuffer.leadtime,    recordformat.id,    recordformat.name,    retentiontime.daysdivx,    retentiontime.daysh264hd,    retentiontime.daysh264mobile,    retentiontime.daysh264sd,    retentiontime.hasextendedretentiontimepermission (optional) (default to catchall.haspermission, contract.hasxlpackage, contract.hasxxlpackage, contract.iscancelled, contract.islocked, contract.isrunning, contract.packagename, erotic.isenabled, fullname, guard.isenabled, id, livestreaming.isenabled, playlists.allowed, recordbuffer.followuptime, recordbuffer.leadtime, recordformat.id, recordformat.name, retentiontime.daysdivx, retentiontime.daysh264hd, retentiontime.daysh264mobile, retentiontime.daysh264sd, retentiontime.hasextendedretentiontimepermission)

try:
    # Endpoint for getting the data of the requesting user.
    api_response = api_instance.user_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGetApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    catchall.haspermission,    contract.hasxlpackage,    contract.hasxxlpackage,    contract.iscancelled,    contract.islocked,    contract.isrunning,    contract.packagename,    erotic.isenabled,    fullname,    guard.isenabled,    id,    livestreaming.isenabled,    playlists.allowed,    recordbuffer.followuptime,    recordbuffer.leadtime,    recordformat.id,    recordformat.name,    retentiontime.daysdivx,    retentiontime.daysh264hd,    retentiontime.daysh264mobile,    retentiontime.daysh264sd,    retentiontime.hasextendedretentiontimepermission | [optional] [default to catchall.haspermission, contract.hasxlpackage, contract.hasxxlpackage, contract.iscancelled, contract.islocked, contract.isrunning, contract.packagename, erotic.isenabled, fullname, guard.isenabled, id, livestreaming.isenabled, playlists.allowed, recordbuffer.followuptime, recordbuffer.leadtime, recordformat.id, recordformat.name, retentiontime.daysdivx, retentiontime.daysh264hd, retentiontime.daysh264mobile, retentiontime.daysh264sd, retentiontime.hasextendedretentiontimepermission]

### Return type

[**SaveTVWebApiResponseModelsUser**](SaveTVWebApiResponseModelsUser.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

