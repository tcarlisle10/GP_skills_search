from marshmallow import Schema, fields

# User schema for search results
class UserSchema(Schema):
    id = fields.Int()
    firstname = fields.Str()
    lastname = fields.Str()
    email = fields.Str()
    location = fields.Str()

# Job schema for search results
class JobSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    location = fields.Str()
    job_type = fields.Str()
    posted_by = fields.Str() 

class SkillSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    users = fields.List(fields.Nested(UserSchema))