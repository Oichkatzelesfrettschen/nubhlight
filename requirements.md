# Build Requirements (nubhlight)

**Role:** C99 GR-radiation-MHD codebase with Python build/test scripts.  
**Authoritative:** `core/`, `prob/`, `script/` build utilities.  
**Non-authoritative / generated:** run directories, `dumps/`, `restarts/`.

## Prerequisites

- C99 compiler
- GSL
- MPI
- HDF5 (`libhdf5` + `libhdf5_hl`)
- `gfortran` (only if Burrows opacities are used)
- Python 3 for build + analysis scripts (`numpy`, `matplotlib`, `h5py` typically)

## Build + run (example)

Nubhlight uses per-problem build scripts. Example (Sod shocktube):

```bash
cd nubhlight/prob/sod
python3 build.py -dir build_sod
./bhlight -p param_template.dat
```

### Notes

- The build selects a host config from `nubhlight/script/machine/*.py`. For Linux
  development hosts, `zz_generic_linux.py` is provided as a catch-all.
- If your distro ships **serial** HDF5 (no MPIO symbols), the code builds with
  serial fallbacks; true parallel HDF5 I/O requires an MPI-enabled HDF5 build.

See `nubhlight/README.md` for additional problem and test harness examples under
`nubhlight/test/`.
