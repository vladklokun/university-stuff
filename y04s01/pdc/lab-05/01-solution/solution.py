"""
Solution to PDC lab about message passing.

Before running, make sure and MPI implementation is installed, e.g. Open MPI, Microsoft MPI etc.

After an MPI environment has been installed, run using:
    mpiexec -n 5 python solution.py
"""
from mpi4py import MPI
import numpy as np

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
)

DIMENSION = 10
THREAD_COUNT = 5
WORKER_IDS = [0, 1, 3, 4]

H = DIMENSION // THREAD_COUNT

D_VAL = 5
B_VAL = np.full((DIMENSION), 2)
Z_VAL = np.full((DIMENSION), 3)
MS_VAL = np.full((DIMENSION, DIMENSION), 1)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def compute_A_H(d, B, Z, MS, chunk_id):
    start = chunk_id * H
    stop = (chunk_id + 1) * H
    B_H = B[start:stop]
    MS_H = MS[:, start:stop]
    A_H = d * B_H + Z.dot(MS_H)
    logging.debug("A_H = {}".format(A_H))

    res = {
        "part_data": A_H,
        "start": start,
        "stop": stop,
    }
    return res

# Follower scenario. Store no data.
if rank != 2:
    data = comm.recv(source=2, tag=1)
    logging.debug(data)
    A_H = compute_A_H(**data, chunk_id=rank)
    comm.send(A_H, dest=2, tag=2)
# Leader scenario. Stores all the data.
elif rank == 2:
    # Initialize data
    A = np.empty(DIMENSION, dtype=np.int)
    d = D_VAL
    B = B_VAL
    Z = Z_VAL
    MS = MS_VAL

    # Gather all data into one dictionary for simple message passing
    data = {
        "d": d,
        "B": B,
        "Z": Z,
        "MS": MS,
    }

    # Send messages to all followers
    for i in WORKER_IDS:
        logging.debug(i)
        comm.send(data, dest=i, tag=1)

    # Receive and compile results from all followers
    for i in WORKER_IDS:
        res = comm.recv(source=i, tag=2)
        logging.debug("Received {} from worker {}".format(res, i))
        A[res["start"]:res["stop"]] = res["part_data"]

    # Compute the leader's part
    res = compute_A_H(**data, chunk_id=2)
    A[res["start"]:res["stop"]] = res["part_data"]

    logging.info("Final A = {}".format(A))
