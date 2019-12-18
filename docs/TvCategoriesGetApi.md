# swagger_client.TvCategoriesGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tv_categories_get**](TvCategoriesGetApi.md#tv_categories_get) | **GET** /v3/tvcategories | Retrieves all available TV categories.
[**tv_categories_get_0**](TvCategoriesGetApi.md#tv_categories_get_0) | **GET** /v3/tvcategories/{id} | Retrieves a single TV category with the given identifier.


# **tv_categories_get**
> list[SaveTVWebApiResponseModelsTvCategory] tv_categories_get(fields=fields, sort=sort)

Retrieves all available TV categories.

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
api_instance = swagger_client.TvCategoriesGetApi(swagger_client.ApiClient(configuration))
fields = ['id, name, tvsubcategories.id, tvsubcategories.name'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    id,    name,    tvsubcategories.id,    tvsubcategories.name (optional) (default to id, name, tvsubcategories.id, tvsubcategories.name)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority (optional)

try:
    # Retrieves all available TV categories.
    api_response = api_instance.tv_categories_get(fields=fields, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvCategoriesGetApi->tv_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    id,    name,    tvsubcategories.id,    tvsubcategories.name | [optional] [default to id, name, tvsubcategories.id, tvsubcategories.name]
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsTvCategory]**](SaveTVWebApiResponseModelsTvCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_categories_get_0**
> SaveTVWebApiResponseModelsTvCategory tv_categories_get_0(id, fields=fields, sort=sort)

Retrieves a single TV category with the given identifier.

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
api_instance = swagger_client.TvCategoriesGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the TV category.
fields = ['id, name, tvsubcategories.id, tvsubcategories.name'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    id,    name,    tvsubcategories.id,    tvsubcategories.name (optional) (default to id, name, tvsubcategories.id, tvsubcategories.name)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority (optional)

try:
    # Retrieves a single TV category with the given identifier.
    api_response = api_instance.tv_categories_get_0(id, fields=fields, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TvCategoriesGetApi->tv_categories_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the TV category. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    id,    name,    tvsubcategories.id,    tvsubcategories.name | [optional] [default to id, name, tvsubcategories.id, tvsubcategories.name]
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority | [optional] 

### Return type

[**SaveTVWebApiResponseModelsTvCategory**](SaveTVWebApiResponseModelsTvCategory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

