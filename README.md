# AI Pregnancy Companion

A voice-enabled AI assistant designed to provide personalized pregnancy support, health monitoring, and intelligent recommendations powered by advanced machine learning and OpenAI's Whisper technology.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Environment Setup](#environment-setup)
- [API Endpoints](#api-endpoints)
- [Development Guide](#development-guide)
- [Deployment](#deployment)
- [Integration Checklist](#integration-checklist)
- [Team Roles](#team-roles)
- [Demo Steps](#demo-steps)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

**AI Pregnancy Companion** helps expecting mothers by:
- 🎤 Converting voice input to text using OpenAI Whisper
- 🧠 Analyzing pregnancy-related health information
- 💡 Providing personalized recommendations
- 📊 Tracking health metrics and milestones
- 🔐 Securely managing sensitive health data

### Key Features
✅ Voice transcription (Whisper API)  
✅ ML-powered health analysis  
✅ RESTful API endpoints  
✅ Docker containerization  
✅ Production-ready deployment  

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Frontend (User Interface)              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Backend API (FastAPI - main.py)             │
│  - POST /api/voice/transcribe                           │
│  - POST /api/voice/process                              │
│  - GET /api/status                                       │
│  - GET /health                                           │
└─────────────┬──────────────────────┬────────────────────┘
              │                      │
              ▼                      ▼
   ┌──────────────────────┐   ┌──────────────────────────┐
   │ Voice Integration    │   │    ML Engine             │
   │ (voice_service.py)   │   │  (ml_model.py)           │
   │ - Whisper API        │   │  - Health Analysis       │
   │ - Audio Upload       │   │  - Recommendations       │
   │ - Transcription      │   │  - JSON Response         │
   └──────────────────────┘   └──────────────────────────┘
              │                      │
              └──────────────┬───────┘
                             ▼
                   ┌──────────────────────┐
                   │  Environment Config  │
                   │  (env_config.py)     │
                   │  - API Keys          │
                   │  - Settings          │
                   └──────────────────────┘
```

---

## 💻 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Language** | Python | 3.10+ |
| **Web Framework** | FastAPI | 0.104+ |
| **Server** | Uvicorn | 0.24+ |
| **Voice AI** | OpenAI Whisper API | Latest |
| **ML Framework** | scikit-learn | 1.3+ |
| **API Validation** | Pydantic | 2.0+ |
| **Containerization** | Docker | Latest |
| **Environment Mgmt** | python-dotenv | 1.0+ |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- OpenAI API Key (get one at https://platform.openai.com/api-keys)
- Docker (optional, for containerized deployment)
- Git

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-org/AI-Pregnancy-Companion.git
cd AI-Pregnancy-Companion
```

### 2️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
```bash
# Copy .env template
cp .env .env.local

# Edit with your OpenAI API Key
# Windows: notepad .env.local
# macOS/Linux: nano .env.local
```

Add your OpenAI API Key:
```
OPENAI_API_KEY=sk-your-key-here
```

### 5️⃣ Run Application Locally
```bash
# Development with auto-reload
uvicorn backend.main:app --reload

# Production
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

API will be available at: http://localhost:8000

### 6️⃣ Test Health Check
```bash
curl http://localhost:8000/health

# Response:
# {"status": "healthy", "service": "AI Pregnancy Companion API"}
```

---

## ⚙️ Environment Setup

### Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | ✅ Yes | OpenAI API key for Whisper | `sk-...` |
| `FLASK_ENV` | ❌ No | Development or production | `development` |
| `DEBUG` | ❌ No | Enable debug mode | `True` |

### Getting OpenAI API Key

1. Go to https://platform.openai.com
2. Sign in or create account
3. Navigate to "API Keys"
4. Create new secret key
5. Copy key immediately (can't view again)
6. Add to `.env` file

### Validating Environment
```bash
# Test environment setup
python -c "from integrations import validate_environment; validate_environment()"
```

### Security Best Practices

⚠️ **NEVER commit `.env` file!**

✅ Use `.env.example` for templates  
✅ Add `.env` to `.gitignore`  
✅ Use environment variables in CI/CD  
✅ Rotate API keys regularly  
✅ Use least-privilege permissions  

---

## 📡 API Endpoints

### 1. Health Check
```http
GET /health
```
Check service health and readiness.

**Response:**
```json
{
  "status": "healthy",
  "service": "AI Pregnancy Companion API"
}
```

### 2. Status Check
```http
GET /api/status
```
Verify all integrations are configured.

**Response:**
```json
{
  "api": "running",
  "voice_integration": "ready",
  "environment": "configured"
}
```

### 3. Transcribe Audio
```http
POST /api/voice/transcribe
```
Convert audio file to text using Whisper.

**Request:**
```bash
curl -X POST http://localhost:8000/api/voice/transcribe \
  -F "audio_file=@/path/to/audio.mp3"
```

**Response:**
```json
{
  "status": "success",
  "transcription": "I'm having back pain in my second trimester"
}
```

**Supported Formats:** mp3, mp4, mpeg, mpga, m4a, wav, webm

### 4. Process Voice Input (Full Pipeline)
```http
POST /api/voice/process
```
Complete pipeline: Audio → Transcription → ML Analysis

**Request:**
```bash
curl -X POST http://localhost:8000/api/voice/process \
  -F "audio_file=@/path/to/audio.wav"
```

**Response:**
```json
{
  "status": "success",
  "result": {
    "analysis": "...",
    "recommendations": [...]
  }
}
```

---

## 👨‍💻 Development Guide

### Project Structure
```
AI-Pregnancy-Companion/
├── integrations/                  # Voice + ML integration layer
│   ├── __init__.py
│   ├── voice_service.py          # Whisper audio transcription
│   └── env_config.py             # Environment management
├── backend/                        # FastAPI application
│   ├── __init__.py
│   └── main.py                   # API routes and endpoints
├── ml_engine/                      # ML processing (Person 1)
│   ├── __init__.py
│   └── ml_model.py               # ML logic (to be implemented)
├── requirements.txt               # Python dependencies
├── Dockerfile                      # Container configuration
├── .env                           # Environment variables (DO NOT COMMIT)
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

### File Responsibilities

**Person 5 (Voice + Integrations + DevOps):**
- ✅ `integrations/voice_service.py` - Whisper integration
- ✅ `integrations/env_config.py` - Environment setup
- ✅ `backend/main.py` - API endpoints
- ✅ `requirements.txt` - Dependencies
- ✅ `Dockerfile` - Container configuration
- ✅ `.env` template - Environment template
- ✅ `.gitignore` - Git configuration
- ✅ `README.md` - Documentation

**Person 1 (ML / Backend):**
- `ml_engine/ml_model.py` - ML processing logic
- ML request/response handling

**Others:**
- Do NOT modify integrations
- Do NOT change voice_service.py
- Do NOT touch environment config

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_voice.py

# Run with coverage
pytest --cov=integrations
```

### Adding New Dependencies
```bash
# Install package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Notify team of changes
```

⚠️ **IMPORTANT:** Only Person 5 updates `requirements.txt` to avoid conflicts.

---

## 🐳 Deployment

### Docker Build & Run

#### Build Container
```bash
docker build -t ai-pregnancy-companion .
```

#### Run Locally
```bash
docker run -p 8000:8000 \
  --env-file .env \
  ai-pregnancy-companion
```

#### Run with Environment Variables
```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=sk-your-key \
  ai-pregnancy-companion
```

### Deployment Platforms

#### Option 1: Render
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repository
4. Set environment variables in dashboard
5. Deploy

#### Option 2: Railway
1. Sign up at https://railway.app
2. Create new project
3. Connect GitHub
4. Add environment variables
5. Deploy

#### Option 3: AWS / GCP / Azure
See respective documentation for FastAPI deployment.

#### Option 4: Local Docker
```bash
docker build -t ai-pregnancy-companion .
docker run -p 8000:8000 --env-file .env ai-pregnancy-companion
```

### Production Checklist
- [ ] Environment variables configured
- [ ] OPENAI_API_KEY set securely
- [ ] All tests passing
- [ ] Docker image builds successfully
- [ ] Health check responds
- [ ] API endpoints functional
- [ ] No secrets in code
- [ ] Documentation updated

---

## ✅ Integration Checklist (Before Demo)

### Pre-Demo Verification
```bash
# 1. Environment validation
python -c "from integrations import validate_environment; validate_environment()"

# 2. Start server
uvicorn backend.main:app --reload

# 3. Test health endpoint
curl http://localhost:8000/health

# 4. Test status endpoint
curl http://localhost:8000/api/status

# 5. Test voice transcription with sample audio
curl -X POST http://localhost:8000/api/voice/transcribe \
  -F "audio_file=@sample_audio.wav"

# 6. Test full pipeline (when ML is ready)
curl -X POST http://localhost:8000/api/voice/process \
  -F "audio_file=@sample_audio.wav"

# 7. Build Docker image
docker build -t ai-pregnancy-companion .

# 8. Run Docker container
docker run -p 8000:8000 --env-file .env ai-pregnancy-companion

# 9. Verify no secrets in git
git status
git log --all -S "sk-" --oneline
```

### Final Checks
✅ OPENAI_API_KEY loads correctly  
✅ Whisper transcription works  
✅ ML integration ready (waiting for Person 1)  
✅ Docker builds without errors  
✅ API responds to requests  
✅ No API keys in repository  
✅ README is complete  
✅ All dependencies in requirements.txt  

---

## 👥 Team Roles & Responsibilities

### Person 1: ML Logic
- Implement `ml_engine/ml_model.py`
- Create `process_voice_text()` function
- Handle health analysis
- Return JSON recommendations
- **Does NOT:** Modify integrations, change voice_service.py

### Person 2: Backend Routes
- Extend FastAPI endpoints
- Add database connections
- Handle user management
- **Does NOT:** Modify integrations, change environment config

### Person 3: Frontend UI
- Build user interface
- Send audio to `/api/voice/process`
- Display ML recommendations
- Handle audio recording
- **Does NOT:** Modify backend, change API structure

### Person 4: Database
- Design data models
- Implement ORM
- Handle migrations
- **Does NOT:** Modify integrations, change API layer

### Person 5: Voice + DevOps (You)
- ✅ Manage Whisper integration
- ✅ Handle environment variables
- ✅ Deploy application
- ✅ Manage dependencies
- ✅ Docker configuration
- ✅ **Does NOT:** Change ML logic, modify backend routes, touch frontend

---

## 🎬 Demo Steps

### Live Demo Scenario

#### Part 1: Setup (2 minutes)
```bash
# 1. Show project structure
tree -I '__pycache__'

# 2. Start server
uvicorn backend.main:app --reload

# 3. Show health check
curl http://localhost:8000/health
```

#### Part 2: Voice Transcription (3 minutes)
```bash
# 1. Show voice_service.py capabilities
cat integrations/voice_service.py

# 2. Upload and transcribe sample audio
curl -X POST http://localhost:8000/api/voice/transcribe \
  -F "audio_file=@pregnancy_question.wav"

# 3. Show transcription result
# Expected: "I'm concerned about morning sickness..."
```

#### Part 3: ML Processing (3 minutes)
```bash
# 1. Show ML integration
cat backend/main.py

# 2. Process voice through full pipeline
curl -X POST http://localhost:8000/api/voice/process \
  -F "audio_file=@pregnancy_question.wav"

# 3. Show ML response with analysis
```

#### Part 4: Docker Deployment (2 minutes)
```bash
# 1. Build image
docker build -t ai-pregnancy-companion .

# 2. Run container
docker run -p 8000:8000 --env-file .env ai-pregnancy-companion

# 3. Test from container
curl http://localhost:8000/api/status
```

**Total Demo Time:** ~10 minutes

---

## 🐛 Troubleshooting

### Issue: "OPENAI_API_KEY not found"
```bash
# Solution 1: Check .env file exists
ls -la .env

# Solution 2: Verify API key is set
cat .env | grep OPENAI_API_KEY

# Solution 3: Set directly in terminal
export OPENAI_API_KEY=sk-your-key
python -c "from integrations import validate_environment; validate_environment()"
```

### Issue: "Module 'openai' not found"
```bash
# Solution: Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import openai; print(openai.__version__)"
```

### Issue: "Audio file not found"
```bash
# Ensure file exists
ls -la /path/to/audio.wav

# Use absolute path instead of relative
curl -X POST http://localhost:8000/api/voice/transcribe \
  -F "audio_file=@$(pwd)/audio.wav"
```

### Issue: "Connection refused" on http://localhost:8000
```bash
# Check if server is running
ps aux | grep uvicorn

# Restart server
uvicorn backend.main:app --reload

# Check port availability
# Windows: netstat -ano | findstr :8000
# macOS/Linux: lsof -i :8000
```

### Issue: "Docker build fails"
```bash
# Clear Docker cache
docker system prune -a

# Build with verbose output
docker build -t ai-pregnancy-companion . --progress=plain

# Check Dockerfile syntax
cat Dockerfile
```

### Issue: "Permission denied" on .env
```bash
# Fix permissions
chmod 600 .env

# Verify
ls -la .env
```

---

## 📚 Additional Resources

### OpenAI Whisper API
- Official Documentation: https://platform.openai.com/docs/guides/speech-to-text
- API Reference: https://platform.openai.com/docs/api-reference/audio
- Pricing: https://openai.com/pricing

### FastAPI
- Official Documentation: https://fastapi.tiangelo.io
- Tutorial: https://fastapi.tiangelo.io/tutorial/
- Deployment Guide: https://fastapi.tiangelo.io/deployment/

### Docker
- Docker Documentation: https://docs.docker.com
- Best Practices: https://docs.docker.com/develop/dev-best-practices/

### Deployment Platforms
- Render: https://render.com
- Railway: https://railway.app
- Heroku: https://www.heroku.com
- AWS: https://aws.amazon.com

---

## 📧 Support & Contact

### Team Communication
- **Bugs/Issues:** Create GitHub issue
- **Questions:** Slack #ai-pregnancy-team
- **Deployments:** Notify ops channel

### Quick Help
- Voice not working? → Ask Person 5
- ML issues? → Ask Person 1
- API problems? → Ask Person 2
- Frontend issues? → Ask Person 3
- Database questions? → Ask Person 4

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🎉 You're all set!

**Your responsibilities as Person 5 are complete. The team can now:**
- ✅ Send voice to `/api/voice/transcribe`
- ✅ Process audio through ML layer
- ✅ Deploy using Docker
- ✅ Configure environment safely
- ✅ Manage all dependencies

**Ready for demo day! 🚀**

---

**Last Updated:** March 4, 2026  
**Maintainer:** Person 5 (Voice + Integrations + DevOps)  
**Version:** 1.0.0
