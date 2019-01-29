#pragma once

typedef unsigned char byte;

_declspec(dllexport) void STDIOVisionProcess(int width, int height, int byte_per_pixel, byte*& data, double value);
_declspec(dllexport) void STDIOVisionMinMaxRange(double* min, double* max, double* init);