Coda API (1.4.17)
API Support: help+api@coda.io
URL: https://coda.io
License: Coda Developer Terms

Introduction
The Coda API is a RESTful API that lets you programmatically interact with Coda docs:

- List and search Coda docs
- Create new docs and copy existing ones
- Share and publish docs
- Discover pages, tables, formulas, and controls
- Read, insert, upsert, update, and delete rows

We reserve the right to remove older APIs and functionality with a 3-month deprecation notice. Changes and new features will be announced in the Developers Central section of our Community, and in the API updates doc.

Getting Started
Our Getting Started Guide helps you learn the basics of working with the API and shows a few ways you can use it, including:

- Reading data from Coda tables and writing back to them
- Building a one-way sync from one Coda doc to another
- Automating reminders
- Syncing your Google Calendar to Coda

Using the API
Coda's REST API is designed to be straightforward to use. You can use any language and platform to make requests. Tools like Postman or Insomnia can help you get a feel for the API.

API Endpoint
This API uses a base path of https://coda.io/apis/v1.

Resource IDs and Links
Each resource instance retrieved via the API has the following fields:

- id: The resource's immutable ID
- type: The type of resource
- href: A fully qualified URI for the resource

Most resources can be queried by their name or ID. We recommend using IDs where possible, as names can be changed by users.

List Endpoints
Endpoints supporting listing of resources have the following fields:

- items: An array of listed resources, limited by query parameters
- nextPageLink: API link to the next page of results, if available
- nextPageToken: Page token for the next page of results, if available

The maximum page size may change at any time. Use the nextPageToken to check for more results, rather than relying on a specific result set size.

Doc IDs
While most object IDs must be discovered via the API, you may often need to get the ID of a specific Coda doc. Use the provided Doc ID Extractor tool to easily extract the ID from a Coda doc URL.

Rate Limiting
The Coda API has rate limits on requests per minute. Exceeding these limits will result in HTTP 429 errors. Current rate limits (subject to change without notice):

- Reading data: 100 requests per 6 seconds
- Writing data: 10 requests per 6 seconds
- Writing doc content: 5 requests per 10 seconds
- Listing docs: 4 requests per 6 seconds
- Reading analytics: 100 requests per 6 seconds
API scripts should implement retry logic for HTTP 429 errors.

Consistency
API edits may take a few seconds to become available. These endpoints return an HTTP 202 status code and a requestId, which can be used with the #getMutationStatus endpoint to check the edit status.

For the most up-to-date data when retrieving doc data, use the X-Coda-Doc-Version: latest header.

Volatile Formulas
Coda's "volatile" formulas (e.g., Today(), Now(), User()) behave differently with the API. Time-based values may only be current to the last doc edit, and user-based values may be blank or invalid.

Free and Paid Workspaces
The Coda API is available to all users free of charge, but API usage is subject to the user's role in the applicable workspace. For example, the #createDoc endpoint requires the API token owner to be a Doc Maker (or Admin) in the workspace.

Examples
This documentation provides code examples in Python, Unix shell, and Google Apps Script to help you get started with the Coda API.

Doc ID Extractor
Paste in a Coda doc URL
 Your doc ID is:    
Rate Limiting
The Coda API has rate limits on requests per minute. Exceeding these limits will result in HTTP 429 errors. Current rate limits (subject to change without notice):

- Reading data: 100 requests per 6 seconds
- Writing data: 10 requests per 6 seconds
- Writing doc content: 5 requests per 10 seconds
- Listing docs: 4 requests per 6 seconds
- Reading analytics: 100 requests per 6 seconds

Python examples
These examples use Python 3.6+. If you don't already have the requests module, use pip or easy_install to get it.

Shell examples
The shell examples are intended to be run in a Unix shell. If you're on Windows, you will need to install WSL.

These examples use the standard cURL utility to pull from the API, and then process it with jq to extract and format example output. If you don't already have it, you can either install it or run the command without it to see the raw JSON output.

Google Apps Script examples

Google Apps Script makes it easy to write code in a JavaScript-like syntax and access many Google products with built-in libraries. You can set up your scripts to run periodically, making it a good environment for writing tools without maintaining your own server.

Coda provides a library for Google Apps Script. To use it, go to Resources -> Libraries... and enter the following library ID: 15IQuWOk8MqT50FDWomh57UqWGH23gjsWVWYFms3ton6L-UHmefYHS9Vl. The library's source code is available here.

Google provides autocomplete for API functions and generated docs. Access these docs via the Libraries dialog by clicking on the library name. Required parameters included in the URL path are positional arguments in these functions, followed by the request body, if applicable. All remaining parameters can be specified in the options object.

OpenAPI/Swagger Spec
We offer an OpenAPI 3.0 specification to standardize our API and make it accessible:

- OpenAPI 3.0 spec - YAML
- OpenAPI 3.0 spec - JSON

Postman collection
To quickly prototype the API in Postman, use one of the links above to import the Coda API into a collection. Set the appropriate header and environment variables.

Client libraries
We currently support only Google Apps Script. To work with the Coda API, use standard network libraries for your language or the appropriate Swagger Generator tool to auto-generate Coda API client libraries. We do not guarantee compatibility of these autogenerated libraries with our API (e.g., some libraries may not work with Bearer authentication).

OpenAPI 3.0
Swagger Generator 3 can generate client libraries for these languages. It is relatively new and supports a limited set of languages.

Third-party client libraries
Some community members have written libraries to work with our API. These aren't officially supported by Coda but are listed here for convenience. (Let us know if you've written a library and would like it included here.)

- PHP by Daniel Stieber
- Node-RED by Mori Sugimoto
- NodeJS by Parker McMullin
- Ruby by Carlos Muñoz at Getro
- Python by Mikhail Beliansky
- Go by Artur Safin

Docs
Coda docs are foundational, top-level collaborative projects that contain pages. The API lets you list and search your docs to obtain basic metadata like titles and ownership information.

List available docs
Returns a list of Coda docs accessible by the user. These are returned in the same order as on the docs page: reverse chronological by the latest event relevant to the user (last viewed, edited, or shared).

AUTHORIZATIONS:
Bearer

QUERY PARAMETERS
- isOwner: boolean - Show only docs owned by the user.
- isPublished: boolean - Show only published docs.
- query: string - Example: query=Supercalifragilisticexpialidocious - Search term used to filter down results.
- sourceDoc: string - Show only docs copied from the specified doc ID.
- isStarred: boolean - If true, returns docs that are starred. If false, returns docs that are not starred.
- inGallery: boolean - Show only docs visible within the gallery.
- workspaceId: string - Show only docs belonging to the given workspace.
- folderId: string - Show only docs belonging to the given folder.
- limit: integer >= 1 - Default: 25 - Example: limit=10 - Maximum number of results to return in this query.
- pageToken: string - Example: pageToken=eyJsaW1pd - An opaque token used to fetch the next page of results.

Responses
- 200: List of Coda docs matching the query.
  - RESPONSE SCHEMA: application/json
    - items: Array of objects (Doc)
    - href: string <url> - API link to these results
    - nextPageToken: string (nextPageToken) - If specified, an opaque token used to fetch the next page of results.
    - nextPageLink: string <url> - If specified, a link that can be used to fetch the next page of results.
- 401: The API token is invalid or has expired.
- 403: The API token does not grant access to this resource.
- 404: The resource could not be located with the current API token.
- 429: The client has sent too many requests.

GET /docs

Request samples
- Python 3.7
- Shell
- Google Apps Script

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.

folderId	
string
The ID of the folder within which to create this doc. Defaults to your "My docs" folder in the oldest workspace you joined; this is subject to change. You can get this ID by opening the folder in the docs list on your computer and grabbing the folderId query parameter.

initialPage	
object
The contents of the initial page of the doc.

Responses
201 Info about the created doc.
RESPONSE SCHEMA: application/json
id
required
string
ID of the Coda doc.

type
required
string
Value: "doc"
The type of this resource.

href
required
string <url>
API link to the Coda doc.

browserLink
required
string <url>
Browser-friendly link to the Coda doc.

name
required
string
Name of the doc.

owner
required
string <email>
Email address of the doc owner.

ownerName
required
string
Name of the doc owner.

createdAt
required
string <date-time>
Timestamp for when the doc was created.

updatedAt
required
string <date-time>
Timestamp for when the doc was last modified.

workspace
required
object (WorkspaceReference)
Reference to a Coda workspace.

folder
required
object (FolderReference)
Reference to a Coda folder.

workspaceId
required
string
Deprecated
ID of the Coda workspace containing this doc.

folderId
required
string
Deprecated
ID of the Coda folder containing this doc.

icon	
object (Icon)
Info about the icon.

docSize	
object (DocSize)
The number of components within a Coda doc.

sourceDoc	
object
Reference to a Coda doc from which this doc was copied, if any.

published	
object (DocPublished)
Information about the publishing state of the document.

requestId	
string
An arbitrary unique identifier for this request.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
429 The client has sent too many requests.

POST
/docs

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"title": "Project Tracker",
"sourceDoc": "iJKlm_noPq",
"timezone": "America/Los_Angeles",
"folderId": "fl-ABcdEFgHJi",
"initialPage": {
"name": "Launch Status",
"subtitle": "See the status of launch-related tasks.",
"iconName": "rocket",
"imageUrl": "https://example.com/image.jpg",
"parentPageId": "canvas-tuVwxYz",
"pageContent": {}
}
}
Response samples
201400401403429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH",
"icon": {
"name": "string",
"type": "string",
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"
},
"name": "Product Launch Hub",
"owner": "user@example.com",
"ownerName": "Some User",
"docSize": {
"totalRowCount": 31337,
"tableAndViewCount": 42,
"pageCount": 10,
"overApiSizeLimit": false
},
"sourceDoc": {
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH"
},
"createdAt": "2018-04-11T00:18:57.946Z",
"updatedAt": "2018-04-11T00:18:57.946Z",
"published": {
"description": "Hello World!",
"browserLink": "https://coda.io/@coda/hello-world",
"imageLink": "string",
"discoverable": true,
"earnCredit": true,
"mode": "view",
"categories": []
},
"folder": {
"id": "fl-1Ab234",
"type": "folder",
"browserLink": "https://coda.io/docs?folderId=fl-1Ab234",
"name": "My docs"
},
"workspace": {
"id": "ws-1Ab234",
"type": "workspace",
"organizationId": "org-2Bc456",
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",
"name": "My workspace"
},
"workspaceId": "ws-1Ab234",
"folderId": "fl-1Ab234",
"requestId": "abc-123-def-456"
}
Get info about a doc
Returns metadata for the specified doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
200 Basic Coda doc metadata.
RESPONSE SCHEMA: application/json
id
required
string
ID of the Coda doc.

