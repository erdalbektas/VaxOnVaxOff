# VaxOnVaxOff 🏯
### "Wax on, wax off. Sand the floor." - Mr. Miyagi

```
                    ████
                  ██░░░░██
                ██░░████░░██
               ██░░██░░██░░██
              ██░░██░░██░░██░██
             ██░░██░░██░░██░░██
            ██░░██░░██░░██░░██░██
           ██░░██░░██░░██░░██░░██
          ██░░██░░██░░██░░██░░██░██
         ██░░██░░██░░██░░██░░██░░██
        ██░░██░░██░░██░░██░░██░░██░██
       ██░░██░░██░░██░░██░░██░░██░░██
      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░██
      ██░░██░░██░░██░░██░░██░░██░░██
       ██░░██░░██░░██░░██░░██░░██░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░██
         ██░░██████░░░░░██████░░██
          ██░░░░░░░░░░░░░░░░░░░░██
           ██████████████████████
```

---

## "First learn stand, then learn fly." - Mr. Miyagi

Welcome to **VaxOnVaxOff**, your personal task planning sensei. Like Mr. Miyagi teaching Daniel-san, this app helps you organize your training (work), schedule your lessons (tasks), and achieve balance in your dojo (life).

---

## 🎯 What VaxOnVaxOff Does

VaxOnVaxOff transforms chaotic task lists into structured training schedules. Mr. Miyagi doesn't just give you tasks—he tells you when to do them, balancing your training with rest and recovery.

### Core Philosophy
- **Projects** = Your Dojos (different areas of training)
- **Tasks** = Training Sessions (with difficulty and duration)
- **Work Schedule** = Your Training Hours (when sensei is available)
- **Calendar** = Your Training Schedule (what Mr. Miyagi tells you to do)

### Key Features
- ✅ Create and manage multiple dojos (projects)
- ✅ Add training sessions (tasks) with deadlines and difficulty
- ✅ Configure your available training hours
- ✅ Auto-generate your daily training schedule
- ⚠️ "You need overtime training" warnings
- 📊 Track your completed training sessions

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

```bash
# 1. Navigate to project directory
cd planner

# 2. Install dependencies
pip install django djangorestframework django-cors-headers

# 3. Set up the database
python manage.py migrate

# 4. Start the training (run the server)
python manage.py runserver 8000
```

### Access the App

Open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 🎓 How to Use

### Step 1: Create Your Dojo (Project)

Every warrior needs a place to train. Create a project for each area of your life.

1. Click **Projects** in the sidebar
2. Enter a name (e.g., "Belt Testing", "Tournament Prep", "Daily chores")
3. Click **Add Project**

### Step 2: Add Training Sessions (Tasks)

Training sessions need direction. Add tasks with clear goals.

1. Click **Tasks** in the sidebar
2. Select your **Dojo** (project)
3. Enter the **training name** (task name)
4. Set the **deadline** (when to complete by)
5. Choose **difficulty** (High/Medium/Low importance)
6. Estimate **training duration** (hours needed)
7. Click **Add Task**

### Step 3: Configure Your Training Hours

Mr. Miyagi only trains when the dojo is open. Set your available hours.

1. Click **Work Schedule** in the sidebar
2. Select your **training days** (check Mon-Fri, etc.)
3. Set your **training hours** (e.g., 9:00 AM - 5:00 PM)
4. Configure **lunch break** (mandatory rest)
5. Toggle **overtime training** if needed

### Step 4: Generate Your Training Schedule

This is where Mr. Miyagi's wisdom shines.

1. Click **Calendar** in the sidebar
2. Click **Generate Calendar**
3. The app assigns tasks to time slots
4. See your daily training plan!

### Step 5: Complete Your Training

Mark tasks as done when you've finished.

1. Click the **checkbox** in task list
2. Or click **✓ Done** in the calendar
3. Watch your progress grow

---

## 📱 The Dashboard

Your command center. Mr. Miyagi shows you:

- **Total Dojos** - How many projects you're juggling
- **Total Training** - All your tasks
- **Completed** - Tasks you've mastered
- **Pending** - Training still ahead
- **Today's Schedule** - What to do right now

