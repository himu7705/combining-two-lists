def get_overlap(a, b):
    a_start, a_end = a["positions"]
    b_start, b_end = b["positions"]
    overlap_start = max(a_start, b_start)
    overlap_end = min(a_end, b_end)
    if overlap_start >= overlap_end:
        return 0
    overlap_length = overlap_end - overlap_start
    a_length = a_end - a_start
    b_length = b_end - b_start
    return max(overlap_length / a_length, overlap_length / b_length)
def combine_lists(list1, list2):
    i = 0
    j = 0
    combined = []
    while i < len(list1) and j < len(list2):
        item1 = list1[i]
        item2 = list2[j]
        if get_overlap(item1, item2) > 0.5:
            new_item = {
                "positions": item1["positions"],
                "values": item1["values"] + item2["values"]
            }
            combined.append(new_item)
            i += 1
            j += 1
        elif item1["positions"][0] < item2["positions"][0]:
            combined.append(item1)
            i += 1
        else:
            combined.append(item2)
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined
