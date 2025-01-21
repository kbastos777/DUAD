
def bubble_sort_len (list_to_be_sorted):
    for out_index in range((len(list_to_be_sorted)-1),-1,-1):
        has_made_changes = False
        for inside_index in range((len(list_to_be_sorted)-1),-1,-1):
            current_index = list_to_be_sorted[inside_index]
            next_index = list_to_be_sorted[inside_index-1]
            if current_index > next_index:
                list_to_be_sorted[inside_index]=next_index
                list_to_be_sorted[inside_index-1]=current_index
                has_made_changes = True
        if not has_made_changes:
            return
    return len(list_to_be_sorted)
