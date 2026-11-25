#include <cuda_runtime.h>
#include <float.h>

__global__ void max_pool_2d_kernel(const float* input, float* output, int H, int W, int kH, int kW, int sH, int sW) {
    // Write code 
    int x = blockDim.x*blockIdx.x + threadIdx.x;
    int y = blockDim.y*blockIdx.y + threadIdx.y;
    int outH = (H - kH) / sH + 1;
    int outW = (W - kW) / sW + 1;
    if(x < outW && y < outH){
        output[y*outW + x] = -FLT_MAX;
        for(int a = 0; a < kH; a++){
            for(int b = 0; b < kW; b++){
                output[y*outW + x] = fmaxf(output[y*outW + x], input[(y*sH + a)*W + x*sW + b]);
            }
        }
    }
    
}

extern "C" void solve(const float* input, float* output, int H, int W, int kH, int kW, int sH, int sW) {
    int outH = (H - kH) / sH + 1;
    int outW = (W - kW) / sW + 1;
    dim3 threads(16, 16);
    dim3 blocks((outW + 15) / 16, (outH + 15) / 16);
    max_pool_2d_kernel<<<blocks, threads>>>(input, output, H, W, kH, kW, sH, sW);
    cudaDeviceSynchronize();
}
