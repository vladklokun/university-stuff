#include "driver.h"
#include "device.tmh"

#ifdef ALLOC_PRAGMA
#pragma alloc_text (PAGE, y03s01syssoftlab05CreateDevice)
#endif

NTSTATUS
y03s01syssoftlab05CreateDevice(
    _Inout_ PWDFDEVICE_INIT DeviceInit
    )

{
    WDF_OBJECT_ATTRIBUTES deviceAttributes;
    PDEVICE_CONTEXT deviceContext;
    WDFDEVICE device;
    NTSTATUS status;

    PAGED_CODE();

    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&deviceAttributes, DEVICE_CONTEXT);

    status = WdfDeviceCreate(&DeviceInit, &deviceAttributes, &device);

    if (NT_SUCCESS(status)) {

        deviceContext = DeviceGetContext(device);

        deviceContext->PrivateDeviceData = 0;

        status = WdfDeviceCreateDeviceInterface(
            device,
            &GUID_DEVINTERFACE_y03s01syssoftlab05,
            NULL // ReferenceString
            );

        if (NT_SUCCESS(status)) {
            status = y03s01syssoftlab05QueueInitialize(device);
        }
    }

    return status;
}
