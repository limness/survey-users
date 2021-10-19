
from django.core.files.base import ContentFile

from io import BytesIO
from PIL import Image

from urllib.parse import urlparse

import requests
import os


def get_filename_by_url(url: str) -> str:
    """ Get the Image name using URL """
    url_data = urlparse(url)
    filename_by_url = os.path.basename(url_data.path)
    return filename_by_url

def open_pillow_file_and_verify(url: str) -> Image:
    """ Method that opens and verifies a file """
    upload_url_image = Image.open(BytesIO(response.content))
    upload_url_image.verify()
    upload_url_image = Image.open(BytesIO(response.content))
    return upload_url_image

def open_pillow_file_from_url_and_verify(url: str) -> Image:
    """ Method that opens and verifies a file by URL """
    response = requests.get(url)
    upload_url_image = Image.open(BytesIO(response.content))
    upload_url_image.verify()
    upload_url_image = Image.open(BytesIO(response.content))
    return upload_url_image

def save_pillow_file_to_buffer(image):
    """ Resizes an image from a Model.ImageField
    and returns a new image as a ContentFile """
    buffer = BytesIO()
    image.save(fp=buffer, format=image.format)
    return ContentFile(buffer.getvalue())

def resize_image(image_field, width, height):
    """ Resizes an image from a Model.ImageField
    and returns a new image as a ContentFile """
    img = Image.open(image_field)
    if width == 0:
        width = img.size[0]
    if height == 0:
        height = img.size[1]
    new_img = img.resize((width, height))
    buffer = BytesIO()
    new_img.save(fp=buffer, format=img.format)
    return ContentFile(buffer.getvalue())
