from pydantic import BaseModel, Field, ValidationError, field_validator

class StudentRegistration(BaseModel):
    name: str = Field(min_length=3)
    roll_number: str = Field(pattern=r"^\d{10}$")
    email: str
    age: int = Field(ge=17, le=22)
    percentage_12th: float = Field(ge=35.0, le=100.0)
    
    @field_validator('email')  
    @classmethod  
    def validate_email_domain(cls, v):  
        if not (v.endswith("@vitstudent.ac.in") or v.endswith("@nitt.edu")):
            raise ValueError("Invalid Email domain")     
        return v 

def test_registration(data):
    try:
        StudentRegistration(**data)
        print(f"✅Valid Student : {data["name"]}")
    except ValidationError as e:
        print(f"❌Error for {data.get("name", "Unknown")}:")
        for error in e.errors():
            print(f" -{error['loc'][0]} : {error['msg']}")

correct_inputs = [
{"name": "Alice", "roll_number": "1234567890", "email": "alice@nitt.edu", "age": 20, "percentage_12th": 85.5},
{"name": "Bob", "roll_number": "2110101234", "email": "bob@vitstudent.ac.in", "age": 20, "percentage_12th": 72.3},
{"name": "Charlie", "roll_number": "9998887776", "email": "charlie@nitt.edu", "age": 21, "percentage_12th": 90.0}
]

incorrect_inputs = [
{"name": "Al", "roll_number": "123", "email": "wrong@gmail.com", "age": 25, "percentage_12th": 26},
{"name": "Dave", "roll_number": "1234567890", "email": "dave@ nitt.edu", "age": 16, "percentage_12th": 90},
{"name": "Eve", "roll_number": "A1B2C3D4E5", "email": "eve@nitt.edu", "age": 19, "percentage_12th": 80}
]

print("--- TESTING CORRECT INPUTS ---")
for item in correct_inputs : test_registration(item)

print("--- TESTING INCORRECT INPUTS ---")
for item in incorrect_inputs : test_registration(item)