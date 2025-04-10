# Customer Issue Classification and Routing System

This system automatically processes customer issues from email and WhatsApp (via Telegram), classifies them into appropriate service groups, and creates service requests.

## Features

- Modern web interface for issue submission and tracking
- Email integration for processing customer issues
- WhatsApp integration (using Telegram Bot API)
- Automatic issue classification using machine learning
- Service request creation and management
- REST API for manual issue submission

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with the following configuration:
```
EMAIL_SERVER=imap.gmail.com
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

3. For Gmail, you'll need to:
   - Enable 2-factor authentication
   - Generate an App Password for the application

4. For Telegram:
   - Create a new bot using @BotFather
   - Get the bot token and add it to the .env file

## Running the Application

Start the application:
```bash
python main.py
```

The application will:
- Start the web server on http://localhost:8000
- Start processing emails in the background
- Initialize the Telegram bot

## Web Interface

The web interface provides the following features:

1. **Dashboard** (`/`)
   - Overview of support channels
   - Recent service requests
   - Quick access to issue submission

2. **Issue Submission** (`/submit`)
   - Form for submitting new issues
   - Priority selection
   - Contact information
   - Automatic classification

## API Endpoints

- `POST /api/process-issue`: Submit a new issue for processing
  ```json
  {
    "text": "Customer issue description",
    "source": "web/email/telegram",
    "contact_email": "customer@example.com",
    "priority": "low/medium/high"
  }
  ```

- `GET /api/recent-requests`: Get the 10 most recent service requests
- `GET /api/request/{request_id}`: Get details of a specific service request

## Service Groups

The system classifies issues into the following groups:
- Technical Support
- Billing
- Account Management
- General Inquiry

## Notes

- The classification model will need to be fine-tuned with your specific data for better accuracy
- For production use, consider adding:
  - Database persistence
  - Authentication
  - Rate limiting
  - Monitoring and logging
  - Error handling and retries
  - SSL/TLS encryption
  - Load balancing 