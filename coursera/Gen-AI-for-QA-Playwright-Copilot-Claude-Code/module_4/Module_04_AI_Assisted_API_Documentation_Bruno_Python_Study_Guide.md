# 🧪 Module 7 --- AI-Assisted API Documentation, Bruno & API Debugging

## Python + Pytest + Requests \| Hinglish Study Guide

> **Source reviewed:** `module_7.zip` contains two unique lesson
> transcripts and their matching English VTT subtitle files. Duplicate
> transcript/subtitle content has been consolidated.
>
> **Course demo stack:** Claude Code, VS Code, pizza-store backend,
> Swagger/OpenAPI, Bruno API client and `.bru` request files.
>
> **Your stack:** Python + Pytest + Requests.
>
> **Source boundary:** The two lessons cover Swagger documentation
> generation and Bruno collection generation/debugging. Data
> transformation (XML-to-JSON and Java POJO examples) is introduced
> conceptually, but a complete hands-on implementation is not present in
> the source.

------------------------------------------------------------------------

# 🗺️ Module roadmap

  ---------------------------------------------------------------------------
  Lesson                  Topic                       Outcome
  ----------------------- --------------------------- -----------------------
  7.1                     Observe frontend API calls  Find requests using
                                                      DevTools Network

  7.2                     Generate Swagger/OpenAPI    Use AI to document APIs
                          docs                        from backend source

  7.3                     Understand API contracts    Extract endpoints,
                                                      methods, payloads,
                                                      responses and
                                                      authentication

  7.4                     Generate Bruno collection   Create organised `.bru`
                                                      requests and local
                                                      environment

  7.5                     Execute Bruno requests      Import/open collection,
                                                      select environment and
                                                      run requests

  7.6                     Debug API requests with AI  Use request file +
                                                      actual error response
                                                      to identify a problem

  7.7                     Data                        Understand XML-to-JSON
                          generation/transformation   and test-data use cases
  ---------------------------------------------------------------------------

**Core principle:** AI can draft API documentation and request
collections, but the backend contract is the source of truth.

------------------------------------------------------------------------

# 🌐 Lesson 7.1 --- Understand frontend/backend API communication

## WHY?

A web application usually has a frontend and a backend.

-   **Frontend:** UI the user interacts with.
-   **Backend:** server-side logic that processes requests and returns
    data.
-   **API:** communication interface between them.

The course demonstrates using browser DevTools to observe this
communication.

## HOW --- DevTools Network tab

1.  Open the web application.
2.  Open browser Developer Tools.
3.  Select **Network**.
4.  Refresh the page.
5.  Perform an action such as loading a menu.
6.  Inspect the requests sent to the backend.
7.  Check request URL, method, status, payload and response.

This helps you understand what the UI calls. It does not automatically
reveal every business rule or backend implementation detail.

## Practice

Record one request:

  Field                     Your observation
  ------------------------- ------------------
  URL                       
  Method                    
  Status                    
  Request payload           
  Response body             
  Triggering UI action      
  Authentication present?   

------------------------------------------------------------------------

# 📘 Lesson 7.2 --- Generate Swagger/OpenAPI documentation using AI

## WHY?

In a real backend project, API documentation helps developers and
testers understand available endpoints and how to call them.

The course identifies Swagger as a popular API documentation option.

## WHAT --- Swagger vs OpenAPI

-   **OpenAPI Specification:** structured description of an HTTP API,
    commonly represented in JSON or YAML.
-   **Swagger tools:** tools used to work with OpenAPI specifications,
    including Swagger UI for interactive documentation.

An OpenAPI document can describe: - Paths and HTTP methods. - Path/query
parameters. - Request bodies. - Response schemas and status codes. -
Authentication/security schemes.

## Course demonstration --- exact workflow

The instructor uses a pizza-store backend that does not already have
Swagger documentation but has access to its source code.

1.  Start a new Claude Code session.
2.  Ask Claude to inspect the backend project.
3.  Ask it to generate Swagger UI documentation.
4.  Claude reads relevant source files and identifies API routes and
    behaviour.
