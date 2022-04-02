import os


HOME_DIR_PATH = os.path.expanduser("~")
YAMTESTS_DIR_PATH = os.path.join(HOME_DIR_PATH, ".yamtests")
BIN_DIR_PATH = os.path.join(YAMTESTS_DIR_PATH, "bin")
PROGRAMS_DIR_PATH = os.path.join(YAMTESTS_DIR_PATH, "programs")
EXPECTED_OUTPUTS_DIR_PATH = os.path.join(YAMTESTS_DIR_PATH, "expected")

YAMASM_BIN_PATH = os.path.join(BIN_DIR_PATH, "yamasm")
YAMINI_BIN_PATH = os.path.join(BIN_DIR_PATH, "yamini")

BIN_DOWNLOAD_URL = "https://projects-frankhart.s3.amazonaws.com/yamtests/bin.zip"
PROGRAM_DOWNLOAD_URL = "https://projects-frankhart.s3.amazonaws.com/yamtests/programs.zip"
EXPECTED_OUTPUTS_DOWNLAOD_URL = "https://projects-frankhart.s3.amazonaws.com/yamtests/expected.zip"

BIN_ZIP_NAME = "bin.zip"
PROGRAM_ZIP_NAME = "programs.zip"
EXPECTED_OUTPUTS_ZIP_NAME = "expected.zip"

BIN_DIR_NAME = "bin"
PROGRAM_DIR_NAME = "programs"
EXPECTED_OUTPUTS_DIR_NAME = "expected"
