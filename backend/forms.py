from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserAddUpdateForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class WorkspaceAddForm(FlaskForm):
    """Form for adding workspaces."""

    readable_name = StringField("Readable Name", validators=[DataRequired()])


class TeamAddUpdateForm(FlaskForm):
    """Form for validating adding and updating a team."""
    name = StringField("Name", validators=[DataRequired()])