5.  Claude proposes installing NPM packages.
6.  The instructor rejects the unnecessary package installation.
7.  The instructor asks Claude to create the Swagger file without extra
    dependencies.
8.  Claude creates `swagger.json` and updates the application to expose
    the documentation.
9.  The instructor restarts the app with `npm start`.
10. Swagger UI is opened in the browser and used to execute a request.

### Course-style prompt

``` text
Inspect this backend project and generate Swagger/OpenAPI
documentation for the APIs implemented in the source code.

Document:
- Existing endpoints and HTTP methods
- Parameters and request bodies
- Response structures and status codes where supported
- Authentication requirements

Do not install additional dependencies.
First explain which files you plan to inspect or modify.
Do not invent endpoints or business rules.
```

## Important lesson --- steer the AI

The instructor does not accept every proposed command. The assistant
wanted to install additional packages; the instructor rejected that
approach and gave a narrower instruction.

Before approving an AI-proposed command, ask: - Is this dependency
necessary? - Does the project already have a way to do this? - Which
files will change? - Is the command safe in this environment?

## Python/Django REST Framework adaptation

Tumhare Python background ke liye same concept Django REST Framework
project par apply hoga.

Illustrative endpoints:

``` text
GET    /api/menu/
GET    /api/orders/
POST   /api/orders/
GET    /api/orders/{order_id}/
POST   /api/auth/login/
```

These are examples, not claims about your actual project.

A DRF project can generate an OpenAPI schema and expose Swagger UI using
a suitable documentation library, if the project allows that dependency.
The uploaded course does not demonstrate Django/DRF setup; this is a
mentor adaptation.

### Python-focused prompt

``` text
Act as a Senior Django REST Framework API Engineer.

Inspect the supplied Django project.

Identify:
1. URL patterns.
2. API views and viewsets.
3. Serializers.
4. Authentication and permission classes.
5. Request fields and validation.
6. Response shapes and status codes.

Create an API inventory in Markdown.

Do not invent request fields or response properties.
Mark details as unknown when the implementation
does not establish them.

Do not install packages or modify files yet.
```

## API documentation review checklist

-   [ ] Every documented endpoint exists.
-   [ ] HTTP methods match the implementation.
-   [ ] Path and query parameters are correct.
-   [ ] Required/optional request fields are correct.
-   [ ] Response schemas match actual responses.
-   [ ] Error status codes are not invented.
-   [ ] Authentication requirements are documented.
-   [ ] The OpenAPI document is valid.
-   [ ] Try-it-out requests use a safe environment.
-   [ ] Internal API documentation is not accidentally exposed publicly.

### Interview answer

> "If I have access to backend source code or an existing API
> specification, I can use an AI coding assistant to identify endpoints,
> methods, request parameters, response structures and authentication
> requirements. It can help generate an OpenAPI document and make the
> APIs easier to understand through Swagger UI. I validate the generated
> documentation against the actual implementation because AI may make
> incorrect assumptions."

------------------------------------------------------------------------

# 🔎 Lesson 7.3 --- Understand APIs from Swagger documentation

The course opens the generated `swagger.json` file and asks Claude to
explain the APIs. The assistant identifies menu, order and authenticated
endpoints, and explains what is needed to call protected endpoints.

## What should a QA engineer extract?

  Field              Meaning
  ------------------ -----------------------------------------------
  Method             GET, POST, PUT, PATCH, DELETE
  Path               Endpoint URL
  Purpose            What the endpoint does
  Authentication     Whether credentials/token are required
  Parameters         Inputs in path or query
  Request body       Data sent to backend
  Success response   Expected success status and schema
  Error response     Validation/authentication/not-found behaviour
  Side effects       Whether data is created, updated or deleted

### Prompt to understand an API

``` text
Read the supplied OpenAPI JSON file.

Create an API inventory with:
- Method
- Path
- Summary
- Path/query parameters
- Request body
- Success responses
- Error responses
- Authentication requirements

Explain the main user workflows these APIs support.

Separate documented facts from assumptions.
Do not invent missing schemas.
```

## Python + Requests example

Illustrative only; verify the endpoint and response contract first.

