CC := gcc
CFLAGS := -Wall -Wextra -Werror -std=c11 -Iinclude
BUILD_DIR := build
TARGET := $(BUILD_DIR)/demo_app
SRCS := src/main.c src/hello.c src/banner.c src/calc.c
OBJS := $(SRCS:src/%.c=$(BUILD_DIR)/%.o)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(BUILD_DIR)/%.o: src/%.c
	mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(BUILD_DIR)
