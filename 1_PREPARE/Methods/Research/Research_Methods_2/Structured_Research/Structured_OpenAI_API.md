https://openai.com/index/introducing-structured-outputs-in-the-api/

Applying Structured Outputs in Python
To use Structured Outputs in Python, you'll need to use the OpenAI API. Here's a step-by-step guide:
Install the OpenAI Python library:
bash
pip install openai

Import the library and set up your API key:
python
import openai
openai.api_key = 'your-api-key-here'

Define your JSON Schema:
python
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

Use the schema in your API call:
python
response = openai.ChatCompletion.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate information for a person."}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "person_info",
            "strict": True,
            "schema": schema
        }
    }
)

print(response.choices[0].message.content)

Parse the response:
python
import json

structured_output = json.loads(response.choices[0].message.content)
print(f"Name: {structured_output['name']}")
print(f"Age: {structured_output['age']}")
print(f"City: {structured_output['city']}")

Best Practices and Tips
Be specific in your schema: The more detailed your schema, the more precise the output will be.
Use strict: true to ensure the model adheres exactly to your schema.
For complex schemas, consider breaking them down into smaller, manageable parts.
Utilize Pydantic for schema validation in Python:
python
from pydantic import BaseModel, Field

class PersonInfo(BaseModel):
    name: str
    age: int = Field(..., ge=0)
    city: str

# Convert Pydantic model to JSON schema
schema = PersonInfo.model_json_schema()

Handle potential errors:
python
try:
    structured_output = PersonInfo.parse_raw(response.choices[0].message.content)
except ValidationError as e:
    print(f"Validation error: {e}")

For function calling, use the tools parameter:
python
response = openai.ChatCompletion.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like in San Francisco?"}
    ],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }]
)

By leveraging Structured Outputs, you can ensure that your AI-generated content is consistent, reliable, and easily integrated into your Python applications. This feature significantly reduces the need for post-processing and error handling, making it easier to build robust AI-powered systems.
