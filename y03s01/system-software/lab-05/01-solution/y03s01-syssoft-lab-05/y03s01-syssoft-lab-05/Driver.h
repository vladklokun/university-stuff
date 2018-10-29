/*++

Module Name:

    driver.h

Abstract:

    This file contains the driver definitions.

Environment:

    Kernel-mode Driver Framework

--*/

#include <ntddk.h>
#include <wdf.h>
#include <initguid.h>

#include "device.h"
#include "queue.h"
#include "trace.h"

EXTERN_C_START

//
// WDFDRIVER Events
//

DRIVER_INITIALIZE DriverEntry;
EVT_WDF_DRIVER_DEVICE_ADD y03s01syssoftlab05EvtDeviceAdd;
EVT_WDF_OBJECT_CONTEXT_CLEANUP y03s01syssoftlab05EvtDriverContextCleanup;

EXTERN_C_END
