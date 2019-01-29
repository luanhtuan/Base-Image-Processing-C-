#ifndef __FRACTAL__
#define __FRACTAL__

typedef void(*DrawLineFunc)(int x1, int y1, int x2, int y2);

static DrawLineFunc DrawLine;

_declspec(dllexport) void InitFunction(DrawLineFunc func);
_declspec(dllexport) void Display();

#endif