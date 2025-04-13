import os

import uvicorn
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv

from app import create_app
from app.db.video_task_dao import init_video_task_table
from app.transcriber.transcriber_provider import get_transcriber
from ffmpeg_helper import ensure_ffmpeg_or_raise

load_dotenv()

# 读取 .env 中的路径
static_path = os.getenv('STATIC', '/static')
out_dir = os.getenv('OUT_DIR', './static/screenshots')

# 自动创建本地目录（static 和 static/screenshots）
static_dir = "static"
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

app = create_app()
app.mount(static_path, StaticFiles(directory=static_dir), name="static")

@app.on_event("startup")
def check_env():
    ensure_ffmpeg_or_raise()
@app.on_event("startup")
async def load_model_on_startup():
    get_transcriber()

@app.on_event("startup")
def startup():
    init_video_task_table()

if __name__ == "__main__":
    port = int(os.getenv("BACKEND_PORT", 8000))

    host = os.getenv("BACKEND_HOST", "0.0.0.0")
    uvicorn.run("main:app", host=host, port=port, reload=True)