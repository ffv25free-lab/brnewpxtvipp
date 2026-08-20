"""Railway entry point for the UID admin panel only.

This launcher intentionally starts only the Flask admin UI/database routes.
Traffic interception, token forwarding, certificate distribution, and game-login
mutation code are not started by this entry point.
"""
import os
import sqlite3

import admin_panel as panel
from flask import abort

# Keep the original defaults so the existing project can start immediately,
# while allowing Railway Variables to override them.
panel.ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", panel.ADMIN_EMAIL)
panel.ADMIN_PASS = os.environ.get("ADMIN_PASSWORD", panel.ADMIN_PASS)
panel.app.secret_key = os.environ.get("SECRET_KEY", panel.app.secret_key)

# Optional persistent Railway Volume, e.g. DB_PATH=/data/bot_data.db
panel.DB_FILE = os.environ.get("DB_PATH", panel.DB_FILE)


def _init_db() -> None:
    db_dir = os.path.dirname(os.path.abspath(panel.DB_FILE))
    os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(panel.DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS whitelist ("
        "uid TEXT PRIMARY KEY, region TEXT DEFAULT 'GLOBAL', expires_at INTEGER DEFAULT 0)"
    )
    try:
        cur.execute("ALTER TABLE whitelist ADD COLUMN expires_at INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass
    cur.execute("CREATE TABLE IF NOT EXISTS blacklist (uid TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS stats (key TEXT PRIMARY KEY, value INTEGER DEFAULT 0)")
    for key in ("total", "allowed", "blocked"):
        cur.execute("INSERT OR IGNORE INTO stats (key, value) VALUES (?, 0)", (key,))
    conn.commit()
    conn.close()


_init_db()


@panel.app.before_request
def _safe_railway_guard():
    # Do not expose the bundled MITM CA certificate through the deployed admin panel.
    from flask import request
    if request.path == "/lay-ma":
        abort(404)


app = panel.app