type
required
string
Value: "doc"
The type of this resource.

href
required
string <url>
API link to the Coda doc.

browserLink
required
string <url>
Browser-friendly link to the Coda doc.

name
required
string
Name of the doc.

owner
required
string <email>
Email address of the doc owner.

ownerName
required
string
Name of the doc owner.

createdAt
required
string <date-time>
Timestamp for when the doc was created.

updatedAt
required
string <date-time>
Timestamp for when the doc was last modified.

workspace
required
object (WorkspaceReference)
Reference to a Coda workspace.

folder
required
object (FolderReference)
Reference to a Coda folder.

workspaceId
required
string
Deprecated
ID of the Coda workspace containing this doc.

folderId
required
string
Deprecated
ID of the Coda folder containing this doc.

icon	
object (Icon)
Info about the icon.

docSize	
object (DocSize)
The number of components within a Coda doc.

sourceDoc	
object
Reference to a Coda doc from which this doc was copied, if any.

published	
object (DocPublished)
Information about the publishing state of the document.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>'
res = requests.get(uri, headers=headers).json()

print(f'The name of the doc is {res["name"]}')
# => The name of the doc is New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH",
"icon": {
"name": "string",
"type": "string",
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"
},
"name": "Product Launch Hub",
"owner": "user@example.com",
"ownerName": "Some User",
"docSize": {
"totalRowCount": 31337,
"tableAndViewCount": 42,
"pageCount": 10,
"overApiSizeLimit": false
},
"sourceDoc": {
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH"
},
"createdAt": "2018-04-11T00:18:57.946Z",
"updatedAt": "2018-04-11T00:18:57.946Z",
"published": {
"description": "Hello World!",
"browserLink": "https://coda.io/@coda/hello-world",
"imageLink": "string",
"discoverable": true,
"earnCredit": true,
"mode": "view",
"categories": []
},
"folder": {
"id": "fl-1Ab234",
"type": "folder",
"browserLink": "https://coda.io/docs?folderId=fl-1Ab234",
"name": "My docs"
},
"workspace": {
"id": "ws-1Ab234",
"type": "workspace",
"organizationId": "org-2Bc456",
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",
"name": "My workspace"
},
"workspaceId": "ws-1Ab234",
"folderId": "fl-1Ab234"
}
Delete doc
Deletes a doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
202 A result indicating that the doc was deleted.
RESPONSE SCHEMA: application/json
object (DocDelete)
The result of a doc deletion.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>'
res = requests.delete(uri, headers=headers).json()
Response samples
202401403404429
Content type
application/json

Copy
{ }
Update doc
Updates metadata for a doc. Note that updating a doc title requires you to be a Doc Maker in the applicable workspace.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for updating the doc.

title	
string
Title of the doc.

iconName	
string
Name of the icon.

Responses
200 Basic Coda doc metadata.
RESPONSE SCHEMA: application/json
object (DocUpdateResult)
The result of a doc update

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

PATCH
/docs/{docId}

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
{
"title": "Project Tracker",
"iconName": "rocket"
}
Response samples
200400401403404429
Content type
application/json

Copy
{ }
Permissions
This API lets you manage sharing and permissions for your docs.

Get sharing metadata
Returns metadata associated with sharing for this Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
200 Metadata associated with sharing permissions for a doc.
RESPONSE SCHEMA: application/json
canShare
required
boolean
When true, the user of the api can share

canShareWithWorkspace
required
boolean
When true, the user of the api can share with the workspace

canShareWithOrg
required
boolean
When true, the user of the api can share with the org

canCopy
required
boolean
When true, the user of the api can copy the doc

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/metadata

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/metadata'
res = requests.get(uri, headers=headers).json()

print(f'Can I share this doc with others? {res["canShare"]}')
# => Can I share this doc with others? true
Response samples
200401403404429
Content type
application/json

Copy
{
"canShare": true,
"canShareWithWorkspace": true,
"canShareWithOrg": true,
"canCopy": true
}
List permissions
Returns a list of permissions for this Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

Responses
200 List of permissions for a doc.
RESPONSE SCHEMA: application/json
items
required
Array of objects (Permission)
href
required
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/permissions

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/permissions'
res = requests.get(uri, headers=headers).json()

print(f'First user with access is {res["items"][0]["principal"]["email"]}')
# => First user with access is foo@bar.com
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/acl?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/acl?pageToken=eyJsaW1pd"
}
Add permission
Adds a new permission to the doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for adding the new permission.

access
required
string (AccessTypeNotNone)
Enum: "readonly" "write" "comment"
Type of access (excluding none).

principal
required
any (AddedPrincipal)
Metadata about a principal to add to a doc.

suppressEmail	
boolean
When true suppresses email notification

Responses
200 Confirmation that the request was applied.
RESPONSE SCHEMA: application/json
object (AddPermissionResult)
The result of sharing a doc.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

POST
/docs/{docId}/acl/permissions

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"access": "readonly",
"principal": {
"type": "email",
"email": "example@domain.com"
},
"suppressEmail": true
}
Response samples
200400401403404429
Content type
application/json

Copy
{ }
Delete permission
Deletes an existing permission.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

permissionId
required
string
Example: AbCDeFGH
ID of a permission on a doc.

Responses
200 Confirmation that the request was applied.
RESPONSE SCHEMA: application/json
object (DeletePermissionResult)
The result of deleting a permission.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}/acl/permissions/{permissionId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/permissions/<permission ID>'
res = requests.delete(uri, headers=headers, json=payload)

# => Revoke access to the doc
Response samples
200400401403404429
Content type
application/json

Copy
{ }
Search principals
Searches for user and group principals matching the query that this doc can be shared with. At most 20 results will be returned for both users and groups. If no query is given then no results are returned.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
query	
string
Example: query=Supercalifragilisticexpialidocious
Search term used to filter down results.

Responses
200 Search results for the given query.
RESPONSE SCHEMA: application/json
users
required
Array of objects (UserSummary)
groups
required
Array of objects (GroupPrincipal)
400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/principals/search

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/principals/search?search=foo'
res = requests.get(uri, headers=headers).json()

print(f'First user with access is {res["users"][0]["email"]}')
# => First user with access is foo@bar.com
Response samples
200400401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"users": [
{}
],
"groups": [
{}
]
}
Get ACL settings
Coda API (1.4.17)
API Support: help+api@coda.io
URL: https://coda.io
License: Coda Developer Terms

Introduction
The Coda API is a RESTful API that lets you programmatically interact with Coda docs:

- List and search Coda docs
- Create new docs and copy existing ones
- Share and publish docs
- Discover pages, tables, formulas, and controls
- Read, insert, upsert, update, and delete rows

We reserve the right to remove older APIs and functionality with a 3-month deprecation notice. Changes and new features will be announced in the Developers Central section of our Community, and in the API updates doc.

Getting Started
Our Getting Started Guide helps you learn the basics of working with the API and shows a few ways you can use it, including:

- Reading data from Coda tables and writing back to them
- Building a one-way sync from one Coda doc to another
- Automating reminders
- Syncing your Google Calendar to Coda

Using the API
Coda's REST API is designed to be straightforward to use. You can use any language and platform to make requests. Tools like Postman or Insomnia can help you get a feel for the API.

API Endpoint
This API uses a base path of https://coda.io/apis/v1.

Resource IDs and Links
Each resource instance retrieved via the API has the following fields:

- id: The resource's immutable ID
- type: The type of resource
- href: A fully qualified URI for the resource

Most resources can be queried by their name or ID. We recommend using IDs where possible, as names can be changed by users.

List Endpoints
Endpoints supporting listing of resources have the following fields:

- items: An array of listed resources, limited by query parameters
- nextPageLink: API link to the next page of results, if available
- nextPageToken: Page token for the next page of results, if available

The maximum page size may change at any time. Use the nextPageToken to check for more results, rather than relying on a specific result set size.

Doc IDs
While most object IDs must be discovered via the API, you may often need to get the ID of a specific Coda doc. Use the provided Doc ID Extractor tool to easily extract the ID from a Coda doc URL.

Rate Limiting
The Coda API has rate limits on requests per minute. Exceeding these limits will result in HTTP 429 errors. Current rate limits (subject to change without notice):

- Reading data: 100 requests per 6 seconds
- Writing data: 10 requests per 6 seconds
- Writing doc content: 5 requests per 10 seconds
- Listing docs: 4 requests per 6 seconds
- Reading analytics: 100 requests per 6 seconds
API scripts should implement retry logic for HTTP 429 errors.

Consistency
API edits may take a few seconds to become available. These endpoints return an HTTP 202 status code and a requestId, which can be used with the #getMutationStatus endpoint to check the edit status.

For the most up-to-date data when retrieving doc data, use the X-Coda-Doc-Version: latest header.

Volatile Formulas
Coda's "volatile" formulas (e.g., Today(), Now(), User()) behave differently with the API. Time-based values may only be current to the last doc edit, and user-based values may be blank or invalid.

Free and Paid Workspaces
The Coda API is available to all users free of charge, but API usage is subject to the user's role in the applicable workspace. For example, the #createDoc endpoint requires the API token owner to be a Doc Maker (or Admin) in the workspace.

Examples
This documentation provides code examples in Python, Unix shell, and Google Apps Script to help you get started with the Coda API.

Doc ID Extractor
Paste in a Coda doc URL
 Your doc ID is:    
Rate Limiting
The Coda API has rate limits on requests per minute. Exceeding these limits will result in HTTP 429 errors. Current rate limits (subject to change without notice):

- Reading data: 100 requests per 6 seconds
- Writing data: 10 requests per 6 seconds
- Writing doc content: 5 requests per 10 seconds
- Listing docs: 4 requests per 6 seconds
- Reading analytics: 100 requests per 6 seconds

Python examples
These examples use Python 3.6+. If you don't already have the requests module, use pip or easy_install to get it.

Shell examples
The shell examples are intended to be run in a Unix shell. If you're on Windows, you will need to install WSL.

These examples use the standard cURL utility to pull from the API, and then process it with jq to extract and format example output. If you don't already have it, you can either install it or run the command without it to see the raw JSON output.

Google Apps Script examples

