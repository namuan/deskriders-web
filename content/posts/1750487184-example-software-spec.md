+++ 
date = 2025-06-21T07:26:24+01:00
title = "Example Software Spec"
description = "Copy of example software spec"
slug = "" 
tags = ["specification", "requirements", "testing"]
categories = ["software"]
externalLink = ""
series = []
+++

Copied from https://dzone.com/articles/software-specs-an-elaborate-example

**Software Specs 2.0: An Elaborate Example**

**Stelios Manioudakis, PhD**

This article is a follow-up to the article that lays the theoretical foundation for software requirement qualities.

Here, I provide an example for how to craft requirements for a User Authentication Login Endpoint. A practical illustration of how essential software requirement qualities can be interwoven when designing specifications for AI-generated code. I demonstrate the crucial interplay between explicitness (to achieve completeness), unambiguity (for machine-first understandability), constraint definition (to guide implementation and ensure viability), and testability (through explicit acceptance criteria). We'll explore how these qualities can practically be achieved through structured documentation. Our goal is that our AI assistant has a clear, actionable blueprint for generating a secure and functional login service.

For explanatory purposes and to make clear how things work, I will provide a detailed requirements document. A blueprint that is by no means exhaustive, but it can serve as the basis for understanding and expanding. Documentation can be lightweight in practice, but this article must focus on details to avoid confusion. The document starts by stating the requirement ID and title. A feature's description follows, along with its functional and non-functional requirements. Data definitions, implementation constraints, acceptance criteria, and error handling fundamentals are also documented.

## Requirement Document: User Authentication - Login Endpoint

### 1. Requirement ID and Title

Unique IDs are crucial for traceability, allowing you to link this specific requirement to design documents, generated code blocks, and test cases. This helps in maintenance and debugging.

- **ID**: REQ-AUTH-001
- **Title**: User Login Endpoint

### 2. Feature Description

The feature description provides a high-level overview and context. For AI, this helps establish the overall goal before diving into specifics. It answers the "what" at a broad level.

This feature provides an API endpoint for registered users to authenticate themselves using their email address and password. Successful authentication will grant access by providing a session token.

### 3. Functional Requirements (FR)

Functional requirements are broken down into atomic, specific statements. Keywords like MUST, SHOULD (though only MUST is used here for strictness) can follow RFC 2119 style, which AI-assistants can be trained to recognize. "Case-insensitive search," "structurally valid email format," and specific counter actions (increment, reset) leave little room for AI misinterpretation.

This promotes unambiguity and precision. Details like checking if an account is disabled and the account lockout mechanism (FR11) cover crucial edge cases and security aspects, aiming for explicitness and completeness.

- **FR1**: The system MUST expose an HTTPS POST endpoint at `/api/v1/auth/login`.
- **FR2**: The endpoint MUST accept a JSON payload containing email (string) and password (string).
- **FR3**: The system MUST validate the provided email:
  - **FR3.1**: It MUST be a non-empty string.
  - **FR3.2**: It MUST be a structurally valid email format (e.g., user@example.com).
- **FR4**: The system MUST validate the provided password:
  - **FR4.1**: It MUST comply with a strong password policy.
- **FR5**: If input validation (FR3, FR4) fails, the system MUST return an error (see Error Handling EH1).
- **FR6**: The system MUST retrieve the user record from the Users database table based on the provided email.
- **FR7**: If no user record is found for the email, or if the user account is marked as disabled, the system MUST return an authentication failure error (see Error Handling EH2).
- **FR8**: If a user record is found and the account is active, the system MUST verify the provided password against the stored hashed password for the user using the defined password hashing algorithm (see IC3: Security).
- **FR9**: If password verification fails, the system MUST increment a failed_login_attempts counter for the user and return an authentication failure error (see Error Handling EH2).
- **FR10**: If password verification is successful:
  - **FR10.1**: The system MUST reset the failed_login_attempts counter for the user to 0.
  - **FR10.2**: The system MUST generate a JSON Web Token (JWT) (see IC3: Security for JWT specifications).
  - **FR10.3**: The system MUST return a success response containing the JWT (see Data Definitions - Output).
- **FR11**: Account lockout: If failed_login_attempts for a user reaches 5, their account MUST be temporarily locked for 15 minutes. Attempts to log in to a locked account MUST return an account locked error (see Error Handling EH3), even with correct credentials.

### 4. Data Definitions

Clearly defining data definitions (schemas) for inputs and outputs is critical for AI to generate correct data validation, serialization, and deserialization logic.

Using terms like "string, required, format: email" helps the AI map to data types and validation rules (e.g., when using Pydantic models). This contributes to Structured Input.

- **Input Payload (JSON)**:
  - `email` (string, required, format: email)
  - `password` (string, required, minLength: 1)
