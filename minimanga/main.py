import sys
import asyncio

import utils
from console import get_command_line_arguments
from exceptions import SpecifiedPathNotFolder, ImagesNotFound


async def main():
    cli_args = get_command_line_arguments()

    try:
        target_folder = utils.path_handler(cli_args.path)
    except SpecifiedPathNotFolder:
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)

    try:
        images = utils.get_all_images(target_folder)
    except ImagesNotFound:
        sys.stderr.write("Images not found.\n")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