Google Apps Script makes it easy to write code in a JavaScript-like syntax and access many Google products with built-in libraries. You can set up your scripts to run periodically, making it a good environment for writing tools without maintaining your own server.

Coda provides a library for Google Apps Script. To use it, go to Resources -> Libraries... and enter the following library ID: 15IQuWOk8MqT50FDWomh57UqWGH23gjsWVWYFms3ton6L-UHmefYHS9Vl. The library's source code is available here.

Google provides autocomplete for API functions and generated docs. Access these docs via the Libraries dialog by clicking on the library name. Required parameters included in the URL path are positional arguments in these functions, followed by the request body, if applicable. All remaining parameters can be specified in the options object.

OpenAPI/Swagger Spec
We offer an OpenAPI 3.0 specification to standardize our API and make it accessible:

- OpenAPI 3.0 spec - YAML
- OpenAPI 3.0 spec - JSON

Postman collection
To quickly prototype the API in Postman, use one of the links above to import the Coda API into a collection. Set the appropriate header and environment variables.

Client libraries
We currently support only Google Apps Script. To work with the Coda API, use standard network libraries for your language or the appropriate Swagger Generator tool to auto-generate Coda API client libraries. We do not guarantee compatibility of these autogenerated libraries with our API (e.g., some libraries may not work with Bearer authentication).

OpenAPI 3.0
Swagger Generator 3 can generate client libraries for these languages. It is relatively new and supports a limited set of languages.

Third-party client libraries
Some community members have written libraries to work with our API. These aren't officially supported by Coda but are listed here for convenience. (Let us know if you've written a library and would like it included here.)

- PHP by Daniel Stieber
- Node-RED by Mori Sugimoto
- NodeJS by Parker McMullin
- Ruby by Carlos Muñoz at Getro
- Python by Mikhail Beliansky
- Go by Artur Safin

Docs
Coda docs are foundational, top-level collaborative projects that contain pages. The API lets you list and search your docs to obtain basic metadata like titles and ownership information.

List available docs
Returns a list of Coda docs accessible by the user. These are returned in the same order as on the docs page: reverse chronological by the latest event relevant to the user (last viewed, edited, or shared).

AUTHORIZATIONS:
Bearer

QUERY PARAMETERS
- isOwner: boolean - Show only docs owned by the user.
- isPublished: boolean - Show only published docs.
- query: string - Example: query=Supercalifragilisticexpialidocious - Search term used to filter down results.
- sourceDoc: string - Show only docs copied from the specified doc ID.
- isStarred: boolean - If true, returns docs that are starred. If false, returns docs that are not starred.
- inGallery: boolean - Show only docs visible within the gallery.
- workspaceId: string - Show only docs belonging to the given workspace.
- folderId: string - Show only docs belonging to the given folder.
- limit: integer >= 1 - Default: 25 - Example: limit=10 - Maximum number of results to return in this query.
- pageToken: string - Example: pageToken=eyJsaW1pd - An opaque token used to fetch the next page of results.

Responses
- 200: List of Coda docs matching the query.
  - RESPONSE SCHEMA: application/json
    - items: Array of objects (Doc)
    - href: string <url> - API link to these results
    - nextPageToken: string (nextPageToken) - If specified, an opaque token used to fetch the next page of results.
    - nextPageLink: string <url> - If specified, a link that can be used to fetch the next page of results.
- 401: The API token is invalid or has expired.
- 403: The API token does not grant access to this resource.
- 404: The resource could not be located with the current API token.
- 429: The client has sent too many requests.

GET /docs

Request samples
- Python 3.7
- Shell
- Google Apps Script

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.
headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs?pageToken=eyJsaW1pd"
}
Create doc
Creates a new Coda doc, optionally copying an existing doc. Note that creating a doc requires you to be a Doc Maker in the applicable workspace (or be auto-promoted to one).

AUTHORIZATIONS:
Bearer
REQUEST BODY SCHEMA: application/json
Parameters for creating the doc.

title	
string
Title of the new doc. Defaults to 'Untitled'.

sourceDoc	
string
An optional doc ID from which to create a copy.

timezone	
string
The timezone to use for the newly created doc.

folderId	
string
The ID of the folder within which to create this doc. Defaults to your "My docs" folder in the oldest workspace you joined; this is subject to change. You can get this ID by opening the folder in the docs list on your computer and grabbing the folderId query parameter.

initialPage	
object
The contents of the initial page of the doc.

Responses
201 Info about the created doc.
RESPONSE SCHEMA: application/json
id
required
string
ID of the Coda doc.

type
required
string
Value: "doc"
The type of this resource.

href
required
string <url>
API link to the Coda doc.

browserLink
required
string <url>
Browser-friendly link to the Coda doc.

name
required
string
Name of the doc.

owner
required
string <email>
Email address of the doc owner.

ownerName
required
string
Name of the doc owner.

createdAt
required
string <date-time>
Timestamp for when the doc was created.

updatedAt
required
string <date-time>
Timestamp for when the doc was last modified.

workspace
required
object (WorkspaceReference)
Reference to a Coda workspace.

folder
required
object (FolderReference)
Reference to a Coda folder.

workspaceId
required
string
Deprecated
ID of the Coda workspace containing this doc.

folderId
required
string
Deprecated
ID of the Coda folder containing this doc.

icon	
object (Icon)
Info about the icon.

docSize	
object (DocSize)
The number of components within a Coda doc.

sourceDoc	
object
Reference to a Coda doc from which this doc was copied, if any.

published	
object (DocPublished)
Information about the publishing state of the document.

requestId	
string
An arbitrary unique identifier for this request.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
429 The client has sent too many requests.

POST
/docs

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"title": "Project Tracker",
"sourceDoc": "iJKlm_noPq",
"timezone": "America/Los_Angeles",
"folderId": "fl-ABcdEFgHJi",
"initialPage": {
"name": "Launch Status",
"subtitle": "See the status of launch-related tasks.",
"iconName": "rocket",
"imageUrl": "https://example.com/image.jpg",
"parentPageId": "canvas-tuVwxYz",
"pageContent": {}
}
}
Response samples
201400401403429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH",
"icon": {
"name": "string",
"type": "string",
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"
},
"name": "Product Launch Hub",
"owner": "user@example.com",
"ownerName": "Some User",
"docSize": {
"totalRowCount": 31337,
"tableAndViewCount": 42,
"pageCount": 10,
"overApiSizeLimit": false
},
"sourceDoc": {
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH"
},
"createdAt": "2018-04-11T00:18:57.946Z",
"updatedAt": "2018-04-11T00:18:57.946Z",
"published": {
"description": "Hello World!",
"browserLink": "https://coda.io/@coda/hello-world",
"imageLink": "string",
"discoverable": true,
"earnCredit": true,
"mode": "view",
"categories": []
},
"folder": {
"id": "fl-1Ab234",
"type": "folder",
"browserLink": "https://coda.io/docs?folderId=fl-1Ab234",
"name": "My docs"
},
"workspace": {
"id": "ws-1Ab234",
"type": "workspace",
"organizationId": "org-2Bc456",
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",
"name": "My workspace"
},
"workspaceId": "ws-1Ab234",
"folderId": "fl-1Ab234",
"requestId": "abc-123-def-456"
}
Get info about a doc
Returns metadata for the specified doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
200 Basic Coda doc metadata.
RESPONSE SCHEMA: application/json
id
required
string
ID of the Coda doc.

type
required
string
Value: "doc"
The type of this resource.

href
required
string <url>
API link to the Coda doc.

browserLink
required
string <url>
Browser-friendly link to the Coda doc.

name
required
string
Name of the doc.

owner
required
string <email>
Email address of the doc owner.

ownerName
required
string
Name of the doc owner.

createdAt
required
string <date-time>
Timestamp for when the doc was created.

updatedAt
required
string <date-time>
Timestamp for when the doc was last modified.

workspace
required
object (WorkspaceReference)
Reference to a Coda workspace.

folder
required
object (FolderReference)
Reference to a Coda folder.

workspaceId
required
string
Deprecated
ID of the Coda workspace containing this doc.

folderId
required
string
Deprecated
ID of the Coda folder containing this doc.

icon	
object (Icon)
Info about the icon.

docSize	
object (DocSize)
The number of components within a Coda doc.

sourceDoc	
object
Reference to a Coda doc from which this doc was copied, if any.

published	
object (DocPublished)
Information about the publishing state of the document.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>'
res = requests.get(uri, headers=headers).json()

print(f'The name of the doc is {res["name"]}')
# => The name of the doc is New Document
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH",
"icon": {
"name": "string",
"type": "string",
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"
},
"name": "Product Launch Hub",
"owner": "user@example.com",
"ownerName": "Some User",
"docSize": {
"totalRowCount": 31337,
"tableAndViewCount": 42,
"pageCount": 10,
"overApiSizeLimit": false
},
"sourceDoc": {
"id": "AbCDeFGH",
"type": "doc",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH",
"browserLink": "https://coda.io/d/_dAbCDeFGH"
},
"createdAt": "2018-04-11T00:18:57.946Z",
"updatedAt": "2018-04-11T00:18:57.946Z",
"published": {
"description": "Hello World!",
"browserLink": "https://coda.io/@coda/hello-world",
"imageLink": "string",
"discoverable": true,
"earnCredit": true,
"mode": "view",
"categories": []
},
"folder": {
"id": "fl-1Ab234",
"type": "folder",
"browserLink": "https://coda.io/docs?folderId=fl-1Ab234",
"name": "My docs"
},
"workspace": {
"id": "ws-1Ab234",
"type": "workspace",
"organizationId": "org-2Bc456",
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",
"name": "My workspace"
},
"workspaceId": "ws-1Ab234",
"folderId": "fl-1Ab234"
}
Delete doc
Deletes a doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
202 A result indicating that the doc was deleted.
RESPONSE SCHEMA: application/json
object (DocDelete)
The result of a doc deletion.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>'
res = requests.delete(uri, headers=headers).json()
Response samples
202401403404429
Content type
application/json

Copy
{ }
Update doc
Updates metadata for a doc. Note that updating a doc title requires you to be a Doc Maker in the applicable workspace.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for updating the doc.

title	
string
Title of the doc.

iconName	
string
Name of the icon.

Responses
200 Basic Coda doc metadata.
RESPONSE SCHEMA: application/json
object (DocUpdateResult)
The result of a doc update

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

