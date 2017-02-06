# -*-coding:Latin-1 -*

import time

#On class
def singleton(classe_definie):
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

#On method
def controlTime(nb_secs):
    def decorator(initialFunc):
        def updatedFunc(*unammedParam, **namedParam):
            start = time.time() 
            result = initialFunc(unammedParam, namedParam)
            end = time.time()
            total = end - start
            if total >= nb_secs:
                print("It took {0} to run {1}".format(total, initialFunc))
            return result
        return updatedFunc
    return decorator
