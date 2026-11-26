import numpy as np

def bank_conflict_analysis(byte_addresses: np.ndarray, num_banks: int = 32, bank_width_bytes: int = 4) -> dict:
    """
    Returns a dict of int64 arrays: bank_ids and conflict_degree.
    """
    bank_ids = byte_addresses // bank_width_bytes % num_banks
    byte_addresses_distinct = np.unique(byte_addresses) 
    bank_ids_distinct = byte_addresses_distinct // bank_width_bytes % num_banks
    frequency = dict()
    for i in range(bank_ids_distinct.size):
        curr_id = bank_ids_distinct[i]
        if curr_id not in frequency:
            frequency[curr_id] = 1
        else:
            frequency[curr_id] = frequency[curr_id] + 1
    conflict_degree = np.zeros(bank_ids.size, dtype = "int64")
    for i in range(conflict_degree.size):
        conflict_degree[i] = frequency[bank_ids[i]]
    return {"bank_ids": bank_ids, "conflict_degree": conflict_degree}