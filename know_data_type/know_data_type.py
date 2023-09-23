import os , shutil

os.chdir('dataa')
for file_name in os.listdir("."):
    if file_name.endswith('.PNG') or file_name.endswith('.JPG') or file_name.endswith('.jpg') or file_name.endswith('.JPEG'):
        if not os.path.exists('images'):
            os.mkdir('images')
        shutil.move(file_name,'images')
    
    elif file_name.endswith('.mp4') or file_name.endswith('.avi') or file_name.endswith('.mov'):
        if not os.path.exists('videos'):
            os.mkdir('videos')
        shutil.move(file_name,'videos')

    elif file_name.endswith('.pdf') or file_name.endswith('.word') or file_name.endswith('.document'):
        if not os.path.exists('documents'):
            os.mkdir('documents')
        shutil.move(file_name,'documents')

    elif file_name.endswith('.setup') or file_name.endswith('.exe'):
        if not os.path.exists('apps'):
            os.mkdir('apps')
        shutil.move(file_name,'apps')

    else:
        if not os.path.exists('other'):
            os.mkdir('other')
        shutil.move(file_name,'other')