from nicegui import app,ui
import os

@ui.page('/')
def main_page():
    ui.label('Hello, NiceGUI!')


port = 8080
ui.run(
        port=int(port),
        show=False,
        favicon="🤡",
        dark=False,
        storage_secret="ghareh324zw35hzaw35hz",
        language="de",
        binding_refresh_interval=2,
        reload=os.environ.get("NICEGUI_RELOAD", "true").lower() == "true",
        reconnect_timeout=60,
        fastapi_docs=True,
        uvicorn_logging_level="info",
    )
