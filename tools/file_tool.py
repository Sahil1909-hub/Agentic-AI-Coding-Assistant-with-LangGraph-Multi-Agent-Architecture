import os
from utils.logger import logger



def save_file(filepath,content):

    directory = os.path.dirname(filepath)

    if directory:

        os.makedirs(directory,exist_ok=True)

    with open(filepath,"w",encoding="utf-8") as file:

        file.write(content)

    return filepath


logger.info('File tool created..')