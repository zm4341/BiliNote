from .sqlite_client import get_connection

def init_video_task_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS video_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT NOT NULL,
            platform TEXT NOT NULL,
            task_id TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_video_task(video_id: str, platform: str, task_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO video_tasks (video_id, platform, task_id)
        VALUES (?, ?, ?)
    """, (video_id, platform, task_id))
    conn.commit()
    conn.close()


def get_task_by_video(video_id: str, platform: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT task_id FROM video_tasks
        WHERE video_id = ? AND platform = ?
        ORDER BY created_at DESC
        LIMIT 1
    """, (video_id, platform))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def delete_task_by_video(video_id: str, platform: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM video_tasks
        WHERE video_id = ? AND platform = ?
    """, (video_id, platform))

    conn.commit()
    conn.close()
