import subprocess
from utils.logger import logger


def run_command(command):

    logger.info('Shell tool creating..')

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "stdout": result.stdout,    
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except Exception as e:

        return {
            "error": str(e)
        }