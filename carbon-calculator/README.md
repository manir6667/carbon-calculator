# Carbon Calculator — CI/CD Beginner Project

A tiny Flask web app you can deploy with **GitHub Actions (CI/CD)** and **Render**.

## What you'll learn
- How to put code on GitHub
- How to run tests automatically (CI)
- How to deploy automatically after tests pass (CD)

## Project structure
```
.
├─ app.py
├─ requirements.txt
├─ templates/
│  └─ index.html
├─ tests/
│  └─ test_app.py
└─ .github/
   └─ workflows/
      └─ ci-cd.yml
```

## 1) Create a GitHub repo
- Create a repository named `carbon-calculator` (Public).
- Upload all files from this folder.

## 2) Enable CI (GitHub Actions)
- The workflow at `.github/workflows/ci-cd.yml` installs deps and runs tests on every push/PR.

## 3) Create a Render Web Service (first-time only)
1. Go to https://render.com and sign up with GitHub.
2. Click **New +** → **Web Service** → choose your `carbon-calculator` repo.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Click **Create Web Service** and wait for the first deploy.

## 4) Add Render Deploy Hook as a GitHub Secret (for CD)
1. On Render, open your service → **Settings** → find **Deploy Hook** and copy its URL.
2. In GitHub: repo **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
3. Name: `RENDER_DEPLOY_HOOK_URL` → paste the URL → **Add secret**.

Now, every push to the `main` branch will:
- run tests (CI) and, if they pass,
- trigger Render to deploy (CD).

## 5) Update your site
- Edit `templates/index.html` (e.g., change the heading), commit to `main`.
- Watch **Actions** tab turn green.
- Render will deploy the new version automatically.

## Local run (optional)
```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

> Emission factors are demo placeholders. For real use, refer to official datasets.
