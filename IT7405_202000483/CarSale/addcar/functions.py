def handle_uploaded_file(file):
    with open('carview/static/carview/img/'+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)