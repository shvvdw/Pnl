Railway Key Server Files
=======================

1. Upload these 3 files to a new GitHub repository:
   - main.py
   - requirements.txt
   - Procfile

2. Go to https://railway.app
3. New Project → Deploy from GitHub repo
4. Select your repository
5. After deploy → Settings → Networking → Generate Domain
6. Copy the URL and put it in your run.py like this:

   API_URL = "https://your-project.up.railway.app/api/validate"
