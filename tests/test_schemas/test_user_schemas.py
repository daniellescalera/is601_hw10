import pytest
from datetime import datetime
from uuid import uuid4
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, LoginRequest

def test_user_base_valid():
    user_data = {
        "nickname": "john_doe_123",
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg"
    }
    user = UserBase(**user_data)
    assert user.nickname == user_data["nickname"]
    assert user.email == user_data["email"]

def test_user_create_valid():
    user_data = {
        "nickname": "john_doe_123",
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "SecurePassword123!",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg"
    }
    user = UserCreate(**user_data)
    assert user.nickname == user_data["nickname"]
    assert user.password == user_data["password"]

def test_user_update_valid():
    update_data = {
        "first_name": "Johnny",
        "last_name": "Dough",
        "email": "john.doe.new@example.com",
        "bio": "Updated bio.",
        "profile_picture_url": "https://example.com/updated.jpg"
    }
    user_update = UserUpdate(**update_data)
    assert user_update.first_name == update_data["first_name"]
    assert user_update.email == update_data["email"]

def test_user_response_valid():
    user_data = {
        "id": str(uuid4()),
        "nickname": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "last_login_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "links": []
    }
    user = UserResponse(**user_data)
    assert user.nickname == user_data["nickname"]
    assert str(user.id) == user_data["id"]

def test_login_request_valid():
    login_data = {
        "email": "john.doe@example.com",
        "password": "SecurePassword123!"
    }
    login = LoginRequest(**login_data)
    assert login.email == login_data["email"]
