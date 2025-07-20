#!/bin/bash

# Start Streamlit with a base path
streamlit run app/streamlit_ui.py --server.port 8501 --server.baseUrlPath /streamlit &

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000
