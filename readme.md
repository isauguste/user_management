## Feature: Profile Fields + Professional Status Upgrade

This branch adds:
- User profile fields and update flow:
  - `first_name`, `last_name`, `bio`, `profile_picture_url`, `linkedin_profile_url`, `github_profile_url`, `location`
  - Users can update their own profile via **`PUT /me`** (JWT required, email must be verified)
- Professional status management:
  - Service method to upgrade a user to professional (`is_professional = true`, timestamp)
  - Admin/Manager endpoints (list/get/delete) are protected by role guards
- Email verification:
  - Registration sends a Mailtrap email with a verification link
  - **`GET /verify-email/{user_id}/{token}`** confirms the account

### New / Modified Endpoints
- `POST /register/` → creates user, sends Mailtrap verification email
- `GET /verify-email/{user_id}/{token}` → verifies email (needed before login succeeds in UX)
- `POST /login/` → OAuth2 password flow, returns **access_token**
- `PUT /me` → update authenticated user's profile fields
- `GET /users/` (ADMIN/MANAGER) → list users
- `GET /users/{user_id}` (ADMIN/MANAGER) → get user by id
- `DELETE /users/{user_id}` (ADMIN/MANAGER) → delete user

### Run Locally
```bash
# create and activate venv (if needed)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# set your environment
cp .env.sample .env
# fill in DB + Mailtrap + jwt_secret

# run migrations
alembic upgrade head

# start app
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

