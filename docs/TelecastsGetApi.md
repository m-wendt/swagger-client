# swagger_client.TelecastsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telecasts_followers**](TelecastsGetApi.md#telecasts_followers) | **GET** /v3/telecasts/{id}/followers | Retrieves the following telecasts for a telecast.
[**telecasts_get**](TelecastsGetApi.md#telecasts_get) | **GET** /v3/telecasts | Retrieves the telecasts that match the filter condition.
[**telecasts_get_0**](TelecastsGetApi.md#telecasts_get_0) | **GET** /v3/telecasts/{id} | Retrieves a single telecast with the given identifier.
[**telecasts_get_suggestions**](TelecastsGetApi.md#telecasts_get_suggestions) | **GET** /v3/telecasts/suggestions | Provides suggestions for the telecast search text.
[**telecasts_telecast_list_ids**](TelecastsGetApi.md#telecasts_telecast_list_ids) | **GET** /v3/telecasts/telecastlistids/{id} | Retrieves telecasts for a telecast list id.
[**telecasts_user_recommendations**](TelecastsGetApi.md#telecasts_user_recommendations) | **GET** /v3/telecasts/userrecommendations/{id} | Retrieves the user recommendations for a TV category.


# **telecasts_followers**
> SaveTVWebApiResponseModelsPagedTelecastList telecasts_followers(id, fields=fields)

Retrieves the following telecasts for a telecast.

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
api_instance = swagger_client.TelecastsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the telecast.
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)

try:
    # Retrieves the following telecasts for a telecast.
    api_response = api_instance.telecasts_followers(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsGetApi->telecasts_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the telecast. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]

### Return type

[**SaveTVWebApiResponseModelsPagedTelecastList**](SaveTVWebApiResponseModelsPagedTelecastList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telecasts_get**
> SaveTVWebApiResponseModelsPagedTelecastList telecasts_get(dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, fields=fields, fsk=fsk, ishighlight=ishighlight, limit=limit, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, nopagingheader=nopagingheader, offset=offset, q=q, searchtextscope=searchtextscope, sort=sort, starids=starids, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)

Retrieves the telecasts that match the filter condition.

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
api_instance = swagger_client.TelecastsGetApi(swagger_client.ApiClient(configuration))
dayofweeks = [56] # list[int] | Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 = Sunday    1 = Monday    2 = Tuesday    3 = Wednesday    4 = Thursday    5 = Friday    6 = Saturday (optional)
exacttitle = 'exacttitle_example' # str | Selects only telecasts whose title matches exactly (but case insensitive) the given value. (optional)
exacttitles = ['exacttitles_example'] # list[str] | Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \"exactTitle\" is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \"\\,\" (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde (optional)
excludedtelecastids = [56] # list[int] | A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. (optional)
excludedtvstations = [56] # list[int] | A comma-separated list of TV station identifiers that must not match. (optional)
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)
fsk = [56] # list[int] | Selects only telecasts whose fsk matches the given value.    Values:    0 = Includes all ages from 0 to 5.    6 = Includes all ages from 6 to 11.    12 = Includes all ages from 12 to 15.    16 = Includes all ages from 16 to 17.    18 = Includes all ages from 18 and above. (optional)
ishighlight = true # bool | Determines whether the telecast must be an highlight or not. (optional)
limit = 56 # int | Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 2000. (optional)
maxenddate = '2013-10-20T19:20:30+01:00' # datetime | The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstartdate = '2013-10-20T19:20:30+01:00' # datetime | The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstarttime = 'maxstarttime_example' # str | The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
minenddate = '2013-10-20T19:20:30+01:00' # datetime | The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstartdate = '2013-10-20T19:20:30+01:00' # datetime | The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstarttime = 'minstarttime_example' # str | The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
nopagingheader = true # bool | By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values (optional)
offset = 56 # int | Sets the number of data items that are skipped in the result set.    The default value: 0. (optional)
q = 'q_example' # str | The search text used for a text search. (optional)
searchtextscope = 56 # int | The scope defines the kind of the text search.    The default value is: 1    Values:     1 = search in all texts    2 = search in title and subtitle (optional)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    category    episode    startdate    subcategory    subtitle    title    tvstationposition    year    Default sorting:    +startdate,+tvstationposition (optional)
starids = [56] # list[int] | A comma-separated list of star identifiers. (optional)
telecastids = [56] # list[int] | A comma-separated list of telecast identifiers. (optional)
timeblock = 56 # int | A time block selects telecasts of one time range.    Values    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15 (optional)
timeblocks = [56] # list[int] | A list of time blocks that selects telecasts of one time range.    Values:    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. (optional)
tvcategories = [56] # list[int] | A comma-separated list of TV category identifiers. (optional)
tvstations = [56] # list[int] | A comma-separated list of TV station identifiers. (optional)
tvsubcategories = [56] # list[int] | A comma-separated list of TV sub category identifiers. (optional)

try:
    # Retrieves the telecasts that match the filter condition.
    api_response = api_instance.telecasts_get(dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, fields=fields, fsk=fsk, ishighlight=ishighlight, limit=limit, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, nopagingheader=nopagingheader, offset=offset, q=q, searchtextscope=searchtextscope, sort=sort, starids=starids, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsGetApi->telecasts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dayofweeks** | [**list[int]**](int.md)| Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 &#x3D; Sunday    1 &#x3D; Monday    2 &#x3D; Tuesday    3 &#x3D; Wednesday    4 &#x3D; Thursday    5 &#x3D; Friday    6 &#x3D; Saturday | [optional] 
 **exacttitle** | **str**| Selects only telecasts whose title matches exactly (but case insensitive) the given value. | [optional] 
 **exacttitles** | [**list[str]**](str.md)| Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \&quot;exactTitle\&quot; is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \&quot;\\,\&quot; (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde | [optional] 
 **excludedtelecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. | [optional] 
 **excludedtvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers that must not match. | [optional] 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]
 **fsk** | [**list[int]**](int.md)| Selects only telecasts whose fsk matches the given value.    Values:    0 &#x3D; Includes all ages from 0 to 5.    6 &#x3D; Includes all ages from 6 to 11.    12 &#x3D; Includes all ages from 12 to 15.    16 &#x3D; Includes all ages from 16 to 17.    18 &#x3D; Includes all ages from 18 and above. | [optional] 
 **ishighlight** | **bool**| Determines whether the telecast must be an highlight or not. | [optional] 
 **limit** | **int**| Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 2000. | [optional] 
 **maxenddate** | **datetime**| The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstartdate** | **datetime**| The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstarttime** | **str**| The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **minenddate** | **datetime**| The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstartdate** | **datetime**| The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstarttime** | **str**| The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **nopagingheader** | **bool**| By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values | [optional] 
 **offset** | **int**| Sets the number of data items that are skipped in the result set.    The default value: 0. | [optional] 
 **q** | **str**| The search text used for a text search. | [optional] 
 **searchtextscope** | **int**| The scope defines the kind of the text search.    The default value is: 1    Values:     1 &#x3D; search in all texts    2 &#x3D; search in title and subtitle | [optional] 
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    category    episode    startdate    subcategory    subtitle    title    tvstationposition    year    Default sorting:    +startdate,+tvstationposition | [optional] 
 **starids** | [**list[int]**](int.md)| A comma-separated list of star identifiers. | [optional] 
 **telecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers. | [optional] 
 **timeblock** | **int**| A time block selects telecasts of one time range.    Values    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15 | [optional] 
 **timeblocks** | [**list[int]**](int.md)| A list of time blocks that selects telecasts of one time range.    Values:    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. | [optional] 
 **tvcategories** | [**list[int]**](int.md)| A comma-separated list of TV category identifiers. | [optional] 
 **tvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers. | [optional] 
 **tvsubcategories** | [**list[int]**](int.md)| A comma-separated list of TV sub category identifiers. | [optional] 

### Return type

[**SaveTVWebApiResponseModelsPagedTelecastList**](SaveTVWebApiResponseModelsPagedTelecastList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telecasts_get_0**
> SaveTVWebApiResponseModelsTelecast telecasts_get_0(id, fields=fields)

Retrieves a single telecast with the given identifier.

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
api_instance = swagger_client.TelecastsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the telecast.
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)

try:
    # Retrieves a single telecast with the given identifier.
    api_response = api_instance.telecasts_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsGetApi->telecasts_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the telecast. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]

### Return type

[**SaveTVWebApiResponseModelsTelecast**](SaveTVWebApiResponseModelsTelecast.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telecasts_get_suggestions**
> list[SaveTVWebApiResponseModelsSuggestion] telecasts_get_suggestions(q=q)

Provides suggestions for the telecast search text.

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
api_instance = swagger_client.TelecastsGetApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str |  (optional)

try:
    # Provides suggestions for the telecast search text.
    api_response = api_instance.telecasts_get_suggestions(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsGetApi->telecasts_get_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsSuggestion]**](SaveTVWebApiResponseModelsSuggestion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telecasts_telecast_list_ids**
> SaveTVWebApiResponseModelsPagedTelecastList telecasts_telecast_list_ids(id, fields=fields)

Retrieves telecasts for a telecast list id.

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
api_instance = swagger_client.TelecastsGetApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the telecast list.
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)

try:
    # Retrieves telecasts for a telecast list id.
    api_response = api_instance.telecasts_telecast_list_ids(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsGetApi->telecasts_telecast_list_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the telecast list. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]

### Return type

[**SaveTVWebApiResponseModelsPagedTelecastList**](SaveTVWebApiResponseModelsPagedTelecastList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telecasts_user_recommendations**
> SaveTVWebApiResponseModelsPagedTelecastList telecasts_user_recommendations(id, fields=fields)

Retrieves the user recommendations for a TV category.

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
api_instance = swagger_client.TelecastsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the TV category.
fields = ['commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year (optional) (default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year)

try:
    # Retrieves the user recommendations for a TV category.
    api_response = api_instance.telecasts_user_recommendations(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsGetApi->telecasts_user_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the TV category. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    commentator,    country,    description,    director,    enddate,    episode,    existsrecord,    id,    imageurl100,    imageurl250,    imageurl500,    interpret,    isblackwhite,    ishighlight,    isomitted,    moderator,    rating,    roles,    roles.rolename,    roles.starid,    roles.starname,    slug,    startdate,    subject,    subtitle,    title,    tvcategory.id,    tvcategory.name,    tvstation.id,    tvstation.isrecordable,    tvstation.largelogourl,    tvstation.name,    tvstation.smalllogourl,    tvsubcategory.id,    tvsubcategory.name,    updatedate,    voluntaryselfregulationofthemovieindustry,    year | [optional] [default to commentator, country, description, director, enddate, episode, existsrecord, id, imageurl100, imageurl250, imageurl500, interpret, isblackwhite, ishighlight, isomitted, moderator, rating, roles, roles.rolename, roles.starid, roles.starname, slug, startdate, subject, subtitle, title, tvcategory.id, tvcategory.name, tvstation.id, tvstation.isrecordable, tvstation.largelogourl, tvstation.name, tvstation.smalllogourl, tvsubcategory.id, tvsubcategory.name, updatedate, voluntaryselfregulationofthemovieindustry, year]

### Return type

[**SaveTVWebApiResponseModelsPagedTelecastList**](SaveTVWebApiResponseModelsPagedTelecastList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

