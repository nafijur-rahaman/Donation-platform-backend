
# Donation Platform Backend

This is the backend service for a donation platform that manages user accounts, donation campaigns, and secure payment processing. The backend provides APIs for handling all core functionalities, including user authentication, campaign management, donation tracking, and more.



## Features

- User Authentication: Secure registration, login, and role-based access control (donors, campaign organizers, admins)
- Campaign Management: Create, update, and manage donation campaigns with goals, descriptions, and progress tracking.
- Payment Integration: Securely process donations via  payment gateways (e.g., SSLCommerz).
- Donation Tracking: Track donation history, and provide real-time campaign updates
- Scalable API: Built to handle high transaction volumes and user activity.




## Tech Stack

**frontend:** Html5,TailwindCSS,Javascript,

**Backend:** Django

**Database:** PostgreSQL

**Payment Gateway:** SSLCommerz

**Cloud Storage:** Cloudinary




## Installation

Clone the repository:

```bash
https://github.com/nafijur-rahaman/Donation-platform-backend
cd donation-platform-backend
```
Create a virtual environment and activate it:

```bash
py -m venv myworld
venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
```bash
SECRET_KEY= your_secret_key

NB: Create email for send email:

EMAIL= your_email
EMAIL_PASSWORD= your_email_pass

NB: Create a free database on supabase then fulfiled the require fields:

DB_NAME=postgres
Db_USER=
DB_PASS=
DB_HOST=aws-0-ap-southeast-1.pooler.supabase.com
DB_PORT=6543

NB: Create a fre cloud on cloudinary and then fulfiled the require fields:
CLOUD_NAME=
API_KEY=
API_SECRET_KEY=
```
Run migrate and migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
Start the development server:
```bash
python manage.py runserver
```

## Api endpoint
#### User Authentication:

- POST /api/register/ – Register a new user

- POST /api/login/ – Log in a user

- POST /api/logout/ – Log out a user
#### Campaign Management:

- GET /api/campaigns/ – List all campaigns

- POST /api/campaigns/create/ – Create a new campaign

- PUT /api/campaigns/update/<id>/ – Update a campaign

- DELETE /api/campaigns/delete/<id>/ – Delete a campaign

#### Donation Management:

- POST /api/donations/ – Process a donation

- GET /api/donations/history/ – View donation history

## Support

For support, email tanjidnafis@.com 

