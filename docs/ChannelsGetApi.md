# swagger_client.ChannelsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_count**](ChannelsGetApi.md#channels_count) | **GET** /v3/channels/count | Retrieves the number of channels for the current account.
[**channels_get**](ChannelsGetApi.md#channels_get) | **GET** /v3/channels | Retrieves the channels for the current account.
[**channels_get_0**](ChannelsGetApi.md#channels_get_0) | **GET** /v3/channels/{id} | Retrieves a single channel with the given identifier.
[**channels_telecasts**](ChannelsGetApi.md#channels_telecasts) | **GET** /v3/channels/{id}/telecasts | Retrieves the telecasts that matches the channel criteria.
[**channels_telecasts_0**](ChannelsGetApi.md#channels_telecasts_0) | **GET** /v3/channels/{id}/telecasts/{telecastid} | Retrieves the telecasts that matches the channel criteria.


# **channels_count**
> SaveTVWebApiResponseModelsChannelCount channels_count()

Retrieves the number of channels for the current account.

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
api_instance = swagger_client.ChannelsGetApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the number of channels for the current account.
    api_response = api_instance.channels_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsGetApi->channels_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SaveTVWebApiResponseModelsChannelCount**](SaveTVWebApiResponseModelsChannelCount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_get**
> list[SaveTVWebApiResponseModelsChannel] channels_get(channelscope=channelscope, fields=fields, sort=sort)

Retrieves the channels for the current account.

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
api_instance = swagger_client.ChannelsGetApi(swagger_client.ApiClient(configuration))
channelscope = 56 # int | The channel scope determines which channels will be returned.    Values:    0 = Selects all channels    1 = Selects only standard channels    2 = Selects only channels created by Catch All    The default value: 0 (optional)
fields = ['channelscope, channeltype, counttelecasts, id, imageurl100, imageurl250, imageurl500, name, searchquery, star.id, star.name, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.name, tvsubcategory.id, tvsubcategory.name'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The fields \"channeltype, id\" are always transmitted.    _The allowed field values:_    channelscope,    channeltype,    counttelecasts,    id,    imageurl100,    imageurl250,    imageurl500,    name,    searchquery,    star.id,    star.name,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.name,    tvsubcategory.id,    tvsubcategory.name (optional) (default to channelscope, channeltype, counttelecasts, id, imageurl100, imageurl250, imageurl500, name, searchquery, star.id, star.name, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.name, tvsubcategory.id, tvsubcategory.name)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    Default sorting:    +name (optional)

try:
    # Retrieves the channels for the current account.
    api_response = api_instance.channels_get(channelscope=channelscope, fields=fields, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsGetApi->channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelscope** | **int**| The channel scope determines which channels will be returned.    Values:    0 &#x3D; Selects all channels    1 &#x3D; Selects only standard channels    2 &#x3D; Selects only channels created by Catch All    The default value: 0 | [optional] 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The fields \&quot;channeltype, id\&quot; are always transmitted.    _The allowed field values:_    channelscope,    channeltype,    counttelecasts,    id,    imageurl100,    imageurl250,    imageurl500,    name,    searchquery,    star.id,    star.name,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.name,    tvsubcategory.id,    tvsubcategory.name | [optional] [default to channelscope, channeltype, counttelecasts, id, imageurl100, imageurl250, imageurl500, name, searchquery, star.id, star.name, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.name, tvsubcategory.id, tvsubcategory.name]
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    Default sorting:    +name | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsChannel]**](SaveTVWebApiResponseModelsChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_get_0**
> SaveTVEpgDataContextChannel channels_get_0(id, fields=fields)

Retrieves a single channel with the given identifier.

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
api_instance = swagger_client.ChannelsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the channel.
fields = ['channelscope, channeltype, counttelecasts, id, imageurl100, imageurl250, imageurl500, name, searchquery, star.id, star.name, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.name, tvsubcategory.id, tvsubcategory.name'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The fields \"channeltype, id\" are always transmitted.    _The allowed field values:_    channelscope,    channeltype,    counttelecasts,    id,    imageurl100,    imageurl250,    imageurl500,    name,    searchquery,    star.id,    star.name,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.name,    tvsubcategory.id,    tvsubcategory.name (optional) (default to channelscope, channeltype, counttelecasts, id, imageurl100, imageurl250, imageurl500, name, searchquery, star.id, star.name, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.name, tvsubcategory.id, tvsubcategory.name)

try:
    # Retrieves a single channel with the given identifier.
    api_response = api_instance.channels_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsGetApi->channels_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the channel. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The fields \&quot;channeltype, id\&quot; are always transmitted.    _The allowed field values:_    channelscope,    channeltype,    counttelecasts,    id,    imageurl100,    imageurl250,    imageurl500,    name,    searchquery,    star.id,    star.name,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.name,    tvsubcategory.id,    tvsubcategory.name | [optional] [default to channelscope, channeltype, counttelecasts, id, imageurl100, imageurl250, imageurl500, name, searchquery, star.id, star.name, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.name, tvsubcategory.id, tvsubcategory.name]

### Return type

[**SaveTVEpgDataContextChannel**](SaveTVEpgDataContextChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_telecasts**
> SaveTVWebApiResponseModelsPagedTelecastList channels_telecasts(id, fields=fields, limit=limit, nopagingheader=nopagingheader, offset=offset, sort=sort)

Retrieves the telecasts that matches the channel criteria.

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
api_instance = swagger_client.ChannelsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the channel.
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)
limit = 56 # int | Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 2000. (optional)
nopagingheader = true # bool | By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values (optional)
offset = 56 # int | Sets the number of data items that are skipped in the result set.    The default value: 0. (optional)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    category    episode    startdate    subcategory    subtitle    title    tvstationposition    year    Default sorting:    +startdate,+tvstationposition (optional)

try:
    # Retrieves the telecasts that matches the channel criteria.
    api_response = api_instance.channels_telecasts(id, fields=fields, limit=limit, nopagingheader=nopagingheader, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsGetApi->channels_telecasts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the channel. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]
 **limit** | **int**| Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 2000. | [optional] 
 **nopagingheader** | **bool**| By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values | [optional] 
 **offset** | **int**| Sets the number of data items that are skipped in the result set.    The default value: 0. | [optional] 
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    category    episode    startdate    subcategory    subtitle    title    tvstationposition    year    Default sorting:    +startdate,+tvstationposition | [optional] 

### Return type

[**SaveTVWebApiResponseModelsPagedTelecastList**](SaveTVWebApiResponseModelsPagedTelecastList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_telecasts_0**
> SaveTVWebApiResponseModelsPagedTelecastList channels_telecasts_0(id, telecast_id, fields=fields)

Retrieves the telecasts that matches the channel criteria.

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
api_instance = swagger_client.ChannelsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the channel.
telecast_id = 56 # int | The identifier of the telecast.
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)

try:
    # Retrieves the telecasts that matches the channel criteria.
    api_response = api_instance.channels_telecasts_0(id, telecast_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsGetApi->channels_telecasts_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the channel. | 
 **telecast_id** | **int**| The identifier of the telecast. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]

### Return type

[**SaveTVWebApiResponseModelsPagedTelecastList**](SaveTVWebApiResponseModelsPagedTelecastList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

