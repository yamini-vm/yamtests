import os
import subprocess
import glob

import yamtests.constants as constants


def run_program(program_file_path, expected_file_path):
    output = subprocess.getoutput(f"{constants.YAMASM_BIN_PATH} {program_file_path}")
    if len(output) > 0:
        raise ValueError(f"Failed to assemble file: {program_file_path}")

    output = subprocess.getoutput(f"{constants.YAMINI_BIN_PATH} a.out").strip()

    with open(expected_file_path, "r") as f:
        expected_output = f.read().strip()

    os.system("rm a.out")

    return output == expected_output


def download_zip(download_url, zip_name, dir_name, dir_path):
    os.system(f"wget {download_url}")
    os.system(f"unzip {zip_name}")
    os.system(f"rm {zip_name}")
    os.system(f"mv {dir_name} {dir_path}")


def download_binaries():
    download_zip(
        download_url=constants.BIN_DOWNLOAD_URL,
        zip_name=constants.BIN_ZIP_NAME,
        dir_name=constants.BIN_DIR_NAME,
        dir_path=constants.YAMTESTS_DIR_PATH,
    )


def download_programs():
    download_zip(
        download_url=constants.PROGRAM_DOWNLOAD_URL,
        zip_name=constants.PROGRAM_ZIP_NAME,
        dir_name=constants.PROGRAM_DIR_NAME,
        dir_path=constants.YAMTESTS_DIR_PATH,
    )


def download_expectated_outputs():
    download_zip(
        download_url=constants.EXPECTED_OUTPUTS_DOWNLAOD_URL,
        zip_name=constants.EXPECTED_OUTPUTS_ZIP_NAME,
        dir_name=constants.EXPECTED_OUTPUTS_DIR_NAME,
        dir_path=constants.YAMTESTS_DIR_PATH,
    )


def run():
    os.makedirs(constants.YAMTESTS_DIR_PATH, exist_ok=True)

    if not os.path.exists(constants.BIN_DIR_PATH):
        print("Downloading binaries...")
        download_binaries()

    if not os.path.exists(constants.PROGRAMS_DIR_PATH):
        print("Downloading programs...")
        download_programs()

    if not os.path.exists(constants.EXPECTED_OUTPUTS_DIR_PATH):
        print("Downloading expected outputs...")
        download_expectated_outputs()

    program_files = glob.glob(f"{constants.PROGRAMS_DIR_PATH}/*.yas")
    expected_output_files = glob.glob(f"{constants.EXPECTED_OUTPUTS_DIR_PATH}/*.expect")

    assert len(program_files) == len(expected_output_files), (
        f"Inconsistent number of program and expected output files, program files: {len(program_files)}, "
        f"expected output files: {len(expected_output_files)}"
    )

    program_expect_pair = []
    for program_file in program_files:
        program_file_name = ".".join(os.path.basename(program_file).split(".")[:-1])
        expected_file = f"{constants.EXPECTED_OUTPUTS_DIR_PATH}/{program_file_name}.expect"

        if not os.path.exists(expected_file):
            raise ValueError(f"Expected output file not found: {expected_file}")

        program_expect_pair.append((program_file, expected_file))

    print(f"Found {len(program_files)} programs.")

    for (program_file, expected_file) in program_expect_pair:
        is_success = run_program(
            program_file_path=program_file,
            expected_file_path=expected_file,
        )

        if is_success:
            print(u"\u2713", end=" ")
            print(f"\033[92mSuccess\033[m: {program_file}")
        else:
            print(u"\u2717", end=" ")
            print(f"\033[91mFailed\033[m: {program_file}")
