FROM rasa/rasa:3.1.0

USER root
WORKDIR /app
COPY . .

RUN rasa train

RUN ["chmod", "+x", "/app/scripts/start_services.sh"]
#RUN chmod +x /app/scripts/*

ENTRYPOINT []

CMD /app/scripts/start_services.sh