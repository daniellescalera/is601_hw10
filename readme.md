Danielle Scalera assignment 10 event manager. 

### Issues resolved with links: 
1. Password Validation Not Enforced
  - Issue: Weak passwords were being accepted.
  - Fix: Enforced password strength via UserCreate schema.
  - Link: schemas/user_schemas.py, UserCreate class

2. Missing Email Verification Logic
  - Issue: Email verification was not being sent properly.
  - Fix: Implemented send_verification_email in EmailService.
  - Link: services/email_service.py, send_verification_email method

3. Invalid Profile Picture Format Was Accepted
  - Issue: Image URLs ending in .txt were accepted.
  - Fix: Added stricter validation for profile picture URLs.
  - Link: schemas/user_schemas.py, validate_url function

4. User ID UUID Mismatch in UserResponse
  - Issue: Test expected a string, but response returned a UUID object.
  - Fix: Updated test to compare UUIDs properly.
  - Link: test_schemas/test_user_schemas.py, test_user_response_valid

5. Tests Called Email Service Function Incorrectly
  - Issue: Email service passed as a lambda but used as a function.
  - Fix: Updated call to get_email_service() instead of get_email_service.
  - Link: test_password_validation.py

6. All pytest failures and errors passed 

Reflection: 
This assignment was not easy, but I learned a lot. 