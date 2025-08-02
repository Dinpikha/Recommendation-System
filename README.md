# Hybrid Recommendation System

## Overview
This is a hybrid movie recommendation system combining collaborative filtering (SVD via a pre-trained model) and content similarity (TF-IDF + cosine similarity). It exposes a FastAPI backend and a Vite + React frontend dashboard for monitoring and retraining.

## Features
- **Hybrid recommendations:** Combines SVD predictions and content similarity to score candidate movies per user.
- **Retrain endpoint:** Trigger model retraining via FastAPI (`/retrain`) which runs the `hybrid.py` script.
- **Admin dashboard:** React-based UI showing metrics and retraining control.
- **CORS-safe development:** Frontend (localhost:5173) communicates with backend safely via configured CORS.

## Setup

### 1. Backend (Python)
```bash
# install dependencies
pip install -r requirements.txt

### 2. Frontend (Vite + React)
```bash
# install dependencies
cd rec_sys
npm install
npm run dev

