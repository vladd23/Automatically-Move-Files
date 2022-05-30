import os
import shutil

# pathurile folderelor

downloads_folder = r"C:\Users\eset\Downloads"
poze_folder = r"C:\Users\eset\Downloads\poze"
video_folder = r"C:\Users\eset\Downloads\video"
aplicatii_folder = r"C:\Users\eset\Downloads\aplicatii"
documente_folder = r"C:\Users\eset\Downloads\documente"
muzici_folder = r"C:\Users\eset\Downloads\muzici"
other_folder = r"C:/Users/eset/Downloads/other"

files = os.listdir(downloads_folder)      #fisierele din folderul Downloads
print(files)
os.chdir(downloads_folder)

for file in files: #luam fiecare fisier in parte, verificam extensia si il mutam in folderul dorit
  if os.path.isfile(file):
      if file.endswith('.mp3'):
          shutil.move(os.path.join(downloads_folder, file), os.path.join(muzici_folder, file))
          #shutil.move(file, muzici_folder)
      elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
          shutil.move(os.path.join(downloads_folder, file), os.path.join(poze_folder, file))
          #shutil.move(file, poze_folder)
      elif file.lower().endswith('.exe'):
          shutil.move(os.path.join(downloads_folder, file), os.path.join(aplicatii_folder, file))
          #shutil.move(file, aplicatii_folder)
      elif file.lower().endswith(('.mp4', '.mov')):
          shutil.move(os.path.join(downloads_folder, file), os.path.join(video_folder, file))
          #shutil.move(file, video_folder)
      elif file.lower().endswith(('.doc', '.docx', '.html', '.htm', '.pdf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.txt')):
          shutil.move(os.path.join(downloads_folder, file), os.path.join(documente_folder, file))
          #shutil.move(file,documente_folder)
      else:
          shutil.move(os.path.join(downloads_folder, file), os.path.join(other_folder, file))
          #shutil.move(file, other_folder)