``` python
import requests

BASE_URL = "http://localhost:8000"


def test_menu_endpoint_returns_success():
    response = requests.get(
        f"{BASE_URL}/api/menu/",
        timeout=10,
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith(
        "application/json"
    )
```

A stronger test also validates the response schema and business rules.

``` python
def test_menu_items_have_required_fields():
    response = requests.get(
        f"{BASE_URL}/api/menu/",
        timeout=10,
    )

    assert response.status_code == 200

    items = response.json()

    for item in items:
        assert "id" in item
        assert "name" in item
        assert isinstance(item["name"], str)
        assert item["name"].strip()
```

The assumed response fields must be verified against the actual API
contract.

------------------------------------------------------------------------

# 🧰 Lesson 7.4 --- Generate a Bruno API collection with Claude Code

## WHY?

An API collection groups requests so testers can: - Reuse requests. -
Organise endpoints into folders. - Select environments. - Execute
requests repeatedly. - Share API exploration setup.

The course mentions Postman, Bruno and the VS Code REST Client
extension. The instructor demonstrates Bruno.

## WHAT --- Bruno

Bruno is an API client. Its collections contain request files, including
`.bru` files.

In the course, Claude creates: - A Bruno collection folder. - Folders
for most API endpoint areas. - Individual `.bru` request files. - A
local environment containing values required by the collection.

The instructor explains that Claude can use backend source code to
generate the collection. If source code is unavailable, a Swagger
specification can provide the API information.

## Course workflow

1.  Start a new Claude Code session.
2.  Ask it to create a Bruno collection for the project.
3.  Claude inspects backend source or API definitions.
4.  It creates collection folders and `.bru` files.
5.  It creates a local environment.
6.  Open the Bruno extension in VS Code.
7.  Import the collection.
8.  Open the imported collection.
9.  Select the local environment.
10. Open the daily-menu request and send it.
11. Inspect the response.

**UI detail from the source:** after importing, the instructor says to
open the collection rather than choosing Import Collection again.

### Course-style prompt

``` text
Inspect this backend project and create a Bruno API collection.

Requirements:
- Organise requests into folders by API area.
- Include endpoints implemented in the project.
- Base request bodies on the actual API contract.
- Create a local environment for reusable variables.
- Do not invent endpoints or request fields.

Before writing files, show me the proposed structure
and explain which source files or API definitions you used.
```

### If backend source is unavailable

``` text
Use the supplied OpenAPI/Swagger specification
to create a Bruno collection.

Include documented endpoints and request examples.
Use an environment variable for the base URL.
Do not invent undocumented fields or responses.

List anything that cannot be represented because
the specification is incomplete.
```

## Bruno vs Python automation

  Tool                Your use
  ------------------- --------------------------------------------------------
  Bruno               Explore requests, inspect responses and debug payloads
  Pytest + Requests   Automated, repeatable API regression tests
  Swagger/OpenAPI     API contract and documentation
  Claude Code         Generate/review collection and help debug requests

Bruno is an API client, not a replacement for your Python automation
framework.

------------------------------------------------------------------------

# 🌱 Lesson 7.5 --- Bruno environments and request execution

The course creates a local environment for the collection.

## WHY use environments?

The same request may need to run against Local, QA or Staging. The base
URL changes while the request can remain the same.

Illustrative values:

``` text
LOCAL_BASE_URL   = http://localhost:8000
QA_BASE_URL      = https://qa.example.test
STAGING_BASE_URL = https://staging.example.test
```

## Environment checklist

-   [ ] Correct collection is open.
-   [ ] Correct environment is selected.
-   [ ] Base URL points to the intended environment.
-   [ ] Method and path are correct.
-   [ ] Required headers are present.
-   [ ] Request body matches the contract.
-   [ ] Response status and body are inspected.
-   [ ] No production secrets or private customer data are used.

Never commit real passwords, tokens, API keys or customer data into a
collection.

------------------------------------------------------------------------

# 🐞 Lesson 7.6 --- Debug Bruno requests using Claude Code

## Exact course demonstration

The instructor intentionally breaks the create-order request by deleting
the `sender` field from its body.

1.  Send the create-order request.
2.  The API returns Bad Request.
3.  The response says:
    `order sender is required and must be a non-empty string`.
