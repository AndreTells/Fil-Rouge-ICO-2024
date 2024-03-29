from random import uniform
from .acceptance_prob_functions import standard_acceptance_prob_function
from solver_step import SolverStep

def taboo_search_solver_factory(get_random_neighbour,
                                state_to_energy,
                                tabu_list_size):
    '''
    def taboo_search(max_iterations):
        s = get_initial_state()
        tabu_list = []
        history = {'current_energy': [], 'state': [], 'tabu_list_size': []}

        if debug_mode:
            print('The maximum iterations is:', max_iterations)
            print('The initial state is:', s)
            print('------------------------------------------------------')

        for _ in range(max_iterations):
            neighbors = [get_random_neighbour(s) for _ in range(tabu_list_size)]
            best_neighbor = min(neighbors, key=state_to_energy)

            if best_neighbor not in tabu_list:
                s = best_neighbor
                tabu_list.append(s)
                if len(tabu_list) > tabu_list_size:
                    tabu_list.pop(0)

            if return_history:
                history['current_energy'].append(state_to_energy(s))
                history['state'].append(s)
                history['tabu_list_size'].append(len(tabu_list))

            if debug_mode:
                print('The current state is:', s, ' with energy: ',
                      state_to_energy(s))
                print('The tabu list is:', tabu_list)
                print('------------------------------------------------------')

        if return_history:
            return s, history

        return s
    '''

    def taboo_search_step(init_state):
        s = init_state.get_best_sol()
        tabu_list = []
        
        for _ in range(init_state.get_step_size()):
            neighbors = [get_random_neighbour(s) for _ in range(tabu_list_size)]
            best_neighbor = min(neighbors, key=state_to_energy)

            if best_neighbor not in tabu_list:
                s = best_neighbor
                tabu_list.append(s)
                if len(tabu_list) > tabu_list_size:
                    tabu_list.pop(0)

        return SolverStep(init_state.get_step_count()+1,s, init_state.get_step_size)

    return taboo_search_step