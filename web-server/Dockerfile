FROM python

WORKDIR /web-server
COPY project-libraries /web-server/project-libraries

RUN pip install --no-cache-dir --upgrade -r /web-server/project-libraries

COPY . /web-server

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]