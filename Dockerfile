FROM python:3.7

RUN python -m pip install --upgrade pip

RUN pip install numpy scipy
