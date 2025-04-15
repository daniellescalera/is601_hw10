import pytest
from app.services.user_service import UserService

@pytest.mark.asyncio
@pytest.mark.parametrize("invalid_password", [
    "short!",                # Too short
    "alllowercase1!",        # Missing uppercase
    "ALLUPPERCASE1!",        # Missing lowercase
    "NoNumber!",             # Missing digit
    "NoSpecial123",          # Missing special character
])
async def test_password_validation_invalid(db_session, invalid_password):
    user_data = {
        "username": f"user_{invalid_password[:4]}",
        "email": f"{invalid_password[:4]}@example.com",
        "password": invalid_password
    }
    user = await UserService.register_user(db_session, user_data)
    assert user is None


@pytest.mark.asyncio
async def test_password_validation_valid(db_session):
    user_data = {
        "username": "validuser123",
        "email": "validuser123@example.com",
        "password": "Valid123!Password"
    }
    user = await UserService.register_user(db_session, user_data)
    assert user is not None
