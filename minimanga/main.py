import sys

from . import cli, config, sorter, image_converter


def main():
    cli_args = cli.get_arguments()

    if not cli_args.path.is_dir():
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)
    else:
        folder = cli_args.path

    if cli_args.is_extraction:
        archives = sorter.find_all(folder.rglob("*"), config.ARCHIVES_SUFFIXES, "Archives")
        print(archives)
    else:
        images = sorter.find_all(folder.rglob("*"), config.IMAGES_SUFFIXES, 'Images')
        image_converter.run(
            target_folder=cli_args.path,
            images=images,
            quality=cli_args.quality,
        )


if __name__ == "__main__":
    main()
