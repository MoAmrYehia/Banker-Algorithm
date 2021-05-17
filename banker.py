"""
PROGRAMMER:Mohamed Amr
DATE CREATED: 17/5/2021                                 
REVISED DATE: 20/5/2021
PURPOSE: It is required to implement the banker’s algorithm inclduing
        1. The safety algorithm
        2. The request algorithm
"""

from utils import set_number_resources, set_number_processes, get_total_allocations, get_all_available_instances, get_process_needed, compare_the_ai_need, get_the_new_ai, check_the_safety

def main():
    
	total_available_instance = []
	origin_available_instance = []
	process = []

	total_allocations = []
	total_resources = []

	# f(x1)
	size = int(input("Please, enter the total number of processes: "))
	number_used_resources = int(input("Please, enter the available number of resources: "))

	# f(x2)
	total_resources = set_number_resources(number_used_resources = number_used_resources)

	# f(x3)
	process = set_number_processes(number_used_resources = number_used_resources, size = size)
    
	total_allocations = get_total_allocations(process = process,
                                           size = len(process),
                                           number_used_resources = number_used_resources)
    
    
	total_available_instance = get_all_available_instances(total_resources = total_resources,
                                                        total_allocations = total_allocations,
                                                        number_used_resources = number_used_resources)
    
	origin_available_instance = list(total_available_instance)
	
	# f(x4)
	process = get_process_needed(process = process,
                              size = len(process),
                              number_used_resources = number_used_resources)

	temp = list(process)

	# f(x5)
	while (len(process) != 0):
		queue, process = compare_the_ai_need(total_available_instance = total_available_instance,
                                       process = process,
                                       size = len(process),
                                       number_used_resources = number_used_resources)
		# f(x6)
		total_available_instance = get_the_new_ai(total_available_instance = total_available_instance,
                                            queue = queue,
                                            size = len(queue), 
                                            number_used_resources = number_used_resources)
	
	# f(x7)
	is_safe, total_available_instance = check_the_safety(origin_available_instance = origin_available_instance,
                                            total_available_instance = total_available_instance,
                                            total_allocations = total_allocations,
                                            number_used_resources = number_used_resources)
	
	process = list(temp)

	print("The Total Resources : {}".format(total_resources))
	print("The Total Allocation : {}".format(total_allocations))
	print("The Original Available Instance : {}".format(origin_available_instance))
	print("New Available Instance : {}".format(total_available_instance))
	print("All Processes : {}".format(process))
	print("It's Safe" if is_safe == True else "It's not Safe")


if __name__ == '__main__':
	main()
