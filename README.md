# 🗂 JobTracker — Job Application Tracking Tool

**Live Demo:** [https://job-tracker-9lmo.onrender.com](https://job-tracker-9lmo.onrender.com)

---

## The Problem

Job seekers applying to multiple companies at the same time face a very specific problem — they lose track of everything.

- Applied to 100 companies but can't remember which ones replied
- Don't know which round they are in for which company
- Can't remember if they followed up or not
- No idea what their overall application status looks like
- End up applying to the same company twice by accident

Most people try to manage this in a WhatsApp note, a random Excel sheet, or just their memory. All of these fail after 10+ applications.

There is no simple, focused tool that just does this one thing well — log your applications and show you exactly where you stand.

**JobTracker solves this.**

---

## What It Does

JobTracker is a full stack web application where job seekers can:

- **Log every job application** — company name, job title, date applied
- **Track application status** — Applied, Interview, Offer, Rejected
- **Add notes** to each application — interview feedback, recruiter name, anything relevant
- **See all applications in one dashboard** — color coded by status so you know exactly where you stand
- **Edit and delete** applications as status changes

---

## Why This Matters

When you are applying to 50 or 100 companies, your brain cannot track all of it. You need a system. JobTracker gives you that system — simple, fast, and completely focused on the one job a job seeker needs to do: stay organized and stay consistent.

The color coded status badges (blue for Applied, yellow for Interview, green for Offer, red for Rejected) mean you can look at your dashboard and understand your entire job search in 3 seconds.

This project was built by someone who was actively job hunting and felt this problem personally. That's why it's focused on exactly what matters — no extra features, no noise.

---

## Features

- User registration and login — your applications are private to you
- Add job applications — title, company, status, notes
- Status tracking — Applied, Interview, Offer, Rejected with color coded badges
- Edit applications — update status as it changes
- Delete applications — remove ones that are no longer relevant
- Auto date — date applied is saved automatically, no manual entry needed
- Secure — you only see your own applications, never another user's
- Fully deployed — accessible from any device, any browser, 24/7

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | PostgreSQL |
| Frontend | HTML, CSS, Bootstrap 5 |
| Authentication | Django built-in auth |
| Deployment | Render |
| Version Control | Git, GitHub |

---

## How to Run Locally

**Step 1 — Clone the repo**
```bash
git clone https://github.com/Tanujadevim/job-tracker.git
cd job-tracker
```

**Step 2 — Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Create .env file in root folder**
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=jobtracker
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
DATABASE_URL=sqlite:///db.sqlite3
```

**Step 5 — Run migrations**
```bash
python manage.py migrate
```

**Step 6 — Create superuser**
```bash
python manage.py createsuperuser
```

**Step 7 — Run server**
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
job-tracker/
    config/              # Django project settings and URLs
    jobs/                # Main app — models, views, forms, templates
        models.py        # Job model with status choices
        views.py         # All views — auth, job list, CRUD
        forms.py         # ModelForm for Job
        templates/       # All HTML templates
    manage.py
    requirements.txt
    Procfile
```

---

## Database Design

```
User
 └── Job (one user has many job applications)
       - title
       - company
       - status (applied / interview / offer / rejected)
       - date_applied (auto)
       - notes
```

Every job is linked to the user who created it. All queries filter by the logged-in user so your applications are always private.

---

## Status Badge Colors

| Status | Color | Meaning |
|---|---|---|
| Applied | Blue | Application submitted, waiting for response |
| Interview | Yellow | Interview scheduled or in progress |
| Offer | Green | Job offer received |
| Rejected | Red | Application not selected |

---

## Live Demo

Try it here: [https://job-tracker-9lmo.onrender.com](https://job-tracker-9lmo.onrender.com)

Register with any username and password to explore the full app.

> Note: This is hosted on Render's free plan. The app may take 30 seconds to wake up on first visit if it has been inactive. After that it works normally.

---

## Author

**Tanuja Devi Muthayalapalli**
Python Full Stack Developer
[GitHub](https://github.com/Tanujadevim) | [LinkedIn](https://linkedin.com/in/tanuja-devi-muthayalapalli)