- **Success Output (JSON, HTTPS 200)**:
  - `access_token` (string, JWT format)
  - `token_type` (string, fixed value: "Bearer")
  - `expires_in` (integer, seconds, representing token validity duration)
- **Error Output (JSON, specific HTTPS status codes - see Error Handling)**:
  - `error_code` (string, e.g., "INVALID_INPUT", "AUTH_FAILED", "ACCOUNT_LOCKED")
  - `message` (string, human-readable error description)

### 5. Non-Functional Requirements (NFRs)

NFRs reduce ambiguity, guide code generation toward aligned behaviors, and make the resulting software easier to verify against clearly defined benchmarks. They make qualities like performance and security testable and unambiguous. Specific millisecond targets and load conditions are set. Also, as an example, specific actions (no password logging, input sanitization) and references to further constraints (IC3) are provided.

- **NFR1 (Performance)**: The average response time for the login endpoint MUST be less than 300ms under a load of 100 concurrent requests. P99 response time MUST be less than 800ms.
- **NFR2 (Security)**: All password handling must adhere to security constraints specified in IC3. No sensitive information (passwords) should be logged. Input sanitization must be performed to prevent common injection attacks.
- **NFR3 (Auditability)**: Successful and failed login attempts MUST be logged to the audit trail with timestamp, user email (for failed attempts, if identifiable), source IP address, and success/failure status. Failed attempts should include the specific failure reason (e.g., "user_not_found," "incorrect_password," "account_locked").

### 6. Implementation Constraints and Guidance (IC)

This section guides the AI's choices (Python/FastAPI, SQLAlchemy, Pydantic, bcrypt, JWT structure) without dictating the exact low-level code. For the purposes of this article, these specific choices are random and are not considered to be optimal in any sense. You are free to choose your own tech stack, architectural patterns, etc. Implementation constraints can guide towards Viability within the project's ecosystem and to meet specific security and architectural requirements.

Also, it should be mentioned that the constraints shown are indicative and are by no means exhaustive. Currently, it depends on the specific AI assistant and the project under development, which constraints are more appropriate. Will there be AI assistants that develop code perfectly without constraints and guidance from humans? It remains to be seen.

- **IC1 (Technology Stack)**:
  - Backend Language/Framework: Python 3.11+ / FastAPI.
  - Data Validation: Pydantic models derived from Data Definitions.
  - Database Interaction: Use SQLAlchemy ORM with the existing project database session configuration. Target table: Users.
- **IC2 (Architectural Pattern)**:
  - Logic should be primarily contained within a dedicated AuthenticationService class. The API endpoint controller should delegate to this service.
- **IC3 (Security - Password and Token)**:
  - Password Hashing: Stored passwords MUST be hashed using bcrypt with a work factor of 12.
  - JWT Specifications:
    - Algorithm: HS256.
    - Secret Key: Retrieved from environment variable JWT_SECRET_KEY.
    - Payload Claims: MUST include sub (user_id), email, exp (expiration time), iat (issued at).
    - Expiration: Tokens MUST expire 1 hour after issuance.
- **IC4 (Environment)**:
  - The service will be deployed as a Docker container. Configuration values (like JWT_SECRET_KEY, database connection string) MUST be configurable via environment variables.
- **IC5 (Coding Standards)**:
  - Adhere to PEP 8 style guide.
  - All functions and methods MUST include type hints.
  - All public functions/methods MUST have docstrings explaining purpose, arguments, and return values.

### 7. Acceptance Criteria (AC - Gherkin Format)

Acceptance criteria make the requirements Testable. Gherkin is an example format that is human-readable and structured. A behaviour-driven development tool that can also be used for AI assistants to derive specific test cases. It can cover happy paths and key error/edge cases, providing concrete examples of expected behavior. This gives clear verification targets for the AI-generated code.

```
Feature: User Login API Endpoint

Background:
Given a user "test@example.com" exists with a bcrypt hashed password for "ValidPassword123"
And the user account "test@example.com" is not disabled
And the user "test@example.com" has 0 failed_login_attempts
And the JWT_SECRET_KEY environment variable is set

Scenario: Successful Login with Valid Credentials
When a POST request is made to "/api/v1/auth/login" with JSON body:
"""
{
"email": "test@example.com",
"password": "ValidPassword123"
}
"""
Then the response status code should be 200
And the response JSON should contain an "access_token" (string)
And the response JSON should contain "token_type" with value "Bearer"
And the response JSON should contain "expires_in" with value 3600
And the "access_token" should be a valid JWT signed with HS256 containing "sub", "email", "exp", "iat" claims
And the failed_login_attempts for "test@example.com" should remain 0

Scenario: Login with Invalid Password
When a POST request is made to "/api/v1/auth/login" with JSON body:
"""
{
"email": "test@example.com",
"password": "InvalidPassword"
}
"""
Then the response status code should be 401
And the response JSON should contain "error_code" with value "AUTHENTICATION_FAILED"
And the response JSON should contain "message" with value "Invalid email or password."
And the failed_login_attempts for "test@example.com" should be 1

Scenario: Login with Non-Existent Email
When a POST request is made to "/api/v1/auth/login" with JSON body:
"""
{
"email": "nouser@example.com",
"password": "AnyPassword"
}
"""
Then the response status code should be 401
And the response JSON should contain "error_code" with value "AUTHENTICATION_FAILED"
And the response JSON should contain "message" with value "Invalid email or password."

Scenario: Account Lockout after 5 Failed Attempts
Given the user "test@example.com" has 4 failed_login_attempts
When a POST request is made to "/api/v1/auth/login" with JSON body: # This is the 5th failed attempt
"""
{
"email": "test@example.com",
"password": "InvalidPasswordAgain"
}
"""
Then the response status code should be 403
And the response JSON should contain "error_code" with value "ACCOUNT_LOCKED"
And the response JSON should contain "message" with value "Account is temporarily locked due to too many failed login attempts."
And the failed_login_attempts for "test@example.com" should be 5
```

