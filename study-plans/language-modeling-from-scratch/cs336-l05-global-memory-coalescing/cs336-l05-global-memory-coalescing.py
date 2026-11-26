import numpy as np

def coalescing_analysis(byte_addresses: np.ndarray, access_width_bytes: int = 4, cache_line_bytes: int = 128) -> dict:
    """
    Returns a dict: line_ids (int64 array), transaction_count (int), useful_byte_fraction (float).
    """
    byte_addresses = np.unique(byte_addresses)
    
    # First touched line IDs
    s = byte_addresses // cache_line_bytes
    e = (byte_addresses + access_width_bytes - 1) // cache_line_bytes
    line_ids = np.unique(np.concatenate((s, e)))
    for i in range(access_width_bytes // cache_line_bytes):
        line_ids = np.unique(np.concatenate((line_ids, s + i)))
    transaction_count = line_ids.size
    U = len({a + k for a in byte_addresses.tolist() for k in range(access_width_bytes)})

    useful_byte_fraction = U/(transaction_count*cache_line_bytes)

    return {"line_ids": line_ids, "transaction_count": transaction_count, "useful_byte_fraction": useful_byte_fraction}
    