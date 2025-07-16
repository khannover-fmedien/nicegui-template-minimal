FROM zauberzeug/nicegui:latest

COPY --chown=appuser:appuser requirements.txt /tmp/requirements.txt

WORKDIR /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY --chown=appuser:appuser ./application /app

CMD ["python", "main.py"]

