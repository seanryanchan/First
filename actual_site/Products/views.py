from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from .models import Product

from PIL import Image
import magic


def secureImage(request, imagePath):
    mimer = magic.Magic(mime=True)
    mimeType = mimer.from_file(imagePath)
    response = HttpResponse(content_type=str(mimeType))
    img = Image.open(imagePath)
    fileType = (mimeType).split('/')[1]
    img.save(response, fileType)
    return response

def getProductPhoto(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # fileHandle = product.imgURL.file.open()
    # h = fileHandle.read()
    # fileHandle.close()
    # return HttpResponse(h)
    return secureImage(request, product.imgURL.path)
