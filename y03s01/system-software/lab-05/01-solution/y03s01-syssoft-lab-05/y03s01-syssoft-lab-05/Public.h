/*++

Module Name:

    public.h

Abstract:

    This module contains the common declarations shared by driver
    and user applications.

Environment:

    user and kernel

--*/

//
// Define an Interface Guid so that apps can find the device and talk to it.
//

DEFINE_GUID (GUID_DEVINTERFACE_y03s01syssoftlab05,
    0x5941b476,0x2ee0,0x4d32,0xae,0x7c,0xc3,0x4a,0x4f,0xc2,0x7d,0x82);
// {5941b476-2ee0-4d32-ae7c-c34a4fc27d82}
