# Urban Service Booking Platform - Project Summary

## 1. Project Overview
A full-stack web application connecting customers with local service providers (plumbers, cleaners, electricians, etc.).
- **Tech Stack**: Django (Backend), HTML5/CSS3/Bootstrap 5 (Frontend), SQLite (Database), JavaScript (Interactivity).

## 2. Key Modules & User Roles

### A. Customer Module
*   **Registration/Login**: Secure signup with role selection.
*   **Service Discovery**:
    *   Search Bar (Home & Service Page) for finding services by keyword.
    *   Category Filtering (Plumbing, Cleaning, etc.).
    *   Rich Service Details (Price, Description, Estimated Time).
*   **Booking System**:
    *   Date & Time Selection (with validation for business hours).
    *   **Geolocation**: "Use My Location" feature to auto-fill map coordinates.
    *   Address Management.
*   **Dashboard**:
    *   View Booking History.
    *   Track Status (Pending, Confirmed, Completed).
    *   Action: Cancel Booking (if pending).

### B. Service Provider Module
*   **Registration**: Specialized signup with Skills & Experience fields.
*   **Profile Management**:
    *   **Service Selection**: Choose specific services to offer.
    *   Update Skills, Experience, and Profile Picture.
*   **Job Management (Dashboard)**:
    *   **Smart Job Matching**: Only see job requests for services they offer.
    *   **Google Maps Integration**: One-click navigation to customer location.
    *   **Workflow**: Accept Jobs -> Confirm -> Complete.
    *   View customer contact details *only* after confirmation (Privacy/Security).

### C. Admin Module
*   **Dashboard**: Visual statistics (Total Revenue, Active Bookings, New Providers).
*   **Management**:
    *   Verify new Service Providers.
    *   Manage Services & Categories.
    *   Oversee all system bookings.

## 3. Core Workflows (Step-by-Step)

### Workflow 1: The Booking Journey
1.  **Search**: Customer searches for "Plumber" on Home Page.
2.  **Select**: Click "View Details" on a service card.
3.  **Book**: Fill Booking Form -> Select Date/Time -> Click "Use My Location".
4.  **Confirm**: System creates a "Pending" booking.

### Workflow 2: The Service Fulfillment
1.  **Notification**: Relevant Providers see the new job in "New Job Requests".
2.  **Acceptance**: Provider clicks "Accept". Booking becomes "Confirmed".
3.  **Connection**: Customer details & Phone Number are revealed to Provider.
4.  **Navigation**: Provider clicks "View on Google Maps" to reach location.
5.  **Completion**: Provider marks job as "Completed" after service.

## 4. Key Technical Features
*   **Smart Filtering**: Backend logic matches Jobs to Providers based on selected Services.
*   **Geolocation API**: Browser-based GPS integration for accurate addressing.
*   **Client-Side Validation**: JavaScript prevents invalid dates (past dates) or times (outside 9-5).
*   **Modern UI/UX**:
    *   Glassmorphism Navbar.
    *   Sticky Filtering Sidebar.
    *   Responsive Grids & Hover Animations.
