from flask import Flask, render_template, send_file
import subprocess
import os
from pathlib import Path
from datetime import datetime

STATIC_DIR = Path(f'{os.environ["HOME"]}/.local/share/wathiq/static')
SCREENSHOTS_DIR = STATIC_DIR / 'screenshots'

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    template_folder=Path(__file__).parent / 'templates',
)


def take_screenshot():
    today = datetime.today().strftime("%Y/%m/%d")

    today_dir = SCREENSHOTS_DIR / today
    today_dir.mkdir(parents=True, exist_ok=True)


    now_time = datetime.now().strftime("%H-%M-%S")
    relative_screenshot_file = f'{today}/{now_time}.png'

    screenshot_file_path = SCREENSHOTS_DIR / relative_screenshot_file

    subprocess.run(
        args=['import', '-window', 'root', '-resize', '50%', screenshot_file_path],
        check=True,
    )

    return relative_screenshot_file


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/last')
def last():
    result = subprocess.run(['last'], capture_output=True, text=True, check=True)
    last_output = result.stdout
    return render_template('last.html', last_output=last_output)


@app.route('/now')
def now():
    screenshot = take_screenshot()
    return render_template('now.html', screenshot=screenshot)


@app.route('/history')
def history():
    screenshots = sorted([
        path.relative_to(SCREENSHOTS_DIR)
        for path in SCREENSHOTS_DIR.glob('**/*.png')
    ], reverse=True)
    return render_template('history.html', screenshots=screenshots)


if __name__ == '__main__':
    app.run()