PATCH
/docs/{docId}

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
{
"title": "Project Tracker",
"iconName": "rocket"
}
Response samples
200400401403404429
Content type
application/json

Copy
{ }
Permissions
This API lets you manage sharing and permissions for your docs.

Get sharing metadata
Returns metadata associated with sharing for this Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
200 Metadata associated with sharing permissions for a doc.
RESPONSE SCHEMA: application/json
canShare
required
boolean
When true, the user of the api can share

canShareWithWorkspace
required
boolean
When true, the user of the api can share with the workspace

canShareWithOrg
required
boolean
When true, the user of the api can share with the org

canCopy
required
boolean
When true, the user of the api can copy the doc

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/metadata

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/metadata'
res = requests.get(uri, headers=headers).json()

print(f'Can I share this doc with others? {res["canShare"]}')
# => Can I share this doc with others? true
Response samples
200401403404429
Content type
application/json

Copy
{
"canShare": true,
"canShareWithWorkspace": true,
"canShareWithOrg": true,
"canCopy": true
}
List permissions
Returns a list of permissions for this Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

Responses
200 List of permissions for a doc.
RESPONSE SCHEMA: application/json
items
required
Array of objects (Permission)
href
required
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/permissions

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/permissions'
res = requests.get(uri, headers=headers).json()

print(f'First user with access is {res["items"][0]["principal"]["email"]}')
# => First user with access is foo@bar.com
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/acl?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/acl?pageToken=eyJsaW1pd"
}
Add permission
Adds a new permission to the doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for adding the new permission.

access
required
string (AccessTypeNotNone)
Enum: "readonly" "write" "comment"
Type of access (excluding none).

principal
required
any (AddedPrincipal)
Metadata about a principal to add to a doc.

suppressEmail	
boolean
When true suppresses email notification

Responses
200 Confirmation that the request was applied.
RESPONSE SCHEMA: application/json
object (AddPermissionResult)
The result of sharing a doc.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

POST
/docs/{docId}/acl/permissions

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"access": "readonly",
"principal": {
"type": "email",
"email": "example@domain.com"
},
"suppressEmail": true
}
Response samples
200400401403404429
Content type
application/json

Copy
{ }
Delete permission
Deletes an existing permission.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

permissionId
required
string
Example: AbCDeFGH
ID of a permission on a doc.

Responses
200 Confirmation that the request was applied.
RESPONSE SCHEMA: application/json
object (DeletePermissionResult)
The result of deleting a permission.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}/acl/permissions/{permissionId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/permissions/<permission ID>'
res = requests.delete(uri, headers=headers, json=payload)

# => Revoke access to the doc
Response samples
200400401403404429
Content type
application/json

Copy
{ }
Search principals
Searches for user and group principals matching the query that this doc can be shared with. At most 20 results will be returned for both users and groups. If no query is given then no results are returned.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
query	
string
Example: query=Supercalifragilisticexpialidocious
Search term used to filter down results.

Responses
200 Search results for the given query.
RESPONSE SCHEMA: application/json
users
required
Array of objects (UserSummary)
groups
required
Array of objects (GroupPrincipal)
400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/principals/search

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/principals/search?search=foo'
res = requests.get(uri, headers=headers).json()

print(f'First user with access is {res["users"][0]["email"]}')
# => First user with access is foo@bar.com
Response samples
200400401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"users": [
{}
],
"groups": [
{}
]
}
Get ACL settings
Returns settings associated with ACLs for this Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
200 Settings associated with access control for a doc.
RESPONSE SCHEMA: application/json
allowEditorsToChangePermissions
required
boolean
When true, allows editors to change doc permissions. When false, only doc owner can change doc permissions.

allowCopying
required
boolean
When true, allows doc viewers to copy the doc.

allowViewersToRequestEditing
required
boolean
When true, allows doc viewers to request editing permissions.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/acl/settings

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/acl/settings'
res = requests.get(uri, headers=headers).json()

print(f'Can editors change sharing permissions? {res["allowEditorsToChangePermissions"]}')
# => Can editors change sharing permissions? false
Response samples
200401403404429
Content type
application/json

Copy
{
"allowEditorsToChangePermissions": true,
"allowCopying": true,
"allowViewersToRequestEditing": true
}
Update ACL settings
Update settings associated with ACLs for this Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for updating the ACL settings.

allowEditorsToChangePermissions	
boolean
When true, allows editors to change doc permissions. When false, only doc owner can change doc permissions.

allowCopying	
boolean
When true, allows doc viewers to copy the doc.

allowViewersToRequestEditing	
boolean
When true, allows doc viewers to request editing permissions.

Responses
200 Settings associated with access control for a doc.
RESPONSE SCHEMA: application/json
allowEditorsToChangePermissions
required
boolean
When true, allows editors to change doc permissions. When false, only doc owner can change doc permissions.

allowCopying
required
boolean
When true, allows doc viewers to copy the doc.

allowViewersToRequestEditing
required
boolean
When true, allows doc viewers to request editing permissions.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

PATCH
/docs/{docId}/acl/settings

Request samples
Payload
Content type
application/json

Copy
{
"allowEditorsToChangePermissions": true,
"allowCopying": true,
"allowViewersToRequestEditing": true
}
Response samples
200401403404429
Content type
application/json

Copy
{
"allowEditorsToChangePermissions": true,
"allowCopying": true,
"allowViewersToRequestEditing": true
}
Publishing
Coda docs can be published publicly and associated with categories to help the world discover them. This API lets you manage the publishing settings of your docs.

Get doc categories
Gets all available doc categories.

AUTHORIZATIONS:
Bearer
Responses
200 List of doc categories
RESPONSE SCHEMA: application/json
items
required
Array of objects (DocCategory)
Categories for the doc.

401 The API token is invalid or has expired.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/categories

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/categories'
res = requests.get(uri, headers=headers).json()

print(f'Category count: {res["categories"].length}')
# => Category count: 10
Response samples
200401404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
]
}
Publish doc
Update publish settings for a doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for changing publish settings.

slug	
string
Slug for the published doc.

discoverable	
boolean
If true, indicates that the doc is discoverable.

earnCredit	
boolean
If true, new users may be required to sign in to view content within this document. You will receive Coda credit for each user who signs up via your doc.

categoryNames	
Array of strings
The names of categories to apply to the document.

mode	
string (DocPublishMode)
Enum: "view" "play" "edit"
Which interaction mode the published doc should use.

Responses
202 Confirmation that the publish request was accepted.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

PUT
/docs/{docId}/publish

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"slug": "my-doc",
"discoverable": true,
"earnCredit": true,
"categoryNames": [
"Project management"
],
"mode": "view"
}
Response samples
202400401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456"
}
Unpublish doc
Unpublishes a doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

Responses
200 A result indicating that the doc was unpublished.
RESPONSE SCHEMA: application/json
object (UnpublishResult)
The result of unpublishing a doc.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}/publish

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/publish'
res = requests.unpublishDoc(uri, headers=headers).json()
Response samples
200401403404429
Content type
application/json

Copy
{ }
Pages
Pages in Coda offer canvases containing rich text, tables, controls, and other objects. At this time, this API lets you list and access pages in a doc.

List pages
Returns a list of pages in a Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

Responses
200 List of pages.
RESPONSE SCHEMA: application/json
items
required
Array of objects (Page)
href	
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/pages

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages'
res = requests.get(uri, headers=headers).json()

print(f'The name of the first page is {res["items"][0]["name"]}')
# => The name of the first page is Page 1
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/pages?pageToken=eyJsaW1pd"
}
Create a page
Create a new page in a doc. Note that creating a page requires you to be a Doc Maker in the applicable workspace.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

REQUEST BODY SCHEMA: application/json
Parameters for creating a page.

name	
string
Name of the page.

subtitle	
string
Subtitle of the page.

iconName	
string
Name of the icon.

imageUrl	
string
Url of the cover image to use.

parentPageId	
string
The ID of this new page's parent, if creating a subpage.

pageContent	
object or object or object or object (PageCreateContent)
Content that can be added to a page at creation time, either text (or rich text) or a URL to create a full-page embed.

Responses
202 A result indicating that the creation request was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

id
required
string
ID of the created page.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

POST
/docs/{docId}/pages

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"name": "Launch Status",
"subtitle": "See the status of launch-related tasks.",
"iconName": "rocket",
"imageUrl": "https://example.com/image.jpg",
"parentPageId": "canvas-tuVwxYz",
"pageContent": {
"type": "canvas",
"canvasContent": {}
}
}
Response samples
202400401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456",
"id": "canvas-tuVwxYz"
}
Get a page
Returns details about a page.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

pageIdOrName
required
string
Example: canvas-IjkLmnO
ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected.

Responses
200 Info about a page.
RESPONSE SCHEMA: application/json
id
required
string
ID of the page.

type
required
string
Value: "page"
The type of this resource.

href
required
string <url>
API link to the page.

name
required
string
Name of the page.

isHidden
required
boolean
Whether the page is hidden in the UI.

isEffectivelyHidden
required
boolean
Whether the page or any of its parents is hidden in the UI.

browserLink
required
string <url>
Browser-friendly link to the page.

children
required
Array of objects (PageReference)
contentType
required
string (PageType)
Enum: "canvas" "embed" "syncPage"
The type of a page in a doc.

subtitle	
string
Subtitle of the page.

icon	
object (Icon)
Info about the icon.

image	
object (Image)
Info about the image.

parent	
object (PageReference)
Reference to a page.

authors	
Array of objects (PersonValue)
Authors of the page

createdAt	
string <date-time>
Timestamp for when the page was created.

createdBy	
object (PersonValue)
A named reference to a person, where the person is identified by email address.

updatedAt	
string <date-time>
Timestamp for when page content was last modified.

updatedBy	
object (PersonValue)
A named reference to a person, where the person is identified by email address.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
410 The resource has been deleted.
429 The client has sent too many requests.

