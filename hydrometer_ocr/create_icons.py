#!/usr/bin/env python3
"""
Create icon.png and logo.png for Hydrometer OCR addon.
Requirements: PIL/Pillow

Usage:
    python3 create_icons.py
"""

from PIL import Image, ImageDraw
import os


def create_icon_png():
    """
    Create icon.png - A simple square icon with water meter theme.
    Size: 256x256 pixels
    """
    img = Image.new('RGBA', (256, 256), color=(25, 130, 180, 255))
    draw = ImageDraw.Draw(img)
    
    circle_color = (72, 209, 204, 255)
    draw.ellipse([50, 50, 206, 206], fill=circle_color, outline=(255, 255, 255, 255), width=3)
    draw.ellipse([80, 80, 176, 176], fill=(25, 130, 180, 255), outline=(255, 255, 255, 255), width=2)
    
    dot_color = (72, 209, 204, 255)
    draw.ellipse([95, 105, 110, 120], fill=dot_color)
    draw.ellipse([125, 100, 140, 115], fill=dot_color)
    draw.ellipse([155, 105, 170, 120], fill=dot_color)
    draw.ellipse([95, 140, 110, 155], fill=dot_color)
    draw.ellipse([155, 140, 170, 155], fill=dot_color)
    
    icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
    img.save(icon_path, 'PNG')
    print(f"Created {icon_path}")


def create_logo_png():
    """
    Create logo.png - A horizontal logo with water meter icon.
    Size: 512x128 pixels
    """
    img = Image.new('RGBA', (512, 128), color=(35, 55, 75, 255))
    draw = ImageDraw.Draw(img)
    
    icon_color = (72, 209, 204, 255)
    draw.ellipse([10, 10, 110, 110], fill=icon_color, outline=(255, 255, 255, 255), width=2)
    draw.ellipse([30, 30, 90, 90], fill=(35, 55, 75, 255), outline=(255, 255, 255, 255), width=1)
    
    dot_color = (255, 200, 50, 255)
    draw.ellipse([40, 45, 50, 55], fill=dot_color)
    draw.ellipse([60, 40, 70, 50], fill=dot_color)
    draw.ellipse([40, 65, 50, 75], fill=dot_color)
    draw.ellipse([80, 45, 90, 55], fill=dot_color)
    draw.ellipse([80, 65, 90, 75], fill=dot_color)
    
    # Draw text
    text_color = (72, 209, 204, 255)
    draw.text((130, 40), "Hydrometer OCR", fill=text_color)
    
    logo_path = os.path.join(os.path.dirname(__file__), 'logo.png')
    img.save(logo_path, 'PNG')
    print(f"Created {logo_path}")


if __name__ == '__main__':
    create_icon_png()
    create_logo_png()
    print("\nIcons created successfully!")
    print("icon.png: 256x256 pixels")
    print("logo.png: 512x128 pixels")
