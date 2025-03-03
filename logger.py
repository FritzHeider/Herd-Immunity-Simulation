import os
from person import Person

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        with open(self.file_name, 'w') as f:
            f.write(f"{pop_size}\t{vacc_percentage}\t{virus_name}\t{mortality_rate}\t{basic_repro_num}\n")

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.
        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        with open(self.file_name, 'a') as f:

            if random_person_sick == True and did_infect == True:
                f.write(f"{person._id} didn't infect {random_person._id} because already sick \n")
            elif random_person_vacc == True and did_infect == True:
                f.write(f"{person._id} didn't infect {random_person._id} because already vaccinated \n")
            elif did_infect == False:
                f.write(f"{person._id} didn't infect {random_person._id} \n")
            elif did_infect == True:
                f.write(f"{person._id} infects {random_person._id} \n")
            else:
                f.write("SHOULD NOT HAPPEN \n")

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        with open(self.file_name, 'a') as f:
            if did_die_from_infection:
                f.write(f"{person._id} died from infection\n")
            else:
                f.write(f"{person._id} survived infection\n")


    def log_time_step(self, time_step_number, newly_infected_count, newly_dead_count, total_infected_count, total_dead_count):
        ''' STRETCH CHALLENGE DETAILS:
        If you choose to extend this method, the format of the summary statistics logged
        are up to you.
        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.
        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        with open(self.file_name, 'a') as f:
            f.write(f"Time step {time_step_number} ended, beginning {time_step_number + 1}\n")

        self.logger = Logger("logfile.txt")
        # Stores created population in self.population attribute
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
