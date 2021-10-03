FROM python:3.8
WORKDIR /app
COPY ./requirements/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit-app.py"]