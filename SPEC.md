# VaxOnVaxOff Specification 🏯
### "Wax on, wax off. Sand the floor." - Mr. Miyagi

## 1. Project Overview

- **Project Name**: VaxOnVaxOff - Your Personal Task Sensei
- **Project Type**: Web Application (Django + Single HTML Frontend)
- **Core Functionality**: A task planning application where Mr. Miyagi helps you organize your training. Users input projects (dojos) with tasks (training sessions), define their work schedule (dojo hours), and receive an optimized training calendar. Detects when overtime training is needed.
- **Target Users**: Professionals, freelancers, and anyone needing to organize tasks within their work schedule - guided by the wisdom of Mr. Miyagi

---

## 2. UI/UX Specification

### Layout Structure

**Page Sections**:
1. **Sidebar Navigation**: Fixed left sidebar with app branding and navigation
2. **Dashboard (Dojo Command Center)**: Stats overview, quick actions, today's schedule
3. **Dojos (Projects)**: Create and manage your training dojos
4. **Training (Tasks)**: Add training sessions with deadlines and difficulty
5. **Dojo Hours (Work Schedule)**: Configure your available training hours
6. **Training Schedule (Calendar)**: See your generated daily training plan

**Responsive Breakpoints**:
- Desktop: >= 1024px (sidebar + main content)
- Tablet: 768px - 1023px (sidebar + stacked content)
- Mobile: < 768px (collapsible sidebar with hamburger menu)

### Visual Design

