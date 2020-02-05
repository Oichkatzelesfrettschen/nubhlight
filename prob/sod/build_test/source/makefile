CC = /usr/bin/mpicc
CCFLAGS = -std=c99 -mcmodel=medium -O2 -march=native -Wall -Werror -Wno-stringop-truncation -fopenmp -Llib/ -Iinclude/ 
LIB_FLAGS = -lm -ldl -lgsl -lgslcblas -Wl,-rpath=lib/
CC_COMPILE = $(CC) $(CCFLAGS) -c
CC_LOAD = $(CC) $(CCFLAGS)
FSRC = 
FOBJ = 
SRC = bounds.c coord.c current.c diag.c electrons.c emissivity.c eos.c eos_gamma.c eos_poly.c eos_stellar_collapse.c estimate_thetae.c fixup.c input.c interact.c io.c main.c make_superphotons.c metric.c mpi.c opac_emis_hdf.c opac_emis_neutrino.c oscillations.c passive.c phys.c problem.c push_superphotons.c rad_utils.c radiation.c random.c reconstruction.c root_finding.c scattering.c step.c tetrads.c timing.c tracers.c util.c utop.c xdmf_output.c 
OBJ = bounds.o coord.o current.o diag.o electrons.o emissivity.o eos.o eos_gamma.o eos_poly.o eos_stellar_collapse.o estimate_thetae.o fixup.o input.o interact.o io.o main.o make_superphotons.o metric.o mpi.o opac_emis_hdf.o opac_emis_neutrino.o oscillations.o passive.o phys.o problem.o push_superphotons.o rad_utils.o radiation.o random.o reconstruction.o root_finding.o scattering.o step.o tetrads.o timing.o tracers.o util.o utop.o xdmf_output.o 
INC = constants.h decs.h defs.h eos_stellar_collapse.h params.h 
EXE = bhlight
.c.o:
	$(CC_COMPILE) $*.c
all: $(EXE)
$(OBJ): $(INC) makefile
$(EXE): $(OBJ) $(FOBJ) $(INC) makefile
	$(CC_LOAD) $(OBJ) $(FOBJ) $(LIB_FLAGS) -o $(EXE)
clean:
	$(RM) $(SRC) $(FSRC) $(OBJ) $(FOBJ) $(EXE) $(INC)
