from app.extensions import ma
from app.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = UserSchema(exclude=['firstname', 'lastname', 'rating'])