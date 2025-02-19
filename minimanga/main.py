import sys
import asyncio

from minimanga import utils
from minimanga.console import get_command_line_arguments
from minimanga.exceptions import SpecifiedPathNotFolder


async def main():
    cli_args = get_command_line_arguments()

    try:
        target_folder = utils.check_path(cli_args.path)
    except SpecifiedPathNotFolder:
        print("The specified path is not a folder.", file=sys.stderr)
        sys.exit(1)
    
    files = utils.get_all_files(target_folder)


if __name__ == "__main__":
    asyncio.run(main())
