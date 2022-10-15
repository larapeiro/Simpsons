FROM python:3.9.15-slim-buster
RUN mkdir SIMPSONS
RUN mkdir SIMPSONS/General
RUN mkdir SIMPSONS/Homer
RUN mkdir SIMPSONS/Lisa
RUN touch SIMPSONS/General/general.csv
RUN touch SIMPSONS/Homer/homer.csv
RUN touch SIMPSONS/Lisa/lisa.csv
COPY main.py ./SIMPSONS
COPY requirements.txt ./SIMPSONS
RUN pip install --upgrade pip
RUN pip install -r ./SIMPSONS/requirements.txt
CMD ["python", "SIMPSONS/main.py"]