GET
/docs/{docId}/pages/{pageIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>'
res = requests.get(uri, headers=headers).json()

print(f'The name of this page is {res["name"]}')
# => The name of this page is Page 1
Response samples
200401403404410429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "canvas-IjkLmnO",
"type": "page",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",
"name": "Launch Status",
"subtitle": "See the status of launch-related tasks.",
"icon": {
"name": "string",
"type": "string",
"browserLink": "https://cdn.coda.io/icons/png/color/icon-32.png"
},
"image": {
"browserLink": "https://codahosted.io/docs/nUYhlXysYO/blobs/bl-lYkYKNzkuT/3f879b9ecfa27448",
"type": "string",
"width": 800,
"height": 600
},
"contentType": "canvas",
"isHidden": true,
"isEffectivelyHidden": true,
"parent": {
"id": "canvas-IjkLmnO",
"type": "page",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",
"name": "Launch Status"
},
"children": [
{}
],
"authors": [
{}
],
"createdAt": "2018-04-11T00:18:57.946Z",
"createdBy": {
"@context": "http://schema.org/",
"@type": "ImageObject",
"additionalType": "string",
"name": "Alice Atkins",
"email": "alice@atkins.com"
},
"updatedAt": "2018-04-11T00:18:57.946Z",
"updatedBy": {
"@context": "http://schema.org/",
"@type": "ImageObject",
"additionalType": "string",
"name": "Alice Atkins",
"email": "alice@atkins.com"
}
}
Update a page
Update properties for a page. Note that updating a page title or icon requires you to be a Doc Maker in the applicable workspace.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

pageIdOrName
required
string
Example: canvas-IjkLmnO
ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected.

REQUEST BODY SCHEMA: application/json
Parameters for updating a page.

name	
string
Name of the page.

subtitle	
string
Subtitle of the page.

iconName	
string
Name of the icon.

imageUrl	
string
Url of the cover image to use.

isHidden	
boolean
Whether the page is hidden or not. Note that for pages that cannot be hidden, like the sole top-level page in a doc, this will be ignored.

contentUpdate	
object
Content with which to update an existing page.

Responses
202 A result indicating that the update was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

id
required
string
ID of the updated page.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

PUT
/docs/{docId}/pages/{pageIdOrName}

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"name": "Launch Status",
"subtitle": "See the status of launch-related tasks.",
"iconName": "rocket",
"imageUrl": "https://example.com/image.jpg",
"isHidden": true,
"contentUpdate": {
"insertionMode": "append",
"canvasContent": {}
}
}
Response samples
202400401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456",
"id": "canvas-tuVwxYz"
}
Delete a page
Deletes the specified page.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

pageIdOrName
required
string
Example: canvas-IjkLmnO
ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected.

Responses
202 A result indicating that the delete was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

id
required
string
ID of the page to be deleted.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}/pages/{pageIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>'
req = requests.delete(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Deleted page')
# => Deleted page
Response samples
202400401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456",
"id": "canvas-tuVwxYz"
}
Begin content export
Initiate an export of content for the given page.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

pageIdOrName
required
string
Example: canvas-IjkLmnO
ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected.

REQUEST BODY SCHEMA: application/json
Parameters for requesting a page content export.

outputFormat
required
string (PageContentOutputFormat)
Enum: "html" "markdown"
Supported output content formats that can be requested for getting content for an existing page.

Responses
202 Export page content response.
RESPONSE SCHEMA: application/json
id
required
string
The identifier of this export request.

status
required
string
The status of this export.

href
required
string
The URL that reports the status of this export. Poll this URL to get the content URL when the export has completed.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
410 The resource has been deleted.
429 The client has sent too many requests.

POST
/docs/{docId}/pages/{pageIdOrName}/export

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
{
"outputFormat": "html"
}
Response samples
202400401403404410429
Content type
application/json

Copy
{
"id": "AbCDeFGH",
"status": "complete",
"href": "https://coda.io/apis/v1/docs/somedoc/pages/somepage/export/some-request-id"
}
Content export status
Check the status of a page content export

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

pageIdOrName
required
string
Example: canvas-IjkLmnO
ID or name of the page. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If you provide a name and there are multiple pages with the same name, an arbitrary one will be selected.

requestId
required
string
Example: abc-123-def-456
ID of the request.

Responses
200 Info about the page content export request.
RESPONSE SCHEMA: application/json
id
required
string
The identifier of this export request.

status
required
string
The status of this export.

href
required
string
The URL that reports the status of this export.

downloadLink	
string
Once the export completes, the location where the resulting export file can be downloaded; this link typically expires after a short time. Call this method again to get a fresh link.

error	
string
Message describing an error, if this export failed.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
410 The resource has been deleted.
429 The client has sent too many requests.

GET
/docs/{docId}/pages/{pageIdOrName}/export/{requestId}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/pages/<page ID>/export/<request ID>'
res = requests.get(uri, headers=headers).json()

print(f'Request status: {res["status"]}')
# => Request status: completed
Response samples
200401403404410429
Content type
application/json

Copy
{
"id": "AbCDeFGH",
"status": "complete",
"href": "https://coda.io/apis/v1/docs/somedoc/pages/somepage/export/some-request-id",
"downloadLink": "https://coda.io/blobs/DOC_EXPORT_RENDERING/some-request-id",
"error": "string"
}
Automations
This API allows you to trigger automations.

Trigger automation
Triggers webhook-invoked automation

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

ruleId
required
string
Example: grid-auto-b3Jmey6jBS
ID of the automation rule.

REQUEST BODY SCHEMA: 
application/json
application/json
Payload for webhook

property name*
additional property
any
Responses
202 A result indicating that the automation trigger was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
422 Unable to process the request.
429 The client has sent too many requests.

POST
/docs/{docId}/hooks/automation/{ruleId}

Request samples
Payload
Content type

application/json
application/json

Copy
{
"message": "The doc that brings words, data, & teams together."
}
Response samples
202400401403404422429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456"
}
Tables
List tables
Returns a list of tables in a Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

sortBy	
string (SortBy)
Value: "name"
Example: sortBy=name
Determines how to sort the given objects.

tableTypes	
Array of strings (TableType)
Items Enum: "table" "view"
Example: tableTypes=table,view
Comma-separated list of table types to include in results. If omitted, includes both tables and views.

Responses
200 List of tables or views in a doc.
RESPONSE SCHEMA: application/json
items
required
Array of objects (TableReference)
href	
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/tables

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables'
res = requests.get(uri, headers=headers).json()

print(f'The name of the first table is {res["items"][0]["name"]}')
# => The name of the first table is To-do List
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/tables?pageToken=eyJsaW1pd"
}
Get a table
Returns details about a specific table or view.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

QUERY PARAMETERS
useUpdatedTableLayouts	
boolean
Return "detail" and "form" for the layout field of detail and form layouts respectively (instead of "masterDetail" for both)

Responses
200 Info about a table.
RESPONSE SCHEMA: application/json
id
required
string
ID of the table.

type
required
string
Value: "table"
The type of this resource.

tableType
required
string (TableType)
Enum: "table" "view"
href
required
string <url>
API link to the table.

name
required
string
Name of the table.

parent
required
object (PageReference)
Reference to a page.

browserLink
required
string <url>
Browser-friendly link to the table.

displayColumn
required
object (ColumnReference)
Reference to a column.

rowCount
required
integer
Total number of rows in the table.

sorts
required
Array of objects (Sort)
Any sorts applied to the table.

layout
required
string (Layout)
Enum: "default" "areaChart" "barChart" "bubbleChart" "calendar" "card" "detail" "form" "ganttChart" "lineChart" "masterDetail" "pieChart" "scatterChart" "slide" "wordCloud"
Layout type of the table or view.

createdAt
required
string <date-time>
Timestamp for when the table was created.

updatedAt
required
string <date-time>
Timestamp for when the table was last modified.

parentTable	
object (TableReference)
Reference to a table or view.

filter	
object
Detailed information about the filter formula for the table, if applicable.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/tables/{tableIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>'
res = requests.get(uri, headers=headers).json()

print(f'Table {res["name"]} has {res["rowCount"]} rows')
# => Table To-do List has 2 rows
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "grid-pqRst-U",
"type": "table",
"tableType": "table",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",
"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",
"name": "Tasks",
"parent": {
"id": "canvas-IjkLmnO",
"type": "page",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",
"name": "Launch Status"
},
"parentTable": {
"id": "grid-pqRst-U",
"type": "table",
"tableType": "table",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",
"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",
"name": "Tasks",
"parent": {}
},
"displayColumn": {
"id": "c-tuVwxYz",
"type": "column",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns/c-tuVwxYz"
},
"rowCount": 130,
"sorts": [
{}
],
"layout": "default",
"filter": {
"valid": true,
"isVolatile": false,
"hasUserFormula": false,
"hasTodayFormula": false,
"hasNowFormula": false
},
"createdAt": "2018-04-11T00:18:57.946Z",
"updatedAt": "2018-04-11T00:18:57.946Z"
}
Columns
While columns in Coda have user-friendly names, they also have immutable IDs that are used when reading and writing rows. These endpoints let you query the columns in a table and get basic information about them.

List columns
Returns a list of columns in a table.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

visibleOnly	
boolean
Example: visibleOnly=true
If true, returns only visible columns for the table. This parameter only applies to base tables, and not views.

Responses
200 List of columns in the table.
RESPONSE SCHEMA: application/json
items
required
Array of objects (Column)
href	
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/tables/{tableIdOrName}/columns

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/columns'
res = requests.get(uri, headers=headers).json()

print(f'This table\'s columns: {", ".join(c["name"] for c in res["items"])}')
# => This table's columns: Task, Duration (hr), Duration (min)
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns?pageToken=eyJsaW1pd"
}
Get a column
Returns details about a column in a table.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

columnIdOrName
required
string
Example: c-tuVwxYz
ID or name of the column. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

Responses
200 Info about a column.
RESPONSE SCHEMA: application/json
id
required
string
ID of the column.

type
required
string
Value: "column"
The type of this resource.

href
required
string <url>
API link to the column.

name
required
string
Name of the column.

parent
required
object (TableReference)
Reference to a table or view.

format
required
any (ColumnFormat)
Format of a column.

display	
boolean
Whether the column is the display column.

calculated	
boolean
Whether the column has a formula set on it.

formula	
string
Formula on the column.

defaultValue	
string
Default value formula for the column.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/tables/{tableIdOrName}/columns/{columnIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/columns/<column ID>'
res = requests.get(uri, headers=headers).json()

is_default = res.get("display", False)
print(f'Column {res["name"]} {"is" if is_default else "is not"} the display column')
# => Column Task is the display column
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "c-tuVwxYz",
"type": "column",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/columns/c-tuVwxYz",
"name": "Completed",
"display": true,
"calculated": true,
"formula": "thisRow.Created()",
"defaultValue": "Test",
"format": {
"type": "text",
"isArray": true,
"label": "Click me",
"disableIf": "False()",
"action": "OpenUrl(\"www.google.com\")"
},
"parent": {
"id": "grid-pqRst-U",
"type": "table",
"tableType": "table",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",
"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",
"name": "Tasks",
"parent": {}
}
}
Rows
You'll likely use this part of the API the most. These endpoints let you retrieve row data from tables in Coda as well as create, upsert, update, and delete them. Most of these endpoints work for both base tables and views, but for inserting/upsering rows, you must use a base table.

