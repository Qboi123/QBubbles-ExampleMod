from zipapp import create_archive

from qcompiler import QCompiler

MODULE_PATH = "examplemod/"
MODULE_VERSION = "1.0.0"
MODULE_MAIN = "ExampleMod"
MODULE_NAME = f"ExampleMod-{MODULE_VERSION}.pyz"

if __name__ == '__main__':
    QCompiler(mod_path=MODULE_PATH, name=MODULE_NAME, compressed=False)
    print(f"Builded module '{MODULE_NAME}' successfully")