---

## ⚠️ "You've Got Overtime Training Ahead"

If your tasks exceed your available hours, Mr. Miyagi will let you know:

```
⚠️ OVERTIME REQUIRED
You need 3.5 hours of overtime training to complete all tasks within deadlines.
Enable overtime in your schedule or extend your training hours.
```

### Solutions
1. **Enable overtime** - Train after hours
2. **Extend work hours** - More training time per day
3. **Reduce task hours** - Estimate more conservatively
4. **Lower task importance** - Defer less critical training

---

## 🎨 Design Philosophy

The app follows the way of the Miyagi dojo:

### Colors
- **Primary Blue** (#58A6FF) - The calm focus of meditation
- **Success Green** (#238636) - Achievement and growth
- **Warning Yellow** (#D29922) - Caution and attention
- **Danger Red** (#F85149) - High priority training

### Importance Levels
- 🔴 **High** - Tournament day training (do first)
- 🟡 **Medium** - Regular practice (do second)
- 🟢 **Low** - Extra drills (do third)

### Current Time Highlighting
The app automatically highlights which training session you're currently in—Mr. Miyagi's way of keeping you on track.

---

## 🏯 App Structure

```
planner/
├── db.sqlite3              # Your training log (database)
├── manage.py               # Sensei's instructions
├── plannerproject/         # The dojo (Django settings)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── planner/                # Training curriculum
│   ├── models.py          # Task definitions
│   ├── views.py           # Scheduling logic
│   ├── serializers.py     # Data formatting
│   ├── urls.py            # Routes
│   └── migrations/        # Database updates
└── templates/
    └── index.html         # The dojo floor (UI)
```

---

## 🔧 API Reference

The app uses a REST API for frontend-backend communication:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects/` | GET, POST | List/Create dojos |
| `/api/projects/{id}/` | GET, PUT, DELETE | Single dojo operations |
| `/api/tasks/` | GET, POST | List/Create training sessions |
| `/api/tasks/{id}/` | GET, PUT, PATCH, DELETE | Single task operations |
| `/api/tasks/{id}/toggle_complete/` | POST | Mark training complete |
| `/api/schedule/` | GET, POST, PUT | Work schedule config |
| `/api/generate-calendar/` | POST | Generate training schedule |

---

## 💡 Mr. Miyagi's Wisdom

> "It's not what you say, it's what you do."

This app is about *doing*. Not just planning, but executing. Mr. Miyagi doesn't believe in endless to-do lists—he believes in focused, scheduled action.

### Best Practices
1. **Start with one dojo** - Don't spread yourself thin
2. **Be realistic with hours** - Honest estimates lead to success
3. **Check the dashboard** - See your progress daily
4. **Complete tasks** - Mark them done to track growth
5. **Use importance levels** - Focus on high-priority training

---

## 🐛 Troubleshooting

### "Database locked" error
```bash
# Remove the database and start fresh
rm db.sqlite3
python manage.py migrate
```

### Server won't start
```bash
# Check if port is in use
lsof -i:8000
# Kill the process or use different port
python manage.py runserver 8001
```

### Changes not showing
```bash
# Restart the server
# Press Ctrl+C to stop, then
python manage.py runserver 8000
```

---

## 🙏 Credits

**VaxOnVaxOff** is inspired by the Karate Kid film series and the teachings of Mr. Miyagi.

Original concept and development by the opencode team.

```
"There's no such thing as a bad student, only a bad teacher. 
 Teacher says, 'Do this.' Student does. Teacher says, 'Why 
 you do that?' Student doesn't remember teacher ever saying 
 'why.'"- Mr. Miyagi
```

---

## 📄 License

This project is open source and available for learning purposes.

---

## 🏆 "Remember, balance. All things are possible." - Mr. Miyagi

May your tasks be organized, your deadlines met, and your dojo in harmony.

```
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║     "Wax on, wax off. Wax on, wax off."    ║
    ║                                           ║
    ║              VaxOnVaxOff                  ║
    ║         Your Personal Task Sensei         ║
    ║                                           ║
    ╚═══════════════════════════════════════════╝
```

---

*Last updated: March 2026*