List table rows
Returns a list of rows in a table.

Value results
The valueFormat parameter dictates in what format the API should return values for individual cells.

simple (default): Returns cell values as the following JSON values: string, number, or boolean. Array values (like multiselects) are returned as comma-delimited strings.
simpleWithArrays: Singleton values are returned as simple. Array values are returned as JSON arrays and the values within are simple values (including nested arrays).
rich: If applicable, returns many values with further encoding, allowing API users to have lossless access to data in Coda.
For text values, returns data in Markdown syntax. If the text field is simple text (e.g. has no formatting), the field will be fully escaped with triple-ticks. E.g ```This is plain text```
For currency, lookup, image, person and hyperlink values, the value will be encoded in JSON-LD format.
  // Currency
  {
    "@context": "http://schema.org",
    "@type": "MonetaryAmount",
    "currency": "USD",
    "amount": 42.42
  }

  // Lookup
  {
    "@context": "http://schema.org",
    "@type": "StructuredValue",
    "additionalType": "row",
    "name": "Row Name",
    "rowId": "i-123456789",
    "tableId": "grid-123456789",
    "tableUrl": "https://coda.io/d/_d123456789/grid-123456789",
    "url": "https://coda.io/d/_d123456789/grid-123456789#_r42",
  }

  // Hyperlink
  {
    "@context": "http://schema.org",
    "@type": "WebPage",
    "name": "Coda",
    "url": "https://coda.io"
  }

  // Image
  {
    "@context": "http://schema.org",
    "@type": "ImageObject",
    "name": "Coda logo",
    "url": "https://coda.io/logo.jpg"
  }

  // People
  {
    "@context": "http://schema.org",
    "@type": "Person",
    "name": "Art Vandalay",
    "email": "art@vandalayindustries.com"
  }
AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

QUERY PARAMETERS
query	
string
Example: query=c-tuVwxYz:"Apple"
Query used to filter returned rows, specified as <column_id_or_name>:<value>. If you'd like to use a column name instead of an ID, you must quote it (e.g., "My Column":123). Also note that value is a JSON value; if you'd like to use a string, you must surround it in quotes (e.g., "groceries").

sortBy	
string (RowsSortBy)
Enum: "createdAt" "natural" "updatedAt"
Specifies the sort order of the rows returned. If left unspecified, rows are returned by creation time ascending. "UpdatedAt" sort ordering is the order of rows based upon when they were last updated. This does not include updates to calculated values. "Natural" sort ordering is the order that the rows appear in the table view in the application. This ordering is only meaningfully defined for rows that are visible (unfiltered). Because of this, using this sort order will imply visibleOnly=true, that is, to only return visible rows. If you pass sortBy=natural and visibleOnly=false explicitly, this will result in a Bad Request error as this condition cannot be satisfied.

useColumnNames	
boolean
Example: useColumnNames=true
Use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors.

valueFormat	
string (ValueFormat)
Enum: "simple" "simpleWithArrays" "rich"
The format that cell values are returned as.

visibleOnly	
boolean
Example: visibleOnly=true
If true, returns only visible rows and columns for the table.

limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

syncToken	
string
Example: syncToken=eyJsaW1pd
An opaque token returned from a previous call that can be used to return results that are relevant to the query since the call where the syncToken was generated.

Responses
200 List of rows in the table.
RESPONSE SCHEMA: application/json
items
required
Array of objects (Row)
href	
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

nextSyncToken	
string (nextSyncToken)
If specified, an opaque token that can be passed back later to retrieve new results that match the parameters specified when the sync token was created.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/tables/{tableIdOrName}/rows

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows'
params = {
  'query': '<column ID>:"Work out"',
}
req = requests.get(uri, headers=headers, params=params)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Matching rows: {len(res["items"])}')
# => Matching rows: 1
Response samples
200400401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows?pageToken=eyJsaW1pd",
"nextSyncToken": "eyJsaW1pd"
}
Insert/upsert rows
Inserts rows into a table, optionally updating existing rows if any upsert key columns are provided. This endpoint will always return a 202, so long as the doc and table exist and are accessible (and the update is structurally valid). Row inserts/upserts are generally processed within several seconds. Note: this endpoint only works for base tables, not views. When upserting, if multiple rows match the specified key column(s), they will all be updated with the specified value.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

QUERY PARAMETERS
disableParsing	
boolean
Example: disableParsing=true
If true, the API will not attempt to parse the data in any way.

REQUEST BODY SCHEMA: application/json
Rows to insert or upsert.

rows
required
Array of objects (RowEdit)
keyColumns	
Array of strings
Optional column IDs, URLs, or names (fragile and discouraged), specifying columns to be used as upsert keys.

Responses
202 A result indicating that the upsert was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

addedRowIds	
Array of strings
Row IDs for rows that will be added. Only applicable when keyColumns is not set or empty.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

POST
/docs/{docId}/tables/{tableIdOrName}/rows

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"rows": [
{}
],
"keyColumns": [
"c-bCdeFgh"
]
}
Response samples
202400401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"requestId": "abc-123-def-456",
"addedRowIds": [
"i-bCdeFgh",
"i-CdEfgHi"
]
}
Delete multiple rows
Deletes the specified rows from the table or view. This endpoint will always return a 202. Row deletions are generally processed within several seconds.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

REQUEST BODY SCHEMA: application/json
Rows to delete.

rowIds
required
Array of strings
Row IDs to delete.

Responses
202 A result indicating that the delete was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

rowIds
required
Array of strings
Row IDs to delete.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}/tables/{tableIdOrName}/rows

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"rowIds": [
"i-bCdeFgh",
"i-CdEfgHi"
]
}
Response samples
202400401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"requestId": "abc-123-def-456",
"rowIds": [
"i-bCdeFgh",
"i-CdEfgHi"
]
}
Get a row
Returns details about a row in a table.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

rowIdOrName
required
string
Example: i-tuVwxYz
ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected.

QUERY PARAMETERS
useColumnNames	
boolean
Example: useColumnNames=true
Use column names instead of column IDs in the returned output. This is generally discouraged as it is fragile. If columns are renamed, code using original names may throw errors.

valueFormat	
string (ValueFormat)
Enum: "simple" "simpleWithArrays" "rich"
The format that cell values are returned as.

Responses
200 Info about a row. If this row was retrieved by name, only one matching row will be returned, with no guarantees as to which one it is.
RESPONSE SCHEMA: application/json
id
required
string
ID of the row.

type
required
string
Value: "row"
The type of this resource.

href
required
string <url>
API link to the row.

name
required
string
The display name of the row, based on its identifying column.

index
required
integer
Index of the row within the table.

browserLink
required
string <url>
Browser-friendly link to the row.

createdAt
required
string <date-time>
Timestamp for when the row was created.

updatedAt
required
string <date-time>
Timestamp for when the row was last modified.

values
required
object
Values for a specific row, represented as a hash of column IDs (or names with useColumnNames) to values.

parent
required
object (TableReference)
Reference to a table or view.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows/<row ID>'
req = requests.get(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Row values are: {", ".join(str(v) for v in res["values"].values())}')
# => Row values are: Get groceries, 1, 60
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "i-tuVwxYz",
"type": "row",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U/rows/i-RstUv-W",
"name": "Apple",
"index": 7,
"browserLink": "https://coda.io/d/_dAbCDeFGH#Teams-and-Tasks_tpqRst-U/_rui-tuVwxYz",
"createdAt": "2018-04-11T00:18:57.946Z",
"updatedAt": "2018-04-11T00:18:57.946Z",
"values": {
"c-tuVwxYz": "Apple",
"c-bCdeFgh": []
},
"parent": {
"id": "grid-pqRst-U",
"type": "table",
"tableType": "table",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/tables/grid-pqRst-U",
"browserLink": "https://coda.io/d/_dAbCDeFGH/#Teams-and-Tasks_tpqRst-U",
"name": "Tasks",
"parent": {}
}
}
Update row
Updates the specified row in the table. This endpoint will always return a 202, so long as the row exists and is accessible (and the update is structurally valid). Row updates are generally processed within several seconds. When updating using a name as opposed to an ID, an arbitrary row will be affected.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

rowIdOrName
required
string
Example: i-tuVwxYz
ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected.

QUERY PARAMETERS
disableParsing	
boolean
Example: disableParsing=true
If true, the API will not attempt to parse the data in any way.

REQUEST BODY SCHEMA: application/json
Row update.

row
required
object (RowEdit)
An edit made to a particular row.

Responses
202 A result indicating that the update was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

id
required
string
ID of the updated row.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

PUT
/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

Request samples
PayloadPython 3.7ShellGoogle Apps Script
Content type
application/json

Copy
Expand allCollapse all
{
"row": {
"cells": []
}
}
Response samples
202400401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456",
"id": "i-tuVwxYz"
}
Delete row
Deletes the specified row from the table or view. This endpoint will always return a 202, so long as the row exists and is accessible (and the update is structurally valid). Row deletions are generally processed within several seconds. When deleting using a name as opposed to an ID, an arbitrary row will be removed.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

rowIdOrName
required
string
Example: i-tuVwxYz
ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected.

Responses
202 A result indicating that the deletion was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

id
required
string
ID of the row to be deleted.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

DELETE
/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows/<row ID>'
req = requests.delete(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Deleted row {res["id"]}')
# => Deleted row <row ID>
Response samples
202401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456",
"id": "i-tuVwxYz"
}
Push a button
Pushes a button on a row in a table. Authorization note: This action is available to API tokens that are authorized to write to the table. However, the underlying button can perform any action on the document, including writing to other tables and performing Pack actions.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

tableIdOrName
required
string
Example: grid-pqRst-U
ID or name of the table. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

rowIdOrName
required
string
Example: i-tuVwxYz
ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected.

columnIdOrName
required
string
Example: c-tuVwxYz
ID or name of the column. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

Responses
202 A result indicating that the push button action was queued for processing.
RESPONSE SCHEMA: application/json
requestId
required
string
An arbitrary unique identifier for this request.

rowId
required
string
ID of the row where the button exists.

