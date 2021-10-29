CC := gcc

CFLAGS := -O3 -Wall -Wextra -Wpedantic
LDLIBS   := -Iinclude

SRCS    = $(shell find $(SRCDIR) -name '*.c')
SRCDIRS = $(shell find . -name '*.c' | dirname {} | sort | uniq | sed 's/\/$(SRCDIR)//g' )
OBJS    = $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(SRCS))

EXEC     := <NAME>

DESTDIR  := /usr/local
PREFIX   := debug

EXECDIR  := build
OBJDIR   := build
SRCDIR   := src
INCLUDE  := include

all: $(EXEC)
$(EXEC): $(OBJS) $(HDRS) Makefile
	mkdir -p $(EXECDIR)/$(PREFIX)
	$(CC) -o $(EXECDIR)/$(PREFIX)/$@ $(OBJS) $(LDLIBS)

$(OBJDIR)/%.o: $(SRCDIR)/%.c
	mkdir -p $(shell dirname $@)
	$(CC) $(OPTS) -c $< $(CFLAGS) $(INCLUDE:%=-I%) -o $@

.PHONY: install
install: $(EXEC)
	mkdir -p $(DESTDIR)/$(PREFIX)/bin
	cp $< $(DESTDIR)/$(PREFIX)/bin/$(EXEC)

.PHONY: uninstall
uninstall:
	rm $(DESTDIR)/$(PREFIX)/bin/$(EXEC)

.PHONY: clean
clean:
	rm -f $(EXECDIR)/$(PREFIX)/$(EXEC) $(OBJS)

.PHONY: compile_commands.json
compile_commands.json: Makefile
	make --always-make --dry-run \
		| grep -wE 'gcc|g++' \
		| grep -w '\-c' \
		| jq -nR '[inputs|{directory:".", command:., file: match(" [^ ]+$$").string[1:]}]' \
		> bin/compile_commands.json
	ln -fs $(OBJDIR)/compile_commands.json compile_commands.json
