from marshmallow import Schema, fields
from app.models import User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True  # Include foreign key fields if needed
        exclude = ["password", "created_at"]  # Exclude sensitive or unnecessary fields

profile_schema = ProfileSchema()