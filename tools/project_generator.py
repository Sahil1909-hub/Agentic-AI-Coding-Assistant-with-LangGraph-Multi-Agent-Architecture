import os
from utils.logger import logger


def generate_project_structure(project_name):
    
    logger.info('Project generator tool..')

    folders = [

        f"{project_name}",

        f"{project_name}/src",

        f"{project_name}/tests",

        f"{project_name}/docs",

        f"{project_name}/config"

    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )

    return "Project created"