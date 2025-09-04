from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username:str

    @field_validator('username')
    def usernameLength(cls,v):
        if(len(v)<4):
            raise ValueError('Username must be atleast 4 characters')
        return v

class SignupData(BaseModel):
    password:str
    confirmPassword:str

    @model_validator(mode='after')
    def passwordMatch(cls,values):
        if(values.password!=values.confirmPassword):
            raise ValueError('Passwords do not match')
        return values