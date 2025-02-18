import sys
import asyncio

import utils

from console import get_command_line_arguments
from exceptions import SpecifiedPathNotFolder


async def main():
    cli_args = get_command_line_arguments()

    try:
        target_folder = utils.check_path(cli_args.path)
    except SpecifiedPathNotFolder:
        print("The specified path is not a folder.", file=sys.stderr)
        sys.exit(1)
    print(target_folder)


if __name__ == "__main__":
    asyncio.run(main())
