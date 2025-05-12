# Disaster Management System

## Overview
This is a **Disaster Management System** that helps to manage crisis situations, volunteers, donations, and relief inventories. It is designed to provide a seamless and efficient way for admins to handle crises and volunteers while enabling the public to contribute through donations. The system also tracks the flow of resources and generates reports for analysis.

---

## Features

### 1. **User Types**
- **Admin**: 
  - Manages and verifies volunteers, crisis reports, donations, and other resources.
- **Volunteer**:
  - Can register, log in, and respond to crises assigned by the admin.
  
### 2. **Donation Fund**
- Users can donate to the disaster-affected areas.
- The total fund amount is visible to all viewers, and a form for donations is available.

### 3. **Charts**
- Provides visual charts for:
  - Daily donations
  - Daily expenses

### 4. **Admin Functions**
- Admin can:
  - Verify and approve volunteers
  - Assign volunteers to specific tasks, crises, and locations.

### 5. **Crisis Management**
- Anonymous users can add crisis entries including:
  - Location tags
  - Title
  - Image
  - Description
  - Severity
  - Required help
- Admin approval is required to make the crisis visible to the public.

### 6. **Inventory Management**
- Volunteers can manage and purchase relief supplies such as:
  - Puffed rice
  - Flattened rice
  - Sugar
  - Fresh water
- Features to manage both donated and purchased goods.

### 7. **Admin Reports**
- Admin can generate/export reports in **CSV/Excel** format for:
  - Daily donations
  - Daily expenses
  - Inventory management

---

## Project Pages

1. **Register Page**: `/register`  
   Allows volunteers to register.

2. **Login Page**: `/login`  
   Login for both admins and volunteers.

3. **Homepage**: `/home` or `/`  
   Displays total donations, recent crises, and available volunteers.

4. **Donation Page**: `/donation`  
   Displays the total amount of donations, along with daily donation and expense charts.

5. **Crisis Page**: `/crisis`  
   Lists all the crises, and allows users to add new ones (pending admin approval).

6. **Volunteer Page**: `/volunteer`  
   Lists volunteers and their assignments.

7. **Inventory Page**: `/inventory` (Optional)  
   Allows management of relief and expense goods.

8. **Profile Page**: `/account` (Optional)  
   Lets users update their information like name, username, phone number, etc.

9. **Admin Management Pages**: `/admin/{{section}}`  
   Admin can manage volunteers, crises, and generate reports.

---

## Technologies Used

- **Backend**: Django (Python)  
- **Frontend**: Bootstrap, Tailwind CSS (using Django templates)  
- **Database**: PostgreSQL  
- **Libraries**:  
  - Django REST Framework (for optional API features)
  - psycopg2-binary (for PostgreSQL support)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/disaster-management-system.git
cd disaster-management-system

