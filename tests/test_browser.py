from automating_anki.browser import saveImage
import tempfile

def test_save_image():
    """It saves the image to a file given the image link."""
    filename = tempfile.NamedTemporaryFile(mode="wb")
    image_link = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnXOdJvstHpTQVpG-hUNxblPMHQunIftJjBw&usqp=CAU"
    saveImage(image_link, filename.name)