################################################################################
#                                                                              #
#  GENERIC LINUX MACHINE FILE                                                  #
#                                                                              #
#  This provides sane defaults for development machines that are not covered by #
#  the upstream host-specific configs.                                          #
#                                                                              #
#  Notes:                                                                      #
#  - Uses system MPI compiler wrapper if available (`mpicc`).                   #
#  - Assumes HDF5 headers are under /usr/include/hdf5/serial (common on Debian/ #
#    Arch-style layouts).                                                      #
#                                                                              #
################################################################################

import os
import shutil
import subprocess


def matches_host() -> bool:
    return os.uname().sysname == "Linux"


def get_options():
    host = {}

    host["NAME"] = os.uname()[1]

    cc = shutil.which("mpicc") or shutil.which("cc") or "cc"
    host["COMPILER"] = cc

    # Warnings-as-errors, but keep the warning set reproducible across distros.
    # Avoid `-Wextra` here because it triggers many unused-parameter warnings in
    # upstream C sources; keep the remaining warnings as errors.
    host["COMPILER_FLAGS"] = "-O2 -march=native -Wall -Werror -Wno-stringop-truncation -fopenmp"
    host["DEBUG_FLAGS"] = "-O0 -g -Wall -Werror -Wno-stringop-truncation -fopenmp"

    # Prefer system installs. If your distro uses a nonstandard include layout,
    # override via `BHLIGHT_EXTRA_INCLUDES`.
    host["GSL_DIR"] = ""

    # Prefer a system HDF5 install discovered via pkg-config. The build system
    # links HDF5 only when `HDF5_DIR` is present in the host config.
    try:
        subprocess.check_call(
            ["pkg-config", "--exists", "hdf5"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        prefix = (
            subprocess.check_output(["pkg-config", "--variable=prefix", "hdf5"])
            .decode()
            .strip()
        )
        if prefix:
            host["HDF5_DIR"] = prefix
    except Exception:
        pass

    # Rely on system include paths by default; if you need a nonstandard layout,
    # override via `BHLIGHT_EXTRA_INCLUDES`.
    host["EXTRA_INCLUDES"] = ""

    # Use mpirun as the default launcher when needed.
    host["EXECUTABLE"] = "mpirun -np 1"
    host["MPI_EXECUTABLE"] = "mpirun"

    return host
