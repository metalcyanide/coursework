SRC_DIR := .
OBJ_DIR := objects
SRC_FILES := $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES := $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRC_FILES))
LDFLAGS := -pthread
CXXFLAGS := -std=c++11 -O4

mcts.out: $(OBJ_FILES)
	g++ $(LDFLAGS) $(CXXFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	g++  $(CXXFLAGS) $(LDFLAGS)  -c -o $@ $<

clean:
	rm -rf $(OBJ_FILES)
	rm -rf mcts.out