4.  Copy the actual error response.
5.  Start a new Claude Code session.
6.  Provide the `create order.bru` request file as context.
7.  Paste the response and ask Claude to update the request.
8.  Claude identifies the missing `sender`.
9.  Approve the edit to the `.bru` file.
10. Reopen and send the request again.
11. The request succeeds.

## WHY is this useful?

Claude receives two useful pieces of evidence: - The actual request
file. - The actual error response from the server.

It can compare the request with the server's validation feedback instead
of guessing from a vague description.

## Safe debugging prompt

``` text
Act as a Senior API Test Engineer.

The selected Bruno request is failing.

Actual API response:
[PASTE RESPONSE]

Inspect the selected request file and compare it
with the error message.

1. Identify missing or invalid request data.
2. Explain why the API rejected the request.
3. Separate facts from assumptions.
4. Propose the smallest correction.
5. Do not modify unrelated requests.
6. Do not invent additional fields.

Show the proposed change before applying it.
```

## Python API equivalent

Broken illustrative request:

``` python
import requests

payload = {
    "items": [
        {"product_id": 1, "quantity": 2}
    ]
}

response = requests.post(
    "http://localhost:8000/api/orders/",
    json=payload,
    timeout=10,
)
```

Suppose the actual response is:

``` json
{
  "detail": "order sender is required and must be a non-empty string"
}
```

The response indicates that `sender` is missing. Confirm this against
the API contract or backend serializer before changing the test.

Illustrative corrected payload:

``` python
payload = {
    "sender": "QA Test User",
    "items": [
        {"product_id": 1, "quantity": 2}
    ],
}
```

Then verify the response using the status code specified by the actual
API contract.

## QA lesson --- test the validation too

The course demonstrates fixing the valid request. As a QA engineer, also
test that missing `sender` is rejected correctly.

``` python
def test_create_order_requires_sender():
    payload = {
        "items": [
            {"product_id": 1, "quantity": 2}
        ]
    }

    response = requests.post(
        "http://localhost:8000/api/orders/",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 400
    assert "sender" in response.text.lower()
```

The status code and error wording are based on the course's demonstrated
response; verify exact behaviour in your own API.

### Common mistakes

-   Adding a field without confirming the contract.
-   Changing expected results to match a defect.
-   Ignoring other required fields.
-   Reusing data that creates duplicate orders.
-   Not inspecting the response body.
-   Allowing AI to modify unrelated `.bru` files.

------------------------------------------------------------------------

# 🔄 Lesson 7.7 --- AI for data generation and transformation

The course introduces AI as useful for converting data between formats
and generating data.

Examples explicitly mentioned: - XML data to JSON data. - Java POJO
classes from API request/response structures. - API request
collections. - Data generation for testing workflows.

The transcript does not include a full XML-to-JSON or POJO
implementation. The following is a mentor-created Python illustration.

## Python example --- XML to JSON-compatible dictionary

``` python
import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>101</id>
    <name>Test User</name>
    <email>qa@example.com</email>
</user>
"""

root = ET.fromstring(xml_data)

user_data = {
    "id": int(root.findtext("id")),
    "name": root.findtext("name"),
    "email": root.findtext("email"),
}

print(user_data)
```

Output:

``` python
{
    "id": 101,
    "name": "Test User",
    "email": "qa@example.com"
}
```

Real XML can include namespaces, attributes, repeated elements and
nested structures. Define mapping rules carefully so information is not
lost.

### AI prompt for data transformation

``` text
Act as a Python data transformation engineer.

Convert the supplied XML into a JSON-compatible
Python dictionary.

Requirements:
- Preserve all fields and values.
- Preserve repeated elements as arrays.
- Explain how attributes are represented.
- Handle missing elements explicitly.
- Do not silently discard information.

First explain the mapping rules.
Then provide Python code and sample output.

XML:
[PASTE XML]
```

### AI prompt for synthetic test data

``` text
Generate synthetic API test data for this request schema.

Include:
- Valid data.
- Missing required field.
- Invalid data type.
- Empty string.
- Boundary values.
- Unexpected but syntactically valid values.

Return valid JSON.
Do not use real personal information.
Do not invent validation rules not present in the schema.
```

