#ifndef __DOTS__
#define __DOTS__

#include <stdio.h>

#include "System/Structure.h"

_declspec(dllexport) char** InitGame(struct STDIONode** DotsHead);
_declspec(dllexport) int setDotsSpeed();
_declspec(dllexport) void AddHead(struct STDIONode** DotsHead);
_declspec(dllexport) void AddTail(struct STDIONode** DotsHead);
_declspec(dllexport) void DeleteHead(struct STDIONode** DotsHead);
_declspec(dllexport) void DeleteTail(struct STDIONode** DotsHead);

#endif
