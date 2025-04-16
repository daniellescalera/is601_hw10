Danielle Scalera assignment 10 event manager. 

### Issues resolved with links: 
1. Password Validation Not Enforced
  - Issue: Weak passwords were being accepted.
  - Fix: Enforced password strength via UserCreate schema.
  - Link: see https://github.com/daniellescalera/is601_hw10/blob/3b7f99a41774dda42266d3440a7483c41ee78684/app/schemas/user_schemas.py#L45 

2. Missing Email Verification Logic
  - Issue: Email verification was not being sent properly.
  - Fix: Implemented send_verification_email in EmailService.
  - Link: [services/email_service.py, send_verification_email method](https://github.com/daniellescalera/is601_hw10/blob/3b7f99a41774dda42266d3440a7483c41ee78684/app/services/email_service.py#L31)

3. Invalid Profile Picture Format Was Accepted
  - Issue: Image URLs ending in .txt were accepted.
  - Fix: Added stricter validation for profile picture URLs.
  - Link: [schemas/user_schemas.py, validate_url function](https://github.com/daniellescalera/is601_hw10/blob/3b7f99a41774dda42266d3440a7483c41ee78684/app/schemas/user_schemas.py#L17)

4. User ID UUID Mismatch in UserResponse
  - Issue: Test expected a string, but response returned a UUID object.
  - Fix: Updated test to compare UUIDs properly.
  - Link: [test_schemas/test_user_schemas.py, test_user_response_valid](https://github.com/daniellescalera/is601_hw10/blob/3b7f99a41774dda42266d3440a7483c41ee78684/tests/test_schemas/test_user_schemas.py#L45)

5. Tests Called Email Service Function Incorrectly
  - Issue: Email service passed as a lambda but used as a function.
  - Fix: Updated call to get_email_service() instead of get_email_service.
  - Link: [tests/test_services/test_password_validation.py ](https://github.com/daniellescalera/is601_hw10/blob/3b7f99a41774dda42266d3440a7483c41ee78684/tests/test_services/test_password_validation.py)

6. All pytest failures and errors passed 

### Reflection: 
Working on this assignment helped me solidify my understanding of FastAPI and the importance of robust validation and testing in a real-world API service. I gained hands-on experience with concepts like schema enforcement, email verification flows, and secure user authentication. Fixing broken code forced me to slow down and read through unfamiliar logic, which was valuable in helping me build better debugging habits and recognize patterns in how errors propagate.

One of the biggest challenges I faced was debugging silently failing tests and resolving issues related to environment configuration, like properly setting up the .env file and getting Mailtrap to work. I also ran into multiple roadblocks with test failures that weren’t immediately clear from the error messages, especially related to UUID mismatches and incorrect password validations. Stepping through each failure, examining logs, and even inspecting code I hadn’t written was key to pushing through. I also had to navigate Docker containers while testing and committing changes, which improved my comfort working with containerized environments.

Overall, this project helped me improve both technically and organizationally. I learned to manage issues through GitHub, link commits to fixes, and maintain a clean and readable project structure. Submitting a partially working repository under time pressure also helped me learn how to prioritize what’s required while still working toward completeness. It wasn’t always easy, but I walked away with a much deeper understanding of backend development, API validation, and collaborative Git workflows.