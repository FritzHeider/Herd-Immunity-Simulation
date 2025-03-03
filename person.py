import random
from virus import Virus
random.seed(42)


class Person(object):
    """Person objects will populate the simulation."""

    def __init__(self, _id, is_vaccinated, infection=None):
        """
        We start out with is_alive = True, because we don't make vampires or
        zombies.
        All other values will be set by the simulation when it makes each
        Person object.
        If person is chosen to be infected when the population is created, the
        simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        """
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection # Virus object or None

    def did_survive_infection(self):
        """
        Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        """

        if random.random() > self.infection.mortality_rate:
            self.is_vaccinated = True
            self.infection = None
            return True
        else:
            self.is_alive = False
            self.infection = None
            return False


"""These are simple tests to ensure that you are instantiating your Person
class correctly."""


def test_vacc_person_instantiation():
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None


def test_sick_person_instantiation():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(3, False, virus)
    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is virus


def test_did_survive_infection():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False, virus)
    survived = person.did_survive_infection()

    if survived:
        assert person.is_alive is True
        assert person._id == 4
        #is vaccinated is set true if they survive
        assert person.is_vaccinated is True
        assert person.infection is virus
    else:
        assert person.is_alive is False
        assert person._id == 4
        assert person.is_vaccinated is False
        assert person.infection is virus
