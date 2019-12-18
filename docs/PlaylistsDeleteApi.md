# swagger_client.PlaylistsDeleteApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlists_delete**](PlaylistsDeleteApi.md#playlists_delete) | **DELETE** /v3/playlists | Deletes the playlists specified by the identifiers.
[**playlists_delete_0**](PlaylistsDeleteApi.md#playlists_delete_0) | **DELETE** /v3/playlists/{id} | Deletes the playlist specified by the identifier.
[**playlists_follow_delete**](PlaylistsDeleteApi.md#playlists_follow_delete) | **DELETE** /v3/playlists/{id}/follow | Remove the playlist from the saved (followed) playlists.
[**playlists_follow_delete_0**](PlaylistsDeleteApi.md#playlists_follow_delete_0) | **DELETE** /v3/playlists/follow | Removes the playlists from the saved (followed) playlists.
[**playlists_items_delete_item**](PlaylistsDeleteApi.md#playlists_items_delete_item) | **DELETE** /v3/playlists/{id}/items/{telecastid} | Deletes the given telecast from the playlist.
[**playlists_items_delete_items**](PlaylistsDeleteApi.md#playlists_items_delete_items) | **DELETE** /v3/playlists/{id}/items | Deletes the given telecasts from the playlist.


# **playlists_delete**
> playlists_delete(playlistids=playlistids)

Deletes the playlists specified by the identifiers.

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
api_instance = swagger_client.PlaylistsDeleteApi(swagger_client.ApiClient(configuration))
playlistids = [56] # list[int] | A comma separated list of playlist identifiers. (optional)

try:
    # Deletes the playlists specified by the identifiers.
    api_instance.playlists_delete(playlistids=playlistids)
except ApiException as e:
    print("Exception when calling PlaylistsDeleteApi->playlists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistids** | [**list[int]**](int.md)| A comma separated list of playlist identifiers. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_delete_0**
> playlists_delete_0(id)

Deletes the playlist specified by the identifier.

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
api_instance = swagger_client.PlaylistsDeleteApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.

try:
    # Deletes the playlist specified by the identifier.
    api_instance.playlists_delete_0(id)
except ApiException as e:
    print("Exception when calling PlaylistsDeleteApi->playlists_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_follow_delete**
> playlists_follow_delete(id)

Remove the playlist from the saved (followed) playlists.

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
api_instance = swagger_client.PlaylistsDeleteApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.

try:
    # Remove the playlist from the saved (followed) playlists.
    api_instance.playlists_follow_delete(id)
except ApiException as e:
    print("Exception when calling PlaylistsDeleteApi->playlists_follow_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_follow_delete_0**
> playlists_follow_delete_0(playlistids=playlistids)

Removes the playlists from the saved (followed) playlists.

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
api_instance = swagger_client.PlaylistsDeleteApi(swagger_client.ApiClient(configuration))
playlistids = [56] # list[int] | A comma separated list of playlist identifiers. (optional)

try:
    # Removes the playlists from the saved (followed) playlists.
    api_instance.playlists_follow_delete_0(playlistids=playlistids)
except ApiException as e:
    print("Exception when calling PlaylistsDeleteApi->playlists_follow_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistids** | [**list[int]**](int.md)| A comma separated list of playlist identifiers. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_delete_item**
> SaveTVWebApiResponseModelsPlaylistItemOperation playlists_items_delete_item(id, telecast_id)

Deletes the given telecast from the playlist.

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
api_instance = swagger_client.PlaylistsDeleteApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
telecast_id = 56 # int | The telecast identifier.

try:
    # Deletes the given telecast from the playlist.
    api_response = api_instance.playlists_items_delete_item(id, telecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsDeleteApi->playlists_items_delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 
 **telecast_id** | **int**| The telecast identifier. | 

### Return type

[**SaveTVWebApiResponseModelsPlaylistItemOperation**](SaveTVWebApiResponseModelsPlaylistItemOperation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_delete_items**
> list[SaveTVWebApiResponseModelsPlaylistItemOperation] playlists_items_delete_items(id, telecastids=telecastids)

Deletes the given telecasts from the playlist.

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
api_instance = swagger_client.PlaylistsDeleteApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
telecastids = [56] # list[int] | A comma separated list of telecast identifiers. (optional)

try:
    # Deletes the given telecasts from the playlist.
    api_response = api_instance.playlists_items_delete_items(id, telecastids=telecastids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsDeleteApi->playlists_items_delete_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 
 **telecastids** | [**list[int]**](int.md)| A comma separated list of telecast identifiers. | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsPlaylistItemOperation]**](SaveTVWebApiResponseModelsPlaylistItemOperation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

