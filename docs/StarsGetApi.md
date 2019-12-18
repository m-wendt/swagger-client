# swagger_client.StarsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stars_get**](StarsGetApi.md#stars_get) | **GET** /v3/stars | Retrieves the stars that match the filter condition.
[**stars_get_0**](StarsGetApi.md#stars_get_0) | **GET** /v3/stars/{id} | Retrieves a single star with the given identifier.


# **stars_get**
> SaveTVWebApiResponseModelsPagedStarList stars_get(fields=fields, hasbirthdaytoday=hasbirthdaytoday, ids=ids, ishighlight=ishighlight, limit=limit, nopagingheader=nopagingheader, offset=offset, playspartinupcomingtelecast=playspartinupcomingtelecast, q=q, sort=sort)

Retrieves the stars that match the filter condition.

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
api_instance = swagger_client.StarsGetApi(swagger_client.ApiClient(configuration))
fields = ['alternativename, awards, awards.count, awards.name, birthdate, birthplace, dateofdeath, description, height, id, imageurls100, imageurls250, imageurls500, ishighlight, links, links.title, links.url, name, nickname, placeofdeath'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    alternativename,    awards,    awards.count,    awards.name,    birthdate,    birthplace,    dateofdeath,    description,    height,    id,    imageurls100,    imageurls250,    imageurls500,    ishighlight,    links,    links.title,    links.url,    name,    nickname,    placeofdeath (optional) (default to alternativename, awards, awards.count, awards.name, birthdate, birthplace, dateofdeath, description, height, id, imageurls100, imageurls250, imageurls500, ishighlight, links, links.title, links.url, name, nickname, placeofdeath)
hasbirthdaytoday = true # bool | Determines whether the star must have birthday today or not. (optional)
ids = [56] # list[int] | A comma-separated list of star identifiers. (optional)
ishighlight = true # bool | Determines whether the star is marked as important star or not. (optional)
limit = 56 # int | Sets the maximum number of items in result set.    The default value: 20.    The maximum allowed value: 500. (optional)
nopagingheader = true # bool | By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values (optional)
offset = 56 # int | Sets the number of data items that are skipped in the result set.    The default value: 0. (optional)
playspartinupcomingtelecast = true # bool | Determines whether the star plays in a telecast within the future EPG. (optional)
q = 'q_example' # str | The search text used for a text search. (optional)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    position    Default sorting:    +name (optional)

try:
    # Retrieves the stars that match the filter condition.
    api_response = api_instance.stars_get(fields=fields, hasbirthdaytoday=hasbirthdaytoday, ids=ids, ishighlight=ishighlight, limit=limit, nopagingheader=nopagingheader, offset=offset, playspartinupcomingtelecast=playspartinupcomingtelecast, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StarsGetApi->stars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    alternativename,    awards,    awards.count,    awards.name,    birthdate,    birthplace,    dateofdeath,    description,    height,    id,    imageurls100,    imageurls250,    imageurls500,    ishighlight,    links,    links.title,    links.url,    name,    nickname,    placeofdeath | [optional] [default to alternativename, awards, awards.count, awards.name, birthdate, birthplace, dateofdeath, description, height, id, imageurls100, imageurls250, imageurls500, ishighlight, links, links.title, links.url, name, nickname, placeofdeath]
 **hasbirthdaytoday** | **bool**| Determines whether the star must have birthday today or not. | [optional] 
 **ids** | [**list[int]**](int.md)| A comma-separated list of star identifiers. | [optional] 
 **ishighlight** | **bool**| Determines whether the star is marked as important star or not. | [optional] 
 **limit** | **int**| Sets the maximum number of items in result set.    The default value: 20.    The maximum allowed value: 500. | [optional] 
 **nopagingheader** | **bool**| By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values | [optional] 
 **offset** | **int**| Sets the number of data items that are skipped in the result set.    The default value: 0. | [optional] 
 **playspartinupcomingtelecast** | **bool**| Determines whether the star plays in a telecast within the future EPG. | [optional] 
 **q** | **str**| The search text used for a text search. | [optional] 
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    position    Default sorting:    +name | [optional] 

### Return type

[**SaveTVWebApiResponseModelsPagedStarList**](SaveTVWebApiResponseModelsPagedStarList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stars_get_0**
> SaveTVWebApiResponseModelsStar stars_get_0(id, fields=fields)

Retrieves a single star with the given identifier.

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
api_instance = swagger_client.StarsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the star.
fields = ['alternativename, awards, awards.count, awards.name, birthdate, birthplace, dateofdeath, description, height, id, imageurls100, imageurls250, imageurls500, ishighlight, links, links.title, links.url, name, nickname, placeofdeath'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    alternativename,    awards,    awards.count,    awards.name,    birthdate,    birthplace,    dateofdeath,    description,    height,    id,    imageurls100,    imageurls250,    imageurls500,    ishighlight,    links,    links.title,    links.url,    name,    nickname,    placeofdeath (optional) (default to alternativename, awards, awards.count, awards.name, birthdate, birthplace, dateofdeath, description, height, id, imageurls100, imageurls250, imageurls500, ishighlight, links, links.title, links.url, name, nickname, placeofdeath)

try:
    # Retrieves a single star with the given identifier.
    api_response = api_instance.stars_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StarsGetApi->stars_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the star. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    alternativename,    awards,    awards.count,    awards.name,    birthdate,    birthplace,    dateofdeath,    description,    height,    id,    imageurls100,    imageurls250,    imageurls500,    ishighlight,    links,    links.title,    links.url,    name,    nickname,    placeofdeath | [optional] [default to alternativename, awards, awards.count, awards.name, birthdate, birthplace, dateofdeath, description, height, id, imageurls100, imageurls250, imageurls500, ishighlight, links, links.title, links.url, name, nickname, placeofdeath]

### Return type

[**SaveTVWebApiResponseModelsStar**](SaveTVWebApiResponseModelsStar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

