# swagger_client.TvStationsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tv_stations_get**](TvStationsGetApi.md#tv_stations_get) | **GET** /v3/tvstations | Retrieves all available TV stations.
[**tv_stations_get_0**](TvStationsGetApi.md#tv_stations_get_0) | **GET** /v3/tvstations/{id} | Retrieves a single TV station with the given identifier.
[**tv_stations_live_stream_live_stream_urls**](TvStationsGetApi.md#tv_stations_live_stream_live_stream_urls) | **GET** /v3/tvstations/{id}/livestream | Returns the live streaming url for the given TV station in all possible formats.


# **tv_stations_get**
> list[SaveTVWebApiResponseModelsTvStation] tv_stations_get(fields=fields, haslivestream=haslivestream, isrecordable=isrecordable, sort=sort)

Retrieves all available TV stations.

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
api_instance = swagger_client.TvStationsGetApi(swagger_client.ApiClient(configuration))
fields = ['homepageurl, id, isrecordable, largelogourl, livestream, name, smalllogourl'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    homepageurl,    id,    isrecordable,    largelogourl,    livestream,    name,    smalllogourl (optional) (default to homepageurl, id, isrecordable, largelogourl, livestream, name, smalllogourl)
haslivestream = true # bool | Select only TV stations that provide / provide not a live stream. (optional)
isrecordable = true # bool | Select only TV station that are / ar not recordable. (optional)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority (optional)

try:
    # Retrieves all available TV stations.
    api_response = api_instance.tv_stations_get(fields=fields, haslivestream=haslivestream, isrecordable=isrecordable, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvStationsGetApi->tv_stations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    homepageurl,    id,    isrecordable,    largelogourl,    livestream,    name,    smalllogourl | [optional] [default to homepageurl, id, isrecordable, largelogourl, livestream, name, smalllogourl]
 **haslivestream** | **bool**| Select only TV stations that provide / provide not a live stream. | [optional] 
 **isrecordable** | **bool**| Select only TV station that are / ar not recordable. | [optional] 
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsTvStation]**](SaveTVWebApiResponseModelsTvStation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_stations_get_0**
> SaveTVWebApiResponseModelsTvStation tv_stations_get_0(id, fields=fields)

Retrieves a single TV station with the given identifier.

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
api_instance = swagger_client.TvStationsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the TV station.
fields = ['homepageurl, id, isrecordable, largelogourl, livestream, name, smalllogourl'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    homepageurl,    id,    isrecordable,    largelogourl,    livestream,    name,    smalllogourl (optional) (default to homepageurl, id, isrecordable, largelogourl, livestream, name, smalllogourl)

try:
    # Retrieves a single TV station with the given identifier.
    api_response = api_instance.tv_stations_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvStationsGetApi->tv_stations_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the TV station. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    homepageurl,    id,    isrecordable,    largelogourl,    livestream,    name,    smalllogourl | [optional] [default to homepageurl, id, isrecordable, largelogourl, livestream, name, smalllogourl]

### Return type

[**SaveTVWebApiResponseModelsTvStation**](SaveTVWebApiResponseModelsTvStation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_stations_live_stream_live_stream_urls**
> SaveTVEpgLiveStreamingLiveStreamUrls tv_stations_live_stream_live_stream_urls(id)

Returns the live streaming url for the given TV station in all possible formats.

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
api_instance = swagger_client.TvStationsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The TV station identifier.

try:
    # Returns the live streaming url for the given TV station in all possible formats.
    api_response = api_instance.tv_stations_live_stream_live_stream_urls(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvStationsGetApi->tv_stations_live_stream_live_stream_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The TV station identifier. | 

### Return type

[**SaveTVEpgLiveStreamingLiveStreamUrls**](SaveTVEpgLiveStreamingLiveStreamUrls.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

