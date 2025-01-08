from setuptools import setup, find_packages

setup(
    name="esl-worksheet-backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0,<0.69.0",
        "uvicorn>=0.15.0,<0.16.0",
        "sqlalchemy>=1.4.23,<1.5.0",
        "psycopg2-binary>=2.9.1,<3.0.0",
        "pydantic>=1.8.0,<2.0.0",
        "spacy>=3.5.0,<4.0.0",
        "python-multipart>=0.0.5,<0.1.0",
        "python-jose[cryptography]>=3.3.0,<4.0.0",
        "passlib[bcrypt]>=1.7.4,<2.0.0"
    ],
) 