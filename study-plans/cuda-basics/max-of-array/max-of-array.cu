#include <cuda_runtime.h>
#include <float.h>

__global__ void max_kernel_block(const float* input, float* partial, int N) {
    // Write code here
    __shared__ float s[256];
    int tid = threadIdx.x;
    int bid = blockIdx.x;
    int idx = blockDim.x*bid + tid;
    if(idx < N){
        s[tid] = input[idx];
    } else {
        s[tid] = -FLT_MAX;
    }

    __syncthreads();
    for(int i = blockDim.x >> 1; i > 0; i >>= 1){
        if(tid < i){
            s[tid] = fmaxf(s[tid], s[tid + i]);
        }
        __syncthreads();
    }

    if(tid == 0){
        partial[bid] = s[0];
    }
}

__global__ void max_kernel_total(const float* partial, float* result, int N) {
    __shared__ float s[256];
    int tid = threadIdx.x;
    if (tid < N) {
        s[tid] = partial[tid];
    } else {
        s[tid] = -FLT_MAX;
    }
    
    __syncthreads();
    for(int i = blockDim.x >> 1; i > 0; i >>= 1){
        if(tid < i){
            s[tid] = fmaxf(s[tid], s[tid + i]);
        }
        __syncthreads();
    }

    if(tid == 0){
       result[0] = s[0];
    }
}

extern "C" void solve(const float* input, float* result, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    float neg_inf = -FLT_MAX;
    float* partial = nullptr;
    cudaMalloc(&partial, blocks * sizeof(float));
    max_kernel_block<<<blocks, threads>>>(input, partial, N);
    max_kernel_total<<<1, threads>>>(partial, result, blocks);
    cudaDeviceSynchronize();
}