### 8. Error Handling (EH)

This dedicated error handling section ensures Completeness by explicitly defining how different failure scenarios are communicated. To improve completeness we need to extensively cover edge cases and error handling. Specify exactly how different errors (validation errors, system errors, network errors) should be caught, logged, and communicated to the user (specific error messages, codes).

- **EH1 (Invalid Input)**:
  - **Trigger**: FR3 or FR4 fails.
  - **HTTPS Status**: 400 Bad Request.
  - **Response Body**: `{ "error_code": "INVALID_INPUT", "message": "Invalid input. Email must be valid and password must not be empty." }` (Example message, could be more specific based on which field failed).
- **EH2 (Authentication Failure)**:
  - **Trigger**: FR7 or FR9 occurs.
  - **HTTPS Status**: 401 Unauthorized.
  - **Response Body**: `{ "error_code": "AUTHENTICATION_FAILED", "message": "Invalid email or password." }` (Generic message to prevent user enumeration).
- **EH3 (Account Locked)**:
  - **Trigger**: Attempt to log in to an account that is locked per FR11.
  - **HTTP Status**: 403 Forbidden.
  - **Response Body**: `{ "error_code": "ACCOUNT_LOCKED", "message": "Account is temporarily locked due to too many failed login attempts." }`

## Final Remarks

**The dual purpose.** The example User Authentication Login Endpoint requirement is carefully chosen so that it can be used for two purposes. The first is to explain the basic qualities of software requirements, irrespective of who writes the code (a human or AI). The second purpose is to focus on AI-assisted code and how to use requirements to our advantage.

**Examples used are not exhaustive.** All data and examples presented in the eight paragraphs, from requirement ID and title to error handling, are indicative. Many more functional/non-functional requirements can be crafted, as well as data definitions. Acceptance criteria and error handling cases are a minimal sample of what is usually needed in practice. Negative constraints (don't use Z, avoid pattern A), for example, are not provided here but can be very beneficial as well. And of course, you may find that there are other paragraphs, beyond the scope of this article, that are tailored to your documentation needs.

**Documentation is not static.** For clarity and completeness in this article, the documentation for the User Authentication Login Endpoint seems to be static. All is well specified upfront and then fed to the AI-assistant that does the job for us. Although a detailed document can be a good starting point, factors like implementation constraints and guidance can be fully interactive. For AI assistants, for example, with sophisticated chat interfaces, a "dialogue" with AI can be an important part of the process. While initial implementation constraints can be vital, some constraints might be refined or even discovered through interaction with the AI.

## Wrapping Up

I provided a requirements document for a User Authentication Login Endpoint requirement. This example document attempts to be explicit, precise, and constrained. Software requirements must necessarily be viable whilst eminently testable. It's structured to provide an AI code generator with sufficient detail to minimize guesswork and the chances of the AI producing undesirable output.

While AI code assistants will probably be more capable and context-aware, the fundamental need for human-defined guidance appears to remain. Guiding an AI assistant for software development could be embedded in project templates. It could be via custom AI assistant configurations (if available), or even as part of a "system prompt" that always precedes specific task prompts.

A dynamic set of principles that inform an ongoing interaction with AI can be based on the following.

- **Initial scaffolding**: We provide the critical initial direction, ensuring the AI starts on the right path aligned with project standards, architecture, and non-negotiable requirements (especially security).
- **Basis for interaction**: Our documentation becomes the foundation for interactive refinement. When the AI produces output, it can be evaluated against our documented requirements.
- **Evolving knowledge base**: As the project progresses, parts of our documentation can be updated, or new ones added, reflecting new decisions or learnings.
- **Guardrails for AI autonomy**: As AIs gain more autonomy in suggesting larger code blocks or even architectural components, such documents can act as essential guardrails, ensuring their "creativity" stays within acceptable project boundaries.
