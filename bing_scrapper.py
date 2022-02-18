def scrape(query,i,folder_name='None'):
  """
    i=1 : If the images has to be saved in a folder , Enter folder_name in this case
    i=2: If images has to be saved as a numpy file
    i=3: If images has to be saved as both"""


  url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"
  from urllib.request import urlopen
  from bs4 import BeautifulSoup
  import cv2
  from urllib.request import urlopen
  import numpy as np
  from tqdm import tqdm


  htmldata = urlopen(url)
  soup = BeautifulSoup(htmldata, 'html.parser')
  images = soup.find_all('img')
  files=[]
  for image in tqdm(images):
    try:
      url=image['src2']
      cap=cv2.VideoCapture(url)
      ret,image=cap.read()
      image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
      image=cv2.resize(image,(250,250))    ## Change this to the required size
      image=np.array(image)
      files.append(image)
    except:
      pass
  print(len(files),' images extracted from given URL')

  if (int(i)==1) | (int(i)==3):
    import os
    try:
      os.mkdir(folder_name)
    except:
      pass
    for i,im in enumerate(files):
      cv2.imwrite(folder_name+'/'+folder_name+str(i)+'.png',im)
    if i==3:
      np.savez(str(folder_name)+'.npz',data=files)
  elif i==2 : 
    np.savez(str(folder_name)+'.npz',data=files)

    
# Example query
query='Pikachu'
scrape(query,3,'pikachu')
