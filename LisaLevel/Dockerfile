FROM python:3.9.15-slim-buster
RUN mkdir LisaLevel
COPY main.py ./LisaLevel
COPY requirements.txt ./LisaLevel
RUN pip install --upgrade pip
RUN pip install -r ./LisaLevel/requirements.txt
WORKDIR LisaLevel
CMD ["python", "main.py"]