# Color Shift GIF

Python script that takes an image and turns it into a color changing GIF.

## Example

![big sur color shifted](./assets/big_sur_sm.gif)

## Setup

```bash
git clone https://github.com/ganttArt/color-shift-gif.git
cd color-shift-gif
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Run

- Move image file into project directory
- Open [main.py](main.py) and change the variable `IMAGE` string to match the file name and extension of your image
- Activate virtual environment: `. venv/bin/activate`
- Run `python main.py`
  - Optional command line arguments:
    - `-nl` `--noloop`: Create a GIF that doesn't loop

## Potential upcoming updates

- Control speed of color change
- Images with transparency maintain transparency
- Caching for rgb to hsv and back process
- start program script