------------------------------------------------------------------------

# 🐍 Python API automation mini-lab

## Suggested repository

``` text
api_qa_project/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py
├── docs/
│   └── api-inventory.md
├── collections/
│   └── bruno/
├── tests/
│   └── api/
│       ├── test_menu_api.py
│       └── test_orders_api.py
└── utils/
    └── api_client.py
```

## Practical workflow

``` text
Inspect API calls in DevTools
          ↓
Read backend source or OpenAPI spec
          ↓
Create/review API inventory
          ↓
Generate Bruno collection
          ↓
Select local environment
          ↓
Execute and inspect requests
          ↓
Debug errors with request + response context
          ↓
Create Python Pytest API tests
          ↓
Run positive and negative tests
```

## AI review prompt for a Python API test

``` text
Review this Python API test.

Check:
- API contract alignment.
- Status code assertion.
- Response schema validation.
- Missing negative scenarios.
- Test data isolation.
- Timeout handling.
- Maintainability.

Do not invent the API response schema.
List missing information separately.

Code:
[PASTE CODE]
```

------------------------------------------------------------------------

# 🎤 Interview questions --- Module 7

## Q1. What is Swagger/OpenAPI?

> OpenAPI is a standard format for describing HTTP APIs, including
> endpoints, methods, parameters, request bodies, responses and security
> requirements. Swagger is a set of tools commonly used to work with
> OpenAPI specifications, including Swagger UI for interactive
> documentation.

## Q2. How can AI help generate API documentation?

> If I have access to backend source code or an existing API
> specification, I can use an AI coding assistant to identify routes,
> methods, request fields, responses and authentication requirements. It
> can help draft an OpenAPI document. I validate the generated
> specification against the actual implementation because AI may make
> incorrect assumptions.

## Q3. What is Bruno?

> Bruno is an API client used to organise and execute requests. I can
> create collections, configure environments and inspect API responses.
> I can use Bruno for manual API exploration and debugging, while Pytest
> with Requests is suitable for repeatable automated API regression
> tests.

## Q4. How can AI help create an API collection?

> I can provide backend source code or an OpenAPI specification and ask
> the assistant to create a Bruno collection. I review endpoint paths,
> methods, request bodies, environment variables and authentication
> configuration before executing the requests.

## Q5. How would you debug a 400 Bad Request?

> I inspect the response body and validation message first. Then I
> compare the method, URL, headers and payload with the API contract. I
> can provide the request file and actual response to an AI assistant
> for help, but I verify its diagnosis. After making the smallest
> correction, I rerun the request and add a negative test to ensure
> invalid input is rejected correctly.

## Q6. Difference between Bruno and Pytest?

> Bruno is an API client for organising and executing requests
> interactively. Pytest is a Python testing framework for repeatable
> automated tests. I can use Bruno to explore and debug an API, then
> implement stable regression checks using Pytest with Requests or
> HTTPX.

## Q7. Why is API documentation important for QA?

> API documentation helps me understand endpoints, methods, required
> fields, response schemas and authentication. It provides a contract
> for designing positive, negative and boundary tests. I still verify
> that the documentation matches the implementation.

------------------------------------------------------------------------

# 🧩 Practice assignments

## Exercise 1 --- DevTools API inspection

1.  Open a safe web application.
2.  Open DevTools → Network.
3.  Reload the page.
4.  Perform a user action.
5.  Identify the API request.

Record URL, method, status, payload, response and triggering action.

## Exercise 2 --- API inventory

Use an OpenAPI document or backend source. Record: - Method. - Path. -
Purpose. - Request fields. - Response fields. - Status codes. -
Authentication.

Mark unknown details rather than guessing.

## Exercise 3 --- Bruno collection

Generate a collection from the reviewed API specification. Verify: -
Collection opens. - Correct environment selected. - GET request works. -
POST request uses valid data. - Invalid request produces expected
validation response.

## Exercise 4 --- Broken request debugging

