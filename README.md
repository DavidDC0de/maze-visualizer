# Maze Visualizer 

A Python + React project that generates mazes and solves them using the A* pathfinding algorithm.  
Built with **FastAPI (backend)** and **React (frontend)**.

## 🎮 Features
- Generates random mazes
- Visualize the maze using React for frontend
- Solve the maze using **A\*** algorithm

## 🚀 Installation
### Clone Repository
```bash
git clone https://github.com/DavidDC0de/maze-visualizer.git
cd maze-visualizer
```
### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
uvicorn main:app --reload
```
### Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
## 📸 Screenshots
### Maze Generation
<img width="600" alt="image" src="https://github.com/user-attachments/assets/fff1699b-2dea-4a9a-8591-c56d9ae3d6ef" />

### Solved Maze
<img width="600" alt="image" src="https://github.com/user-attachments/assets/a418281d-b73e-44b8-b466-105a958f906f" />


## 📖 Tech Stack
- Python (FastAPI) → backend + maze generation + pathfinding
- React (Vite) → frontend UI
- A* algorithm → efficient pathfinding
- GitHub → version control and project documentation

## ✨ Future Improvements
- Let users selct maze size
- Interactive step-by-step solving display



