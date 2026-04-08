# Hate-Speech-Classification

An end-to-end machine learning project that detects hate speech in text data.

## Features
- Detects abusive, discriminatory, or harmful language
- Improves safety by flagging offensive content
- Supports text classification using NLP techniques

## Tech Stack
- Python
- TensorFlow
- nltk
- FastAPI
- Pandas
- NumPy
- Docker
- MLflow
<!-- - DVC -->
- GitHub Actions
- AWS(S3, ..)

## MLOps Workflow
This project follows MLOps practices to make the pipeline reproducible, scalable, and maintainable.

### MLOps Concepts Used
- Data versioning
- Model versioning
- Experiment tracking
- Automated model training
- Docker containerization
- CI/CD pipeline
- Deployment and monitoring

### Tools Used
<!-- - DVC for dataset versioning -->
- MLflow for experiment tracking
- Docker for containerization
- GitHub Actions for CI/CD

## Installation

## Project Structure

```bash
📁Hate-Speech-Classification
└── 📁data
    ├── dataset.zip
└── 📁notebook
    ├── hate_speech_exp.ipynb
└── 📁src
    └── 📁__pycache__
        ├── __init__.cpython-311.pyc
    └── 📁aws_configuration
        ├── __init__.py
        ├── s3_config.py
    └── 📁components
        ├── __init__.py
        ├── data_ingestion.py
        ├── data_transformation.py
        ├── model_evaluation.py
        ├── model_pusher.py
        ├── model_trainer.py
    └── 📁configuration
        ├── __init__.py
    └── 📁constants
        └── 📁__pycache__
            ├── __init__.cpython-311.pyc
        ├── __init__.py
    └── 📁entity
        ├── __init__.py
        ├── artifact_entity.py
        ├── config_entity.py
    └── 📁exception
        ├── __init__.py
    └── 📁logger
        └── 📁__pycache__
            ├── __init__.cpython-311.pyc
        ├── __init__.py
    └── 📁ml
        ├── __init__.py
        ├── model.py
    └── 📁pipeline
        ├── __init__.py
        ├── predction_pipline.py
        ├── train_pipline.py
    └── 📁utils
        ├── __init__.py
    ├── __init__.py
├── .dockerignore
├── .env
├── .gitignore
├── app.py
├── demo.py
├── Dockerfile
├── LICENSE
├── note.txt
├── README.md
├── requirements.txt
├── setup.py
└── template.py

```

## Screenshots or Demo

## Future Improvements
<!-- - Add multilingual support -->
<!-- - Improve model accuracy
- Deploy on cloud platforms
- Add real-time monitoring dashboard -->

## License