1.  Remove a required field from a safe local request.
2.  Execute it.
3.  Capture the error response.
4.  Give request + response to AI.
5.  Review the proposed correction.
6.  Fix the valid request.
7.  Add a negative Pytest test for the missing field.

## Exercise 5 --- Python API tests

Create: - One positive GET test. - One positive POST test. - One
missing-required-field test. - One invalid-data-type test.

Use the actual API contract. Do not copy illustrative endpoints/status
codes without verification.

## Exercise 6 --- XML transformation

Convert a small XML sample into a Python dictionary/JSON. Test missing
fields, repeated elements, numeric values, empty values and nested
structures.

------------------------------------------------------------------------

# 📊 Module 7 progress tracker

  -----------------------------------------------------------------------
  Topic                   Status                  Evidence
  ----------------------- ----------------------- -----------------------
  7.1 DevTools API        ⬜ Not started          Recorded one real
  inspection                                      request

  7.2 Swagger/OpenAPI     ⬜ Not started          Reviewed API
                                                  documentation

  7.3 API understanding   ⬜ Not started          Verified API inventory

  7.4 Bruno collection    ⬜ Not started          Imported and reviewed
                                                  collection

  7.5 Environment and     ⬜ Not started          Successful local
  execution                                       requests

  7.6 AI-assisted         ⬜ Not started          Broken request
  debugging                                       diagnosis and verified
                                                  fix

  7.7 Data transformation ⬜ Not started          XML/JSON practical

  Python API mini-lab     ⬜ Not started          Positive and negative
                                                  Pytest API tests
  -----------------------------------------------------------------------

## Mastery levels

-   **L1 --- Awareness:** Explain Swagger, Bruno and AI-assisted
    debugging.
-   **L2 --- Guided:** Generate a collection and run requests with help.
-   **L3 --- Independent:** Review API contracts, debug requests and
    write Python API tests.
-   **L4 --- Interview-ready:** Defend design decisions, validation,
    authentication and test data choices.

------------------------------------------------------------------------

# 📌 Source coverage and limitations

## Explicitly covered in the uploaded Module 7

-   Frontend/backend interaction and observing API requests in DevTools
    Network.
-   Swagger as an API documentation option.
-   Generating Swagger documentation using AI when backend source is
    available.
-   Steering Claude away from unnecessary NPM dependencies.
-   Creating `swagger.json` and exposing documentation in the demo app.
-   Executing requests through Swagger UI.
-   Asking AI for an overview of menu, order and authenticated
    endpoints.
-   AI data transformation/generation examples: XML-to-JSON and Java
    POJO.
-   Generating Bruno collections from backend source or Swagger.
-   Creating `.bru` files and a local environment.
-   Importing/opening a collection in Bruno for VS Code.
-   Selecting a local environment and executing the daily-menu request.
-   Debugging a broken create-order request with the actual error
    response and `.bru` file.
-   Fixing the missing `sender` field and rerunning the request.

## Not fully covered in the source

-   Full Bruno installation/configuration.
-   Complete `.bru` syntax reference.
-   Full Postman collection conversion.
-   Complete Python API automation implementation.
-   Django REST Framework OpenAPI setup.
-   Full XML-to-JSON implementation.
-   Full Java POJO generation.
-   Detailed API security testing methodology.

Python code, DRF adaptation, exercises and interview answers in this
guide are mentor extensions, not verbatim course demonstrations.

------------------------------------------------------------------------

# 🏁 Final mentor standard

Module 7 is mastered when you can independently:

1.  Find frontend API calls in DevTools.
2.  Explain why API documentation matters.
3.  Read an OpenAPI specification.
4.  Identify methods, paths, request/response schemas and
    authentication.
5.  Ask AI to generate documentation from verified source context.
6.  Review and correct generated documentation.
7.  Generate and inspect a Bruno collection.
8.  Configure and execute requests in a local environment.
9.  Diagnose a failed request using its actual error response.
10. Translate API behaviour into Python + Pytest tests.
11. Explain why Bruno and Pytest serve different purposes.
12. Defend your assertions and test data choices.

**Final principle:** AI can draft the API documentation and request
collection, but the backend contract is the source of truth. Verify
every endpoint, payload, response and validation rule before trusting
generated tests.
