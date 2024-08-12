import openai
import json
from pydantic import BaseModel, Field, ValidationError

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

# Define your JSON Schema using Pydantic
class PersonInfo(BaseModel):
    name: str
    age: int = Field(..., ge=0)
    city: str

# Convert Pydantic model to JSON schema
schema = PersonInfo.model_json_schema()

# Use the schema in your API call
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

# Parse the response
try:
    structured_output = PersonInfo.parse_raw(response.choices[0].message.content)
    print(f"Name: {structured_output.name}")
    print(f"Age: {structured_output.age}")
    print(f"City: {structured_output.city}")
except ValidationError as e:
    print(f"Validation error: {e}")