columnId
required
string
ID of the column where the button exists.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

POST
/docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName}/buttons/{columnIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/tables/<table ID>/rows/<row ID>/buttons/<column ID>'
req = requests.post(uri, headers=headers)
req.raise_for_status() # Throw if there was an error.
res = req.json()
print(f'Pushed button')
# => Pushed button
Response samples
202400401403404429
Content type
application/json

Copy
{
"requestId": "abc-123-def-456",
"rowId": "i-tuVwxYz",
"columnId": "i-tuVwxYz"
}
Formulas
Formulas can be great for performing one-off computations, or used with tables and other formulas to compute a single value. With this API, you can discover formulas in a doc and obtain computed results.

List formulas
Returns a list of named formulas in a Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

sortBy	
string (SortBy)
Value: "name"
Example: sortBy=name
Determines how to sort the given objects.

Responses
200 List of formulas that have names in a doc.
RESPONSE SCHEMA: application/json
items
required
Array of objects (FormulaReference)
href	
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/formulas

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/formulas'
res = requests.get(uri, headers=headers).json()

print(f'This doc\'s formulas are: {", ".join(i["name"] for i in res["items"])}')
# => This doc's formulas are: Total Duration, Time Now
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas?pageToken=eyJsaW1pd"
}
Get a formula
Returns info on a formula.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

formulaIdOrName
required
string
Example: f-fgHijkLm
ID or name of the formula. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

Responses
200 Details about a formula.
RESPONSE SCHEMA: application/json
id
required
string
ID of the formula.

type
required
string
Value: "formula"
The type of this resource.

href
required
string <url>
API link to the formula.

name
required
string
Name of the formula.

value
required
(ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of (ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of ScalarValue (strings or numbers or booleans))) (Value)
A Coda result or entity expressed as a primitive type, or array of primitive types.

parent	
object (PageReference)
Reference to a page.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/formulas/{formulaIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/formulas/<formula ID>'
res = requests.get(uri, headers=headers).json()

print(f'It will take {res["value"]} hours to complete everything')
# => It will take 3 hours to complete everything
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "f-fgHijkLm",
"type": "formula",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/formulas/f-fgHijkLm",
"name": "Sum of expenses",
"parent": {
"id": "canvas-IjkLmnO",
"type": "page",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",
"name": "Launch Status"
},
"value": "$12.34"
}
Controls
Controls provide a user-friendly way to input a value that can affect other parts of the doc. This API lets you list controls and get their current values.

List controls
Returns a list of controls in a Coda doc.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
limit	
integer >= 1
Default: 25
Example: limit=10
Maximum number of results to return in this query.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

sortBy	
string (SortBy)
Value: "name"
Example: sortBy=name
Determines how to sort the given objects.

Responses
200 List of controls in a doc.
RESPONSE SCHEMA: application/json
items
required
Array of objects (ControlReference)
href	
string <url>
API link to these results

nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/controls

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/controls'
res = requests.get(uri, headers=headers).json()

print(f'Controls here are: {", ".join(i["name"] for i in res["items"])}')
# => Controls here are: Control 1, Control 2
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/controls?limit=20",
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/docs/AbCDeFGH/controls?pageToken=eyJsaW1pd"
}
Get a control
Returns info on a control.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

controlIdOrName
required
string
Example: ctrl-cDefGhij
ID or name of the control. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it.

Responses
200 Details about a control.
RESPONSE SCHEMA: application/json
id
required
string
ID of the control.

type
required
string
Value: "control"
The type of this resource.

href
required
string <url>
API link to the control.

name
required
string
Name of the control.

controlType
required
string (ControlType)
Enum: "button" "checkbox" "datePicker" "dateRangePicker" "dateTimePicker" "lookup" "multiselect" "select" "scale" "slider" "reaction" "textbox" "timePicker"
Type of the control.

value
required
(ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of (ScalarValue (ScalarValue (string) or ScalarValue (number) or ScalarValue (boolean))) or (Array of ScalarValue (strings or numbers or booleans))) (Value)
A Coda result or entity expressed as a primitive type, or array of primitive types.

parent	
object (PageReference)
Reference to a page.

401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/docs/{docId}/controls/{controlIdOrName}

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = f'https://coda.io/apis/v1/docs/<doc ID>/controls/<control ID>'
res = requests.get(uri, headers=headers).json()

print(f'The control is a {res["controlType"]}')
# => The control is a slider
Response samples
200401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"id": "ctrl-cDefGhij",
"type": "control",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/controls/ctrl-cDefGhij",
"name": "Cost",
"parent": {
"id": "canvas-IjkLmnO",
"type": "page",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO",
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",
"name": "Launch Status"
},
"controlType": "slider",
"value": "$12.34"
}
Account
At this time, the API exposes some limited information about your account. However, /whoami is a good endpoint to hit to verify that you're hitting the API correctly and that your token is working as expected.

Get user info
Returns basic info about the current user.

AUTHORIZATIONS:
Bearer
Responses
200 Info about the current user.
RESPONSE SCHEMA: application/json
name
required
string
Name of the user.

loginId
required
string
Email address of the user.

type
required
string
Value: "user"
The type of this resource.

scoped
required
boolean
True if the token used to make this request has restricted/scoped access to the API.

tokenName
required
string
Returns the name of the token used for this request.

href
required
string <url>
API link to the user.

workspace
required
object (WorkspaceReference)
Reference to a Coda workspace.

pictureLink	
string <url>
Browser-friendly link to the user's avatar image.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/whoami

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/whoami'
res = requests.get(uri, headers=headers).json()

print(f'Your name is {res["name"]}')
# => Your name is John Doe
Response samples
200401429
Content type
application/json

Copy
Expand allCollapse all
{
"name": "John Doe",
"loginId": "user@example.com",
"type": "user",
"pictureLink": "https://cdn.coda.io/avatars/default_avatar.png",
"scoped": false,
"tokenName": "My API token",
"href": "https://coda.io/apis/v1beta/whoami",
"workspace": {
"id": "ws-1Ab234",
"type": "workspace",
"organizationId": "org-2Bc456",
"browserLink": "https://coda.io/docs?workspaceId=ws-1Ab234",
"name": "My workspace"
}
}
Analytics
This API offers analytics data for your docs and Packs over time.

List doc analytics
Returns analytics data for available docs per day.

AUTHORIZATIONS:
Bearer
QUERY PARAMETERS
docIds	
Array of strings
List of docIds to fetch.

workspaceId	
string
Example: workspaceId=ws-1Ab234
ID of the workspace.

query	
string
Example: query=Supercalifragilisticexpialidocious
Search term used to filter down results.

isPublished	
boolean
Limit results to only published items.

sinceDate	
string <date>
Example: sinceDate=2020-08-01
Limit results to activity on or after this date.

untilDate	
string <date>
Example: untilDate=2020-08-05
Limit results to activity on or before this date.

scale	
string (AnalyticsScale)
Enum: "daily" "cumulative"
Example: scale=daily
Quantization period over which to view analytics. Defaults to daily.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

orderBy	
string (DocAnalyticsOrderBy)
Enum: "date" "docId" "title" "createdAt" "publishedAt" "likes" "copies" "views" "sessionsDesktop" "sessionsMobile" "sessionsOther" "totalSessions" "aiCreditsChat" "aiCreditsBlock" "aiCreditsColumn" "aiCreditsAssistant" "aiCreditsReviewer" "aiCredits"
Use this parameter to order the doc analytics returned.

direction	
string (SortDirection)
Enum: "ascending" "descending"
Direction to sort results in.

limit	
integer [ 1 .. 5000 ]
Default: 1000
Example: limit=10
Maximum number of results to return in this query.

Responses
200 List of Coda doc analytics.
RESPONSE SCHEMA: application/json
items
required
Array of objects (DocAnalyticsItem)
nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/analytics/docs

Request samples
Python 3.7Shell

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/analytics/docs'
params = {
  'limit': 10,
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["doc"]["title"]}')
# => First doc is: New Document
Response samples
200401429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/analytics/docs?pageToken=xyz"
}
List page analytics
Returns analytics data for a given doc within the day. This method will return a 401 if the given doc is not in an Enterprise workspace.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
docId
required
string
Example: AbCDeFGH
ID of the doc.

QUERY PARAMETERS
sinceDate	
string <date>
Example: sinceDate=2020-08-01
Limit results to activity on or after this date.

untilDate	
string <date>
Example: untilDate=2020-08-05
Limit results to activity on or before this date.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

limit	
integer [ 1 .. 5000 ]
Default: 1000
Example: limit=10
Maximum number of results to return in this query.

Responses
200 List of page analytics for the given Coda doc.
RESPONSE SCHEMA: application/json
items
required
Array of objects (PageAnalyticsItem)
nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/analytics/docs/{docId}/pages

Request samples
Python 3.7Shell

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/analytics/docs/abcdefghi/pages'
params = {
  'limit': 10,
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First page is: {res["items"][0]["page"]["name"]}')
# => First page is: My Page
Response samples
200401429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/analytics/docs/DOC_ID/pages?pageToken=xyz"
}
Get doc analytics summary
Returns summarized analytics data for available docs.

AUTHORIZATIONS:
Bearer
QUERY PARAMETERS
isPublished	
boolean
Limit results to only published items.

sinceDate	
string <date>
Example: sinceDate=2020-08-01
Limit results to activity on or after this date.

untilDate	
string <date>
Example: untilDate=2020-08-05
Limit results to activity on or before this date.

workspaceId	
string
Example: workspaceId=ws-1Ab234
ID of the workspace.

Responses
200 Response of Coda doc summary analytics.
RESPONSE SCHEMA: application/json
totalSessions
required
integer
Total number of sessions across all docs.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/analytics/docs/summary

Response samples
200401429
Content type
application/json

Copy
{
"totalSessions": 1337
}
List Pack analytics
Returns analytics data for Packs the user can edit.

AUTHORIZATIONS:
Bearer
QUERY PARAMETERS
packIds	
Array of integers
Which Pack IDs to fetch.

workspaceId	
string
Example: workspaceId=ws-1Ab234
ID of the workspace.

query	
string
Example: query=Supercalifragilisticexpialidocious
Search term used to filter down results.

sinceDate	
string <date>
Example: sinceDate=2020-08-01
Limit results to activity on or after this date.

untilDate	
string <date>
Example: untilDate=2020-08-05
Limit results to activity on or before this date.

