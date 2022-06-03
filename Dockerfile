FROM rasa/rasa:3.1.1

USER root
WORKDIR /app
COPY . .

#RUN rasa train

RUN ["chmod", "+x", "/app/scripts/start_services.sh"]


ENTRYPOINT []

CMD /app/scripts/start_services.sh