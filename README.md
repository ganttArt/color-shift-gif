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
```

## Run

- Move image file into project directory
- Open [main.py](main.py) and change the name of the variable `IMAGE` to match the file name and extension of your image
- On the command line run:

    ```bash
    . venv/bin/activate
    python main.py
    deactivate
    ```

## Potential upcoming updates

- Control speed of color change
- Images with transparency maintain transparency
