#!/bin/bash

# Start FastAPI in background
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit in foreground
streamlit run app/streamlit_ui.py --server.port 8501
