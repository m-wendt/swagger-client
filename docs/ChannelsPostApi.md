# swagger_client.ChannelsPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_post_catch_all_channel**](ChannelsPostApi.md#channels_post_catch_all_channel) | **POST** /v3/channels/catchall | Creates the catch all channels for the requested TV stations or for all TV stations.
[**channels_post_full_text_search_channel**](ChannelsPostApi.md#channels_post_full_text_search_channel) | **POST** /v3/channels/fulltextsearch | Creates a full text search channel.
[**channels_post_star_channel**](ChannelsPostApi.md#channels_post_star_channel) | **POST** /v3/channels/star | Creates a star channel.
[**channels_post_telecast_ids_channel**](ChannelsPostApi.md#channels_post_telecast_ids_channel) | **POST** /v3/channels/telecastids | Creates a channel by various telecast ids.
[**channels_post_title_channel**](ChannelsPostApi.md#channels_post_title_channel) | **POST** /v3/channels/title | Creates a title channel.
[**channels_post_tv_station_channel**](ChannelsPostApi.md#channels_post_tv_station_channel) | **POST** /v3/channels/tvstation | Creates a TV station channel.


# **channels_post_catch_all_channel**
> list[SaveTVWebApiResponseModelsChannel] channels_post_catch_all_channel(catch_all_channel)

Creates the catch all channels for the requested TV stations or for all TV stations.

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
api_instance = swagger_client.ChannelsPostApi(swagger_client.ApiClient(configuration))
catch_all_channel = swagger_client.SaveTVWebApiRequestModelsCatchAllChannel() # SaveTVWebApiRequestModelsCatchAllChannel | The catch all channel.

try:
    # Creates the catch all channels for the requested TV stations or for all TV stations.
    api_response = api_instance.channels_post_catch_all_channel(catch_all_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsPostApi->channels_post_catch_all_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catch_all_channel** | [**SaveTVWebApiRequestModelsCatchAllChannel**](SaveTVWebApiRequestModelsCatchAllChannel.md)| The catch all channel. | 

### Return type

[**list[SaveTVWebApiResponseModelsChannel]**](SaveTVWebApiResponseModelsChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post_full_text_search_channel**
> SaveTVWebApiResponseModelsChannelBase channels_post_full_text_search_channel(full_text_search_channel)

Creates a full text search channel.

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
api_instance = swagger_client.ChannelsPostApi(swagger_client.ApiClient(configuration))
full_text_search_channel = swagger_client.SaveTVWebApiRequestModelsFullTextSearchChannel() # SaveTVWebApiRequestModelsFullTextSearchChannel | The full text search channel.

try:
    # Creates a full text search channel.
    api_response = api_instance.channels_post_full_text_search_channel(full_text_search_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsPostApi->channels_post_full_text_search_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full_text_search_channel** | [**SaveTVWebApiRequestModelsFullTextSearchChannel**](SaveTVWebApiRequestModelsFullTextSearchChannel.md)| The full text search channel. | 

### Return type

[**SaveTVWebApiResponseModelsChannelBase**](SaveTVWebApiResponseModelsChannelBase.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post_star_channel**
> SaveTVWebApiResponseModelsChannelBase channels_post_star_channel(star_channel)

Creates a star channel.

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
api_instance = swagger_client.ChannelsPostApi(swagger_client.ApiClient(configuration))
star_channel = swagger_client.SaveTVWebApiRequestModelsStarChannel() # SaveTVWebApiRequestModelsStarChannel | The star channel.

try:
    # Creates a star channel.
    api_response = api_instance.channels_post_star_channel(star_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsPostApi->channels_post_star_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **star_channel** | [**SaveTVWebApiRequestModelsStarChannel**](SaveTVWebApiRequestModelsStarChannel.md)| The star channel. | 

### Return type

[**SaveTVWebApiResponseModelsChannelBase**](SaveTVWebApiResponseModelsChannelBase.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post_telecast_ids_channel**
> SaveTVWebApiResponseModelsChannelBase channels_post_telecast_ids_channel(telecast_ids_channel)

Creates a channel by various telecast ids.

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
api_instance = swagger_client.ChannelsPostApi(swagger_client.ApiClient(configuration))
telecast_ids_channel = swagger_client.SaveTVWebApiRequestModelsTelecastIdsChannel() # SaveTVWebApiRequestModelsTelecastIdsChannel | The telecast ids channel.

try:
    # Creates a channel by various telecast ids.
    api_response = api_instance.channels_post_telecast_ids_channel(telecast_ids_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsPostApi->channels_post_telecast_ids_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telecast_ids_channel** | [**SaveTVWebApiRequestModelsTelecastIdsChannel**](SaveTVWebApiRequestModelsTelecastIdsChannel.md)| The telecast ids channel. | 

### Return type

[**SaveTVWebApiResponseModelsChannelBase**](SaveTVWebApiResponseModelsChannelBase.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post_title_channel**
> SaveTVWebApiResponseModelsChannelBase channels_post_title_channel(title_channel)

Creates a title channel.

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
api_instance = swagger_client.ChannelsPostApi(swagger_client.ApiClient(configuration))
title_channel = swagger_client.SaveTVWebApiRequestModelsTitleChannel() # SaveTVWebApiRequestModelsTitleChannel | The title channel.

try:
    # Creates a title channel.
    api_response = api_instance.channels_post_title_channel(title_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsPostApi->channels_post_title_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_channel** | [**SaveTVWebApiRequestModelsTitleChannel**](SaveTVWebApiRequestModelsTitleChannel.md)| The title channel. | 

### Return type

[**SaveTVWebApiResponseModelsChannelBase**](SaveTVWebApiResponseModelsChannelBase.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post_tv_station_channel**
> SaveTVWebApiResponseModelsChannelBase channels_post_tv_station_channel(tv_station_channel)

Creates a TV station channel.

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
api_instance = swagger_client.ChannelsPostApi(swagger_client.ApiClient(configuration))
tv_station_channel = swagger_client.SaveTVWebApiRequestModelsTvStationChannel() # SaveTVWebApiRequestModelsTvStationChannel | The TV station channel.

try:
    # Creates a TV station channel.
    api_response = api_instance.channels_post_tv_station_channel(tv_station_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsPostApi->channels_post_tv_station_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_station_channel** | [**SaveTVWebApiRequestModelsTvStationChannel**](SaveTVWebApiRequestModelsTvStationChannel.md)| The TV station channel. | 

### Return type

[**SaveTVWebApiResponseModelsChannelBase**](SaveTVWebApiResponseModelsChannelBase.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

