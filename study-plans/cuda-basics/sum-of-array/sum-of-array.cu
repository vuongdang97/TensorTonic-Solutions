#include <cuda_runtime.h>

__global__ void sum_kernel(const float* input, float* result, int N) {
    // Write code here

    __shared__ float s[256];

    int tid = threadIdx.x;
    int idx = blockDim.x*blockIdx.x + threadIdx.x;

    if(idx < N){
        s[tid] = input[idx];
    } else{
        s[tid] = 0;
    }
    
     __syncthreads();

    for(int st = blockDim.x >> 1; st > 0; st >>= 1){
        if(tid < st){
            s[tid] += s[tid + st];
        }
        __syncthreads();
    }

    if(tid == 0){
        atomicAdd(result, s[0]);
    }
    
}

extern "C" void solve(const float* input, float* result, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    cudaMemset(result, 0, sizeof(float));
    sum_kernel<<<blocks, threads>>>(input, result, N);
    cudaDeviceSynchronize();
}
