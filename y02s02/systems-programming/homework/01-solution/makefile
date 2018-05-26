NAME = homework
NASM = /usr/local/Cellar/nasm/2.13.03/bin/nasm
ASM_FLAGS = -fmacho64
ASM_CMD = $(NASM) $(ASM_FLAGS)
LLD = clang

SRC_ASM = p01findminmax.asm p02dirtree.asm arrload.asm main.asm

OBJ_ASM = $(SRC_ASM:.asm=.o)

all: $(NAME)

$(NAME): $(OBJ_ASM)
	$(LLD) -o $(NAME) $(OBJ_ASM)

%.o: %.asm
	$(NASM) $(ASM_FLAGS) -o $@ $<
.PHONY: clean

clean:
	rm $(OBJ_ASM) $(NAME)
