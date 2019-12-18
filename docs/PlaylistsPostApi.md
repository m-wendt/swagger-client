# swagger_client.PlaylistsPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlists_follow_post**](PlaylistsPostApi.md#playlists_follow_post) | **POST** /v3/playlists/{id}/follow | Add the playlist of another account to the own saved (followed) playlists.
[**playlists_follow_post_0**](PlaylistsPostApi.md#playlists_follow_post_0) | **POST** /v3/playlists/follow | Adds the playlists of another accounts to the own saved (followed) playlists.
[**playlists_items_post_item**](PlaylistsPostApi.md#playlists_items_post_item) | **POST** /v3/playlists/{id}/items/{telecastid} | Appends the given telecast to the playlist.
[**playlists_items_post_item_0**](PlaylistsPostApi.md#playlists_items_post_item_0) | **POST** /v3/playlists/watch-later/items/{telecastid} | Appends the given telecast to the default playlist \&quot;Sp�ter ansehen\&quot;.
[**playlists_items_post_items**](PlaylistsPostApi.md#playlists_items_post_items) | **POST** /v3/playlists/{id}/items | Appends the given telecasts to the playlist.
[**playlists_items_post_items_0**](PlaylistsPostApi.md#playlists_items_post_items_0) | **POST** /v3/playlists/watch-later/items | Appends the given telecasts to the default playlist \&quot;Sp�ter ansehen\&quot;.
[**playlists_items_post_position**](PlaylistsPostApi.md#playlists_items_post_position) | **POST** /v3/playlists/{id}/items/{telecastid}/positions/{position} | Sets the given telecast at the given index in the playlist.
[**playlists_items_post_positions**](PlaylistsPostApi.md#playlists_items_post_positions) | **POST** /v3/playlists/{id}/items/positions | Sets the positions off all playlist items.
[**playlists_items_view_item**](PlaylistsPostApi.md#playlists_items_view_item) | **POST** /v3/playlists/{id}/items/{telecastid}/view | Sets the given telecast of the given the playlist as last viewed. This telecast will be used as start video when the playlist is resumed.
[**playlists_post**](PlaylistsPostApi.md#playlists_post) | **POST** /v3/playlists | Creates a new  playlist.
[**playlists_post_0**](PlaylistsPostApi.md#playlists_post_0) | **POST** /v3/playlists/{id} | Updates an existing playlist.


# **playlists_follow_post**
> playlists_follow_post(id)

Add the playlist of another account to the own saved (followed) playlists.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.

try:
    # Add the playlist of another account to the own saved (followed) playlists.
    api_instance.playlists_follow_post(id)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_follow_post: %s\n" % e)
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

# **playlists_follow_post_0**
> playlists_follow_post_0(playlist_id_list)

Adds the playlists of another accounts to the own saved (followed) playlists.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
playlist_id_list = swagger_client.SaveTVWebApiRequestModelsPlaylistIdList() # SaveTVWebApiRequestModelsPlaylistIdList | The playlist identifier list.

try:
    # Adds the playlists of another accounts to the own saved (followed) playlists.
    api_instance.playlists_follow_post_0(playlist_id_list)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_follow_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id_list** | [**SaveTVWebApiRequestModelsPlaylistIdList**](SaveTVWebApiRequestModelsPlaylistIdList.md)| The playlist identifier list. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_post_item**
> SaveTVWebApiResponseModelsPlaylistItemOperation playlists_items_post_item(id, telecast_id)

Appends the given telecast to the playlist.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
telecast_id = 56 # int | The telecast identifier.

try:
    # Appends the given telecast to the playlist.
    api_response = api_instance.playlists_items_post_item(id, telecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_post_item: %s\n" % e)
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

# **playlists_items_post_item_0**
> SaveTVWebApiResponseModelsPlaylistItemOperation playlists_items_post_item_0(telecast_id)

Appends the given telecast to the default playlist \"Sp�ter ansehen\".

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
telecast_id = 56 # int | The identifier.

try:
    # Appends the given telecast to the default playlist \"Sp�ter ansehen\".
    api_response = api_instance.playlists_items_post_item_0(telecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_post_item_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecast_id** | **int**| The identifier. | 

### Return type

[**SaveTVWebApiResponseModelsPlaylistItemOperation**](SaveTVWebApiResponseModelsPlaylistItemOperation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_post_items**
> playlists_items_post_items(id, telecast_id_list)

Appends the given telecasts to the playlist.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
telecast_id_list = swagger_client.SaveTVWebApiRequestModelsTelecastIdList() # SaveTVWebApiRequestModelsTelecastIdList | The new playlist item.

try:
    # Appends the given telecasts to the playlist.
    api_instance.playlists_items_post_items(id, telecast_id_list)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_post_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 
 **telecast_id_list** | [**SaveTVWebApiRequestModelsTelecastIdList**](SaveTVWebApiRequestModelsTelecastIdList.md)| The new playlist item. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_post_items_0**
> list[SaveTVWebApiResponseModelsPlaylistItemOperation] playlists_items_post_items_0(telecast_id_list)

Appends the given telecasts to the default playlist \"Sp�ter ansehen\".

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
telecast_id_list = swagger_client.SaveTVWebApiRequestModelsTelecastIdList() # SaveTVWebApiRequestModelsTelecastIdList | The new playlist item.

try:
    # Appends the given telecasts to the default playlist \"Sp�ter ansehen\".
    api_response = api_instance.playlists_items_post_items_0(telecast_id_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_post_items_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecast_id_list** | [**SaveTVWebApiRequestModelsTelecastIdList**](SaveTVWebApiRequestModelsTelecastIdList.md)| The new playlist item. | 

### Return type

[**list[SaveTVWebApiResponseModelsPlaylistItemOperation]**](SaveTVWebApiResponseModelsPlaylistItemOperation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_post_position**
> playlists_items_post_position(id, position, telecast_id)

Sets the given telecast at the given index in the playlist.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
position = 56 # int | The target position.
telecast_id = 56 # int | The telecast identifier.

try:
    # Sets the given telecast at the given index in the playlist.
    api_instance.playlists_items_post_position(id, position, telecast_id)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_post_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 
 **position** | **int**| The target position. | 
 **telecast_id** | **int**| The telecast identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_post_positions**
> playlists_items_post_positions(id, telecast_id_list)

Sets the positions off all playlist items.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier.
telecast_id_list = swagger_client.SaveTVWebApiRequestModelsTelecastIdList() # SaveTVWebApiRequestModelsTelecastIdList | The telecast identifier list.

try:
    # Sets the positions off all playlist items.
    api_instance.playlists_items_post_positions(id, telecast_id_list)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_post_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier. | 
 **telecast_id_list** | [**SaveTVWebApiRequestModelsTelecastIdList**](SaveTVWebApiRequestModelsTelecastIdList.md)| The telecast identifier list. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_items_view_item**
> SaveTVWebApiResponseModelsPlaylistItemOperation playlists_items_view_item(id, telecast_id)

Sets the given telecast of the given the playlist as last viewed. This telecast will be used as start video when the playlist is resumed.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
telecast_id = 56 # int | The telecast identifier.

try:
    # Sets the given telecast of the given the playlist as last viewed. This telecast will be used as start video when the playlist is resumed.
    api_response = api_instance.playlists_items_view_item(id, telecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_items_view_item: %s\n" % e)
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

# **playlists_post**
> SaveTVWebApiResponseModelsPlaylist playlists_post(playlist)

Creates a new  playlist.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
playlist = swagger_client.SaveTVWebApiRequestModelsPlaylist() # SaveTVWebApiRequestModelsPlaylist | The data for the new playlist.

try:
    # Creates a new  playlist.
    api_response = api_instance.playlists_post(playlist)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist** | [**SaveTVWebApiRequestModelsPlaylist**](SaveTVWebApiRequestModelsPlaylist.md)| The data for the new playlist. | 

### Return type

[**SaveTVWebApiResponseModelsPlaylist**](SaveTVWebApiResponseModelsPlaylist.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_post_0**
> SaveTVWebApiResponseModelsPlaylist playlists_post_0(id, playlist)

Updates an existing playlist.

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
api_instance = swagger_client.PlaylistsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The playlist identifier.
playlist = swagger_client.SaveTVWebApiRequestModelsPlaylist() # SaveTVWebApiRequestModelsPlaylist | The new data for the existing playlist.

try:
    # Updates an existing playlist.
    api_response = api_instance.playlists_post_0(id, playlist)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsPostApi->playlists_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The playlist identifier. | 
 **playlist** | [**SaveTVWebApiRequestModelsPlaylist**](SaveTVWebApiRequestModelsPlaylist.md)| The new data for the existing playlist. | 

### Return type

[**SaveTVWebApiResponseModelsPlaylist**](SaveTVWebApiResponseModelsPlaylist.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

