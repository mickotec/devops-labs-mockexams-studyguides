#!/usr/bin/env python3
import os
import struct
import zlib

def make_png_from_pixels(width, height, pixels):
    """pixels is list of rows, each row is list of (r,g,b,a) tuples 0-255"""
    # PNG signature
    png = b'\x89PNG\r\n\x1a\n'

    def png_chunk(chunk_type, data):
        return struct.pack('>I', len(data)) + chunk_type + data + struct.pack('>I', 
            0xffffffff & (zlib.crc32(chunk_type + data) ^ 0xffffffff))

    # IHDR
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)  # 8-bit RGBA
    png += png_chunk(b'IHDR', ihdr)

    # IDAT
    # each scanline starts with a filter byte (0 = none)
    scanlines = b''.join(b'\x00' + b''.join(struct.pack('BBBB', *rgba) for rgba in row) for row in pixels)
    png += png_chunk(b'IDAT', zlib.compress(scanlines))

    # IEND
    png += png_chunk(b'IEND', b'')
    return png

def make_pomodoro_icon(size, color_hex="#EF4444", paused=False):
    """Create a pomodoro (tomato) icon.
    If paused=True, overlay a pause symbol (two vertical bars)."""
    # Base tomato shape (simple circle)
    center = size // 2
    radius = size * 0.4
    # Background transparent
    pixels = [[(0,0,0,0) for _ in range(size)] for _ in range(size)]
    # Fill circle
    for y in range(size):
        for x in range(size):
            dx = x - center
            dy = y - center
            if dx*dx + dy*dy <= radius*radius:
                r = int(color_hex[1:3], 16)
                g = int(color_hex[3:5], 16)
                b = int(color_hex[5:7], 16)
                pixels[y][x] = (r, g, b, 255)
    if paused:
        # Draw two white rects for pause bar
        bar_width = max(2, size // 6)
        gap = max(2, size // 6)
        total_width = 2*bar_width + gap
        start_x = center - total_width//2
        bar_height = int(size * 0.6)
        top = center - bar_height//2
        bottom = top + bar_height
        for y in range(top, bottom):
            for x in range(start_x, start_x+bar_width):
                if 0 <= x < size and 0 <= y < size:
                    pixels[y][x] = (255,255,255,255)
            for x in range(start_x+bar_width+gap, start_x+2*bar_width+gap):
                if 0 <= x < size and 0 <= y < size:
                    pixels[y][x] = (255,255,255,255)
    return pixels

def write_icon(path, pixels):
    size = len(pixels)
    png = make_png_from_pixels(size, size, pixels)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(png)

def main():
    base_dir = os.path.join(os.path.dirname(__file__), 'icons')
    # Normal icons (work red)
    for sz in [16,48,128]:
        pixels = make_pomodoro_icon(sz, color_hex="#EF4444", paused=False)
        write_icon(os.path.join(base_dir, f'icon{sz}.png'), pixels)
    # Paused icons (same color but with pause overlay)
    for sz in [16,48,128]:
        pixels = make_pomodoro_icon(sz, color_hex="#EF4444", paused=True)
        write_icon(os.path.join(base_dir, f'icon_paused{sz}.png'), pixels)
    print("Generated normal and paused pomodoro icons")

if __name__ == '__main__':
    main()