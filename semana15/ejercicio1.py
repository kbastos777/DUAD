def sort_list (list_to_be_sorted):
    for out_index in range((len(list_to_be_sorted)-1),0,-1):
        has_made_changes = False
        print(list_to_be_sorted)
        for inside_index in range((len(list_to_be_sorted)-1),0,-1):
            current_index = list_to_be_sorted[inside_index]
            next_index = list_to_be_sorted[inside_index-1]
            if current_index < next_index:
                list_to_be_sorted[inside_index]=next_index
                list_to_be_sorted[inside_index-1]=current_index
                has_made_changes = True
            out_index = out_index - 1    
    if not has_made_changes:
        return
            

list_of_numbers = [10,58,-5,10,2,6]
sort_list(list_of_numbers)