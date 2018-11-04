CCX =clang++
IDIR =.
CPPFLAGS =-I$(IDIR) -Wall -std=c++11
DEPS = 

OBJ = main.o

%.o: %.cpp $(DEPS)
	$(CCX) -c -o $@ $< $(CPPFLAGS)

task-03: $(OBJ)
	$(CCX) -o $@ $^ $(CPPFLAGS)

.PHONY: clean

clean:
	rm -f *.o task-03
