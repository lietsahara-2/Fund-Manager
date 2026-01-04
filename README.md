# Fund-Manager
The project is a financial group management system built with Django and Django Rest Framework
It is designed to support group-based financial operations such as:

* Member contributions
* Loan applications and approvals
* Automatic transaction recording
* Role-based access (admins vs members)

Members make requests and administrators approve or reject them.

## Features

### Groups & Memberships

* Users belong to groups via memberships
* Each group has an administrator
* Memberships link users to all financial records

### Contributions

* Members submit contributions
* Contributions are pending by default
* Admins approve contributions
* Approved contributions automatically create a transaction record

### Loans

* Members request loans
* Loans start with `pending` status
* Admins can approve or reject loans

### Transactions

* Transactions are not **edited manually**
* Created automatically when:

  * A contribution is approved
  * A loan is approved 
* Users can view transactions
* Admins manage all financial data

## Audit
* Prior user actions can be viewed here
* No user has permission to modify it ensuring records integrity

### Authentication & Permissions

* Custom user model (email-based login)
* Token authentication
* Role-based access:

  * **Admins**: approve/reject contributions & loans
  * **Users**: create and view records
  
* It is important to note that all users can view eachothers records as this is the model used in for the group for which the app is made. 

---

## Tech Stack

* **Backend:** Django, Django Rest Framework
* **Database:** SQLite 
* **Authentication:** DRF Token Authentication
* **Permissions:** `IsAuthenticated`, `IsAdminUser`
* **API Architecture:** RESTful APIs + custom actions

---

## Approval Workflow

### Contribution Flow

1. Member submits contribution
2. Contribution saved as unverified
3. Admin approves contribution
4. System:

   * Marks contribution as verified
   * Records approver and time
   * Creates a transaction

### Loan Flow

1. Member submits loan request
2. Loan status = `pending`
3. Admin approves or rejects
4. If approved:

   * Outstanding balance is initialized
   * Loan disbursement transaction is created

---

## API Endpoints (Examples)

### Contributions

Create contribution           POST    `/finance/contributions/`                   
View contributions            GET     `/finance/contributions/`        
Approve contribution (admin)  PATCH   `/finance/contributionsadmin/{id}/approve/` 

### Loans

Request loan          POST    `/finance/loans/`                   
View loans            GET     `/finance/loans/`               
Approve loan (admin)  PATCH   `/finance/loansadmin/{id}/approve/`
Reject loan (admin)   PATCH   `/finance/loansadmin/{id}/reject/` 

### Transactions
View transactions   GET     `/finance/transactions/`

## Audit
View user actions   GET   `/audit/`

## Groups
View groups             GET     `/goups/listgroups/`
View memberships        GET     `/groups/listmemberships`
Manage  groups          POST    `/groups/groupadmin`
Modify memberships      POST    `/groups/membershipadmin/`

## Users
View users              GET     `/users/listuser/`
manage users            POST    `/users/adminuser/`
updating own info       PATCH   `/users/update/`

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd project
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate
```


### 3.Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```
---

## Notes & Design Decisions

* Transactions are **system-generated only** 
* Approval logic lives in **custom DRF actions**
* Comments in code explain business logic and future extensibility
* Filtering by user can be enabled later if required

---

## Project Scope

This project is for educational purposes and can be extended for real-world
use with additional security, validations, and UI improvements.




