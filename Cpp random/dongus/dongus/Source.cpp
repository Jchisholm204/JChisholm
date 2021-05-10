#include <iostream>
#include "includes.h"
#include <time.h>
void Sleep(int millis) {
    clock_t time_end;
    time_end = clock() + millis * CLOCKS_PER_SEC / 1000;
    while (clock() < time_end)
    {
    }
}