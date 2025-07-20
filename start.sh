#!/bin/bash

# Start Streamlit in the background
streamlit run app/streamlit_ui.py --server.port 8501 &

# Start FastAPI (Uvicorn)
uvicorn app.main:app --host 0.0.0.0 --port 8000
