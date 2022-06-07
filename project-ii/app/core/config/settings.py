from os.path import abspath, dirname, join


class Settings: 

    ROOT_PATH = dirname(dirname(dirname(dirname(dirname(abspath(__file__))))))
    
    PROJECT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    
    MODELS_PATH = join(ROOT_PATH, "models")

    RECOGNITION_MODEL = join(MODELS_PATH, "recognition_model.h5")
