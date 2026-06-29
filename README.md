# FixIt.ai - Future of Local Services ⚡

FixIt.ai is a modern, high-end full-stack web application designed to bridge the gap between users and local service providers (plumbers, electricians, AC technicians, etc.). Featuring a futuristic, glassmorphism-inspired UI/UX layout, the platform integrates an intelligent rule-based matching engine and a real-time live monitoring admin workspace.

---

## 🚀 Core Features

### 👤 Customer Experience (`index.html`)
* **Dynamic Search & Filters:** Instantly filter service providers by professional categories, pricing, ratings, or relative distance.
* **Smart Comparison Drawer:** Compare multiple service providers side-by-side using key performance data before initiating a booking.
* **AI Diagnosis Pipeline:** Integrated frontend components designed to support computer-vision-assisted fault analysis.

### ⚙️ Heuristic Matching Engine (`app.py`)
* **Natural Language Parsing:** Automatically processes natural language descriptions of household problems to extract targeted service categories.
* **Intelligent Ranking System:** Evaluates and sorts candidates using a weighted multi-factor scoring algorithm:
  $$\text{Score} = (\text{Rating} \times 20) + \min(\text{Experience Years} \times 5, 30) + \text{Bio Bonus} + \text{Location Match}$$

### 📊 Admin Console (`admin.html` / `admin.py`)
* **Glassmorphic Control Center:** Sleek, high-contrast dashboard visualization tracking critical operational metrics.
* **Interactive Geo-Surveillance:** Built-in Leaflet.js mapping utilizing custom dark-mode tile layers and dynamic intensity heatmap overlays for live service provider tracking.
* **Dispute Resolution Flow:** Direct management dashboard to audit, evaluate, and resolve conflicts between users and active partners.

---

## 🛠️ Technology Stack

* **Backend Architecture:** Python, Flask Core
* **Frontend Design:** Tailwind CSS, Glassmorphic UI overlays, Space Grotesk typography
* **Data Visualization & Mapping:** Leaflet.js (Geospatial data maps), Leaflet.heat (Density monitoring), Chart.js (Operational analytics)
* **Iconography:** Lucide Icons

---

## 📂 Project Structure

```text
├── admin.py             # Admin blueprint routes, metrics calculation, & actions
├── app.py               # Main Flask server application & Heuristic Matching Engine
├── data.py              # In-memory mock data generator for platform staging
├── requirements.txt     # Python project dependencies
└── templates/
    ├── admin.html       # Futuristic Admin Console UI
    └── index.html       # High-performance Customer Discovery Portal