scale	
string (AnalyticsScale)
Enum: "daily" "cumulative"
Example: scale=daily
Quantization period over which to view analytics. Defaults to daily.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

orderBy	
string (PackAnalyticsOrderBy)
Enum: "date" "packId" "name" "createdAt" "docInstalls" "workspaceInstalls" "numFormulaInvocations" "numActionInvocations" "numSyncInvocations" "numMetadataInvocations" "docsActivelyUsing" "docsActivelyUsing7Day" "docsActivelyUsing30Day" "docsActivelyUsing90Day" "docsActivelyUsingAllTime" "workspacesActivelyUsing" "workspacesActivelyUsing7Day" "workspacesActivelyUsing30Day" "workspacesActivelyUsing90Day" "workspacesActivelyUsingAllTime" "workspacesWithActiveSubscriptions" "workspacesWithSuccessfulTrials" "revenueUsd"
Use this parameter to order the Pack analytics returned.

direction	
string (SortDirection)
Enum: "ascending" "descending"
Direction to sort results in.

isPublished	
boolean
Limit results to only published items. If false or unspecified, returns all items including published ones.

limit	
integer [ 1 .. 5000 ]
Default: 1000
Example: limit=10
Maximum number of results to return in this query.

Responses
200 Response of Coda Pack analytics.
RESPONSE SCHEMA: application/json
items
required
Array of objects (PackAnalyticsItem)
nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/analytics/packs

Request samples
Python 3.7Shell

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/analytics/packs'
params = {
  'limit': 10,
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First Pack is: {res["items"][0]["pack"]["name"]}')
# => First Pack is: New Pack
Response samples
200401429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/analytics/packs?pageToken=xyz"
}
Get Pack analytics summary
Returns summarized analytics data for Packs the user can edit.

AUTHORIZATIONS:
Bearer
QUERY PARAMETERS
packIds	
Array of integers
Which Pack IDs to fetch.

workspaceId	
string
Example: workspaceId=ws-1Ab234
ID of the workspace.

isPublished	
boolean
Limit results to only published items. If false or unspecified, returns all items including published ones.

sinceDate	
string <date>
Example: sinceDate=2020-08-01
Limit results to activity on or after this date.

untilDate	
string <date>
Example: untilDate=2020-08-05
Limit results to activity on or before this date.

Responses
200 Response of Coda Pack summary analytics.
RESPONSE SCHEMA: application/json
totalDocInstalls
required
integer
The number of times this Pack was installed in docs.

totalWorkspaceInstalls
required
integer
The number of times this Pack was installed in workspaces.

totalInvocations
required
integer
The number of times formulas in this Pack were invoked.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/analytics/packs/summary

Response samples
200401429
Content type
application/json
{
  "totalDocInstalls": 0,
  "totalWorkspaceInstalls": 0,
  "totalInvocations": 0
}

GET /analytics/packs/summary
Returns summary analytics for Packs.
- Query Parameters:
  - workspaceId (string): ID of the workspace.
  - isPublished (boolean): Limit to published items.
  - sinceDate (string <date>): Activity on or after this date.
  - untilDate (string <date>): Activity on or before this date.
- Responses:
  - 200: JSON with totalDocInstalls, totalWorkspaceInstalls, totalInvocations.
  - 401: Invalid or expired API token.
  - 429: Too many requests.

GET /analytics/packs/{packId}/formulas
Returns analytics data for Pack formulas.
- Path Parameters:
  - packId (integer >= 1): ID of a Pack.
- Query Parameters:
  - packFormulaNames (Array of strings): List of formula names.
  - packFormulaTypes (Array of strings): List of formula types.
  - sinceDate (string <date>): Activity on or after this date.
  - untilDate (string <date>): Activity on or before this date.
  - scale (string): "daily" or "cumulative".
  - pageToken (string): Token for next page of results.
  - orderBy (string): Field to order results by.
  - direction (string): "ascending" or "descending".
  - limit (integer [1..5000]): Max results to return.
- Responses:
  - 200: JSON with items, nextPageToken, nextPageLink.
  - 401: Invalid or expired API token.
  - 429: Too many requests.

GET /analytics/updated
Returns last updated dates for analytics.
- Responses:
  - 200: JSON with docAnalyticsLastUpdated, packAnalyticsLastUpdated, packFormulaAnalyticsLastUpdated.
  - 429: Too many requests.

GET /resolveBrowserLink
Resolves a Coda browser link to metadata.
- Query Parameters:
  - url (string <url>): The browser link.
  - degradeGracefully (boolean): Resolve to next-available object if deleted.
- Responses:
  - 200: JSON with type, href, resource, browserLink.
  - 400: Invalid request parameters.
  - 401: Invalid or expired API token.
  - 403: No access to resource.
  - 404: Resource not found.
  - 429: Too many requests.

untilDate	
string <date>
Example: untilDate=2020-08-05
Limit results to activity on or before this date.

scale	
string (AnalyticsScale)
Enum: "daily" "cumulative"
Example: scale=daily
Quantization period over which to view analytics. Defaults to daily.

pageToken	
string
Example: pageToken=eyJsaW1pd
An opaque token used to fetch the next page of results.

orderBy	
string (PackFormulaAnalyticsOrderBy)
Enum: "date" "formulaName" "formulaType" "formulaInvocations" "medianLatencyMs" "medianResponseSizeBytes" "errors" "docsActivelyUsing" "docsActivelyUsing7Day" "docsActivelyUsing30Day" "docsActivelyUsing90Day" "docsActivelyUsingAllTime" "workspacesActivelyUsing" "workspacesActivelyUsing7Day" "workspacesActivelyUsing30Day" "workspacesActivelyUsing90Day" "workspacesActivelyUsingAllTime"
Use this parameter to order the Pack formula analytics returned.

direction	
string (SortDirection)
Enum: "ascending" "descending"
Direction to sort results in.

limit	
integer [ 1 .. 5000 ]
Default: 1000
Example: limit=10
Maximum number of results to return in this query.

Responses
200 Response of Coda Pack formula analytics.
RESPONSE SCHEMA: application/json
items
required
Array of objects (PackFormulaAnalyticsItem)
nextPageToken	
string (nextPageToken)
If specified, an opaque token used to fetch the next page of results.

nextPageLink	
string <url>
If specified, a link that can be used to fetch the next page of results.

401 The API token is invalid or has expired.
429 The client has sent too many requests.

GET
/analytics/packs/{packId}/formulas

Response samples
200401429
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{}
],
"nextPageToken": "eyJsaW1pd",
"nextPageLink": "https://coda.io/apis/v1/analytics/packs/:packId/formulas?pageToken=xyz"
}
Get analytics last updated day
Returns days based on Pacific Standard Time when analytics were last updated.

AUTHORIZATIONS:
Bearer
Responses
200 Response of analytics last updated days.
RESPONSE SCHEMA: application/json
docAnalyticsLastUpdated
required
string <date>
Date that doc analytics were last updated.

packAnalyticsLastUpdated
required
string <date>
Date that Pack analytics were last updated.

packFormulaAnalyticsLastUpdated
required
string <date>
Date that Pack formula analytics were last updated.

429 The client has sent too many requests.

GET
/analytics/updated

Response samples
200429
Content type
application/json

Copy
{
"docAnalyticsLastUpdated": "2022-05-01",
"packAnalyticsLastUpdated": "2022-05-01",
"packFormulaAnalyticsLastUpdated": "2022-05-01"
}
Miscellaneous
These endpoints wouldn't fit anywhere else, but you may find them useful when working with Coda.

Resolve browser link
Given a browser link to a Coda object, attempts to find it and return metadata that can be used to get more info on it. Returns a 400 if the URL does not appear to be a Coda URL or a 404 if the resource cannot be located with the current credentials.

AUTHORIZATIONS:
Bearer
QUERY PARAMETERS
url
required
string <url>
Example: url=https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO
The browser link to try to resolve.

degradeGracefully	
boolean
Example: degradeGracefully=true
By default, attempting to resolve the Coda URL of a deleted object will result in an error. If this flag is set, the next-available object, all the way up to the doc itself, will be resolved.

Responses
200 Metadata for the resolved resource.
RESPONSE SCHEMA: application/json
type
required
string
Value: "apiLink"
The type of this resource.

href
required
string <url>
Self link to this query.

resource
required
object (ApiLinkResolvedResource)
Reference to the resolved resource.

browserLink	
string <url>
Canonical browser-friendly link to the resolved resource.

400 The request parameters did not conform to expectations.
401 The API token is invalid or has expired.
403 The API token does not grant access to this resource.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.

GET
/resolveBrowserLink

Request samples
Python 3.7ShellGoogle Apps Script

Copy
import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/resolveBrowserLink'
params = {
  'url': 'https://coda.io/d/Some-Doc_d<doc ID>/#To-do-List_tu<table ID>',
}
res = requests.get(uri, headers=headers, params=params).json()
resolved_uri = res["resource"]["href"]

res = requests.get(resolved_uri, headers=headers).json()
print(f'This link points to a {res["type"]} named {res["name"]}')
# => This link points to a table named To-do List
Response samples
200400401403404429
Content type
application/json

Copy
Expand allCollapse all
{
"type": "apiLink",
"href": "https://coda.io/apis/v1/resolveBrowserLink?url=https%3A%2F%2Fcoda.io%2Fd%2F_dAbCDeFGH%2FLaunch-Status_sumnO",
"browserLink": "https://coda.io/d/_dAbCDeFGH/Launch-Status_sumnO",
"resource": {
"type": "aclMetadata",
"id": "canvas-IjkLmnO",
"name": "My Page",
"href": "https://coda.io/apis/v1/docs/AbCDeFGH/pages/canvas-IjkLmnO"
}
}
Get mutation status
Get the status for an asynchronous mutation to know whether or not it has been completed. Each API endpoint that mutates a document will return a request id that you can pass to this endpoint to check the completion status. Status information is not guaranteed to be available for more than one day after the mutation was completed. It is intended to be used shortly after the request was made.

AUTHORIZATIONS:
Bearer
PATH PARAMETERS
requestId
required
string
Example: abc-123-def-456
ID of the request.

Responses
200 Info about the mutation.
RESPONSE SCHEMA: application/json
completed
required
boolean
Returns whether the mutation has completed.

warning	
string
A warning if the mutation completed but with caveats.

401 The API token is invalid or has expired.
404 The resource could not be located with the current API token.
429 The client has sent too many requests.
429 The client has sent too many requests.
