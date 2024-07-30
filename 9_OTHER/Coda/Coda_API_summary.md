Here is a comprehensive and expanded list of all methods available in the Coda API (version 1.4.17), organized by category with additional details:

1. Docs
- GET /docs 
  - List available docs
  - Supports filtering by owner, published status, search query, source doc, starred status, gallery visibility, workspace, and folder
- POST /docs 
  - Create a new doc
  - Can optionally copy an existing doc
- GET /docs/{docId} 
  - Get detailed information about a specific doc
- DELETE /docs/{docId} 
  - Permanently delete a doc

2. Pages
- GET /docs/{docId}/pages 
  - List all pages in a doc
  - Supports filtering by page type
- POST /docs/{docId}/pages 
  - Create a new page in a doc
- GET /docs/{docId}/pages/{pageIdOrName} 
  - Get details about a specific page
- PUT /docs/{docId}/pages/{pageIdOrName} 
  - Update page properties (e.g., name, icon)
- DELETE /docs/{docId}/pages/{pageIdOrName} 
  - Remove a page from a doc
- POST /docs/{docId}/pages/{pageIdOrName}/export 
  - Initiate an asynchronous content export for a page
- GET /docs/{docId}/pages/{pageIdOrName}/export/{requestId} 
  - Check the status of a content export request

3. Tables
- GET /docs/{docId}/tables 
  - List all tables in a doc
- GET /docs/{docId}/tables/{tableIdOrName} 
  - Get detailed information about a specific table

4. Columns
- GET /docs/{docId}/tables/{tableIdOrName}/columns 
  - List all columns in a table
- GET /docs/{docId}/tables/{tableIdOrName}/columns/{columnIdOrName} 
  - Get details about a specific column

5. Rows
- GET /docs/{docId}/tables/{tableIdOrName}/rows 
  - List rows in a table
  - Supports pagination, filtering, and sorting
- POST /docs/{docId}/tables/{tableIdOrName}/rows 
  - Insert new rows or upsert existing rows
  - Supports bulk operations
- GET /docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName} 
  - Get details about a specific row
- PUT /docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName} 
  - Update an existing row
- DELETE /docs/{docId}/tables/{tableIdOrName}/rows 
  - Delete multiple rows in bulk
- DELETE /docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName} 
  - Delete a specific row

6. Formulas
- GET /docs/{docId}/formulas 
  - List all formulas in a doc
- GET /docs/{docId}/formulas/{formulaIdOrName} 
  - Get details about a specific formula

7. Controls
- GET /docs/{docId}/controls 
  - List all controls in a doc
- GET /docs/{docId}/controls/{controlIdOrName} 
  - Get details about a specific control

8. Permissions and ACL (Access Control List)
- GET /docs/{docId}/acl/permissions 
  - List all permissions for a doc
- POST /docs/{docId}/acl/permissions 
  - Add a new permission to a doc
- DELETE /docs/{docId}/acl/permissions/{permissionId} 
  - Remove a specific permission from a doc
- GET /docs/{docId}/acl/principals/search 
  - Search for users or groups that can be granted permissions
- GET /docs/{docId}/acl/metadata 
  - Get sharing metadata for a doc
- GET /docs/{docId}/acl/settings 
  - Retrieve ACL settings for a doc
- PATCH /docs/{docId}/acl/settings 
  - Update ACL settings for a doc

9. Publishing
- GET /categories 
  - Get a list of available doc categories for publishing
- PUT /docs/{docId}/publish 
  - Publish a doc, making it publicly accessible
- DELETE /docs/{docId}/publish 
  - Unpublish a doc, removing public access

10. Automations
- POST /docs/{docId}/hooks/automation/{ruleId} 
  - Manually trigger a specific automation rule

11. Analytics
- GET /analytics/docs 
  - List analytics data for accessible docs
- GET /analytics/docs/{docId}/pages 
  - Get page-level analytics for a specific doc
- GET /analytics/docs/summary 
  - Retrieve a summary of analytics data for all accessible docs
- GET /analytics/packs 
  - List analytics data for Packs (collections of formulas and automations)
- GET /analytics/packs/summary 
  - Get a summary of analytics data for all accessible Packs
- GET /analytics/packs/{packId}/formulas 
  - Retrieve analytics data for formulas within a specific Pack
- GET /analytics/updated 
  - Get the last updated date for various analytics data types

12. Miscellaneous
- GET /whoami 
  - Retrieve information about the authenticated user
- GET /resolveBrowserLink 
  - Convert a browser link to an API resource link
- GET /mutationStatus/{requestId} 
  - Check the status of an asynchronous mutation request

Additional API Features:
- Rate Limiting: The API enforces rate limits to ensure fair usage.
- Authentication: All requests require a Bearer token for authentication.
- Pagination: List endpoints support pagination for large result sets.
- Error Handling: The API uses standard HTTP status codes and provides detailed error messages.
- Versioning: The API is versioned to ensure backward compatibility.

This comprehensive list covers all the methods available in the Coda API as of version 1.4.17. Each method allows developers to interact with different aspects of Coda docs programmatically, from managing doc content and structure to handling permissions and retrieving analytics data. The API provides a powerful toolset for integrating Coda's collaborative document features into custom applications and workflows.

For the most up-to-date and detailed information, always refer to the official Coda API documentation at https://coda.io/developers/apis/v1.

Citations:
[1] https://coda.io/developers/apis/v1
[2] https://coda.io/developers/apis/v1beta1
[3] https://coda.io/@oleg/getting-started-guide-coda-api
[4] https://github.com/parker-codes/coda-js
[5] https://pipedream.com/apps/coda
[6] https://mixedanalytics.com/knowledge-base/import-coda-data-to-google-sheets/