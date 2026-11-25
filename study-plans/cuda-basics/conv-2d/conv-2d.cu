#include <cuda_runtime.h>

__global__ void conv2d_kernel(const float* input, const float* kernel, float* output, int H, int W, int kH, int kW) {
    // Write code here
    int col = blockDim.x*blockIdx.x + threadIdx.x;
    int row = blockDim.y*blockIdx.y + threadIdx.y;
    int outH = H - kH + 1;
    int outW = W - kW + 1;
    if(row < outH && col < outW){
        output[row*outW + col] = 0;
        for(int a = 0; a < kH; a++){
            for(int b = 0; b < kW; b++){
               output[row*outW + col] += input[(row + a)*W + col + b]*kernel[a*kW + b] ;
            }
        }
    }
}

extern "C" void solve(const float* input, const float* kernel, float* output, int H, int W, int kH, int kW) {
    int outH = H - kH + 1;
    int outW = W - kW + 1;
    dim3 threads(16, 16);
    dim3 blocks((outW + 15) / 16, (outH + 15) / 16);
    conv2d_kernel<<<blocks, threads>>>(input, kernel, output, H, W, kH, kW);
    cudaDeviceSynchronize();
}
