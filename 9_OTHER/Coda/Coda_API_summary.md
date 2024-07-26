Here is a comprehensive list of all methods available in the Coda API, organized by category:

Docs:
- GET /docs - List available docs
- POST /docs - Create doc 
- GET /docs/{docId} - Get info about a doc
- DELETE /docs/{docId} - Delete doc

Pages:
- GET /docs/{docId}/pages - List pages
- POST /docs/{docId}/pages - Create a page
- GET /docs/{docId}/pages/{pageIdOrName} - Get a page
- PUT /docs/{docId}/pages/{pageIdOrName} - Update a page
- DELETE /docs/{docId}/pages/{pageIdOrName} - Delete a page
- POST /docs/{docId}/pages/{pageIdOrName}/export - Begin content export
- GET /docs/{docId}/pages/{pageIdOrName}/export/{requestId} - Content export status

Tables:
- GET /docs/{docId}/tables - List tables
- GET /docs/{docId}/tables/{tableIdOrName} - Get a table

Columns:
- GET /docs/{docId}/tables/{tableIdOrName}/columns - List columns
- GET /docs/{docId}/tables/{tableIdOrName}/columns/{columnIdOrName} - Get a column

Rows:
- GET /docs/{docId}/tables/{tableIdOrName}/rows - List table rows
- POST /docs/{docId}/tables/{tableIdOrName}/rows - Insert/upsert rows
- GET /docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName} - Get a row
- PUT /docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName} - Update row
- DELETE /docs/{docId}/tables/{tableIdOrName}/rows - Delete multiple rows
- DELETE /docs/{docId}/tables/{tableIdOrName}/rows/{rowIdOrName} - Delete row

Formulas:
- GET /docs/{docId}/formulas - List formulas
- GET /docs/{docId}/formulas/{formulaIdOrName} - Get a formula

Controls:
- GET /docs/{docId}/controls - List controls
- GET /docs/{docId}/controls/{controlIdOrName} - Get a control

Permissions and ACL:
- GET /docs/{docId}/acl/permissions - List permissions
- POST /docs/{docId}/acl/permissions - Add permission
- DELETE /docs/{docId}/acl/permissions/{permissionId} - Delete permission
- GET /docs/{docId}/acl/principals/search - Search principals
- GET /docs/{docId}/acl/metadata - Get sharing metadata
- GET /docs/{docId}/acl/settings - Get ACL settings
- PATCH /docs/{docId}/acl/settings - Update ACL settings

Publishing:
- GET /categories - Get doc categories
- PUT /docs/{docId}/publish - Publish doc
- DELETE /docs/{docId}/publish - Unpublish doc

Automations:
- POST /docs/{docId}/hooks/automation/{ruleId} - Trigger automation

Analytics:
- GET /analytics/docs - List doc analytics
- GET /analytics/docs/{docId}/pages - List page analytics
- GET /analytics/docs/summary - Get doc analytics summary
- GET /analytics/packs - List Pack analytics
- GET /analytics/packs/summary - Get Pack analytics summary
- GET /analytics/packs/{packId}/formulas - List Pack formula analytics
- GET /analytics/updated - Get analytics last updated day

Miscellaneous:
- GET /whoami - Get user info
- GET /resolveBrowserLink - Resolve browser link
- GET /mutationStatus/{requestId} - Get mutation status

This list covers all the methods available in the Coda API as of version 1.4.17. Each method allows you to interact with different aspects of Coda docs programmatically, from managing doc content to handling permissions and retrieving analytics data.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/343060/cfbe775e-c0a8-4fb9-831d-4f25b807023d/paste.txt
[2] https://coda.io/%40oleg/getting-started-guide-coda-api
[3] https://pipedream.com/apps/coda
[4] https://github.com/parker-codes/coda-js
[5] https://mixedanalytics.com/knowledge-base/import-coda-data-to-google-sheets/
[6] https://coda.io/developers/apis/v1