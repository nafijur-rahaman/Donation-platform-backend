
# Donation Platform Backend

This is the backend service for a donation platform that manages user accounts, donation campaigns, and secure payment processing. The backend provides APIs for handling all core functionalities, including user authentication, campaign management, donation tracking, and more.



## Features

- User Authentication: Secure registration, login, and role-based access control (donors, campaign organizers, admins)
- Campaign Management: Create, update, filter and manage donation campaigns with goals, descriptions, and progress tracking.
- Payment Integration: Securely process donations via  payment gateways (e.g., SSLCommerz).
- Donation Tracking: Track donation history, filter and provide real-time campaign updates
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

## Models

### User Model

- **email**: `EmailField` (unique=True)
- **image**: `CloudinaryField` (default='dummyimage.jpg')
- **profession**: `CharField` (max_length=100, default="Software Engineer")
- **phone_number**: `CharField` (max_length=11, blank=True, null=True)
- **bio**: `TextField` (blank=True)
- **status**: `CharField` (max_length=30, choices=STATUS_CHOICES, default="active")
- **address**: `CharField` (max_length=200, blank=True, null=True)
- **created**: `DateField` (auto_now_add=True, blank=True, null=True)

### Campaigns Model

- **creator**: `ForeignKey` to `Creator`
- **title**: `CharField` (max_length=200)
- **image**: `CloudinaryField` (default='placeholder_image_public_id')
- **description**: `TextField` (blank=True, null=True)
- **goal_amount**: `DecimalField` (max_digits=12, decimal_places=2)
- **fund_raised**: `DecimalField` (max_digits=12, decimal_places=2, default=0)
- **location**: `CharField` (max_length=200)
- **deadline**: `DateField`
- **type**: `CharField` (choices=TYPE_CHOICES, max_length=20)
- **status**: `CharField` (choices=STATUS_CHOICES, default='Pending')
- **created_at**: `DateTimeField` (auto_now_add=True)

### CreatorRequest Model

- **user**: `ForeignKey` to `User`
- **organization**: `CharField` (max_length=200, blank=True, null=True)
- **experience_years**: `PositiveIntegerField` (default=0)
- **service_areas**: `TextField` (blank=True, null=True)
- **message**: `TextField`
- **status**: `CharField` (max_length=10, choices=STATUS_CHOICES1, default='pending')

### ManagerModel

- **user**: `ForeignKey` to `User`
- **designation**: `CharField` (max_length=100, default="manager")

## Database Schema

- **Users**: Stores information for all users, including creators and managers, linked to Django’s `User` model.
- **Campaigns**: Contains data related to fundraising campaigns created by users.
- **CreatorRequests**: Stores requests made by users to become creators on the platform.
- **ManagerModel**: Stores information about managers associated with user accounts.


## API Endpoints

### User Authentication

- **Register a New User**  
  `POST` [https://donation-platform-backend-psi.vercel.app/api/users/register/](https://donation-platform-backend-psi.vercel.app/api/users/register/)
  
- **Log in a User**  
  `POST` [https://donation-platform-backend-psi.vercel.app/api/users/login/](https://donation-platform-backend-psi.vercel.app/api/users/login/)
  
- **Log in Admin**  
  `POST` [https://donation-platform-backend-psi.vercel.app/api/manager/login/](https://donation-platform-backend-psi.vercel.app/api/manager/login/)
  
- **Log out a User**  
  `GET` [https://donation-platform-backend-psi.vercel.app/api/users/logout/](https://donation-platform-backend-psi.vercel.app/api/users/logout/)
  
- **Log out Admin**  
  `GET` [https://donation-platform-backend-psi.vercel.app/api/manager/logout/](https://donation-platform-backend-psi.vercel.app/api/manager/logout/)

### Campaign Management

- **List All Campaigns**  
  `GET` [https://donation-platform-backend-psi.vercel.app/api/campaign/list/](https://donation-platform-backend-psi.vercel.app/api/campaign/list/)
  
- **Create a New Campaign**  
  `POST` [https://donation-platform-backend-psi.vercel.app/api/campaign/list/](https://donation-platform-backend-psi.vercel.app/api/campaign/list/)
  
- **Update a Campaign**  
  `PUT` [https://donation-platform-backend-psi.vercel.app/api/campaign/list/campaignId/](https://donation-platform-backend-psi.vercel.app/api/campaign/list/campaignId/)
  
- **Delete a Campaign**  
  `DELETE` [https://donation-platform-backend-psi.vercel.app/api/campaign/list/campaignId/](https://donation-platform-backend-psi.vercel.app/api/campaign/list/campaignId/)

### Donation Management

- **Process a Donation**  
  `POST` [https://donation-platform-backend-psi.vercel.app/api/transactions/initiate-payment/](https://donation-platform-backend-psi.vercel.app/api/transactions/initiate-payment/)
  
- **View Donation History**  
  `GET` [https://donation-platform-backend-psi.vercel.app/api/transactions/list/](https://donation-platform-backend-psi.vercel.app/api/transactions/list/)

### Notes

- Replace `user_id` and `tuitionId` in the URLs with the actual user or tuition post ID as required.
- Ensure you handle authentication tokens properly in your requests.


## Contact

For inquiries or support, please contact:
- **Project Developer**: Md. Nafijur Rahaman
- **Email**: tanjidnafis@gmail.com

