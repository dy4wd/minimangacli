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
        print("The specified path is not a folder.", file=sys.stderr)
        sys.exit(1)

    files = utils.get_all_files(target_folder)

    try:
        images = utils.sort_images(files)
    except ImagesNotFound:
        print("Images not found.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
