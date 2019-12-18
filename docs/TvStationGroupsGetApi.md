# swagger_client.TvStationGroupsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tv_station_groups_get**](TvStationGroupsGetApi.md#tv_station_groups_get) | **GET** /v3/tvstationgroups | Retrieves all available TV stations groups.
[**tv_station_groups_get_0**](TvStationGroupsGetApi.md#tv_station_groups_get_0) | **GET** /v3/tvstationgroups/{id} | Retrieves a single TV station group with the given identifier.


# **tv_station_groups_get**
> list[SaveTVWebApiResponseModelsTvStationGroup] tv_station_groups_get(fields=fields)

Retrieves all available TV stations groups.

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
api_instance = swagger_client.TvStationGroupsGetApi(swagger_client.ApiClient(configuration))
fields = ['id, name, tvstations.homepageurl, tvstations.id, tvstations.largelogourl, tvstations.name, tvstations.smalllogourl'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    id,    name,    tvstations.homepageurl,    tvstations.id,    tvstations.largelogourl,    tvstations.name,    tvstations.smalllogourl (optional) (default to id, name, tvstations.homepageurl, tvstations.id, tvstations.largelogourl, tvstations.name, tvstations.smalllogourl)

try:
    # Retrieves all available TV stations groups.
    api_response = api_instance.tv_station_groups_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvStationGroupsGetApi->tv_station_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    id,    name,    tvstations.homepageurl,    tvstations.id,    tvstations.largelogourl,    tvstations.name,    tvstations.smalllogourl | [optional] [default to id, name, tvstations.homepageurl, tvstations.id, tvstations.largelogourl, tvstations.name, tvstations.smalllogourl]

### Return type

[**list[SaveTVWebApiResponseModelsTvStationGroup]**](SaveTVWebApiResponseModelsTvStationGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_station_groups_get_0**
> SaveTVWebApiResponseModelsTvStationGroup tv_station_groups_get_0(id, fields=fields)

Retrieves a single TV station group with the given identifier.

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
api_instance = swagger_client.TvStationGroupsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the TV station group.
fields = ['id, name, tvstations.homepageurl, tvstations.id, tvstations.largelogourl, tvstations.name, tvstations.smalllogourl'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    id,    name,    tvstations.homepageurl,    tvstations.id,    tvstations.largelogourl,    tvstations.name,    tvstations.smalllogourl (optional) (default to id, name, tvstations.homepageurl, tvstations.id, tvstations.largelogourl, tvstations.name, tvstations.smalllogourl)

try:
    # Retrieves a single TV station group with the given identifier.
    api_response = api_instance.tv_station_groups_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvStationGroupsGetApi->tv_station_groups_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the TV station group. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    id,    name,    tvstations.homepageurl,    tvstations.id,    tvstations.largelogourl,    tvstations.name,    tvstations.smalllogourl | [optional] [default to id, name, tvstations.homepageurl, tvstations.id, tvstations.largelogourl, tvstations.name, tvstations.smalllogourl]

### Return type

[**SaveTVWebApiResponseModelsTvStationGroup**](SaveTVWebApiResponseModelsTvStationGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

