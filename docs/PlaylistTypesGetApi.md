# swagger_client.PlaylistTypesGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlist_types_get**](PlaylistTypesGetApi.md#playlist_types_get) | **GET** /v3/playlisttypes | Gets details about the available playlist types.


# **playlist_types_get**
> list[SaveTVWebApiResponseModelsPlaylistType] playlist_types_get()

Gets details about the available playlist types.

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
api_instance = swagger_client.PlaylistTypesGetApi(swagger_client.ApiClient(configuration))

try:
    # Gets details about the available playlist types.
    api_response = api_instance.playlist_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistTypesGetApi->playlist_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SaveTVWebApiResponseModelsPlaylistType]**](SaveTVWebApiResponseModelsPlaylistType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

