FROM ...
WORKDIR /opt/fastapi_demo
COPY . .
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root
EXPOSE 8000
CMD ["gunicorn", "-c", "conf/gunicorn.conf.py", "manage:app"]
