FROM docker.io/python:3.6-alpine
RUN pip install requests
USER root
COPY . /dns-test
RUN chgrp -R 0 /dns-test \
    && chmod -R g=u /dns-test
USER 1001
WORKDIR /dns-test

ENTRYPOINT ["python"]
CMD ["app/app.py"]
