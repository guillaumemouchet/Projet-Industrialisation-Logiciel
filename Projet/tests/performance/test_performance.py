"""cProfile test package"""
import cProfile, pstats
from main import random_password


def test_perf():
    """Main function"""
    # - https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/
    # - Démarrer le profilage de CProfile
    profiler = cProfile.Profile()
    profiler.enable()

    # https://stackoverflow.com/questions/8682716/python-variables-scope-and-profile-run
    profiler.runctx("f(p1, p2)", {"f": random_password, "p1": 15, "p2": True}, {})
    profiler.runctx("f(p1, p2)", {"f": random_password, "p1": 15, "p2": False}, {})
    profiler.runctx("f(p1, p2)", {"f": random_password, "p1": 20, "p2": True}, {})
    profiler.runctx("f(p1, p2)", {"f": random_password, "p1": 20, "p2": False}, {})

    # - Stopper le profilage
    profiler.disable()

    # - Utiliser pstats pour trier le profilage suivant la colonne 'ncalls'
    # - Afficher les résultats dans la console.
    pstats.Stats(profiler).sort_stats("ncalls").print_stats()

if __name__ == "__main__":
    test_perf()
