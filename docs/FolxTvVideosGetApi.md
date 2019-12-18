# swagger_client.FolxTvVideosGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folx_tv_videos_download**](FolxTvVideosGetApi.md#folx_tv_videos_download) | **GET** /v3/folxtvvideos/{id}/downloads/{recordformat} | Downloads the specified identifier.
[**folx_tv_videos_get**](FolxTvVideosGetApi.md#folx_tv_videos_get) | **GET** /v3/folxtvvideos | Retrieves all erotic videos.


# **folx_tv_videos_download**
> SaveTVWebApiResponseModelsDownload folx_tv_videos_download(id, record_format)

Downloads the specified identifier.

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
api_instance = swagger_client.FolxTvVideosGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier.
record_format = 56 # int | The record format used for download.    Values:    4 = Mobile (480x270)    5 = SD (1024x576)    6 = HD (1280x720)    9 = Full-HD (1920x1280)

try:
    # Downloads the specified identifier.
    api_response = api_instance.folx_tv_videos_download(id, record_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolxTvVideosGetApi->folx_tv_videos_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier. | 
 **record_format** | **int**| The record format used for download.    Values:    4 &#x3D; Mobile (480x270)    5 &#x3D; SD (1024x576)    6 &#x3D; HD (1280x720)    9 &#x3D; Full-HD (1920x1280) | 

### Return type

[**SaveTVWebApiResponseModelsDownload**](SaveTVWebApiResponseModelsDownload.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folx_tv_videos_get**
> folx_tv_videos_get()

Retrieves all erotic videos.

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
api_instance = swagger_client.FolxTvVideosGetApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves all erotic videos.
    api_instance.folx_tv_videos_get()
except ApiException as e:
    print("Exception when calling FolxTvVideosGetApi->folx_tv_videos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

