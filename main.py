import sys
from sql_concatenator.app import App
from sql_concatenator.utils.file_utils import file_path
from sql_concatenator.tests.tests import run_tests

def main() -> None:
    app = App()
    app.iconbitmap(file_path("face.ico"))
    app.mainloop()

if __name__ == "__main__":
    if '-test' in sys.argv or '-t' in sys.argv:
        run_tests()
    else:
        main()
