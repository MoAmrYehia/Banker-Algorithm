"""
PROGRAMMER:Mohamed Amr
DATE CREATED: 17/5/2021                                 
REVISED DATE: 20/5/2021
PURPOSE: Appling Software Engineering consepts
"""
from string import ascii_uppercase
Letter = list(ascii_uppercase)



def set_number_resources(number_used_resources = 0):
# =============================================================================
# This function is to set the total numer of resources      
# =============================================================================
	total_resources = []
	for resource_number in range(0, number_used_resources):
		total_resources.append(int(input("Total Resources, value for {}: ".format(Letter[resource_number]))))
	return total_resources



def set_number_processes(number_used_resources = 0, size=0):
# =============================================================================
# This function is to set the total numer of processes      
# =============================================================================
    cur_allocation = []
    max_allocation = []
    process = []
    for index in range(0, size):
        for resource_number in range(0, number_used_resources):
            cur_allocation.append(int(input("Current Allocation #{}, value for {}: ".format(index + 1, Letter[resource_number]))))
        for resource_number in range(0, number_used_resources):
            max_allocation.append(int(input("Max Allocation #{}, value for {}: ".format(index + 1, Letter[resource_number]))))

        process.append([max_allocation, cur_allocation])
        max_allocation = []
        cur_allocation = []
    return process



def get_total_allocations(process=[], size = 0, number_used_resources = 0):
# =============================================================================
# This function is to get the total numer of allcocations      
# =============================================================================
	summation = 0
	total_allocations = []
	for resource_number in range(0, number_used_resources):
		for index in range(0, size):
			summation += process[index][1][resource_number]
		total_allocations.append(summation)
		summation = 0
	return total_allocations



def get_all_available_instances(total_resources=[], total_allocations = [], number_used_resources = 0):
# =============================================================================
# This function is to get all available instances      
# =============================================================================
	total_available_instance = list([abs(rn_total_resources - rn_total_allocation) for rn_total_resources, rn_total_allocation in zip(total_resources, total_allocations)])
	return total_available_instance



def get_process_needed(process=[], size=0, number_used_resources = 0):
# =============================================================================
# This function is to get all processes needed   
# =============================================================================
	for index in range(0, size):
		need = list([abs(rn_max_alloc - rn_current_alloc) for index, rn_max_alloc, rn_current_alloc in zip(process, process[index][0], process[index][1])])
		process[index].append(need)
		need = []
	return process



def compare_the_ai_need(total_available_instance=[], process=[], size=0, number_used_resources = 0):
	for_removal = []
	queue = []
	for index in range(0, size):
		if (process[index][2] < total_available_instance):
			queue.append([process[index][2], process[index][0]])
			for_removal.append(process[index])
	queue.sort()
	for index in range(0, len(for_removal)):
		process.remove(for_removal[index])
	return queue, process



def get_the_new_ai(total_available_instance=[], queue=[], size=0, number_used_resources = 0):
    
	for index in range(0, size):
		for resource_number in range(0, number_used_resources):
			total_available_instance[resource_number] = abs(total_available_instance[resource_number] - queue[index][0][resource_number]) + queue[index][1][resource_number]
	return total_available_instance



def check_the_safety(origin_available_instance=[], total_available_instance=[], total_allocations = [], number_used_resources = 0):
# =============================================================================
# This function is to check the safty     
# =============================================================================    
	total_available_instance = list([abs(rn_available_instance - rn_total_allocation) for rn_available_instance, rn_total_allocation in zip(total_available_instance, total_allocations)])
	return (True if (origin_available_instance == total_available_instance) else False), total_available_instance