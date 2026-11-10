# HLE indirect draws (Donkey Kong Bananza terrain)

Donkey Kong Bananza draws its terrain with NVN's indexed indirect draw macro. A culling dispatch
fills in a 5-word record per piece (index count, instance count, first index, base vertex, base
instance) and the macro's parameters continue with the record itself, in a GP entry that points at
GPU-written memory.

Reading that record on the CPU means copying the command list from the GPU and waiting for the
copy (`DmaPusher::ReadGpuWrittenCommands`), for every call: about 20,000 a second in the open
areas. Instead, the split front recognizes the macro by its register writes on its first calls
(`FrontRunMacro`: the sixteen writes of `IndirectDrawWrites`) and, for records on GPU-written
pages, has the back issue `vkCmdDrawIndexedIndirect` from the record
(`Maxwell3D::BackDrawIndexedIndirect`). A barrier orders the indirect read after the buffer writes
(`BufferCache::TakeIndirectBarrier`, `RasterizerVulkan::DrawIndirect`).

Ported from Dozer (Anka's `86eafa98`, itself modelled on `HLE_DrawIndexedIndirect`).

`EDEN_NX2_HLE_INDIRECT=0` turns it off and restores the copy-and-wait path. The log says
`Macro at ... is NVN's indexed indirect draw` once the macro is recognized and prints a count of
HLE draws at powers of two from 1024.
