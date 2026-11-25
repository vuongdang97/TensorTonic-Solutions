def gpu_occupancy(
    threads_per_block: int, registers_per_thread: int, shared_mem_per_block: int,
    max_threads_per_sm: int, max_warps_per_sm: int, max_blocks_per_sm: int,
    max_registers_per_sm: int, max_shared_mem_per_sm: int, warp_size: int = 32,
) -> dict:
    """
    Returns a dict: blocks_per_sm (int), resident_warps (int), occupancy (float).
    """
    # Recompute the actuan registers and threads need
    (warps, threads_leftover) = divmod(threads_per_block, warp_size)
    if(threads_leftover):
        warps = warps + 1
    threads_per_block = warps*warp_size
    registers_per_blocks = registers_per_thread*threads_per_block
    # Calculate blocks_per_sm allowed based on 5 limits of threads, wraps, regiters, bytes and default max blocks
    blocks_per_sm = min(max_blocks_per_sm, max_threads_per_sm // threads_per_block)
    blocks_per_sm = min(blocks_per_sm, max_warps_per_sm // warps)
    if(registers_per_blocks > 0):
        blocks_per_sm = min(blocks_per_sm, max_registers_per_sm // registers_per_blocks)
    if(shared_mem_per_block > 0):    
        blocks_per_sm = min(blocks_per_sm, max_shared_mem_per_sm // shared_mem_per_block)
    # Calculate resident wrap
    resident_warps = blocks_per_sm*warps
    occupancy = resident_warps/max_warps_per_sm

    return {"blocks_per_sm":blocks_per_sm, "resident_warps": resident_warps, "occupancy": occupancy}
    