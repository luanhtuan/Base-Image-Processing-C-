#pragma once

#include <stdio.h>

#include "System/STDIOVisionBridge.h"

#include "STDIOVision/STDIOVision.h"
#include "STDIOCalculator/STDIOCalculator.h"
#include "STDIOPencil/STDIOPencil.h"
#include "STDIODots/STDIODots.h"

#ifdef __cplusplus 
extern "C"
{
#endif

_declspec(dllexport) void STDIO_main();

#ifdef __cplusplus 
}
#endif