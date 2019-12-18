# swagger_client.EroticVideosGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**erotic_videos_download**](EroticVideosGetApi.md#erotic_videos_download) | **GET** /v3/eroticvideos/{id}/downloads/{recordformat} | Requests the download URL for a record.
[**erotic_videos_get**](EroticVideosGetApi.md#erotic_videos_get) | **GET** /v3/eroticvideos | Retrieves all erotic videos.
[**erotic_videos_get_0**](EroticVideosGetApi.md#erotic_videos_get_0) | **GET** /v3/eroticvideos/{id} | Retrieves one erotic video.


# **erotic_videos_download**
> SaveTVWebApiResponseModelsDownload erotic_videos_download(id, record_format)

Requests the download URL for a record.

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
api_instance = swagger_client.EroticVideosGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the telecast.
record_format = 56 # int | The record format used for download.    Values:    4 = Mobile (480x270)    5 = SD (1024x576)    6 = HD (1280x720)    9 = Full-HD (1920x1280)

try:
    # Requests the download URL for a record.
    api_response = api_instance.erotic_videos_download(id, record_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EroticVideosGetApi->erotic_videos_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the telecast. | 
 **record_format** | **int**| The record format used for download.    Values:    4 &#x3D; Mobile (480x270)    5 &#x3D; SD (1024x576)    6 &#x3D; HD (1280x720)    9 &#x3D; Full-HD (1920x1280) | 

### Return type

[**SaveTVWebApiResponseModelsDownload**](SaveTVWebApiResponseModelsDownload.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **erotic_videos_get**
> list[SaveTVWebApiResponseModelsEroticVideo] erotic_videos_get()

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
api_instance = swagger_client.EroticVideosGetApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves all erotic videos.
    api_response = api_instance.erotic_videos_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EroticVideosGetApi->erotic_videos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SaveTVWebApiResponseModelsEroticVideo]**](SaveTVWebApiResponseModelsEroticVideo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **erotic_videos_get_0**
> SaveTVWebApiResponseModelsEroticVideo erotic_videos_get_0(id)

Retrieves one erotic video.

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
api_instance = swagger_client.EroticVideosGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The erotic video identifier.

try:
    # Retrieves one erotic video.
    api_response = api_instance.erotic_videos_get_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EroticVideosGetApi->erotic_videos_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The erotic video identifier. | 

### Return type

[**SaveTVWebApiResponseModelsEroticVideo**](SaveTVWebApiResponseModelsEroticVideo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

