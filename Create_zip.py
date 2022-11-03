import os
import shutil


def creation():
    # desktop path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                           'Desktop\Analisi_III')
    shutil.make_archive('result', 'zip', desktop)
    return 0
