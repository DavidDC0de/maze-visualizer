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
### Solved Maze

## 📖 Tech Stack
- Python (FastAPI) → backend + maze generation + pathfinding
- React (Vite) → frontend UI
- A* algorithm → efficient pathfinding
- GitHub → version control and project documentation

## ✨ Future Improvements
- Let users selct maze size
- Interactive step-by-step solving display



