import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pe = np.zeros((seq_len, d_model))
    pos = np.linspace(0, seq_len - 1, seq_len).reshape(-1, 1)
    d_half = int(np.ceil(d_model/2))
    omega = np.linspace(0, d_half - 1, d_half)
    omega = 1/np.power(base, 2*omega/d_model)
    pe[:, 0::2] = np.sin(pos*omega)
    pe[:, 1::2] = np.cos(pos*omega[0:d_model//2])

    return pe
    