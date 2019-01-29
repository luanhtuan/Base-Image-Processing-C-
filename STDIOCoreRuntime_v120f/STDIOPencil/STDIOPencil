#include "STDIOCoreRuntime.h"

void InitFunction(DrawLineFunc func)
{
	DrawLine = func;
}

void DrawTriangle(int x1, int y1, int x2, int y2, int x3, int y3)
{
	DrawLine(x1, y1, x2, y2);
	DrawLine(x1, y1, x3, y3);
	DrawLine(x2, y2, x3, y3);
}

void Display()
{
	DrawTriangle(100, 100, 50, 200, 150, 300);
}