**Color Palette**:
- Background: `#0D1117` (deep navy black - the night sky)
- Card Background: `#161B22` (dark slate - dojo walls)
- Card Border: `#30363D` (muted gray)
- Primary Accent: `#58A6FF` (bright blue - focus energy)
- Secondary Accent: `#238636` (green - achievement/completed)
- Warning: `#D29922` (amber - overtime/caution)
- Danger: `#F85149` (red - high priority/headband red)
- Text Primary: `#E6EDF3` (off-white)
- Text Secondary: `#8B949E` (muted gray)
- Logo Color: `#dc2626` (red - Mr. Miyagi's headband)

**Importance Levels (Training Difficulty)**:
- 🔴 **High** - Tournament day training (do first)
- 🟡 **Medium** - Regular practice (do second)  
- 🟢 **Low** - Extra drills (do third)

**Typography**:
- Font Family: `'JetBrains Mono', 'Fira Code', monospace` for headings/code
- Font Family: `'IBM Plex Sans', -apple-system, sans-serif` for body
- Heading 1: 24px, weight 700 (page titles)
- Heading 2: 18px, weight 600 (section titles)
- Body: 14px, weight 400
- Small/Labels: 12px, weight 500

**Spacing System**:
- Base unit: 4px
- Card padding: 20px
- Section gaps: 24px
- Element gaps: 12px
- Border radius: 8px-12px

**Visual Effects**:
- Card shadows: `0 4px 6px rgba(0, 0, 0, 0.4)`
- Hover transitions: 200ms ease
- Input focus: 3px solid with 15% primary color
- Logo glow: red gradient with shadow
- Animations: fadeIn, slideUp, pulse for loading states

### Theme: Karate Kid

**Naming Convention**:
- Projects → Dojos (training grounds)
- Tasks → Training Sessions
- Work Schedule → Dojo Hours
- Calendar → Training Schedule
- Dashboard → Dojo Command Center

**Branding Elements**:
- Logo: 🏯 (Japanese gate emoji) with red gradient
- Tagline: "Wax on, wax off." - Mr. Miyagi
- Primary actions use martial arts metaphors
- Overtime warnings: "You've got overtime training ahead"

---

## 3. Functionality Specification

### Core Features

**Dojo Management (Projects)**:
- Create new dojos with unique names
- View list of all dojos (paginated: 5 items shown, "Show all" option)
- Delete dojos (cascades to associated training sessions)
- Data persists in SQLite database

**Training Session Management (Tasks)**:
- Add training sessions to specific dojos
- Each training has:
  - Name (required, string)
  - Deadline (required, date)
  - Importance/Difficulty (required, enum: High/Medium/Low)
  - Work hours estimate (required, number, 0.5-24)
  - Completed status (boolean)
  - Completed timestamp (auto-set when marked complete)
- View all training organized by dojo (paginated: 5 items)
- Edit existing training sessions via modal
- Delete individual training sessions
- Mark training as complete/incomplete via checkbox

**Dojo Hours Configuration (Work Schedule)**:
- Select training days (checkboxes for Mon-Sun, default: Mon-Fri)
- Set training start time (default: 09:00)
- Set training end time (default: 17:00)
- Optional lunch break (default: 12:00-13:00)
- Option to enable overtime training (default: false)

**Training Schedule Generation (Calendar)**:
- Prioritize training by:
  1. Deadline (earliest first)
  2. Difficulty (High > Medium > Low) as tiebreaker
- Assign training to earliest available time slots
- Respect training day boundaries
- Account for lunch breaks
- When overtime enabled: allow scheduling beyond end time
- When overtime disabled: mark as "overtime required" if impossible

**Dashboard Features**:
- Stats cards: Total Dojos, Total Training, Completed, Pending
- Quick actions: Open New Dojo, Add Training, Get Training Schedule
- Today's Schedule: Shows today's tasks from last generated calendar
  - Separates upcoming vs completed (passed) tasks
  - Completed tasks show at bottom with strikethrough

**Calendar Features**:
- Day-by-day breakdown showing:
  - Date header with day name
  - Total hours scheduled
  - Assigned training with time slots
- Color coding by difficulty level
- Training cards showing: name, dojo, time range, complete button
- Current time highlighting: glow effect on current time slot
- Overtime warning banner if needed

### User Interactions & Flows

1. **Open New Dojo Flow**:
   - User enters dojo name → clicks "Open New Dojo" → dojo appears in list

2. **Add Training Flow**:
   - User selects dojo → enters training details → clicks "Add Training" → training appears in list

3. **Configure Dojo Hours Flow**:
   - User selects training days → sets hours → configures lunch → optionally enables overtime

4. **Get Training Schedule Flow**:
   - User clicks "Get Training Schedule" → algorithm runs → schedule displays
   - Dashboard updates with today's tasks

5. **Mark Training Complete Flow**:
   - User clicks checkbox → training marked complete → stats update
   - User clicks "✓ Done" in calendar → same result

6. **Edit Training Flow**:
   - User clicks ✏️ button → modal opens with current values → user edits → clicks "Save Changes"

### Data Handling

- All data stored in SQLite database (via Django ORM)
- REST API for frontend-backend communication
- localStorage used for persisting last generated calendar (for Dashboard)
- Filtering happens client-side for passed tasks

### Edge Cases

- No dojos created → disable training input
- No training sessions → disable schedule generation
- Training deadline in past → mark as overdue (shown in red)
- Training duration exceeds available hours → overtime warning
- All training days occupied → show full schedule message
- Tasks with passed time slots → auto-move to "Completed" section

---

## 4. Acceptance Criteria

### Visual Checkpoints
- [x] Dark theme with specified color palette applied
- [x] Sidebar navigation with app branding
- [x] Responsive layout adapts on smaller screens
- [x] Cards have proper shadows and borders
- [x] Difficulty levels show distinct colors (red/yellow/green)
- [x] Training schedule displays training with time assignments
- [x] Current time slot highlighted with glow effect
- [x] Karate Kid theme visible in branding and copy
- [x] "Show more" pagination for lists

### Functional Checkpoints
- [x] Can add multiple dojos
- [x] Can add training with all required fields
- [x] Can configure dojo hours and training days
- [x] Calendar generates with training assigned
- [x] Overtime detection works when training exceeds available time
- [x] Overtime warning displays correctly
- [x] Training is sorted by deadline and difficulty
- [x] Can delete dojos and training sessions
- [x] Can edit existing training sessions
- [x] Can mark training complete/incomplete
- [x] Dashboard shows today's schedule from last generation
- [x] Passed tasks shown in "Completed" section

### Technical Checkpoints
- [x] Django backend serves API endpoints
- [x] Single HTML frontend consumes API
- [x] No console errors on page load
- [x] All interactive elements respond to clicks
- [x] Form validation prevents invalid submissions
- [x] localStorage persistence for Dashboard calendar

---

## 5. API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects/` | GET, POST | List/Create dojos |
| `/api/projects/{id}/` | GET, PUT, DELETE | Single dojo operations |
| `/api/tasks/` | GET, POST | List/Create training sessions |
| `/api/tasks/{id}/` | GET, PUT, PATCH, DELETE | Single training operations |
| `/api/tasks/{id}/toggle_complete/` | POST | Mark training complete |
| `/api/schedule/` | GET, POST, PUT | Dojo hours config |
| `/api/generate-calendar/` | POST | Generate training schedule |

---

## 6. Mr. Miyagi's Wisdom

> "First learn stand, then learn fly."

This app follows the way of the Miyagi dojo:
- **Dojos** are your training grounds
- **Training sessions** are your lessons
- **Schedule** is when Mr. Miyagi tells you to train
- **Completion** is when you've mastered the technique

```
"There's no such thing as a bad student, only a bad teacher."
```
