from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of patient', description='Give the name of patient in less than 50 chars', examples=['Henil', 'Nitish'])]

    email: EmailStr
    linkdin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married : Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

patient_info = {'name':'Henil', 'email':'abc@gmail.com', 'linkdin_url':'http://linkdin.com/1322', 'age':'30', 'weight':75.2, 'contact_details':{'phone':'234567'}}

patient1 = Patient(**patient_info)

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print('Updated')

update_patient_data(patient1)