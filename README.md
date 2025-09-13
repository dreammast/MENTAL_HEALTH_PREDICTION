# Campus Mind - Mental Health Chatbot

A comprehensive mental health support platform for college students featuring AI-powered chatbot, mood tracking, mindfulness exercises, and career guidance.

## Features

- 🤖 **AI Chatbot**: Powered by LangChain and Groq LLM
- 📝 **Mood Tracker**: Track daily moods with notes and history
- 🧠 **Mindfulness Exercises**: Guided breathing, meditation, and relaxation
- 👥 **Peer Support**: Connect with other students
- 🩺 **Therapist Sessions**: Book appointments with licensed professionals
- 📚 **Self-Help Resources**: Articles, videos, and workbooks
- 🎯 **Career Assessment**: Personalized career guidance and skill development

## Deployment Options

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:
   ```bash
   heroku create campus-mind-chatbot
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Deploy**:
   ```bash
   git init
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

5. **Open your app**:
   ```bash
   heroku open
   ```

### Option 2: Railway

1. **Connect to Railway**:
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Set environment variables in Railway dashboard

2. **Set environment variables**:
   - `GROQ_API_KEY`: Your Groq API key

3. **Deploy**: Railway will automatically deploy from your repository

### Option 3: Render

1. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Create a new Web Service
   - Connect your GitHub repository

2. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Set environment variables

### Option 4: VPS/Cloud Server

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   export GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run with Gunicorn**:
   ```bash
   gunicorn app:app --bind 0.0.0.0:8000
   ```

4. **Use Nginx** as reverse proxy (optional)

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)
- `FLASK_ENV`: Set to 'production' for production deployment

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   export GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open** http://localhost:5000

## API Endpoints

- `GET /`: Main application interface
- `POST /api/chat`: Chat with the AI bot

## File Structure

```
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend HTML template
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version
└── README.md            # This file
```

## Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- Consider implementing rate limiting for production
- Add authentication if needed for your use case

## Support

For issues or questions, please check the documentation or create an issue in the repository.
