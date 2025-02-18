import asyncio

from console import get_command_line_arguments


async def main():
    cli_args = get_command_line_arguments()
    print(cli_args)


if __name__ == "__main__":
    asyncio.run(main())
