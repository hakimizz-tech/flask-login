# Login Assignment

This project is a Flask-based web application that demonstrates user authentication and login functionality. It uses MongoDB for data storage, Flask-Mail for email functionality, and PyOpenSSL for HTTPS support.

## Prerequisites
Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- MongoDB Compass (or MongoDB server)
- PyOpenSSL (`pip install pyopenssl`)
- A mail server (e.g., Gmail, Outlook, or a local SMTP server)

## Setup Instructions

### 1. Generate Private and Public Keys for HTTPS
To enable HTTPS, you need to generate a private key and a self-signed certificate using PyOpenSSL.

Run the following command to generate the keys:

```bash
python index.py
```

This will generate two files:

- `private.key`: The private key.
- `certificate.crt`: The self-signed certificate.

Place these files in the `ssl` directory of your project.

### 2. Generate a Secret Key
Flask requires a secret key for securely signing session cookies. You can generate a secure 16-character hexadecimal secret key using Python's `secrets` module:

```python
import secrets

secret_key = secrets.token_hex(16)
print(secret_key)
```

Set this key in your Flask application configuration.

### 3. Create a Virtual Environment
Create a virtual environment to isolate the project dependencies.

Navigate to the project directory:

```bash
cd path/to/project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies
Install the required Python packages listed in `requirements.txt`.

Run the following command:

```bash
pip install -r requirements.txt
```

### 5. Set Up MongoDB
Install MongoDB Compass or start a MongoDB server.

Open MongoDB Compass and create a new database (e.g., `login_assignment`).

Update the MongoDB connection URI in `app.py`:

```python
app.config['MONGO_URI'] = 'mongodb://localhost:27017/login_assignment'
```

### 6. Configure the Mail Server
Set up the mail server configuration in `app.py`.

Update the following settings with your mail server details:

```python
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587  # Replace with your SMTP port
app.config['MAIL_USE_TLS'] = True  # Use TLS for security
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your email password
```

If using Gmail, enable "Allow less secure apps" or generate an App Password.

### 7. Run the Development Server
Start the Flask development server.

Run the following command:

```bash
python run.py
```

Open your browser and navigate to:

```
https://localhost:5000
```

**Note:** Since you're using a self-signed certificate, your browser may show a security warning. Proceed to the site by accepting the warning.
