# Mandelbrot Set Generator

Simple Mandelbrot set PNG generator in Python.

Usage

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate an image (modify parameters as needed): 

```bash
python3 mandelbrot.py --width 800 --height 600 --max-iter 300 --output mandelbrot.png
```

Adjust `--x-center`, `--y-center`, and `--scale` to zoom and pan.

For the Zoom Mode, it opens an interactive window where you can click on the image, zoom in 4x (up to a scale of ~10e-12) and generate a gif of the zoom in journey (se): 

```bash
python3 zoom_mode.py --width 800 --height 600 --max-iter 300
```
