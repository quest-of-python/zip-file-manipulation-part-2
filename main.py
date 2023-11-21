import pathlib

from zip_manipulation import retrieve_sum_from_uuids


def main():
    archive_path = pathlib.Path("archive.zip")
    result = retrieve_sum_from_uuids(archive_path)

    print(f"Result extracted from valid files: {result}.")


if __name__ == '__main__':
    main()
