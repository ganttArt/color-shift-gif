# Color Shift GIF

Python script that takes an image and turns it into a color changing GIF.

## Example

![big sur color shifted](./assets/readme-examples/big_sur_sm.gif)

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

### Optional Command Line Arguments

- `-nl` `--noloop`: Create a GIF that doesn't loop
- `-t` `--transparent`: Maintain transparency of input image in GIF.
  - Note: Semi-transparent pixels will convert to fully transparent pixels. GIF image format does not support semi-transparent pixels
- `-p` `--posterize`: Create posterize effect in GIF (experimental effect, works poorly for some images)
  - ![posterized example](./assets/readme-examples/posterization.png)

## Potential upcoming updates

- Control speed of color change
- Caching for rgb to hsv and back to rgb process
- Command line argument for image file selected