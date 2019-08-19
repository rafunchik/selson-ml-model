FROM python:3.7-slim
#FROM test_seldon:1
COPY . /app/
WORKDIR /app/spotlight-master/
RUN pip install -r /app/requirements.txt
RUN python setup.py install --force
WORKDIR /app/
EXPOSE 5000

# Define environment variable
ENV MODEL_NAME MyModel
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

CMD exec seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE
