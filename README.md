# FastAPI-Boilerplate 

Boilerplate to quickly get started with FastAPI projects

## Setup

```bash
# Create a virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate

# Install requirements
pip install -r requirements.txt

# Run server 
uvicorn app.main:app --reload
```

**Note**: Do not forget to create the .env file with the database credentials
