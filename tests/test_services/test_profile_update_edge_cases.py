import pytest
from app.services.user_service import UserService

@pytest.mark.asyncio
async def test_update_all_profile_fields(db_session, user):
    updated_data = {
        "full_name": "Updated Name",
        "bio": "This is an updated bio.",
        "profile_picture_url": "https://example.com/profile.jpg"
    }
    updated_user = await UserService.update(db_session, user.id, updated_data)
    assert updated_user.full_name == updated_data["full_name"]
    assert updated_user.bio == updated_data["bio"]
    assert updated_user.profile_picture_url == updated_data["profile_picture_url"]

@pytest.mark.asyncio
@pytest.mark.parametrize("field, value", [
    ("full_name", "Solo Name Update"),
    ("bio", "Just the bio, thanks."),
    ("profile_picture_url", "https://example.com/solo.png"),
])
async def test_update_single_profile_field(db_session, user, field, value):
    updated_user = await UserService.update(db_session, user.id, {field: value})
    assert getattr(updated_user, field) == value

@pytest.mark.asyncio
async def test_invalid_profile_picture_url_format(db_session, user):
    updated_data = {
        "profile_picture_url": "https://example.com/file.txt"
    }
    updated_user = await UserService.update(db_session, user.id, updated_data)
    assert updated_user is None  # Should fail validation

@pytest.mark.asyncio
@pytest.mark.parametrize("field", ["full_name", "bio"])
async def test_update_with_empty_string(db_session, user, field):
    updated_user = await UserService.update(db_session, user.id, {field: ""})
    # Depends on design — this assumes empty strings are allowed
    assert getattr(updated_user, field) == ""
