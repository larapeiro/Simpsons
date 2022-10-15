FROM python:3.9.15-slim-buster
RUN mkdir MaggieLevel
RUN mkdir MaggieLevel/General
RUN mkdir MaggieLevel/Homer
RUN mkdir MaggieLevel/Lisa
RUN touch MaggieLevel/General/general.csv
RUN touch MaggieLevel/Homer/homer.csv
RUN touch MaggieLevel/Lisa/lisa.csv
COPY main.py ./MaggieLevel
COPY requirements.txt ./MaggieLevel
RUN pip install --upgrade pip
RUN pip install -r ./MaggieLevel/requirements.txt
CMD ["python", "MaggieLevel/main.py"]
