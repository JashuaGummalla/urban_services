# Deploying to Render

Render is a unified cloud to build and run all your apps and websites with free SSL, a global CDN, and private networks.

## Prerequisites

1.  **GitHub Account**: Ensure your code is pushed to a GitHub repository.
2.  **Render Account**: Sign up at [render.com](https://render.com/).

## Step 1: Create a PostgreSQL Database

1.  Log in to your Render Dashboard.
2.  Click **New +** and select **PostgreSQL**.
3.  **Name**: Give your database a name (e.g., `urban-services-db`).
4.  **Region**: Choose a region closest to you (e.g., Singapore, Frankfurt, Oregon).
5.  **Instance Type**: Select **Free**.
6.  Click **Create Database**.
7.  Once created, copy the **Internal DB URL** (you will need this later, but Render often auto-configures it if you link services).
    *   *Note: If you plan to connect from your local machine, use the External Database URL, but for the web service, the Internal one is faster and secure.*

## Step 2: Create a Web Service

1.  Go back to the Dashboard and click **New +**, then select **Web Service**.
2.  Connect your GitHub repository.
3.  **Name**: Give your service a name (e.g., `urban-services`).
4.  **Region**: Choose the same region as your database.
5.  **Branch**: `main` (or `master`).
6.  **Runtime**: **Python 3**.
7.  **Build Command**:
    ```bash
    pip install -r requirements.txt && python manage.py migrate
    ```
    *   *Note: This command installs dependencies and applies database migrations automatically during deployment.*
    *   *If you need to create a superuser, you might need to use the Shell tab in Render after deployment or add a script.*
8.  **Start Command**:
    ```bash
    gunicorn urban_services.wsgi:application
    ```
9.  **Instance Type**: Select **Free**.

## Step 3: Environment Variables

Scroll down to the **Environment Variables** section and add the following keys:

| Key | Value |
| :--- | :--- |
| `PYTHON_VERSION` | `3.11.0` (Matches your runtime.txt) |
| `SECRET_KEY` | Generate a random secret key (you can use an online generator). |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*` (Or your specific Render URL once generated, e.g., `urban-services.onrender.com`) |
| `DATABASE_URL` | select "Add from existing" and choose the database you created in Step 1. Render will automatically populate this. |

## Step 4: Deploy

1.  Click **Create Web Service**.
2.  Render will start building your application. You can watch the logs in the dashboard.
3.  Once the build finishes and the service is "Live", click the URL at the top left (e.g., `https://urban-services.onrender.com`) to view your app.

## Troubleshooting

-   **Static Files**: If images/CSS are missing, ensure `whitenoise` is configured in `MIDDLEWARE` in `settings.py` (it should be).
-   **Database Errors**: Check the `DATABASE_URL` environment variable.
-   **Logs**: Check the "Logs" tab in Render for any detailed error messages.

## Superuser Creation

To access the Django Admin:

1.  Go to your Web Service in Render.
2.  Click on the **Shell** tab (Connect via SSH).
3.  Run:
    ```bash
    python manage.py createsuperuser
    ```
4.  Follow the prompts to create your admin account.
